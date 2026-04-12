import json
import re
from collections import defaultdict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "global_chunks.json"
OUTPUT_FILE = BASE_DIR / "global_extractions.json"
PROMPT_FILE = BASE_DIR / "qwen_extraction_prompt.txt"
GRAPH_FILE = BASE_DIR / "concept_graph.json"
ALIASES_FILE = BASE_DIR / "concept_aliases.json"


COMPONENT_PATTERNS = [
    r"\bAmazon\s+[A-Z][A-Za-z0-9@.-]+(?:\s+[A-Z][A-Za-z0-9@.-]+){0,4}\b",
    r"\bAWS\s+[A-Z][A-Za-z0-9@.-]+(?:\s+[A-Z][A-Za-z0-9@.-]+){0,4}\b",
    r"\bAPI Gateway\b",
    r"\bLambda\b",
    r"\bDynamoDB\b",
    r"\bOpenSearch(?: Service)?\b",
    r"\bStep Functions\b",
    r"\bSecrets Manager\b",
    r"\bCloudWatch(?: Logs| Logs Insights)?\b",
    r"\bX-Ray\b",
    r"\bSageMaker(?: AI| Processing| Model Registry| JumpStart)?\b",
]

CONCEPT_TERMS = [
    "foundation model integration",
    "model selection",
    "model routing",
    "provider switching",
    "prompt engineering",
    "prompt management",
    "prompt chaining",
    "rag",
    "retrieval augmented generation",
    "vector database",
    "vector store",
    "vector search",
    "semantic retrieval",
    "knowledge base",
    "agentic ai",
    "multi-agent",
    "agent orchestration",
    "memory",
    "session memory",
    "long-term memory",
    "evaluation",
    "model evaluation",
    "validation",
    "guardrails",
    "responsible ai",
    "security",
    "governance",
    "compliance",
    "observability",
    "monitoring",
    "cost optimization",
    "performance optimization",
    "troubleshooting",
    "latency optimization",
    "streaming responses",
    "response streaming",
    "api design",
    "event-driven architecture",
    "serverless",
    "ci/cd",
    "cross-region inference",
    "circuit breaker",
    "graceful degradation",
]

PATTERN_TERMS = [
    "api gateway + lambda",
    "rest api",
    "websocket",
    "request-response",
    "asynchronous processing",
    "event-driven architecture",
    "pub/sub",
    "batch processing",
    "step functions workflow",
    "circuit breaker",
    "cross-region inference",
    "prompt chaining",
    "model routing",
    "provider switching",
    "rag",
    "vector search",
    "semantic retrieval",
    "serverless architecture",
    "ci/cd pipeline",
    "streaming responses",
    "response streaming",
    "caching",
    "multi-agent orchestration",
    "knowledge base retrieval",
    "tool use",
]

COMPONENT_CANONICAL_MAP = {
    "lambda": "AWS Lambda",
    "aws lambda": "AWS Lambda",
    "api gateway": "Amazon API Gateway",
    "amazon api gateway": "Amazon API Gateway",
    "amazon api gateway rest api": "Amazon API Gateway",
    "amazon api gateway rest apis": "Amazon API Gateway",
    "dynamodb": "Amazon DynamoDB",
    "amazon dynamodb": "Amazon DynamoDB",
    "opensearch": "Amazon OpenSearch Service",
    "opensearch service": "Amazon OpenSearch Service",
    "amazon opensearch service": "Amazon OpenSearch Service",
    "step functions": "AWS Step Functions",
    "aws step functions": "AWS Step Functions",
    "cloudwatch": "Amazon CloudWatch",
    "amazon cloudwatch": "Amazon CloudWatch",
    "cloudwatch logs": "Amazon CloudWatch Logs",
    "amazon cloudwatch logs": "Amazon CloudWatch Logs",
    "secrets manager": "AWS Secrets Manager",
    "aws secrets manager": "AWS Secrets Manager",
    "sagemaker": "Amazon SageMaker AI",
    "sagemaker ai": "Amazon SageMaker AI",
    "amazon sagemaker ai": "Amazon SageMaker AI",
    "bedrock": "Amazon Bedrock",
    "amazon bedrock": "Amazon Bedrock",
    "amazon bedrock fm": "Amazon Bedrock",
    "amazon bedrock api": "Amazon Bedrock",
    "amazon comprehend pii": "Amazon Comprehend",
    "amazon comprehend": "Amazon Comprehend",
}

