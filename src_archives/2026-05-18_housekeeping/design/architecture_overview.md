# Architecture Overview

## Purpose

The Obsidian knowledge dashboard is split into a browser frontend and an agents backend. The frontend provides the React/Vite dashboard experience. The backend exposes FastAPI endpoints used by the Agents panel and connects to the local LM Studio API.

## Runtime Components

| Component | Path | Port | Role |
| --- | --- | --- | --- |
| Dashboard frontend | `/Users/emilygao/LocalDocuments/Obsidian/dashboard` | `5173` in development | Serves the React/Vite UI in the browser. |
| Agents backend | `/Users/emilygao/LocalDocuments/Obsidian/agents` | `8765` | Serves `/agents/*` API routes for health, concept loading, and agent runs. |
| LM Studio API | local LM Studio process | `1234` | Provides the local model endpoint consumed by the agents backend. |
| launchd agent | `/Users/emilygao/Library/LaunchAgents/com.emilygao.knowledge-dashboard.plist` | starts backend on `8765` | Starts and keeps the backend service available after login. |

## Request Flow

```text
Browser
  |
  | http://127.0.0.1:5173
  v
React/Vite dashboard
  |
  | /agents/*
  v
Vite dev proxy
  |
  | http://127.0.0.1:8765/agents/*
  v
FastAPI agents backend
  |
  | LM_STUDIO_URL=http://127.0.0.1:1234/v1/chat/completions
  v
LM Studio local model
```

## Why There Are Two Dashboard Ports

The dashboard uses two ports because the UI and API are separate processes during development:

- `5173` is the Vite development server. It serves the React dashboard and handles frontend hot reload.
- `8765` is the FastAPI backend. It handles agent-related API requests under `/agents/*`.

The frontend does not call `8765` directly from application code in development. Instead, `dashboard/vite.config.ts` proxies `/agents` requests to `http://127.0.0.1:8765`, so browser code can call relative paths such as `/agents/health`, `/agents/concepts`, and `/agents/run`.

## Frontend

The frontend lives in:

```text
/Users/emilygao/LocalDocuments/Obsidian/dashboard
```

Key commands:

```bash
npm install
npm run dev
```

The development server normally runs at:

```text
http://127.0.0.1:5173
```

The package scripts are defined in `dashboard/package.json`:

- `npm run dev` starts Vite.
- `npm run build` runs TypeScript build checks and creates the production bundle.
- `npm run preview` previews the built frontend.

## Backend

The backend entrypoint is:

```text
/Users/emilygao/LocalDocuments/Obsidian/agents/server.py
```

It defines the FastAPI application:

```text
agents.server:app
```

Important routes:

- `GET /agents/health` returns backend health and the number of loaded concepts.
- `GET /agents/concepts` returns concept names for frontend dropdowns.
- `POST /agents/run` sends a user request to the agent orchestrator.

The backend also mounts the built React dashboard from `dashboard/dist` when that directory exists. This means production-style serving can happen through the backend after running the frontend build.

## Autostart Behavior

The backend is configured to start automatically through launchd:

```text
/Users/emilygao/Library/LaunchAgents/com.emilygao.knowledge-dashboard.plist
```

The launch agent uses:

```text
WorkingDirectory=/Users/emilygao/LocalDocuments/Obsidian
/Users/emilygao/LocalDocuments/Obsidian/agents/.venv/bin/uvicorn agents.server:app --host 127.0.0.1 --port 8765 --log-level info
```

It also sets:

```text
LM_STUDIO_MODEL=qwen2.5-14b-instruct
LM_STUDIO_URL=http://127.0.0.1:1234/v1/chat/completions
```

Logs are written to:

```text
/tmp/knowledge-dashboard.out.log
/tmp/knowledge-dashboard.err.log
```

## Local Development Startup

For the full dashboard with the Agents panel:

1. Start or confirm LM Studio is running on `127.0.0.1:1234`.
2. Confirm the backend is running on `127.0.0.1:8765`.
3. Start the frontend:

```bash
cd /Users/emilygao/LocalDocuments/Obsidian/dashboard
npm run dev
```

Then open:

```text
http://127.0.0.1:5173
```

If the launch agent is active, the backend should already be running. To start it manually:

```bash
cd /Users/emilygao/LocalDocuments/Obsidian
source agents/.venv/bin/activate
uvicorn agents.server:app --reload --host 127.0.0.1 --port 8765
```

## Operational Checks

Check which process owns port `8765`:

```bash
lsof -nP -iTCP:8765 -sTCP:LISTEN
```

Check the backend command:

```bash
ps -p <PID> -o pid,ppid,user,command
```

Check launchd configuration:

```bash
plutil -p /Users/emilygao/Library/LaunchAgents/com.emilygao.knowledge-dashboard.plist
```

Check backend health:

```bash
curl http://127.0.0.1:8765/agents/health
```

## Production-Style Serving

The backend can serve the compiled frontend if `dashboard/dist` exists:

```bash
cd /Users/emilygao/LocalDocuments/Obsidian/dashboard
npm run build
```

After the build, `agents/server.py` mounts `dashboard/dist` as static files. In that mode, the backend can serve both the API routes and the built dashboard assets from one FastAPI process.

