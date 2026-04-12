import argparse
import json
import math
import re
from collections import defaultdict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
GRAPH_FILE = BASE_DIR / "concept_graph.json"
ALIASES_FILE = BASE_DIR / "concept_aliases.json"
EXTRACTIONS_FILE = BASE_DIR / "global_extractions.json"

STOPWORDS = {
    "a",
    "an",
    "and",
    "api",
    "architectures",
    "architecture",
    "best",
    "between",
    "build",
    "by",
    "for",
    "from",
    "how",
    "i",
    "if",
    "implement",
    "in",
    "is",
    "my",
    "of",
    "on",
    "or",
    "should",
    "the",
    "to",
    "use",
    "vs",
    "what",
    "when",
    "with",
}

TYPE_PRIORITY = {"concept": 0, "pattern": 1, "component": 2}
STANDARD_EDGE_TYPES = {"implemented_by", "realized_as", "uses"}
COMPARISON_KEYWORDS = ["vs", "versus", "compare", "difference", "better", "instead of", "tradeoff"]


def load_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_text(text: str) -> str:
    text = text.lower().replace("_", " ")
    text = re.sub(r"[^a-z0-9+/ -]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    return [token for token in normalize_text(text).split() if token and token not in STOPWORDS]


def contains_phrase(query_text: str, phrase: str) -> bool:
    query_tokens = normalize_text(query_text).split()
    phrase_tokens = normalize_text(phrase).split()
    if not phrase_tokens or len(phrase_tokens) > len(query_tokens):
        return False
    return any(
        query_tokens[index : index + len(phrase_tokens)] == phrase_tokens
        for index in range(len(query_tokens) - len(phrase_tokens) + 1)
    )


def jaccard_score(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def build_indexes(
    graph: dict,
    aliases: list[dict],
    extractions: dict,
) -> tuple:
    nodes = {node["id"]: node for node in graph["nodes"]}

    adjacency = defaultdict(list)
    pair_edges = defaultdict(list)
    for edge in graph["edges"]:
        pair_edges[frozenset({edge["from"], edge["to"]})].append(edge)
        adjacency[edge["from"]].append(
            {
                "neighbor": edge["to"],
                "type": edge["type"],
                "confidence": edge["confidence"],
                "evidence_count": edge["evidence_count"],
                "source_diversity": edge["source_diversity"],
                "direction": "forward",
            }
        )
        adjacency[edge["to"]].append(
            {
                "neighbor": edge["from"],
                "type": edge["type"],
                "confidence": edge["confidence"],
                "evidence_count": edge["evidence_count"],
                "source_diversity": edge["source_diversity"],
                "direction": "reverse",
            }
        )

    alias_entries = []
    for item in aliases:
        variants = [item["label"], *item.get("aliases", []), item["canonical"].replace("_", " ")]
        for variant in variants:
            normalized = normalize_text(variant)
            if not normalized:
                continue
            alias_entries.append(
                (
                    normalized,
                    {
                        "node_id": item["canonical"],
                        "label": item["label"],
                        "confidence": item.get("confidence", 0.5),
                    },
                )
            )

    for item in extractions.get("pattern_registry", []):
        variants = [item["name"], item["structure"], *item.get("aliases", []), item["pattern_id"].replace("_", " ")]
        for variant in variants:
            normalized = normalize_text(variant)
            if not normalized:
                continue
            alias_entries.append(
                (
                    normalized,
                    {
                        "node_id": item["pattern_id"],
                        "label": item["name"],
                        "confidence": item.get("confidence", 0.4),
                    },
                )
            )

    label_entries = []
    for node in graph["nodes"]:
        normalized = normalize_text(node["label"])
        if not normalized:
            continue
        label_entries.append(
            (
                normalized,
                {
                    "node_id": node["id"],
                    "label": node["label"],
                    "type": node["type"],
                    "confidence": node.get("confidence", 0.8),
                },
            )
        )

    return nodes, adjacency, {"aliases": alias_entries, "labels": label_entries}, pair_edges


def node_weight(node: dict) -> float:
    return max(node.get("confidence", 0.8), 0.2)


def resolve_query(query: str, nodes: dict[str, dict], lookup: dict[str, list]) -> list[dict]:
    normalized_query = normalize_text(query)
    query_tokens = set(tokenize(query))
    candidates: dict[str, dict] = {}

    def add_match(node_id: str, label: str, score: float, reason: str) -> None:
        if score <= 0:
            return
        entry = candidates.setdefault(node_id, {"score": 0.0, "reasons": set(), "label": label})
        entry["score"] = max(entry["score"], score)
        entry["reasons"].add(reason)

    for phrase, item in lookup["aliases"]:
        phrase_tokens = set(tokenize(phrase))
        if not phrase_tokens:
            continue
        if phrase == normalized_query:
            score = 1.0 * item["confidence"]
            add_match(item["node_id"], item["label"], score, f"exact alias match: {phrase}")
            continue
        if contains_phrase(normalized_query, phrase):
            score = 0.95 * item["confidence"]
            add_match(item["node_id"], item["label"], score, f"alias phrase match: {phrase}")
            continue
        overlap = jaccard_score(query_tokens, phrase_tokens)
        if overlap >= 0.6:
            score = overlap * 0.85 * item["confidence"]
            add_match(item["node_id"], item["label"], score, f"alias token overlap: {phrase}")

    for phrase, item in lookup["labels"]:
        phrase_tokens = set(tokenize(phrase))
        if not phrase_tokens:
            continue
        if contains_phrase(normalized_query, phrase):
            score = 0.9 * item["confidence"]
            add_match(item["node_id"], item["label"], score, f"label phrase match: {phrase}")
            continue
        overlap = jaccard_score(query_tokens, phrase_tokens)
        minimum = 0.5 if len(phrase_tokens) > 1 else 1.0
        if overlap >= minimum:
            score = overlap * 0.75 * item["confidence"]
            add_match(item["node_id"], item["label"], score, f"label token overlap: {phrase}")

    ranked = []
    for node_id, item in candidates.items():
        node = nodes.get(node_id)
        if not node:
            continue
        ranked.append(
            {
                "node_id": node_id,
                "label": node["label"],
                "type": node["type"],
                "score": round(item["score"], 4),
                "reasons": sorted(item["reasons"]),
            }
        )

    ranked.sort(key=lambda item: (-item["score"], TYPE_PRIORITY[item["type"]], item["label"]))
    return ranked[:5]


def relation_text(step: dict, left_label: str, right_label: str) -> str:
    forward = {
        "implemented_by": f"{left_label} is implemented by {right_label}",
        "realized_as": f"{left_label} is realized as {right_label}",
        "uses": f"{left_label} uses {right_label}",
        "contrasts_with": f"{left_label} contrasts with {right_label}",
        "tradeoff": f"{left_label} trades off with {right_label}",
    }
    reverse = {
        "implemented_by": f"{left_label} implements {right_label}",
        "realized_as": f"{left_label} realizes {right_label}",
        "uses": f"{left_label} is used by {right_label}",
        "contrasts_with": f"{left_label} contrasts with {right_label}",
        "tradeoff": f"{left_label} trades off with {right_label}",
    }
    mapping = forward if step["direction"] == "forward" else reverse
    return mapping.get(step["type"], f"{left_label} relates to {right_label}")


def is_comparison_query(query: str) -> bool:
    lowered = query.lower()
    return any(keyword in lowered for keyword in COMPARISON_KEYWORDS)


def get_neighbors(
    node_id: str,
    nodes: dict[str, dict],
    adjacency: dict[str, list[dict]],
    target_type: str | None = None,
    edge_types: set[str] | None = None,
) -> dict[str, dict]:
    neighbors = {}
    for edge in adjacency.get(node_id, []):
        if edge_types and edge["type"] not in edge_types:
            continue
        neighbor = nodes[edge["neighbor"]]
        if target_type and neighbor["type"] != target_type:
            continue
        current = neighbors.get(neighbor["id"])
        if not current or edge["confidence"] > current["confidence"]:
            neighbors[neighbor["id"]] = {
                "node_id": neighbor["id"],
                "label": neighbor["label"],
                "type": neighbor["type"],
                "confidence": edge["confidence"],
                "edge_type": edge["type"],
                "direction": edge["direction"],
                "evidence_count": edge["evidence_count"],
                "source_diversity": edge["source_diversity"],
            }
    return neighbors


def pick_comparison_targets(seed_matches: list[dict]) -> list[dict]:
    if len(seed_matches) < 2:
        return []
    compare_priority = {"pattern": 0, "concept": 1, "component": 2}
    ranked = sorted(
        seed_matches,
        key=lambda item: (-item["score"], compare_priority[item["type"]], item["label"]),
    )
    picks = []
    seen = set()
    for item in ranked:
        if item["node_id"] in seen:
            continue
        picks.append(item)
        seen.add(item["node_id"])
        if len(picks) == 2:
            break
    return picks


def serialize_neighbor_list(items: dict[str, dict], limit: int = 6) -> list[dict]:
    ranked = sorted(items.values(), key=lambda item: (-item["confidence"], item["label"]))
    return [
        {
            "node_id": item["node_id"],
            "label": item["label"],
            "confidence": item["confidence"],
            "edge_type": item["edge_type"],
        }
        for item in ranked[:limit]
    ]


def serialize_difference_list(items: dict[str, dict], other_ids: set[str], limit: int = 6) -> list[dict]:
    filtered = [item for item in items.values() if item["node_id"] not in other_ids]
    filtered.sort(key=lambda item: (-item["confidence"], item["label"]))
    return [
        {
            "node_id": item["node_id"],
            "label": item["label"],
            "confidence": item["confidence"],
            "edge_type": item["edge_type"],
        }
        for item in filtered[:limit]
    ]


def build_qwen_comparison_prompt(comparison: dict) -> str:
    a = comparison["concept_a"]["label"]
    b = comparison["concept_b"]["label"]
    lines = [
        f"Compare these two architectures: {a} and {b}.",
        "",
        f"{a}:",
    ]
    for item in comparison["unique_to_a"][:5]:
        lines.append(f"- component: {item['label']}")
    for item in comparison["shared_components"][:5]:
        lines.append(f"- shared component: {item['label']}")
    lines.append("")
    lines.append(f"{b}:")
    for item in comparison["unique_to_b"][:5]:
        lines.append(f"- component: {item['label']}")
    for item in comparison["shared_components"][:5]:
        lines.append(f"- shared component: {item['label']}")
    lines.append("")
    lines.append("Explain:")
    lines.append("- key differences")
    lines.append("- when to use each")
    lines.append("- tradeoffs")
    return "\n".join(lines)


def run_comparison_mode(
    query: str,
    nodes: dict[str, dict],
    adjacency: dict[str, list[dict]],
    lookup: dict[str, list],
    pair_edges: dict[frozenset[str], list[dict]],
) -> dict:
    seed_matches = resolve_query(query, nodes, lookup)
    targets = pick_comparison_targets(seed_matches)
    if len(targets) < 2:
        return traverse_query(query, nodes, adjacency, lookup)

    left = targets[0]
    right = targets[1]
    left_node = nodes[left["node_id"]]
    right_node = nodes[right["node_id"]]

    direct_edges = pair_edges.get(frozenset({left["node_id"], right["node_id"]}), [])
    left_components = get_neighbors(
        left["node_id"], nodes, adjacency, target_type="component", edge_types={"uses", "implemented_by"}
    )
    right_components = get_neighbors(
        right["node_id"], nodes, adjacency, target_type="component", edge_types={"uses", "implemented_by"}
    )
    left_concepts = get_neighbors(
        left["node_id"], nodes, adjacency, target_type="concept", edge_types={"realized_as"}
    )
    right_concepts = get_neighbors(
        right["node_id"], nodes, adjacency, target_type="concept", edge_types={"realized_as"}
    )

    shared_component_ids = set(left_components) & set(right_components)
    shared_concept_ids = set(left_concepts) & set(right_concepts)

    direct_relationships = []
    key_differences = []
    recommended_usage = []
    for edge in sorted(direct_edges, key=lambda item: (-item["confidence"], item["type"])):
        payload = {
            "type": edge["type"],
            "from": nodes[edge["from"]]["label"],
            "to": nodes[edge["to"]]["label"],
            "confidence": edge["confidence"],
            "evidence_count": edge.get("evidence_count"),
            "source_diversity": edge.get("source_diversity"),
        }
        if edge.get("dimensions"):
            payload["dimensions"] = {
                dimension: nodes[winner_id]["label"]
                for dimension, winner_id in edge["dimensions"].items()
            }
            for dimension, winner_id in edge["dimensions"].items():
                key_differences.append({"dimension": dimension, "favors": nodes[winner_id]["label"]})
        direct_relationships.append(payload)

        for node_id, guidance in edge.get("recommended_usage", {}).items():
            recommended_usage.append(
                {
                    "architecture": nodes[node_id]["label"],
                    "guidance": guidance,
                }
            )

    comparison = {
        "query": query,
        "mode": "comparison",
        "seed_matches": seed_matches,
        "concept_a": {
            "node_id": left["node_id"],
            "label": left_node["label"],
            "type": left_node["type"],
            "score": left["score"],
        },
        "concept_b": {
            "node_id": right["node_id"],
            "label": right_node["label"],
            "type": right_node["type"],
            "score": right["score"],
        },
        "direct_relationships": direct_relationships,
        "shared_components": serialize_neighbor_list(
            {node_id: left_components[node_id] for node_id in shared_component_ids}
        ),
        "unique_to_a": serialize_difference_list(left_components, set(right_components)),
        "unique_to_b": serialize_difference_list(right_components, set(left_components)),
        "shared_related_concepts": serialize_neighbor_list(
            {node_id: left_concepts[node_id] for node_id in shared_concept_ids}
        ),
        "key_differences": key_differences,
        "recommended_usage": recommended_usage,
    }
    comparison["qwen_comparison_prompt"] = build_qwen_comparison_prompt(comparison)
    return comparison


def traverse_query(
    query: str,
    nodes: dict[str, dict],
    adjacency: dict[str, list[dict]],
    lookup: dict[str, list],
    max_depth: int = 3,
    depth_decay: float = 0.9,
    min_step_score: float = 0.02,
) -> dict:
    seeds = resolve_query(query, nodes, lookup)
    if not seeds:
        return {"query": query, "seed_matches": [], "top_results": {}, "paths": []}

    aggregate_scores = defaultdict(float)
    best_paths: dict[str, dict] = {}

    for seed in seeds:
        initial_score = seed["score"]
        aggregate_scores[seed["node_id"]] += initial_score
        best_paths[seed["node_id"]] = {
            "score": round(initial_score, 4),
            "nodes": [seed["node_id"]],
            "steps": [],
        }

        frontier = [
            {
                "node_id": seed["node_id"],
                "score": initial_score,
                "nodes": [seed["node_id"]],
                "steps": [],
            }
        ]

        for depth in range(1, max_depth + 1):
            next_frontier = []
            for state in frontier:
                for edge in adjacency.get(state["node_id"], []):
                    if edge["type"] not in STANDARD_EDGE_TYPES:
                        continue
                    neighbor_id = edge["neighbor"]
                    if neighbor_id in state["nodes"]:
                        continue

                    neighbor = nodes[neighbor_id]
                    step_score = (
                        state["score"]
                        * edge["confidence"]
                        * node_weight(neighbor)
                        * math.pow(depth_decay, depth - 1)
                    )
                    if step_score < min_step_score:
                        continue

                    aggregate_scores[neighbor_id] += step_score
                    path = {
                        "node_id": neighbor_id,
                        "score": round(step_score, 4),
                        "nodes": [*state["nodes"], neighbor_id],
                        "steps": [*state["steps"], edge | {"from_node": state["node_id"]}],
                    }

                    if step_score > best_paths.get(neighbor_id, {}).get("score", 0):
                        best_paths[neighbor_id] = path

                    next_frontier.append(path)
            frontier = next_frontier

    ranked_nodes = []
    for node_id, score in aggregate_scores.items():
        node = nodes[node_id]
        ranked_nodes.append(
            {
                "node_id": node_id,
                "label": node["label"],
                "type": node["type"],
                "score": round(score, 4),
                "confidence": node.get("confidence"),
            }
        )
    ranked_nodes.sort(key=lambda item: (-item["score"], TYPE_PRIORITY[item["type"]], item["label"]))

    grouped = {"concepts": [], "patterns": [], "components": []}
    seed_ids = {item["node_id"] for item in seeds}
    type_map = {"concept": "concepts", "pattern": "patterns", "component": "components"}
    for item in ranked_nodes:
        bucket = grouped[type_map[item["type"]]]
        if len(bucket) >= 5:
            continue
        bucket.append(item)

    paths = []
    for node in ranked_nodes:
        if node["node_id"] in seed_ids and best_paths[node["node_id"]]["steps"] == []:
            continue
        best = best_paths.get(node["node_id"])
        if not best:
            continue
        if len(paths) >= 8:
            break
        labels = [nodes[node_id]["label"] for node_id in best["nodes"]]
        path_steps = []
        current = best["nodes"][0]
        for step in best["steps"]:
            left_label = nodes[current]["label"]
            right_label = nodes[step["neighbor"]]["label"]
            path_steps.append(
                {
                    "from": left_label,
                    "to": right_label,
                    "type": step["type"],
                    "direction": step["direction"],
                    "confidence": step["confidence"],
                    "evidence_count": step["evidence_count"],
                    "source_diversity": step["source_diversity"],
                    "explanation": relation_text(step, left_label, right_label),
                }
            )
            current = step["neighbor"]

        paths.append(
            {
                "target": node["label"],
                "target_type": node["type"],
                "score": best["score"],
                "path_labels": labels,
                "path_steps": path_steps,
            }
        )

    return {
        "query": query,
        "mode": "traversal",
        "seed_matches": seeds,
        "top_results": grouped,
        "paths": paths,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run weighted traversal over the concept graph.")
    parser.add_argument(
        "--query",
        action="append",
        dest="queries",
        help="Query to run. Repeat for multiple queries.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional JSON output path.",
    )
    args = parser.parse_args()

    graph = load_json(GRAPH_FILE)
    aliases = load_json(ALIASES_FILE)
    extractions = load_json(EXTRACTIONS_FILE)
    nodes, adjacency, lookup, pair_edges = build_indexes(graph, aliases, extractions)

    queries = args.queries or [
        "How should I build RAG on AWS?",
        "What should I use for model evaluation and observability?",
        "When should I use WebSocket API instead of REST API?",
    ]
    results = [
        run_comparison_mode(query, nodes, adjacency, lookup, pair_edges)
        if is_comparison_query(query)
        else traverse_query(query, nodes, adjacency, lookup)
        for query in queries
    ]

    if args.output:
        args.output.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(f"Wrote {args.output}")

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