CONCEPT_CANONICAL_MAP = {
    "rag": "retrieval augmented generation (RAG)",
    "retrieval augmented generation": "retrieval augmented generation (RAG)",
    "ci/cd": "CI/CD",
    "vector database": "vector store",
    "streaming responses": "response streaming",
    "knowledge base retrieval": "knowledge base",
    "evaluation": "model evaluation",
}

PATTERN_CANONICAL_MAP = {
    "rag": "retrieval augmented generation (RAG)",
    "websocket": "WebSocket API",
    "rest api": "REST API",
    "ci/cd pipeline": "CI/CD pipeline",
    "pub/sub": "publish-subscribe",
    "semantic retrieval": "vector search",
    "streaming responses": "response streaming",
    "knowledge base retrieval": "retrieval augmented generation (RAG)",
}

NOISY_COMPONENTS = {
    "aws documentation",
    "aws certified generative ai developer",
}

CONCEPT_ALIAS_MAP = {
    "retrieval augmented generation (RAG)": ["rag", "retrieval augmented generation"],
    "vector store": ["vector database", "vector store"],
    "response streaming": ["streaming responses", "response streaming"],
    "CI/CD": ["ci/cd"],
    "knowledge base": ["knowledge base", "knowledge base retrieval"],
}

PATTERN_ALIAS_MAP = {
    "retrieval augmented generation (RAG)": ["rag", "knowledge base retrieval"],
    "vector search": ["vector search", "semantic retrieval"],
    "response streaming": ["streaming responses", "response streaming"],
    "REST API": ["rest api"],
    "WebSocket API": ["websocket"],
    "publish-subscribe": ["pub/sub"],
    "CI/CD pipeline": ["ci/cd pipeline"],
}

PATTERN_NAME_MAP = {
    "retrieval augmented generation (RAG)": "Retrieval Augmented Generation",
    "vector search": "Vector Search",
    "response streaming": "Response Streaming",
    "REST API": "REST API Integration",
    "WebSocket API": "WebSocket Streaming",
    "api gateway + lambda": "API Gateway Plus Lambda",
    "step functions workflow": "Step Functions Workflow",
    "event-driven architecture": "Event-Driven Architecture",
    "batch processing": "Batch Processing",
    "model routing": "Model Routing",
    "caching": "Caching Layer",
    "provider switching": "Provider Switching",
    "cross-region inference": "Cross-Region Inference",
    "circuit breaker": "Circuit Breaker",
    "prompt chaining": "Prompt Chaining",
    "request-response": "Request Response",
    "asynchronous processing": "Asynchronous Processing",
    "serverless architecture": "Serverless Architecture",
    "publish-subscribe": "Publish Subscribe",
    "CI/CD pipeline": "CI/CD Pipeline",
}

COMPARISON_RULES = [
    {
        "left": "WebSocket API",
        "right": "REST API",
        "dimensions": {
            "real_time": "WebSocket API",
            "bidirectional": "WebSocket API",
            "simplicity": "REST API",
            "request_response": "REST API",
        },
        "recommended_usage": {
            "WebSocket API": [
                "Use when the client needs a persistent connection for real-time or bidirectional updates.",
                "Prefer when low-latency incremental delivery matters more than stateless simplicity.",
            ],
            "REST API": [
                "Use for synchronous stateless request-response inference and standard API integrations.",
                "Prefer when implementation simplicity and broad client compatibility matter most.",
            ],
        },
    },
    {
        "left": "request-response",
        "right": "asynchronous processing",
        "dimensions": {
            "latency": "request-response",
            "decoupling": "asynchronous processing",
            "throughput": "asynchronous processing",
            "simplicity": "request-response",
        },
        "recommended_usage": {
            "request-response": [
                "Use when the caller needs an immediate answer and the workflow fits a synchronous boundary.",
                "Prefer for simpler low-latency inference calls with direct user interaction.",
            ],
            "asynchronous processing": [
                "Use for long-running or bursty workloads where producers and consumers should be decoupled.",
                "Prefer when resilience and throughput matter more than immediate completion.",
            ],
        },
    },
    {
        "left": "response streaming",
        "right": "batch processing",
        "dimensions": {
            "time_to_first_token": "response streaming",
            "offline_throughput": "batch processing",
            "interactive_ux": "response streaming",
            "large_scale_jobs": "batch processing",
        },
        "recommended_usage": {
            "response streaming": [
                "Use when the user should see output as it is generated.",
                "Prefer for interactive copilots, chat, and progressive delivery experiences.",
            ],
            "batch processing": [
                "Use for offline bulk jobs where aggregate throughput matters more than immediate feedback.",
                "Prefer for scheduled processing and large backfills.",
            ],
        },
    },
]

