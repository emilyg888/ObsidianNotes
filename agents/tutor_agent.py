"""Tutor agent: Q&A about concepts, grounded in the extracted knowledge graph."""
from __future__ import annotations

from typing import Any

from .base import AgentResponse, BaseAgent
from .context_loader import KnowledgeContext
from .lm_studio_client import LMStudioClient


SYSTEM_PROMPT = (
    "You are an AWS generative AI architecture tutor. "
    "Answer the user's question clearly and concisely, grounded in the supplied "
    "knowledge-base context. Use AWS-specific terminology. "
    "Structure your answer as: (1) a short explanation, "
    "(2) key AWS components involved, (3) common pitfalls or tradeoffs."
)


class TutorAgent(BaseAgent):
    def __init__(self, llm: LMStudioClient, context: KnowledgeContext) -> None:
        self._llm = llm
        self._ctx = context

    def run(self, payload: dict[str, Any]) -> AgentResponse:
        question = str(payload.get("query", "")).strip()
        concept_name = payload.get("concept")

        # Prefer the explicitly-selected concept; fall back to detecting it
        concept = self._ctx.find_concept(concept_name) if concept_name else None
        detected = self._ctx.find_concepts_in_text(question, limit=3)
        if not concept and detected:
            concept = detected[0]

        context_blocks = []
        if concept:
            context_blocks.append(self._ctx.summarize_concept(concept))
        for extra in detected:
            if not concept or extra["concept"] != concept["concept"]:
                context_blocks.append(self._ctx.summarize_concept(extra))

        context_text = "\n\n".join(context_blocks) or "(no specific concept context available)"

        user_prompt = (
            f"Question: {question}\n\n"
            f"Knowledge-base context:\n{context_text}\n\n"
            f"Answer:"
        )

        answer = self._llm.chat(SYSTEM_PROMPT, user_prompt, temperature=0.2, max_tokens=800)

        output = {
            "answer": answer or "(empty response from model)",
            "concept": concept["concept"] if concept else None,
            "related_components": concept.get("related_components", [])[:6] if concept else [],
            "related_patterns": concept.get("related_patterns", [])[:6] if concept else [],
        }
        return AgentResponse(output=output, metadata={"agent": "tutor"})
