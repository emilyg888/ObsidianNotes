"""Quiz agent: generates MCQ quizzes on a concept/component or comparisons."""
from __future__ import annotations

from typing import Any

from .base import AgentResponse, BaseAgent
from .context_loader import KnowledgeContext
from .lm_studio_client import LMStudioClient, parse_json_object


SYSTEM_PROMPT = (
    "You are an AWS certification quiz generator. "
    "Return STRICT JSON only. No prose, no code fences, no commentary. "
    "Every question must have exactly 4 options (A–D), one correct answer, "
    "and a brief explanation grounding the correct answer in AWS practice."
)


class QuizAgent(BaseAgent):
    def __init__(self, llm: LMStudioClient, context: KnowledgeContext) -> None:
        self._llm = llm
        self._ctx = context

    def run(self, payload: dict[str, Any]) -> AgentResponse:
        query = str(payload.get("query", "")).strip()
        concept_name = payload.get("concept")
        count = int(payload.get("count", 5))
        difficulty = payload.get("difficulty", "associate")

        concept = self._ctx.find_concept(concept_name) if concept_name else None
        detected = self._ctx.find_concepts_in_text(query, limit=3)
        topics = [c["concept"] for c in detected]
        if concept and concept["concept"] not in topics:
            topics.insert(0, concept["concept"])

        topic_line = ", ".join(topics) if topics else (query or "AWS generative AI")

        context_blocks = []
        if concept:
            context_blocks.append(self._ctx.summarize_concept(concept))
        for extra in detected[:2]:
            if not concept or extra["concept"] != concept["concept"]:
                context_blocks.append(self._ctx.summarize_concept(extra))
        context_text = "\n\n".join(context_blocks) or "(no structured context; use general AWS knowledge)"

        user_prompt = f"""\
Create {count} {difficulty}-level multiple-choice questions.

User request: {query}
Topic(s): {topic_line}

Knowledge-base context to ground the questions:
{context_text}

Return STRICT JSON with exactly this schema:
{{
  "questions": [
    {{
      "id": 1,
      "question": "...",
      "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
      "answer": "A",
      "explanation": "..."
    }}
  ]
}}
"""

        raw = self._llm.chat(SYSTEM_PROMPT, user_prompt, temperature=0.3, max_tokens=1500)
        parsed = parse_json_object(raw) or {}
        questions = parsed.get("questions") if isinstance(parsed, dict) else None

        if not isinstance(questions, list) or not questions:
            output = {
                "questions": [],
                "topics": topics,
                "raw": raw,
                "parse_error": "model did not return valid quiz JSON",
            }
        else:
            output = {"questions": questions, "topics": topics}

        return AgentResponse(output=output, metadata={"agent": "quiz"})
