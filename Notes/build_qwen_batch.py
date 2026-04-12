import json
from pathlib import Path

from chunk_aip_c01 import (
    SYSTEM_PROMPT,
    build_prompt,
    build_semantic_sections,
    input_files,
    load_prompt_template,
    load_text,
)

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "qwen_batch_payloads.jsonl"


def main() -> None:
    template = load_prompt_template()
    sections = []
    for input_file in input_files():
        sections.extend(build_semantic_sections(load_text(input_file), input_file.name))

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        for index, section in enumerate(sections, start=1):
            record = {
                "custom_id": f"section-{index}",
                "source": section["source"],
                "section_title": section["section_title"],
                "messages": [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": build_prompt(template, section),
                    }
                ],
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {OUTPUT_FILE}")
    print(f"Records: {len(sections)}")


if __name__ == "__main__":
    main()
