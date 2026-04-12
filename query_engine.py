import argparse
import json
import os
import re
from collections import deque
from pathlib import Path
from urllib import error, request


# ========================
# CONFIG
# ========================
BASE_DIR = Path(__file__).resolve().parent
GRAPH_FILE = BASE_DIR / "Notes" / "concept_graph.json"
EXTRACTIONS_FILE = BASE_DIR / "Notes" / "global_extractions.json"
CONCEPT_SEARCH_INDEX_FILE = BASE_DIR / "Notes" / "concept_search_index.json"
CONCEPT_LIST_FILE = BASE_DIR / "Notes" / "concept_list.json"

LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://127.0.0.1:1234/v1/chat/completions")
QWEN_MODEL = os.getenv("LM_STUDIO_MODEL", "qwen2.5-14b-instruct")
TOP_K_CONCEPTS = 5
TOP_K_QWEN_RESULTS = 8
TOP_K_EDGES = 5
MAX_HOPS = 2
STANDARD_EDGE_TYPES = {"implemented_by", "realized_as", "uses"}
SEMANTIC_WEIGHT = 0.7
ALIAS_WEIGHT = 0.2
KEYWORD_WEIGHT = 0.1
STOPWORDS = {
    "a",
    "an",
    "and",
    "architecture",
    "aws",
    "does",
    "for",
    "how",
    "in",
    "is",
    "of",
    "on",
    "the",
    "to",
    "what",
    "work",
}

MATCHING_MODE = "lm_studio_qwen_semantic_rerank"
QWEN_QUERY_CACHE = {}


# ========================
# LOAD DATA
# ========================
with GRAPH_FILE.open("r", encoding="utf-8") as f:
    graph = json.load(f)

with EXTRACTIONS_FILE.open("r", encoding="utf-8") as f:
    extractions = json.load(f)

nodes = graph["nodes"]
edges = graph["edges"]
concept_index = extractions["global_concept_index"]
concept_aliases = extractions.get("concept_aliases", [])


def load_concept_search_index() -> list[dict]:
    if CONCEPT_SEARCH_INDEX_FILE.exists():
        return json.loads(CONCEPT_SEARCH_INDEX_FILE.read_text(encoding="utf-8"))

    fallback = []
    for item in concept_index:
        fallback.append(
            {
                "concept": item["concept"],
                "aliases": item.get("aliases", []),
                "related_components": item.get("related_components", []),
                "related_patterns": item.get("related_patterns", []),
                "graph_confidence": item.get("confidence", 0.5),
                "frequency": item.get("frequency", 0),
                "source_count": item.get("source_count", 0),
            }
        )
    return fallback


concept_records_from_index = load_concept_search_index()


# ========================
# BUILD LOOKUPS
# ========================
node_lookup = {node["id"]: node for node in nodes}
concept_node_lookup = {
    node["label"]: node["id"]
    for node in nodes
    if node["type"] == "concept"
}

concept_records = []
for concept in concept_records_from_index:
    node_id = concept_node_lookup.get(concept["concept"])
    if not node_id:
        continue
    concept_records.append(
        {
            "concept": concept["concept"],
            "node_id": node_id,
            "aliases": concept.get("aliases", []),
            "related_components": concept.get("related_components", []),
            "related_patterns": concept.get("related_patterns", []),
            "graph_confidence": concept.get("graph_confidence", concept.get("confidence", 0.5)),
            "frequency": concept.get("frequency", 0),
            "source_count": concept.get("source_count", 0),
        }
    )

if not concept_records:
    raise ValueError("No graph-backed concept records were available")

concept_lookup = {record["concept"]: record for record in concept_records}
concept_by_node_id = {record["node_id"]: record for record in concept_records}
concept_record_by_name = {record["concept"]: record for record in concept_records}
concept_list = [record["concept"] for record in concept_records]

adjacency = {}
for edge in edges:
    if edge["type"] not in STANDARD_EDGE_TYPES:
        continue
    adjacency.setdefault(edge["from"], []).append(edge)


