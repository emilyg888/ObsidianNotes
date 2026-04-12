import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
EXTRACTIONS_FILE = BASE_DIR / "Notes" / "global_extractions.json"
SEARCH_INDEX_FILE = BASE_DIR / "Notes" / "concept_search_index.json"
CONCEPT_LIST_FILE = BASE_DIR / "Notes" / "concept_list.json"


def main() -> None:
    data = json.loads(EXTRACTIONS_FILE.read_text(encoding="utf-8"))
    concept_index = data["global_concept_index"]

    concepts = []
    concept_names = []
    for item in concept_index:
        concept_names.append(item["concept"])
        concepts.append(
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

    SEARCH_INDEX_FILE.write_text(json.dumps(concepts, indent=2), encoding="utf-8")
    CONCEPT_LIST_FILE.write_text(json.dumps(concept_names, indent=2), encoding="utf-8")

    print(f"Wrote {SEARCH_INDEX_FILE}")
    print(f"Wrote {CONCEPT_LIST_FILE}")
    print(f"Concepts indexed: {len(concepts)}")


if __name__ == "__main__":
    main()
