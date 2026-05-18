# Architecture

## 1. Purpose

This repository is a local knowledge workspace for AWS and related study material. It supports three main use cases:

- authoring and storing Markdown knowledge notes inside an Obsidian vault;
- converting those notes into structured graph artifacts for local semantic retrieval;
- interacting with the resulting knowledge base through a Python CLI and a dashboard-backed multi-agent UI.

## 2. Current System Shape

The system is a mixed Python and TypeScript project centered on local files rather than a database.

- The `Notes/` directory contains primary source notes plus generated JSON artifacts such as chunks, extractions, concept graph data, and concept catalogs.
- Root Python scripts provide indexing and query entrypoints.
- The `agents/` package exposes a FastAPI API for the dashboard’s routed agent experience.
- The `dashboard/` folder contains a React/Vite frontend that loads graph artifacts directly and calls `/agents/*` for live agent interactions.
- Local LM Studio provides the `Qwen2.5-14B-Instruct` model endpoint used by the ingestion pipeline, query engine, and agent backend.

## 3. Component Map

| Component | Path | Responsibility | Key dependencies |
|---|---|---|---|
| Query CLI | `ask.py` | Answer user questions from the knowledge graph and LM Studio synthesis | `query_engine.py`, `Notes/query_concept_graph.py`, LM Studio |
| Semantic matcher | `query_engine.py` | Rank concepts semantically and traverse graph relations | `Notes/global_extractions.json`, `Notes/concept_graph.json`, LM Studio |
| Concept index builder | `build_embedding_cache.py` | Build `concept_search_index.json` and `concept_list.json` from extraction output | `Notes/global_extractions.json` |
| Chunking pipeline | `Notes/chunk_aip_c01.py` | Split source notes into semantic chunks and extract structured metadata in one pass | LM Studio, Markdown source files |
| Batch payload builder | `Notes/build_qwen_batch.py` | Build batch LM Studio prompt payloads from semantic sections | `Notes/chunk_aip_c01.py` helpers |
| Extraction rollup | `Notes/extract_knowledge.py` | Roll chunk-level metadata into global concepts, patterns, aliases, and graph outputs | `Notes/global_chunks.json` |
| Graph query helpers | `Notes/query_concept_graph.py` | Comparison-oriented graph query utilities | `Notes/concept_graph.json`, `Notes/global_extractions.json` |
| Agents backend | `agents/server.py` | Serve `/agents/health`, `/agents/concepts`, and `/agents/run` | FastAPI, `AgentOrchestrator`, LM Studio |
| Agent orchestration | `agents/orchestrator.py` | Route requests to tutor, quiz, or review agents | Router agent, specialist agents |
| Knowledge context loader | `agents/context_loader.py` | Load concept and graph data once for agent prompts | `Notes/global_extractions.json`, `Notes/concept_graph.json` |
| Dashboard frontend | `dashboard/src/` | Render graph, concepts, patterns, and the agent interaction panel | React, Vite, D3 |
| Dashboard static data | `dashboard/public/` | Serve graph and extraction artifacts to the frontend | Generated JSON copied into `public/` |

## 4. Runtime Flow

```text
Markdown notes → Qwen chunk/extract pipeline → global JSON artifacts → query/agent loading
User query → semantic concept ranking → graph traversal → Qwen answer synthesis
Browser → Vite frontend → /agents proxy → FastAPI backend → routed agent → LM Studio
```

## 5. Data Flow

Primary note sources live under `Notes/*.md`, plus other vault Markdown such as `Snowflake.md` and `Welcome.md`.

The ingestion pipeline creates:

- `Notes/global_chunks.json`
- `Notes/global_extractions.json`
- `Notes/concept_graph.json`
- `Notes/concept_aliases.json`
- `Notes/concept_search_index.json`
- `Notes/concept_list.json`

The CLI path reads those generated artifacts directly. The agents backend loads `global_extractions.json` and `concept_graph.json` once at startup for context injection and routing support. The dashboard loads `concept_graph.json` and `global_extractions.json` from `dashboard/public/` for graph rendering, while `/agents/*` requests are proxied to the FastAPI backend in development.

## 6. Configuration

Important runtime configuration:

- `LM_STUDIO_URL` — defaults to `http://127.0.0.1:1234/v1/chat/completions`
- `LM_STUDIO_MODEL` — defaults to `qwen2.5-14b-instruct`

Relevant config files:

- `.claude/launch.json` — local multi-process launch configuration
- `.obsidian/` — vault behavior and plugin settings
- `dashboard/vite.config.ts` — frontend dev proxy to `127.0.0.1:8765`
- `agents/requirements.txt` — backend Python dependencies
- `dashboard/package.json` — frontend scripts and dependencies

Secret values are not stored in repository docs. The local LM Studio endpoint is expected to be available on the same machine.

## 7. Testing and SIT

Current practical validation is smoke/SIT oriented rather than unit-test heavy.

Commands used in this housekeeping pass:

- `python3 -m py_compile ask.py build_embedding_cache.py query_engine.py Notes/build_qwen_batch.py Notes/chunk_aip_c01.py Notes/extract_knowledge.py Notes/query_concept_graph.py agents/*.py`
- `cd dashboard && npm run build`
- `curl -s http://127.0.0.1:8765/agents/health`

The compile and frontend build checks passed. The live backend health check failed because the local FastAPI service was not listening at the time of validation.

## 8. Deployment / Execution

Local development:

- Frontend: `cd dashboard && npm run dev`
- Backend: `uvicorn agents.server:app --reload --host 127.0.0.1 --port 8765`
- CLI query: `python3 ask.py "..."`

Production-style local serving:

- `cd dashboard && npm run build`
- start `agents.server:app`
- `agents/server.py` mounts `dashboard/dist` when present, so one FastAPI process can serve both UI and API

The repository also contains launch configuration indicating the backend can be kept alive locally as a long-running service.

## 9. Governance / Operational Notes

- The project is local-file driven; generated JSON artifacts are part of runtime behavior and should be refreshed when source notes materially change.
- LM Studio is a hard runtime dependency for full semantic matching and agent responses.
- The dashboard frontend is buildable independently of the live backend, but the Agents panel requires both FastAPI and LM Studio.
- Root-level `.obsidian/` is intentionally tracked for vault behavior, which may create collaboration noise if the vault becomes multi-user.
- There is no repository-local CI workflow visible in the current checkout.

## 10. Known Gaps

See `design/issues-pending-review.md`.
