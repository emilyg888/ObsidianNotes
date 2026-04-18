# Agents Tab — Qwen-powered Tutor, Quiz, Reviewer with Dynamic Routing

## Context

The dashboard currently visualizes the extracted knowledge base (concepts, components, patterns). The user wants to interact with that knowledge via three AI agents powered by local Qwen 2.5-14B (via LM Studio):

1. **Tutor agent** — answer questions about a concept/component (RAG-style, grounded in the existing concept graph)
2. **Quiz agent** — generate MCQ quizzes about a concept or compare components
3. **Reviewer agent** — review an architecture flow based on a concept or component

A **router agent** (also Qwen) classifies each incoming query and dynamically dispatches to the correct specialist. The reference project at `/Users/emilygao/LocalDocuments/Projects/aws/AP1-C01/aws-genai-airlab` uses the same three-agent split but with AWS Bedrock and manual selection — we port the pattern to local Qwen + add the LLM router.

## Architecture

```
┌─────────────────────┐        HTTP           ┌──────────────────────────┐
│  React dashboard    │ ─────────────────────▶│  FastAPI backend         │
│  (Agents tab)       │                        │  localhost:8000          │
│                     │ ◀─────────────────────│                          │
└─────────────────────┘                        │  POST /agents/run        │
                                               │    │                     │
                                               │    ▼                     │
                                               │  RouterAgent (Qwen)      │
                                               │    │                     │
                                               │    ├──▶ TutorAgent       │
                                               │    ├──▶ QuizAgent        │
                                               │    └──▶ ReviewerAgent    │
                                               │                          │
                                               │  Context loaded from:    │
                                               │   Notes/global_extractions.json
                                               │   Notes/concept_graph.json│
                                               │                          │
                                               │  LLM: LM Studio Qwen      │
                                               │   http://127.0.0.1:1234  │
                                               └──────────────────────────┘
```

## Backend (new `agents/` directory at repo root)

```
agents/
  __init__.py
  requirements.txt        # fastapi, uvicorn, pydantic
  base.py                 # BaseAgent, AgentResponse (ported from reference)
  lm_studio_client.py     # Qwen chat-completions client (pattern from Notes/chunk_aip_c01.py)
  context_loader.py       # Loads concept graph + extractions once at startup
  router_agent.py         # RouterAgent: Qwen classifies → {tutor|quiz|review}
  tutor_agent.py          # Q&A grounded in concept components/patterns/aliases
  quiz_agent.py           # Strict-JSON MCQ generator; supports single concept or compare mode
  reviewer_agent.py       # Architecture review with scored categories
  orchestrator.py         # AgentOrchestrator dict router
  server.py               # FastAPI app: POST /agents/run, /agents/health
```

### Key design decisions

- **Single endpoint `POST /agents/run`** with body `{ "query": "...", "concept": "optional concept name" }`. Backend routes internally. Response: `{ agent: "tutor"|"quiz"|"review", output: {...}, metadata: {...} }`. This matches the user's "dynamic routing" requirement.
- **Context injection** — TutorAgent retrieves the selected concept's related components/patterns from the already-loaded `global_extractions.json` and injects them into the prompt as structured context (the same catalog Qwen already sees in `query_engine.py`).
- **Router prompt** — asks Qwen to return strict JSON `{ "agent": "tutor|quiz|review", "reason": "..." }` based on verb/intent keywords ("quiz", "test me", "review", "evaluate", vs questions).
- **Reuse existing LM Studio config** — same `LM_STUDIO_URL` / `LM_STUDIO_MODEL` env vars the pipeline scripts already use.

### Agent output shapes (what frontend consumes)

```jsonc
// Tutor
{ "agent": "tutor", "output": { "answer": "markdown text", "related_components": [...], "related_patterns": [...] } }

// Quiz
{ "agent": "quiz", "output": { "questions": [ { "id", "question", "options": ["A","B","C","D"], "answer", "explanation" } ] } }

// Reviewer
{ "agent": "review", "output": { "scores": {security,scalability,cost_efficiency,reliability,operational_excellence}, "overall", "strengths": [], "risks": [], "recommendations": [] } }
```

## Frontend (new component in existing `dashboard/`)

```
dashboard/src/
  components/
    AgentsPanel.tsx          # NEW: chat interface with concept picker
    TutorResponse.tsx        # NEW: renders tutor output
    QuizResponse.tsx         # NEW: interactive MCQ with reveal
    ReviewerResponse.tsx     # NEW: score bars + strengths/risks lists
  hooks/
    useAgents.ts             # NEW: POST to /agents/run, handle streaming not needed
  App.tsx                    # MODIFY: add "agents" tab
  types.ts                   # MODIFY: add AgentResponse types
  components/Sidebar.tsx     # MODIFY: add "🤖 Agents" tab entry
```

### Frontend behavior

- New "Agents" tab (5th tab) in the sidebar
- Chat-like interface: input at bottom, scrollable message history above
- **Concept selector** dropdown above input (lists the 39 concepts already loaded); selecting one sets context for the query
- Each agent response renders with a **type-specific component**:
  - **TutorResponse** — markdown answer + related component/pattern chips
  - **QuizResponse** — each question as a card with clickable options; reveal correct answer + explanation on click; running score at top
  - **ReviewerResponse** — 5 horizontal score bars (security/scalability/etc.) with overall score badge + bulleted strengths/risks/recommendations
- Agent badge on each response so user sees which agent answered (e.g. "🎓 Tutor", "📝 Quiz", "🔍 Reviewer")

### Dev proxy

Add proxy to `dashboard/vite.config.ts` so the frontend can call `/agents/*` without CORS:

```ts
server: { proxy: { '/agents': 'http://localhost:8000' } }
```

## Launch config update

Add the FastAPI server to `.claude/launch.json` so both services start together.

## Implementation Steps

1. Scaffold `agents/` directory with `requirements.txt` (fastapi, uvicorn, pydantic)
2. Port `base.py` from reference (BaseAgent + AgentResponse dataclasses)
3. Write `lm_studio_client.py` using the same pattern as `Notes/chunk_aip_c01.py::run_qwen_chunking`
4. Write `context_loader.py` — loads `Notes/global_extractions.json` once; exposes `get_concept(name)` helper
5. Write each agent (tutor, quiz, reviewer) with inline f-string prompts + strict-JSON parsing + fallbacks
6. Write `router_agent.py` — Qwen-based intent classifier returning `{agent, reason}`
7. Write `orchestrator.py` — route → run specialist agent
8. Write `server.py` — FastAPI app with `POST /agents/run` + CORS middleware
9. Add Vite proxy to `dashboard/vite.config.ts`
10. Add `agents` tab in `Sidebar.tsx` + App.tsx tab switch
11. Build `AgentsPanel.tsx` with chat UI + concept selector
12. Build `TutorResponse.tsx`, `QuizResponse.tsx`, `ReviewerResponse.tsx`
13. Wire `useAgents.ts` hook for API calls
14. Update `.claude/launch.json` with the backend config
15. Verify end-to-end with LM Studio running locally

## Verification

- `cd agents && pip install -r requirements.txt && uvicorn agents.server:app --reload`
- `cd dashboard && npm run dev`
- Open dashboard, switch to **Agents** tab
- Type "What is RAG?" → routed to Tutor → markdown answer with related components
- Type "Quiz me on guardrails" → routed to Quiz → 5 interactive MCQs
- Type "Review a RAG architecture using Lambda and OpenSearch" → routed to Reviewer → scored review
- Confirm the agent badge shown matches the expected route each time
