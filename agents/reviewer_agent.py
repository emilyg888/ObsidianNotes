"""Reviewer agent: scores an architecture flow and returns strengths/risks."""
from __future__ import annotations

from typing import Any

from .base import AgentResponse, BaseAgent
from .context_loader import KnowledgeContext
from .lm_studio_client import LMStudioClient, parse_json_object


SYSTEM_PROMPT = (
    "You are an AWS architecture reviewer. "
    "Return STRICT JSON only. Score each category from 1 to 10. "
    "Ground strengths and risks in AWS best practices and the supplied context."
)

CATEGORIES = [
    "security",
    "scalability",
    "cost_efficiency",
    "reliability",
    "operational_excellence",
]


class ReviewerAgent(BaseAgent):
    def __init__(self, llm: LMStudioClient, context: KnowledgeContext) -> None:
        self._llm = llm
        self._ctx = context

    def run(self, payload: dict[str, Any]) -> AgentResponse:
        query = str(payload.get("query", "")).strip()
        concept_name = payload.get("concept")

        concept = self._ctx.find_concept(concept_name) if concept_name else None
        detected = self._ctx.find_concepts_in_text(query, limit=3)
        if not concept and detected:
            concept = detected[0]

        context_blocks = []
        if concept:
            context_blocks.append(self._ctx.summarize_concept(concept))
        for extra in detected:
            if not concept or extra["concept"] != concept["concept"]:
                context_blocks.append(self._ctx.summarize_concept(extra))
        context_text = "\n\n".join(context_blocks) or "(no structured context)"

        user_prompt = f"""\
Review this AWS generative AI architecture/flow described by the user.

Architecture description: {query}

Knowledge-base context:
{context_text}

Return STRICT JSON with exactly this schema:
{{
  "scores": {{
    "security": 0,
    "scalability": 0,
    "cost_efficiency": 0,
    "reliability": 0,
    "operational_excellence": 0
  }},
  "overall": 0,
  "strengths": ["..."],
  "risks": ["..."],
  "recommendations": ["..."]
}}

Scores are integers from 1 to 10. Overall is the average rounded to one decimal.
"""

        raw = self._llm.chat(SYSTEM_PROMPT, user_prompt, temperature=0.2, max_tokens=1200)
        parsed = parse_json_object(raw) or {}

        # Normalize / fill missing fields
        scores_in = parsed.get("scores", {}) if isinstance(parsed, dict) else {}
        scores = {
            key: _coerce_int(scores_in.get(key), default=5) for key in CATEGORIES
        }
        overall = parsed.get("overall") if isinstance(parsed, dict) else None
        try:
            overall = round(float(overall), 1) if overall is not None else round(sum(scores.values()) / len(CATEGORIES), 1)
        except (TypeError, ValueError):
            overall = round(sum(scores.values()) / len(CATEGORIES), 1)

        output = {
            "scores": scores,
            "overall": overall,
            "strengths": parsed.get("strengths", []) if isinstance(parsed, dict) else [],
            "risks": parsed.get("risks", []) if isinstance(parsed, dict) else [],
            "recommendations": parsed.get("recommendations", []) if isinstance(parsed, dict) else [],
            "concept": concept["concept"] if concept else None,
        }
        if not parsed:
            output["parse_error"] = "model did not return valid review JSON"
            output["raw"] = raw

        return AgentResponse(output=output, metadata={"agent": "review"})


def _coerce_int(value: Any, default: int = 5) -> int:
    try:
        n = int(round(float(value)))
    except (TypeError, ValueError):
        return default
    return max(1, min(10, n))
