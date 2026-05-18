# ObsidianNotes

## Overview

This repository is an Obsidian knowledge workspace with a local knowledge-processing pipeline, a semantic query CLI, a FastAPI agent backend, and a React/Vite dashboard for browsing and interacting with the extracted graph.

## Architecture Summary

The project turns Markdown study notes into structured knowledge artifacts under `Notes/`, uses local `Qwen2.5-14B-Instruct` via LM Studio for chunking, extraction, semantic ranking, and agent responses, and serves the resulting graph through both Python tools and the dashboard UI.

## Repository Structure

- `Notes/` — source notes plus generated chunk, extraction, graph, and concept catalog artifacts
- `agents/` — FastAPI backend and specialist agents for tutoring, quizzing, and review
- `dashboard/` — React/Vite frontend that loads graph artifacts and proxies `/agents/*`
- `design/` — architecture and review-tracking documents
- `src_archives/` — archived obsolete documents preserved during housekeeping
- Root Python scripts — local query and indexing entrypoints

## Setup

Python backend:

```bash
python3 -m venv agents/.venv
source agents/.venv/bin/activate
pip install -r agents/requirements.txt
```

Frontend:

```bash
cd dashboard
npm install
```

## Run

Dashboard frontend:

```bash
cd dashboard
npm run dev
```

Agents backend:

```bash
cd /Users/emilygao/LocalDocuments/Obsidian
source agents/.venv/bin/activate
uvicorn agents.server:app --reload --host 127.0.0.1 --port 8765
```

CLI query:

```bash
python3 ask.py "What is RAG and when should I use it?"
```

The live stack expects LM Studio on `http://127.0.0.1:1234/v1/chat/completions`.

## Test / SIT

Python compile smoke test:

```bash
python3 -m py_compile ask.py build_embedding_cache.py query_engine.py Notes/build_qwen_batch.py Notes/chunk_aip_c01.py Notes/extract_knowledge.py Notes/query_concept_graph.py agents/*.py
```

Frontend build:

```bash
cd dashboard
npm run build
```

Live API health check:

```bash
curl -s http://127.0.0.1:8765/agents/health
```

See `design/issues-pending-review.md` for the latest recorded results.

## Configuration

Important environment variables:

- `LM_STUDIO_URL`
- `LM_STUDIO_MODEL`

The frontend dev server proxies `/agents/*` to `127.0.0.1:8765`.

## Documentation

- Architecture: `design/architecture.md`
- Pending review issues: `design/issues-pending-review.md`

## Current Status

- Housekeeping completed on `2026-05-18`
- Legacy architecture notes and generic dashboard scaffold docs were archived under `src_archives/2026-05-18_housekeeping/`
- The repo still depends on local services for full end-to-end agent runtime validation
