"""Router agent: uses Qwen to classify the user's intent and pick a specialist."""
from __future__ import annotations

import re
from typing import Any

from .base import AgentResponse, BaseAgent
from .lm_studio_client import LMStudioClient, parse_json_object


VALID_AGENTS = {"tutor", "quiz", "review"}

SYSTEM_PROMPT = (
    "You are a routing classifier for a multi-agent system. "
    "Given a user query, return STRICT JSON picking exactly one agent:\n"
    '- "tutor": the user is asking a question to learn or understand a concept.\n'
    '- "quiz": the user wants a test, practice questions, MCQs, or to be quizzed.\n'
    '- "review": the user wants feedback, evaluation, scoring, or a review of an architecture / design.\n'
    "Return only JSON. No prose, no code fences."
)

USER_TEMPLATE = """\
User query: {query}

Return JSON shaped like:
{{"agent": "tutor" | "quiz" | "review", "reason": "one short sentence"}}
"""


class RouterAgent(BaseAgent):
    def __init__(self, llm: LMStudioClient) -> None:
        self._llm = llm

    def run(self, payload: dict[str, Any]) -> AgentResponse:
        query = str(payload.get("query", "")).strip()
        if not query:
            return AgentResponse(
                output={"agent": "tutor", "reason": "empty query defaults to tutor"},
                metadata={"agent": "router", "method": "default"},
            )

        # Fast heuristic so obvious intent doesn't burn an LLM call.
        quick = _heuristic_route(query)
        if quick:
            return AgentResponse(
                output={"agent": quick, "reason": "keyword heuristic match"},
                metadata={"agent": "router", "method": "heuristic"},
            )

        raw = self._llm.chat(
            SYSTEM_PROMPT,
            USER_TEMPLATE.format(query=query),
            temperature=0.0,
            max_tokens=100,
        )
        parsed = parse_json_object(raw) or {}
        agent = str(parsed.get("agent", "")).lower().strip()
        if agent not in VALID_AGENTS:
            agent = "tutor"  # safest default
            parsed.setdefault("reason", "router produced no valid agent; defaulting to tutor")

        return AgentResponse(
            output={"agent": agent, "reason": parsed.get("reason", "")},
            metadata={"agent": "router", "method": "llm", "raw": raw},
        )


def _heuristic_route(query: str) -> str | None:
    lowered = query.lower()
    quiz_keywords = [
        "quiz",
        "mcq",
        "multiple choice",
        "test me",
        "test my",
        "practice question",
        "practice questions",
        "exam question",
    ]
    review_keywords = [
        "review",
        "evaluate",
        "feedback on",
        "critique",
        "score ",
        "assess",
        "audit",
    ]
    if any(kw in lowered for kw in quiz_keywords):
        return "quiz"
    if any(kw in lowered for kw in review_keywords):
        return "review"
    # "review this architecture" or "review my design"
    if re.search(r"\breview\b.*\b(architecture|design|flow|pipeline|diagram)\b", lowered):
        return "review"
    return None