CONCEPT_CANONICAL_SPECS = {
    "retrieval augmented generation (RAG)": {
        "id": "retrieval_augmented_generation",
        "aliases": ["rag", "retrieval augmented generation"],
    },
    "model evaluation": {
        "id": "model_evaluation",
        "aliases": ["evaluation", "eval", "model eval"],
    },
    "vector store": {
        "id": "vector_store",
        "aliases": ["vector database", "vector db", "vector store"],
    },
    "response streaming": {
        "id": "response_streaming",
        "aliases": ["streaming responses", "response streaming"],
    },
    "knowledge base": {
        "id": "knowledge_base",
        "aliases": ["knowledge base", "knowledge base retrieval"],
    },
    "CI/CD": {
        "id": "ci_cd",
        "aliases": ["ci/cd", "continuous integration", "continuous delivery"],
    },
}

COMPONENT_FAMILY_KEYWORDS = [
    ("knowledge base", ["knowledge base", "kendra"]),
    ("prompt management", ["prompt management", "prompt flows"]),
    ("vector store", ["opensearch", "vector", "embeddings"]),
    ("orchestration", ["step functions", "agentcore", "agent squad"]),
    ("compute", ["lambda", "ecs", "ec2", "fargate", "app runner"]),
    ("api interface", ["api gateway", "websocket"]),
    ("observability", ["cloudwatch", "x-ray", "cloudtrail", "grafana"]),
    ("security", ["secrets manager", "macie", "kms", "cognito", "organizations"]),
    ("database", ["dynamodb", "aurora", "rds", "documentdb"]),
    ("data processing", ["glue", "textract", "comprehend", "datasync"]),
    ("foundation model platform", ["bedrock", "titan", "nova"]),
    ("model lifecycle", ["sagemaker", "model monitor", "jumpstart"]),
]


