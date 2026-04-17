"""Loads concept/pattern data once at startup for agent context injection."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
EXTRACTIONS_FILE = REPO_ROOT / "Notes" / "global_extractions.json"
GRAPH_FILE = REPO_ROOT / "Notes" / "concept_graph.json"


class KnowledgeContext:
    def __init__(self) -> None:
        self._extractions: dict[str, Any] = {}
        self._graph: dict[str, Any] = {}
        self._concept_index: dict[str, dict[str, Any]] = {}
        self._pattern_index: dict[str, dict[str, Any]] = {}
        self._load()

    def _load(self) -> None:
        if EXTRACTIONS_FILE.exists():
            self._extractions = json.loads(
                EXTRACTIONS_FILE.read_text(encoding="utf-8")
            )
        if GRAPH_FILE.exists():
            self._graph = json.loads(GRAPH_FILE.read_text(encoding="utf-8"))

        # Build lookups for fast access
        for entry in self._extractions.get("global_concept_index", []):
            self._concept_index[entry["concept"].lower()] = entry
            for alias in entry.get("aliases", []):
                self._concept_index.setdefault(alias.lower(), entry)
        for entry in self._extractions.get("pattern_registry", []):
            self._pattern_index[entry["structure"].lower()] = entry

    @property
    def concept_names(self) -> list[str]:
        return [
            entry["concept"]
            for entry in self._extractions.get("global_concept_index", [])
        ]

    def find_concept(self, name: str | None) -> dict[str, Any] | None:
        if not name:
            return None
        return self._concept_index.get(name.lower().strip())

    def find_concepts_in_text(self, text: str, limit: int = 5) -> list[dict[str, Any]]:
        lowered = text.lower()
        matches = []
        for entry in self._extractions.get("global_concept_index", []):
            if entry["concept"].lower() in lowered:
                matches.append(entry)
                continue
            for alias in entry.get("aliases", []):
                if alias.lower() in lowered:
                    matches.append(entry)
                    break
        return matches[:limit]

    def summarize_concept(self, entry: dict[str, Any]) -> str:
        components = ", ".join(entry.get("related_components", [])[:8]) or "(none)"
        patterns = ", ".join(entry.get("related_patterns", [])[:6]) or "(none)"
        aliases = ", ".join(entry.get("aliases", [])) or "(none)"
        return (
            f"Concept: {entry['concept']}\n"
            f"Aliases: {aliases}\n"
            f"Related AWS components: {components}\n"
            f"Related patterns: {patterns}\n"
            f"Frequency: {entry.get('frequency', 0)}, "
            f"confidence: {entry.get('confidence', 0):.2f}"
        )


# Module-level singleton (loaded once)
_instance: KnowledgeContext | None = None


def get_context() -> KnowledgeContext:
    global _instance
    if _instance is None:
        _instance = KnowledgeContext()
    return _instance