# ========================
# MATCHING HELPERS
# ========================
def normalize_text(text):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", text.lower())).strip()


def tokenize(text):
    return [token for token in normalize_text(text).split() if token and token not in STOPWORDS]


def lexical_similarity(left, right):
    left_tokens = set(tokenize(left))
    right_tokens = set(tokenize(right))
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens | right_tokens)


def phrase_in_text(text, phrase):
    return f" {normalize_text(phrase)} " in f" {normalize_text(text)} "


alias_lookup = {}
for item in concept_aliases:
    variants = [item["label"], *item.get("aliases", [])]
    for variant in variants:
        normalized = normalize_text(variant)
        if normalized:
            alias_lookup[normalized] = {
                "node_id": item["canonical"],
                "label": item["label"],
                "alias": variant,
                "confidence": item.get("confidence", 0.5),
            }


def direct_alias_matches(query):
    normalized_query = normalize_text(query)
    matches = []
    seen = set()

    for alias_text, payload in alias_lookup.items():
        if alias_text == normalized_query or f" {alias_text} " in f" {normalized_query} ":
            concept = concept_by_node_id.get(payload["node_id"])
            if not concept or concept["concept"] in seen:
                continue
            seen.add(concept["concept"])
            matches.append(
                {
                    "concept": concept["concept"],
                    "similarity": 1.0,
                    "semantic_score": 1.0,
                    "matched_phrase": payload["alias"],
                    "match_type": "alias_direct",
                    "alias_match": 1.0,
                    "keyword_overlap": 0.0,
                }
            )

    return matches


def alias_score(query, concept_name):
    record = concept_record_by_name[concept_name]
    candidates = [record["concept"], *record.get("aliases", [])]
    normalized_query = normalize_text(query)

    best_score = 0.0
    best_phrase = record["concept"]
    for phrase in candidates:
        normalized_phrase = normalize_text(phrase)
        if not normalized_phrase:
            continue
        score = 0.0
        if normalized_phrase == normalized_query:
            score = 1.0
        elif phrase_in_text(normalized_query, normalized_phrase):
            score = 1.0
        if score > best_score:
            best_score = score
            best_phrase = phrase
    return best_score, best_phrase


def keyword_overlap_score(query, concept_name):
    record = concept_record_by_name[concept_name]
    candidates = [record["concept"], *record.get("aliases", [])]
    best_score = 0.0
    best_phrase = record["concept"]
    for phrase in candidates:
        score = lexical_similarity(query, phrase)
        if score > best_score:
            best_score = score
            best_phrase = phrase
    return best_score, best_phrase


def parse_json_list(content: str) -> list[dict]:
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    candidates = [text]
    left = text.find("[")
    right = text.rfind("]")
    if left != -1 and right != -1 and right > left:
        candidates.append(text[left : right + 1])

    for candidate in candidates:
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, list):
            return parsed
        if isinstance(parsed, dict):
            for key in ("results", "items", "matches"):
                value = parsed.get(key)
                if isinstance(value, list):
                    return value

    raise ValueError("LM Studio response did not contain a JSON list")


def read_message_content(body: dict) -> str:
    choices = body.get("choices", [])
    if not choices:
        return ""
    content = choices[0].get("message", {}).get("content", "")
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(item.get("text", ""))
        return "\n".join(parts).strip()
    return str(content).strip()


def build_semantic_rank_prompt(query: str) -> str:
    candidates = []
    for record in concept_records:
        candidates.append(
            {
                "concept": record["concept"],
                "aliases": record.get("aliases", [])[:5],
                "components": record.get("related_components", [])[:5],
                "patterns": record.get("related_patterns", [])[:5],
            }
        )

    return "\n".join(
        [
            "Rank the concept catalog for semantic relevance to the user query.",
            "Return JSON list only.",
            "Use exact concept names from the catalog.",
            f"Return at most {TOP_K_QWEN_RESULTS} items.",
            "Each item must contain: concept, semantic_score, matched_phrase.",
            "semantic_score must be a number between 0 and 1.",
            "Only include concepts that are genuinely relevant.",
            "",
            f"Query: {query}",
            "",
            "Concept catalog:",
            json.dumps(candidates, ensure_ascii=False, indent=2),
        ]
    )


