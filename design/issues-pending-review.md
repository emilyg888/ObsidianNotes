# Issues Pending Review

## Summary

| ID | Severity | Area | Issue | Recommended action | Status |
|---|---|---|---|---|---|
| ISSUE-001 | Medium | Tests | Live `/agents/health` check failed because the FastAPI backend was not listening on `127.0.0.1:8765` during housekeeping | Confirm the backend startup path and re-run the health check with LM Studio online | Pending review |
| ISSUE-002 | Low | Docs | The worktree was not clean at baseline because `research/` existed as untracked user content | Decide whether `research/` belongs in the repo, should be ignored, or should remain intentionally local | Pending review |
| ISSUE-003 | Low | Config | The repo intentionally tracks root `.obsidian/` settings, which may mix stable vault config with user-specific preferences over time | Review which `.obsidian/` files are truly project-level and trim or ignore user-local ones if collaboration expands | Pending review |

## SIT Results

| Command | Result | Notes |
|---|---|---|
| `python3 -m py_compile ask.py build_embedding_cache.py query_engine.py Notes/build_qwen_batch.py Notes/chunk_aip_c01.py Notes/extract_knowledge.py Notes/query_concept_graph.py agents/*.py` | Passed | Python smoke compile for the main runtime and pipeline files |
| `cd dashboard && npm run build` | Passed | Vite production build completed successfully |
| `curl -s http://127.0.0.1:8765/agents/health` | Failed | Exit code `7`; local backend was not listening during validation |

## Archived Code Review

| Original path | Archived path | Reason | Review needed? |
|---|---|---|---|
| `design/architecture_overview.md` | `src_archives/2026-05-18_housekeeping/design/architecture_overview.md` | Superseded by the new canonical `design/architecture.md`; no references found and old doc covered only part of the repo | No |
| `dashboard/README.md` | `src_archives/2026-05-18_housekeeping/dashboard/README.md` | Generic Vite scaffold doc unrelated to the project’s actual dashboard behavior; no references found | No |

## Detailed Issues

### ISSUE-001 — Backend API was not live during SIT

- Severity: Medium
- Area: Tests
- Evidence:
  `curl -s http://127.0.0.1:8765/agents/health` exited with code `7`.
- Impact:
  The repository is buildable, but the full dashboard-plus-agents runtime was not verified end to end during housekeeping.
- Recommended action:
  Start the FastAPI backend and LM Studio locally, then re-run the health check and one representative `/agents/run` request.
- Status: Pending review

### ISSUE-002 — Baseline worktree was already dirty

- Severity: Low
- Area: Config
- Evidence:
  `git status --short` showed `?? research/` before housekeeping changes were made.
- Impact:
  The repo includes user-owned local content that was intentionally preserved but not incorporated into the housekeeping commit.
- Recommended action:
  Decide whether `research/` should be added to version control, ignored, or maintained locally outside the repo lifecycle.
- Status: Pending review

### ISSUE-003 — Root Obsidian settings are tracked

- Severity: Low
- Area: Architecture
- Evidence:
  Root `.obsidian/` settings and plugin configuration are part of the tracked repository contents.
- Impact:
  This may be acceptable for a personal vault, but it can create review noise and accidental preference churn in a collaborative workflow.
- Recommended action:
  Reassess which `.obsidian/` files are essential project configuration versus user-local ergonomics.
- Status: Pending review