def load_chunks(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_phrase(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def title_case_if_upper(name: str) -> str:
    return name.title() if name.isupper() and len(name) > 4 else name


def clean_component_name(name: str) -> str:
    value = normalize_phrase(name)
    value = re.split(r"[.!?]\s+", value, maxsplit=1)[0]
    value = re.sub(r"[,:;]+$", "", value)
    value = re.sub(r"\s+\.\s*the$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"\.\s*the$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"\s+\(.*?\)$", "", value)
    return value.strip()


def canonicalize(name: str, mapping: dict[str, str]) -> str:
    key = normalize_phrase(name).lower()
    return mapping.get(key, name)


def normalize_string_list(items: object) -> list[str]:
    if not isinstance(items, list):
        return []
    values = []
    seen = set()
    for item in items:
        if not isinstance(item, str):
            continue
        value = normalize_phrase(item)
        if not value:
            continue
        lowered = value.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        values.append(value)
    return values


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return slug or "item"


def find_components(text: str) -> list[str]:
    found = set()
    for pattern in COMPONENT_PATTERNS:
        for match in re.findall(pattern, text):
            value = title_case_if_upper(clean_component_name(match))
            if len(value) >= 3:
                value = canonicalize(value, COMPONENT_CANONICAL_MAP)
                if value.lower() in NOISY_COMPONENTS:
                    continue
                found.add(value)
    return sorted(found)


def find_terms(text: str, candidates: list[str]) -> list[str]:
    lowered = text.lower()
    found = []
    for term in candidates:
        if term.lower() in lowered:
            found.append(term)
    return sorted(set(found))


def canonicalize_terms(items: list[str], mapping: dict[str, str]) -> list[str]:
    return sorted({canonicalize(item, mapping) for item in items})


def infer_component_families(components: list[str]) -> list[str]:
    families = set()
    for component in components:
        lowered = component.lower()
        for family, keywords in COMPONENT_FAMILY_KEYWORDS:
            if any(keyword in lowered for keyword in keywords):
                families.add(family)
    return sorted(families)


def build_chunk_record(chunk: dict) -> dict:
    combined_text = " ".join(
        part
        for part in [
            chunk.get("prev_chunk_summary") or "",
            chunk.get("full_text") or "",
            chunk.get("next_chunk_summary") or "",
        ]
        if part
    )
    provided_components = []
    for component in normalize_string_list(chunk.get("components")):
        value = title_case_if_upper(clean_component_name(component))
        if len(value) < 3:
            continue
        value = canonicalize(value, COMPONENT_CANONICAL_MAP)
        if value.lower() in NOISY_COMPONENTS:
            continue
        provided_components.append(value)

    provided_concepts = canonicalize_terms(
        normalize_string_list(chunk.get("concepts")),
        CONCEPT_CANONICAL_MAP,
    )
    provided_patterns = canonicalize_terms(
        normalize_string_list(chunk.get("patterns")),
        PATTERN_CANONICAL_MAP,
    )

    components = sorted(set(provided_components)) if provided_components else find_components(combined_text)
    concepts = (
        sorted(set(provided_concepts))
        if provided_concepts
        else canonicalize_terms(find_terms(combined_text, CONCEPT_TERMS), CONCEPT_CANONICAL_MAP)
    )
    patterns = (
        sorted(set(provided_patterns))
        if provided_patterns
        else canonicalize_terms(find_terms(combined_text, PATTERN_TERMS), PATTERN_CANONICAL_MAP)
    )

    return {
        "chunk_id": chunk["chunk_id"],
        "title": chunk["title"],
        "sources": chunk["sources"],
        "prev_chunk_summary": chunk.get("prev_chunk_summary"),
        "next_chunk_summary": chunk.get("next_chunk_summary"),
        "concepts": concepts,
        "components": components,
        "component_families": infer_component_families(components),
        "patterns": patterns,
    }


def roll_up(chunk_records: list[dict], key: str) -> list[dict]:
    index = defaultdict(lambda: {"count": 0, "chunks": set(), "sources": set()})

    for record in chunk_records:
        for item in record[key]:
            index[item]["count"] += 1
            index[item]["chunks"].add(record["chunk_id"])
            index[item]["sources"].update(record["sources"])

    rolled = []
    for name, meta in index.items():
        rolled.append(
            {
                "name": name,
                "count": meta["count"],
                "chunks": sorted(meta["chunks"]),
                "sources": sorted(meta["sources"]),
            }
        )

    return sorted(rolled, key=lambda item: (-item["count"], item["name"]))


def build_concept_index(chunk_records: list[dict]) -> list[dict]:
    index = defaultdict(
        lambda: {
            "frequency": 0,
            "chunks": set(),
            "sources": set(),
            "related_components": defaultdict(int),
            "related_component_families": defaultdict(int),
            "related_patterns": defaultdict(int),
        }
    )

    for record in chunk_records:
        for concept in record["concepts"]:
            meta = index[concept]
            meta["frequency"] += 1
            meta["chunks"].add(record["chunk_id"])
            meta["sources"].update(record["sources"])
            for component in record["components"]:
                meta["related_components"][component] += 1
            for family in record["component_families"]:
                meta["related_component_families"][family] += 1
            for pattern in record["patterns"]:
                meta["related_patterns"][pattern] += 1

    results = []
    for concept, meta in index.items():
        results.append(
            {
                "concept": concept,
                "aliases": CONCEPT_CANONICAL_SPECS.get(
                    concept,
                    {"aliases": CONCEPT_ALIAS_MAP.get(concept, [])},
                )["aliases"],
                "frequency": meta["frequency"],
                "related_components": [
                    name
                    for name, _ in sorted(
                        meta["related_components"].items(),
                        key=lambda item: (-item[1], item[0]),
                    )[:8]
                ],
                "related_component_families": [
                    name
                    for name, _ in sorted(
                        meta["related_component_families"].items(),
                        key=lambda item: (-item[1], item[0]),
                    )[:6]
                ],
                "related_patterns": [
                    name
                    for name, _ in sorted(
                        meta["related_patterns"].items(),
                        key=lambda item: (-item[1], item[0]),
                    )[:6]
                ],
                "source_count": len(meta["sources"]),
                "pattern_link_count": len(meta["related_patterns"]),
                "component_link_count": len(meta["related_components"]),
                "chunks": sorted(meta["chunks"]),
                "sources": sorted(meta["sources"]),
            }
        )

    max_frequency = max((item["frequency"] for item in results), default=1)
    max_source_count = max((item["source_count"] for item in results), default=1)
    max_pattern_links = max((item["pattern_link_count"] for item in results), default=1)
    max_component_links = max((item["component_link_count"] for item in results), default=1)

    for item in results:
        frequency_score = item["frequency"] / max_frequency
        source_score = item["source_count"] / max_source_count
        pattern_score = item["pattern_link_count"] / max_pattern_links
        component_score = item["component_link_count"] / max_component_links
        item["confidence"] = round(
            0.4 * frequency_score
            + 0.2 * source_score
            + 0.2 * pattern_score
            + 0.2 * component_score,
            2,
        )

    return sorted(results, key=lambda item: (-item["frequency"], item["concept"]))


def build_pattern_registry(chunk_records: list[dict]) -> list[dict]:
    index = defaultdict(
        lambda: {
            "frequency": 0,
            "chunks": set(),
            "sources": set(),
            "concepts": defaultdict(int),
            "components": defaultdict(int),
            "families": defaultdict(int),
        }
    )

    for record in chunk_records:
        for pattern in record["patterns"]:
            meta = index[pattern]
            meta["frequency"] += 1
            meta["chunks"].add(record["chunk_id"])
            meta["sources"].update(record["sources"])
            for concept in record["concepts"]:
                meta["concepts"][concept] += 1
            for component in record["components"]:
                meta["components"][component] += 1
            for family in record["component_families"]:
                meta["families"][family] += 1

    max_frequency = max((meta["frequency"] for meta in index.values()), default=1)
    results = []
    for pattern, meta in index.items():
        used_in = [
            name
            for name, _ in sorted(
                meta["concepts"].items(),
                key=lambda item: (-item[1], item[0]),
            )
            if name != pattern
        ][:4]
        if not used_in:
            used_in = [
                name
                for name, _ in sorted(
                    meta["families"].items(),
                    key=lambda item: (-item[1], item[0]),
                )
            ][:4]

        confidence = round(meta["frequency"] / max_frequency, 2)

        results.append(
            {
                "pattern_id": slugify(pattern),
                "name": PATTERN_NAME_MAP.get(pattern, pattern.title()),
                "structure": pattern,
                "aliases": PATTERN_ALIAS_MAP.get(pattern, []),
                "used_in": used_in,
                "related_components": [
                    name
                    for name, _ in sorted(
                        meta["components"].items(),
                        key=lambda item: (-item[1], item[0]),
                    )[:6]
                ],
                "confidence": confidence,
                "frequency": meta["frequency"],
                "chunks": sorted(meta["chunks"]),
                "sources": sorted(meta["sources"]),
            }
        )

    return sorted(results, key=lambda item: (-item["frequency"], item["name"]))


def build_concept_component_map(concept_index: list[dict]) -> list[dict]:
    return [
        {
            "concept": item["concept"],
            "components": item["related_components"],
            "component_families": item["related_component_families"],
            "patterns": item["related_patterns"],
            "frequency": item["frequency"],
            "confidence": item["confidence"],
        }
        for item in concept_index
    ]


def concept_id(concept: str) -> str:
    return CONCEPT_CANONICAL_SPECS.get(concept, {}).get("id", slugify(concept))


def component_id(component: str) -> str:
    return slugify(component)


def build_concept_aliases(concept_index: list[dict]) -> list[dict]:
    aliases = []
    for item in concept_index:
        aliases.append(
            {
                "canonical": concept_id(item["concept"]),
                "label": item["concept"],
                "aliases": item["aliases"],
                "frequency": item["frequency"],
                "confidence": item["confidence"],
            }
        )
    return aliases


def build_membership_index(chunk_records: list[dict], key: str) -> dict[str, dict[str, set]]:
    index = defaultdict(lambda: {"chunks": set(), "sources": set()})
    for record in chunk_records:
        for item in record[key]:
            index[item]["chunks"].add(record["chunk_id"])
            index[item]["sources"].update(record["sources"])
    return index


def build_comparison_edges(pattern_registry: list[dict]) -> list[dict]:
    patterns = {item["structure"]: item for item in pattern_registry}
    edges = []

    for rule in COMPARISON_RULES:
        left = patterns.get(rule["left"])
        right = patterns.get(rule["right"])
        if not left or not right:
            continue

        left_components = set(left["related_components"])
        right_components = set(right["related_components"])
        left_sources = set(left["sources"])
        right_sources = set(right["sources"])
        left_used_in = set(left["used_in"])
        right_used_in = set(right["used_in"])

        component_overlap = len(left_components & right_components) / max(
            len(left_components | right_components), 1
        )
        source_overlap = len(left_sources & right_sources) / max(len(left_sources | right_sources), 1)
        concept_overlap = len(left_used_in & right_used_in) / max(len(left_used_in | right_used_in), 1)
        dimension_score = min(len(rule["dimensions"]) / 4, 1.0)
        confidence = round(
            0.45
            + 0.25 * component_overlap
            + 0.15 * source_overlap
            + 0.05 * concept_overlap
            + 0.10 * dimension_score,
            2,
        )

        shared_components = sorted(left_components & right_components)
        shared_sources = sorted(left_sources & right_sources)
        shared_used_in = sorted(left_used_in & right_used_in)
        dimensions = {
            key: left["pattern_id"] if winner == rule["left"] else right["pattern_id"]
            for key, winner in rule["dimensions"].items()
        }
        recommended_usage = {}
        for label, guidance in rule["recommended_usage"].items():
            node_id = left["pattern_id"] if label == rule["left"] else right["pattern_id"]
            recommended_usage[node_id] = guidance

        base_payload = {
            "from": left["pattern_id"],
            "to": right["pattern_id"],
            "confidence": confidence,
            "evidence_count": len(shared_components),
            "source_diversity": len(shared_sources),
            "shared_components": shared_components,
            "shared_sources": shared_sources,
            "shared_contexts": shared_used_in,
        }

        edges.append(base_payload | {"type": "contrasts_with"})
        edges.append(
            base_payload
            | {
                "type": "tradeoff",
                "dimensions": dimensions,
                "recommended_usage": recommended_usage,
            }
        )

    return edges


def build_concept_graph(
    chunk_records: list[dict],
    concept_index: list[dict],
    pattern_registry: list[dict],
) -> dict:
    nodes = {}
    raw_edges = []

    def add_node(node_id: str, node_type: str, label: str, **extra) -> None:
        payload = {"id": node_id, "type": node_type, "label": label}
        payload.update(extra)
        nodes[node_id] = payload

    def add_edge(
        from_id: str,
        to_id: str,
        edge_type: str,
        left_chunks: set,
        right_chunks: set,
        left_sources: set,
        right_sources: set,
    ) -> None:
        shared_chunks = left_chunks & right_chunks
        shared_sources = left_sources & right_sources
        if not shared_chunks:
            return
        raw_edges.append(
            {
                "from": from_id,
                "to": to_id,
                "type": edge_type,
                "evidence_count": len(shared_chunks),
                "source_diversity": len(shared_sources),
            }
        )

    concept_membership = {
        item["concept"]: {
            "chunks": set(item["chunks"]),
            "sources": set(item["sources"]),
        }
        for item in concept_index
    }
    pattern_membership = {
        item["structure"]: {
            "chunks": set(item["chunks"]),
            "sources": set(item["sources"]),
            "confidence": item["confidence"],
            "name": item["name"],
        }
        for item in pattern_registry
    }
    component_membership = build_membership_index(chunk_records, "components")

    for concept in concept_index:
        c_id = concept_id(concept["concept"])
        add_node(
            c_id,
            "concept",
            concept["concept"],
            confidence=concept["confidence"],
        )
        concept_chunks = concept_membership[concept["concept"]]["chunks"]
        concept_sources = concept_membership[concept["concept"]]["sources"]

        for component in concept["related_components"]:
            comp_id = component_id(component)
            add_node(comp_id, "component", component)
            add_edge(
                c_id,
                comp_id,
                "implemented_by",
                concept_chunks,
                component_membership[component]["chunks"],
                concept_sources,
                component_membership[component]["sources"],
            )

        for pattern in concept["related_patterns"]:
            pat_id = slugify(pattern)
            pattern_info = pattern_membership[pattern]
            add_node(
                pat_id,
                "pattern",
                pattern_info["name"],
                confidence=pattern_info["confidence"],
            )
            add_edge(
                c_id,
                pat_id,
                "realized_as",
                concept_chunks,
                pattern_info["chunks"],
                concept_sources,
                pattern_info["sources"],
            )

    for pattern in pattern_registry:
        pat_id = pattern["pattern_id"]
        add_node(
            pat_id,
            "pattern",
            pattern["name"],
            confidence=pattern["confidence"],
        )
        pattern_chunks = pattern_membership[pattern["structure"]]["chunks"]
        pattern_sources = pattern_membership[pattern["structure"]]["sources"]
        for component in pattern["related_components"]:
            comp_id = component_id(component)
            add_node(comp_id, "component", component)
            add_edge(
                pat_id,
                comp_id,
                "uses",
                pattern_chunks,
                component_membership[component]["chunks"],
                pattern_sources,
                component_membership[component]["sources"],
            )

    max_evidence = max((edge["evidence_count"] for edge in raw_edges), default=1)
    max_source_diversity = max((edge["source_diversity"] for edge in raw_edges), default=1)
    edges = []
    for edge in raw_edges:
        cooccurrence_score = edge["evidence_count"] / max_evidence
        source_score = edge["source_diversity"] / max_source_diversity
        edge["confidence"] = round(0.7 * cooccurrence_score + 0.3 * source_score, 2)
        edges.append(edge)

    comparison_edges = build_comparison_edges(pattern_registry)
    edges.extend(comparison_edges)

    return {
        "nodes": sorted(nodes.values(), key=lambda item: (item["type"], item["id"])),
        "edges": sorted(edges, key=lambda item: (item["from"], item["to"], item["type"])),
    }


def write_prompt_template(path: Path) -> None:
    prompt = """Split the following text into coherent semantic chunks.

Rules:
- Keep related ideas together
- Do NOT split question + explanation
- Each chunk should be independently understandable
- Return JSON list
- Each item must use keys: text, concepts, components, patterns
- concepts should be abstract ideas or capabilities
- components should be concrete services, tools, or systems
- patterns should be reusable architecture or workflow patterns

Text:
...
"""
    path.write_text(prompt, encoding="utf-8")


def main() -> None:
    chunks = load_chunks(INPUT_FILE)
    chunk_records = [build_chunk_record(chunk) for chunk in chunks]
    concept_index = build_concept_index(chunk_records)
    pattern_registry = build_pattern_registry(chunk_records)
    concept_component_map = build_concept_component_map(concept_index)
    concept_aliases = build_concept_aliases(concept_index)
    concept_graph = build_concept_graph(chunk_records, concept_index, pattern_registry)
    comparison_registry = [edge for edge in concept_graph["edges"] if edge["type"] == "tradeoff"]

    output = {
        "metadata": {
            "input_file": INPUT_FILE.name,
            "chunk_count": len(chunks),
        },
        "chunk_extractions": chunk_records,
        "global_concepts": roll_up(chunk_records, "concepts"),
        "global_components": roll_up(chunk_records, "components"),
        "global_component_families": roll_up(chunk_records, "component_families"),
        "global_patterns": roll_up(chunk_records, "patterns"),
        "global_concept_index": concept_index,
        "pattern_registry": pattern_registry,
        "concept_component_map": concept_component_map,
        "concept_aliases": concept_aliases,
        "comparison_registry": comparison_registry,
    }

    OUTPUT_FILE.write_text(json.dumps(output, indent=2), encoding="utf-8")
    GRAPH_FILE.write_text(json.dumps(concept_graph, indent=2), encoding="utf-8")
    ALIASES_FILE.write_text(json.dumps(concept_aliases, indent=2), encoding="utf-8")
    write_prompt_template(PROMPT_FILE)
    print(f"Wrote {OUTPUT_FILE}")
    print(f"Wrote {GRAPH_FILE}")
    print(f"Wrote {ALIASES_FILE}")
    print(f"Wrote {PROMPT_FILE}")
    print(f"Chunks processed: {len(chunks)}")
    print(f"Global concepts: {len(output['global_concepts'])}")
    print(f"Global components: {len(output['global_components'])}")
    print(f"Global component families: {len(output['global_component_families'])}")
    print(f"Global patterns: {len(output['global_patterns'])}")
    print(f"Global concept index: {len(output['global_concept_index'])}")
    print(f"Pattern registry: {len(output['pattern_registry'])}")
    print(f"Concept component map: {len(output['concept_component_map'])}")
    print(f"Concept aliases: {len(output['concept_aliases'])}")
    print(f"Comparison registry: {len(output['comparison_registry'])}")
    print(f"Graph nodes: {len(concept_graph['nodes'])}")
    print(f"Graph edges: {len(concept_graph['edges'])}")


if __name__ == "__main__":
    main()