def run_qwen_semantic_rank(query: str) -> dict[str, dict]:
    normalized_query = normalize_text(query)
    cached = QWEN_QUERY_CACHE.get(normalized_query)
    if cached is not None:
        return cached

    prompt = build_semantic_rank_prompt(query)
    payload = json.dumps(
        {
            "model": QWEN_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You rank knowledge-graph concepts for retrieval. Return JSON only.",
                },
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "temperature": 0.1,
        }
    ).encode("utf-8")
    req = request.Request(
        LM_STUDIO_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(req) as response:
            body = json.loads(response.read().decode("utf-8"))
        content = read_message_content(body)
        if not content:
            raise RuntimeError("LM Studio returned an empty response")
        items = parse_json_list(content)
    except (RuntimeError, ValueError, error.HTTPError, error.URLError):
        QWEN_QUERY_CACHE[normalized_query] = {}
        return {}

    scores = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        concept_name = str(item.get("concept", "")).strip()
        if concept_name not in concept_lookup:
            continue
        try:
            semantic_score = float(item.get("semantic_score", 0.0))
        except (TypeError, ValueError):
            semantic_score = 0.0
        semantic_score = max(0.0, min(1.0, semantic_score))
        matched_phrase = str(item.get("matched_phrase", "")).strip() or concept_name
        scores[concept_name] = {
            "semantic_score": semantic_score,
            "matched_phrase": matched_phrase,
        }

    QWEN_QUERY_CACHE[normalized_query] = scores
    return scores


# ========================
# MATCH QUERY -> CONCEPTS
# ========================
def match_concepts(query):
    direct_matches = {item["concept"]: item for item in direct_alias_matches(query)}
    qwen_scores = run_qwen_semantic_rank(query)
    ranked = []

    for concept in concept_list:
        alias_match, alias_phrase = alias_score(query, concept)
        keyword_score, keyword_phrase = keyword_overlap_score(query, concept)
        semantic_payload = qwen_scores.get(concept, {})
        semantic_score = float(semantic_payload.get("semantic_score", 0.0))
        graph_score = float(concept_lookup[concept].get("graph_confidence", 0.0))

        if concept in direct_matches:
            ranked.append(direct_matches[concept])
            continue

        if semantic_score > 0:
            final_score = (
                SEMANTIC_WEIGHT * semantic_score
                + ALIAS_WEIGHT * alias_match
                + KEYWORD_WEIGHT * keyword_score
            )
        else:
            final_score = (
                0.6 * alias_match
                + 0.25 * keyword_score
                + 0.15 * graph_score
            )

        if semantic_score > 0:
            matched_phrase = semantic_payload.get("matched_phrase") or alias_phrase or keyword_phrase
            match_type = "qwen_semantic_rerank"
        elif alias_match > 0:
            matched_phrase = alias_phrase
            match_type = "alias_boost_fallback"
        elif keyword_score > 0:
            matched_phrase = keyword_phrase
            match_type = "keyword_overlap_fallback"
        else:
            matched_phrase = concept
            match_type = "low_signal_fallback"

        ranked.append(
            {
                "concept": concept,
                "similarity": final_score,
                "semantic_score": semantic_score,
                "alias_match": alias_match,
                "keyword_overlap": keyword_score,
                "matched_phrase": matched_phrase,
                "match_type": match_type,
            }
        )

    ranked.sort(key=lambda item: item["similarity"], reverse=True)
    return ranked[:TOP_K_CONCEPTS]


# ========================
# GRAPH TRAVERSAL
# ========================
def traverse(start_concepts):
    results = []

    for item in start_concepts:
        concept_name = item["concept"]
        concept = concept_lookup[concept_name]
        start_id = concept["node_id"]
        start_score = item["similarity"]

        visited = {start_id}
        queue = deque([(start_id, start_score, 0)])

        while queue:
            current_id, path_score, depth = queue.popleft()

            if depth >= MAX_HOPS:
                continue

            for edge in adjacency.get(current_id, []):
                next_node_id = edge["to"]
                edge_conf = edge.get("confidence", 0.5)
                new_score = path_score * edge_conf

                results.append(
                    {
                        "from": current_id,
                        "from_label": node_lookup[current_id]["label"],
                        "to": next_node_id,
                        "to_label": node_lookup[next_node_id]["label"],
                        "type": edge["type"],
                        "edge_confidence": round(edge_conf, 3),
                        "score": round(new_score, 3),
                    }
                )

                if next_node_id not in visited:
                    visited.add(next_node_id)
                    queue.append((next_node_id, new_score, depth + 1))

    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:TOP_K_EDGES]


