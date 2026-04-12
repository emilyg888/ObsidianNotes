import argparse
import contextlib
import importlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
from urllib import error, request

BASE_DIR = Path(__file__).resolve().parent
GRAPH_QUERY_PATH = BASE_DIR / "Notes" / "query_concept_graph.py"
LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://127.0.0.1:1234/v1/chat/completions")
QWEN_MODEL = os.getenv("LM_STUDIO_MODEL", "qwen2.5-14b-instruct")

SYSTEM_PROMPT = """You answer questions using only the supplied graph context.
Be concise, concrete, and AWS-specific.
If the question is comparative, explain key differences, tradeoffs, and when to use each option.
If the context is weak or incomplete, say so plainly instead of guessing."""

COMPARISON_ALIAS_REWRITES = {
    r"\bwebsocket\b": "WebSocket API",
    r"\brest\b": "REST API",
    r"\brequest response\b": "request-response",
    r"\brequest-response\b": "request-response",
}


def load_graph_module():
    spec = importlib.util.spec_from_file_location("query_concept_graph_module", GRAPH_QUERY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load graph query module from {GRAPH_QUERY_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_query_engine_module():
    buffer_out = io.StringIO()
    buffer_err = io.StringIO()
    with contextlib.redirect_stdout(buffer_out), contextlib.redirect_stderr(buffer_err):
        return importlib.import_module("query_engine")


def build_comparison_context(query_engine_module, graph_module, query: str) -> dict:
    graph = graph_module.load_json(graph_module.GRAPH_FILE)
    aliases = graph_module.load_json(graph_module.ALIASES_FILE)
    extractions = graph_module.load_json(graph_module.EXTRACTIONS_FILE)
    nodes, adjacency, lookup, pair_edges = graph_module.build_indexes(graph, aliases, extractions)

    normalized_query = query
    for pattern, replacement in COMPARISON_ALIAS_REWRITES.items():
        normalized_query = re.sub(pattern, replacement, normalized_query, flags=re.IGNORECASE)

    result = graph_module.run_comparison_mode(normalized_query, nodes, adjacency, lookup, pair_edges)
    if result.get("mode") == "comparison" and result.get("qwen_comparison_prompt"):
        return {
            "mode": "comparison",
            "context": result,
            "prompt": result["qwen_comparison_prompt"],
        }

    fallback = query_engine_module.query_engine(query)
    return {
        "mode": "semantic_fallback",
        "context": {
            "comparison_attempt": result,
            "semantic_answer": fallback,
        },
        "prompt": fallback["qwen_answer_prompt"],
    }


def build_semantic_context(query: str) -> dict:
    query_engine_module = load_query_engine_module()
    result = query_engine_module.query_engine(query)
    return {
        "mode": "semantic",
        "context": result,
        "prompt": result["qwen_answer_prompt"],
    }


def run_qwen(prompt: str) -> str:
    payload = json.dumps(
        {
            "model": QWEN_MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "temperature": 0.2,
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
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"LM Studio chat completions API returned HTTP {exc.code}: {detail}"
        ) from exc
    except error.URLError as exc:
        raise RuntimeError(
            "Could not reach LM Studio chat completions API. Ensure the local server is running."
        ) from exc

    choices = body.get("choices", [])
    answer = ""
    if choices:
        message = choices[0].get("message", {})
        answer = str(message.get("content", "")).strip()
    if not answer:
        raise RuntimeError("LM Studio returned an empty response")
    return answer


def fallback_comparison_answer(context: dict) -> str:
    left = context["concept_a"]["label"]
    right = context["concept_b"]["label"]

    lines = [f"{left} and {right} serve different interaction patterns."]

    if context.get("key_differences"):
        favored = []
        for item in context["key_differences"][:4]:
            favored.append(f"{item['dimension']}: {item['favors']}")
        lines.append("Key differences: " + "; ".join(favored) + ".")

    shared = [item["label"] for item in context.get("shared_components", [])[:4]]
    if shared:
        lines.append("Shared components: " + ", ".join(shared) + ".")

    unique_a = [item["label"] for item in context.get("unique_to_a", [])[:3]]
    if unique_a:
        lines.append(f"{left} is more associated with " + ", ".join(unique_a) + ".")

    unique_b = [item["label"] for item in context.get("unique_to_b", [])[:3]]
    if unique_b:
        lines.append(f"{right} is more associated with " + ", ".join(unique_b) + ".")

    usage = []
    seen = set()
    for item in context.get("recommended_usage", []):
        guidance = item["guidance"]
        if not isinstance(guidance, str):
            guidance = json.dumps(guidance, sort_keys=True)
        key = (item["architecture"], guidance)
        if key in seen:
            continue
        seen.add(key)
        usage.append(f"{item['architecture']}: {guidance}")
        if len(usage) == 2:
            break
    if usage:
        lines.append("Recommended usage: " + " ".join(usage))

    return "\n".join(lines)


def fallback_semantic_answer(context: dict) -> str:
    matched = context.get("matched_concepts", [])
    relations = context.get("top_relations", [])
    if not matched:
        return "I could not find a strong match in the local knowledge graph."

    top = matched[0]
    lines = [f"The strongest match is {top['concept']}."]

    components = top.get("components", [])[:5]
    if components:
        lines.append("Key AWS components: " + ", ".join(components) + ".")

    patterns = top.get("patterns", [])[:4]
    if patterns:
        lines.append("Related patterns: " + ", ".join(patterns) + ".")

    if relations:
        summaries = [
            f"{item['from_label']} {item['type']} {item['to_label']}"
            for item in relations[:3]
        ]
        lines.append("Top graph relations: " + "; ".join(summaries) + ".")

    return "\n".join(lines)


def fallback_answer(mode: str, context: dict) -> str:
    if mode == "comparison":
        return fallback_comparison_answer(context)
    if mode == "semantic_fallback":
        return fallback_semantic_answer(context["semantic_answer"])
    return fallback_semantic_answer(context)


def ask(query: str) -> dict:
    graph_module = load_graph_module()
    query_engine_module = load_query_engine_module()
    if graph_module.is_comparison_query(query):
        package = build_comparison_context(query_engine_module, graph_module, query)
    else:
        result = query_engine_module.query_engine(query)
        package = {
            "mode": "semantic",
            "context": result,
            "prompt": result["qwen_answer_prompt"],
        }

    generation_error = None
    generator = "qwen"
    try:
        answer = run_qwen(package["prompt"])
    except RuntimeError as exc:
        generation_error = str(exc)
        generator = "fallback"
        answer = fallback_answer(package["mode"], package["context"])

    return {
        "query": query,
        "mode": package["mode"],
        "generator": generator,
        "answer": answer,
        "context": package["context"],
        "generation_error": generation_error,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ask the local knowledge graph and synthesize with LM Studio Qwen."
    )
    parser.add_argument("query", help="Question to answer")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full result object instead of only the answer",
    )
    args = parser.parse_args()

    result = ask(args.query)
    if args.json:
        print(json.dumps(result, indent=2))
        return

    print(result["answer"])


if __name__ == "__main__":
    main()
