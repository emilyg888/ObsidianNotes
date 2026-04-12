import json
import os
import re
from pathlib import Path
from urllib import error, request


BASE_DIR = Path(__file__).resolve().parent
EXCLUDED_INPUT_FILES = {"AGENTS.md"}
OUTPUT_FILE = BASE_DIR / "global_chunks.json"
PROMPT_FILE = BASE_DIR / "qwen_extraction_prompt.txt"
LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://127.0.0.1:1234/v1/chat/completions")
MODEL_NAME = os.getenv("LM_STUDIO_MODEL", "qwen2.5-14b-instruct")

MIN_SECTION_CHARS = 2500
MAX_SECTION_CHARS = 12000
QUESTION_BOUNDARY_PATTERNS = [
    r"^\d+/\d+\s+Question\b",
    r"^Question\b",
    r"^Official Practice Question Set:",
]
XML_NOISE_PATTERNS = [
    r"^<mxfile\b",
    r"^</mxfile>$",
    r"^<diagram\b",
    r"^</diagram>$",
    r"^<mxGraphModel\b",
    r"^</mxGraphModel>$",
    r"^<root>$",
    r"^</root>$",
    r"^<mxCell\b",
    r"^</mxCell>$",
    r"^<mxGeometry\b",
    r"^</mxGeometry>$",
]

SYSTEM_PROMPT = """You split source text into semantic chunks and extract knowledge in one pass.
Return JSON only.
Each output item must contain:
- text
- concepts
- components
- patterns
"""

DEFAULT_PROMPT = """Split the following text into coherent semantic chunks.

Rules:
- Keep related ideas together
- Do NOT split question + explanation
- Each chunk should be independently understandable
- Return JSON list
- Each item must use keys: text, concepts, components, patterns
- concepts should be abstract ideas or capabilities
- components should be concrete services, tools, or systems
- patterns should be reusable architecture or workflow patterns
"""