# ========================
# BUILD ANSWER
# ========================
def build_synthesis_prompt(query, matched_concepts, relations):
    lines = [
        f"Question: {query}",
        "",
        "Use these concepts, components, and graph relations to explain the answer.",
        "Be concise and concrete. Prefer AWS-specific terminology from the provided context.",
        "",
        "Matched concepts:",
    ]

    for item in matched_concepts:
        lines.append(
            f"- {item['concept']} (confidence: {item['confidence']}, graph_confidence: {item.get('graph_confidence')})"
        )
        if item["components"]:
            lines.append(f"  components: {', '.join(item['components'][:6])}")
        if item["patterns"]:
            lines.append(f"  patterns: {', '.join(item['patterns'][:6])}")

    lines.append("")
    lines.append("Top relations:")
    for relation in relations[:TOP_K_EDGES]:
        lines.append(
            f"- {relation['from_label']} --{relation['type']} ({relation['edge_confidence']})--> {relation['to_label']}"
        )

    lines.append("")
    lines.append("Answer:")
    return "\n".join(lines)


def build_answer(query, concepts, relations):
    answer = {
        "query": query,
        "matching_mode": MATCHING_MODE,
        "matcher_cache": {
            "concept_count": len(concept_list),
            "qwen_query_cache_size": len(QWEN_QUERY_CACHE),
        },
        "matched_concepts": [],
        "top_relations": relations,
    }

    for item in concepts:
        concept_name = item["concept"]
        concept = concept_lookup.get(concept_name, {})
        answer["matched_concepts"].append(
            {
                "concept": concept_name,
                "node_id": concept.get("node_id"),
                "confidence": round(float(item["similarity"]), 3),
                "matched_phrase": item["matched_phrase"],
                "match_type": item.get("match_type"),
                "semantic_score": round(float(item.get("semantic_score", 0.0)), 3),
                "alias_match": round(float(item.get("alias_match", 0.0)), 3),
                "keyword_overlap": round(float(item.get("keyword_overlap", 0.0)), 3),
                "graph_confidence": concept.get("graph_confidence"),
                "components": concept.get("related_components", []),
                "patterns": concept.get("related_patterns", []),
            }
        )

    answer["qwen_answer_prompt"] = build_synthesis_prompt(
        query,
        answer["matched_concepts"],
        relations,
    )
    return answer


# ========================
# MAIN QUERY FUNCTION
# ========================
def query_engine(query):
    concepts = match_concepts(query)
    relations = traverse(concepts)
    return build_answer(query, concepts, relations)


# ========================
# CLI
# ========================
def main():
    parser = argparse.ArgumentParser(description="Semantic query engine over Notes knowledge graph.")
    parser.add_argument("--query", help="Run a single query and print JSON.")
    args = parser.parse_args()

    if args.query:
        print(json.dumps(query_engine(args.query), indent=2))
        return

    while True:
        q = input("\nAsk something (or 'exit'): ").strip()
        if q.lower() == "exit":
            break
        if not q:
            continue

        result = query_engine(q)
        print("\n--- Answer ---")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
