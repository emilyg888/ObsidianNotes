"""FastAPI server exposing the multi-agent system to the dashboard."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .context_loader import get_context
from .orchestrator import AgentOrchestrator


REPO_ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_DIST = REPO_ROOT / "dashboard" / "dist"


app = FastAPI(title="Knowledge Dashboard Agents", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

_orchestrator: AgentOrchestrator | None = None


def orchestrator() -> AgentOrchestrator:
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = AgentOrchestrator()
    return _orchestrator


class RunRequest(BaseModel):
    query: str = Field(..., description="User's question or request")
    concept: str | None = Field(
        None, description="Optional concept name to inject as context"
    )
    count: int | None = Field(None, description="Quiz question count (quiz agent only)")
    difficulty: str | None = Field(
        None, description="Quiz difficulty: associate | professional"
    )


@app.get("/agents/health")
def health() -> dict[str, Any]:
    ctx = get_context()
    return {
        "status": "ok",
        "concepts_loaded": len(ctx.concept_names),
    }


@app.get("/agents/concepts")
def concepts() -> dict[str, Any]:
    """Returns the concept list so the frontend can populate its dropdown."""
    ctx = get_context()
    return {"concepts": ctx.concept_names}


@app.post("/agents/run")
def run(request: RunRequest) -> dict[str, Any]:
    try:
        payload = request.model_dump(exclude_none=True)
        return orchestrator().run(payload)
    except RuntimeError as exc:
        # LM Studio not reachable or HTTP error
        raise HTTPException(status_code=503, detail=str(exc))
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc))


# Serve the built React dashboard as static assets (production mode).
# Mount LAST so API routes above take precedence. If dist/ doesn't exist
# (e.g. you haven't run `npm run build` yet), the mount is skipped and the
# app still serves the API — just without the UI.
if DASHBOARD_DIST.exists():
    app.mount(
        "/",
        StaticFiles(directory=DASHBOARD_DIST, html=True),
        name="frontend",
    )
