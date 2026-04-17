"""Orchestrator: routes queries to the correct specialist agent."""
from __future__ import annotations

from typing import Any

from .base import AgentResponse
from .context_loader import get_context
from .lm_studio_client import LMStudioClient
from .quiz_agent import QuizAgent
from .reviewer_agent import ReviewerAgent
from .router_agent import RouterAgent
from .tutor_agent import TutorAgent


class AgentOrchestrator:
    def __init__(self, llm: LMStudioClient | None = None) -> None:
        self._llm = llm or LMStudioClient()
        ctx = get_context()
        self._router = RouterAgent(self._llm)
        self._agents = {
            "tutor": TutorAgent(self._llm, ctx),
            "quiz": QuizAgent(self._llm, ctx),
            "review": ReviewerAgent(self._llm, ctx),
        }

    def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        routed = self._router.run(payload)
        agent_name = str(routed.output.get("agent", "tutor"))
        specialist = self._agents.get(agent_name, self._agents["tutor"])
        response: AgentResponse = specialist.run(payload)

        return {
            "agent": agent_name,
            "routing": {
                "reason": routed.output.get("reason", ""),
                "method": routed.metadata.get("method"),
            },
            "output": response.output,
            "metadata": response.metadata,
        }