def load_text(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def input_files() -> list[Path]:
    return sorted(
        file_path
        for file_path in BASE_DIR.glob("*.md")
        if file_path.name not in EXCLUDED_INPUT_FILES
    )


def load_prompt_template() -> str:
    if PROMPT_FILE.exists():
        return PROMPT_FILE.read_text(encoding="utf-8").strip()
    return DEFAULT_PROMPT.strip()


def is_xml_noise_line(text: str) -> bool:
    stripped = text.strip()
    return any(re.match(pattern, stripped) for pattern in XML_NOISE_PATTERNS)


def split_markdown_blocks(text: str) -> list[tuple[str, str]]:
    blocks = []
    current_lines = []
    in_code_fence = False
    in_xml_block = False

    for line in text.splitlines():
        stripped = line.strip()

        if stripped.startswith("```"):
            current_lines.append(line)
            if in_code_fence:
                blocks.append(("code", "\n".join(current_lines).strip()))
                current_lines = []
            in_code_fence = not in_code_fence
            continue

        if in_code_fence:
            current_lines.append(line)
            continue

        if stripped.startswith("<mxfile"):
            if current_lines:
                block_text = "\n".join(current_lines).strip()
                if block_text:
                    blocks.append((classify_block(block_text), block_text))
                current_lines = []
            in_xml_block = True
            continue

        if in_xml_block:
            if stripped == "</mxfile>":
                in_xml_block = False
            continue

        if is_xml_noise_line(stripped):
            continue

        if re.fullmatch(r"[-*_]{3,}", stripped):
            if current_lines:
                block_text = "\n".join(current_lines).strip()
                if block_text:
                    blocks.append((classify_block(block_text), block_text))
                current_lines = []
            blocks.append(("separator", stripped))
            continue

        if not stripped:
            if current_lines:
                block_text = "\n".join(current_lines).strip()
                if block_text:
                    blocks.append((classify_block(block_text), block_text))
                current_lines = []
            continue

        current_lines.append(line)

    if current_lines:
        block_text = "\n".join(current_lines).strip()
        blocks.append(("code" if in_code_fence else classify_block(block_text), block_text))

    return blocks


def classify_block(block_text: str) -> str:
    first_line = block_text.splitlines()[0].strip()
    if re.match(r"^#{1,6}\s+", first_line):
        return "heading"
    if re.match(r"^\s*([-*+]|\d+[.)])\s+", first_line):
        return "list"
    return "paragraph"


def heading_level(block_text: str) -> int | None:
    match = re.match(r"^(#{1,6})\s+", block_text.strip())
    if not match:
        return None
    return len(match.group(1))


def clean_heading(block_text: str) -> str:
    return re.sub(r"^#{1,6}\s*", "", block_text.strip())


def normalize_phrase(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def is_question_boundary(text: str) -> bool:
    candidate = normalize_phrase(text)
    return any(re.match(pattern, candidate) for pattern in QUESTION_BOUNDARY_PATTERNS)


def build_semantic_sections(text: str, source_name: str) -> list[dict]:
    sections = []
    current_blocks: list[str] = []
    current_chars = 0
    current_title = source_name
    section_index = 1

    def flush() -> None:
        nonlocal current_blocks, current_chars, section_index
        if not current_blocks:
            return
        section_text = "\n\n".join(current_blocks).strip()
        if section_text:
            sections.append(
                {
                    "section_id": section_index,
                    "source": source_name,
                    "section_title": current_title,
                    "text": section_text,
                }
            )
            section_index += 1
        current_blocks = []
        current_chars = 0

    for block_type, block_text in split_markdown_blocks(text):
        if block_type == "separator":
            if current_chars >= MIN_SECTION_CHARS:
                flush()
            continue

        stripped = block_text.strip()
        if not stripped:
            continue

        level = heading_level(stripped) if block_type == "heading" else None
        boundary = block_type == "heading" and level is not None and level <= 2
        question_boundary = is_question_boundary(stripped)

        if (boundary or question_boundary) and current_blocks and current_chars >= MIN_SECTION_CHARS:
            flush()

        if block_type == "heading":
            current_title = clean_heading(stripped) or source_name

        if current_blocks and current_chars + len(stripped) > MAX_SECTION_CHARS:
            flush()

        current_blocks.append(stripped)
        current_chars += len(stripped) + 2

    flush()

    if not sections and text.strip():
        sections.append(
            {
                "section_id": 1,
                "source": source_name,
                "section_title": source_name,
                "text": text.strip(),
            }
        )

    return sections


def build_prompt(template: str, section: dict) -> str:
    return (
        f"{template.strip()}\n\n"
        f"Source: {section['source']}\n"
        f"Section: {section['section_title']}\n\n"
        f"Text:\n{section['text']}"
    )


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
            for key in ("chunks", "items", "results"):
                value = parsed.get(key)
                if isinstance(value, list):
                    return value

    raise ValueError("LM Studio response did not contain a JSON list of chunks")


def run_qwen_chunking(prompt: str) -> list[dict]:
    payload = json.dumps(
        {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
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
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"LM Studio chat completions API returned HTTP {exc.code}: {detail}"
        ) from exc
    except error.URLError as exc:
        raise RuntimeError(
            "Could not reach LM Studio chat completions API. Ensure the local server is running."
        ) from exc

    content = read_message_content(body)
    if not content:
        raise RuntimeError("LM Studio returned an empty response")
    return parse_json_list(content)


def normalize_list(items: object) -> list[str]:
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


def generate_title(chunk_text_value: str) -> str:
    cleaned = re.sub(r"`{1,3}", "", chunk_text_value)
    cleaned = re.sub(r"^#{1,6}\s*", "", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
    cleaned = normalize_phrase(cleaned)
    return " ".join(cleaned.split()[:10])


def generate_summary(chunk_text_value: str, word_limit: int = 24) -> str:
    cleaned = re.sub(r"`{1,3}", "", chunk_text_value)
    cleaned = re.sub(r"^#{1,6}\s*", "", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
    cleaned = normalize_phrase(cleaned)
    return " ".join(cleaned.split()[:word_limit])


def normalize_model_chunks(raw_chunks: list[dict], section: dict) -> list[dict]:
    normalized = []
    for item in raw_chunks:
        if not isinstance(item, dict):
            continue
        text = normalize_phrase(str(item.get("text", "")))
        if not text:
            continue
        normalized.append(
            {
                "source": section["source"],
                "section_title": section["section_title"],
                "full_text": text,
                "concepts": normalize_list(item.get("concepts", [])),
                "components": normalize_list(item.get("components", [])),
                "patterns": normalize_list(item.get("patterns", [])),
            }
        )
    return normalized


def build_output(records: list[dict]) -> list[dict]:
    output = []
    for index, record in enumerate(records, start=1):
        text = record["full_text"]
        output.append(
            {
                "chunk_id": index,
                "title": generate_title(text),
                "sources": [record["source"]],
                "section_title": record["section_title"],
                "sentence_count": max(1, len(re.split(r"(?<=[.!?])\s+", text))),
                "context_summary": generate_summary(text),
                "full_text": text,
                "concepts": record["concepts"],
                "components": record["components"],
                "patterns": record["patterns"],
            }
        )

    for index, chunk in enumerate(output):
        chunk["prev_chunk_summary"] = output[index - 1]["context_summary"] if index > 0 else None
        chunk["next_chunk_summary"] = (
            output[index + 1]["context_summary"] if index < len(output) - 1 else None
        )

    return output


def main() -> None:
    files = input_files()
    print(f"Found {len(files)} markdown files in {BASE_DIR}")
    for input_file in files:
        print(f"- {input_file.name}")

    template = load_prompt_template()
    sections = []
    for input_file in files:
        sections.extend(build_semantic_sections(load_text(input_file), input_file.name))

    print(f"Prepared {len(sections)} semantic sections")

    raw_chunk_records = []
    for index, section in enumerate(sections, start=1):
        print(
            f"[{index}/{len(sections)}] "
            f"{section['source']} :: {section['section_title']}"
        )
        prompt = build_prompt(template, section)
        raw_chunks = run_qwen_chunking(prompt)
        normalized_chunks = normalize_model_chunks(raw_chunks, section)
        if not normalized_chunks:
            raise RuntimeError(
                f"No valid semantic chunks returned for {section['source']} :: {section['section_title']}"
            )
        raw_chunk_records.extend(normalized_chunks)

    output = build_output(raw_chunk_records)
    OUTPUT_FILE.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Done -> {OUTPUT_FILE}")
    print(f"Chunks written: {len(output)}")


if __name__ == "__main__":
    main()
