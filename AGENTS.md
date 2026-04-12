# Repository Guidelines

## Project Structure & Module Organization
This repository is a minimal Obsidian vault, not an application codebase. Store content as top-level Markdown notes such as `AIP-C01.md`. Keep Obsidian settings in `.obsidian/` and avoid manual edits there unless you are intentionally changing vault behavior. There are currently no `src/`, `tests/`, or asset folders; if the vault grows, group related notes in clearly named directories such as `aws/`, `drafts/`, or `references/`.

## Build, Test, and Development Commands
There is no build pipeline. Use lightweight validation instead:

- `open -a Obsidian .` opens the vault locally in Obsidian.
- `rg '^#' *.md` checks heading structure across notes.
- `markdownlint "**/*.md"` validates Markdown formatting if `markdownlint` is installed.

Prefer commands that inspect content without rewriting files automatically.

## Coding Style & Naming Conventions
Write notes in Markdown with clear heading hierarchy and short sections. Use sentence-style prose, fenced code blocks for commands, and backticks for services, paths, and filenames. Name notes descriptively with stable topic labels, for example `AIP-C01.md` or `bedrock-knowledge-bases.md`. Use hyphenated lowercase names for new multiword files unless an existing naming scheme already applies.

## Testing Guidelines
There is no automated test framework in this vault. Validation means checking Markdown rendering, link accuracy, and note completeness in Obsidian. Before submitting changes, confirm:

- headings render correctly
- internal links resolve
- long notes remain scannable with concise sections

If you add scripts later, place them in a dedicated folder and document how to run them here.

## Commit & Pull Request Guidelines
Git history is not available in this workspace, so use a simple default convention: imperative, scope-first commit messages such as `docs: refine AIP-C01 study guide`. Keep each commit focused on one note set or one configuration change. PRs should include a short summary, affected paths, screenshots only when `.obsidian/` UI settings change, and any manual validation performed.

## Agent-Specific Instructions
Do not overwrite user-authored note content without preserving intent. Keep edits narrow, avoid unnecessary `.obsidian/` churn, and prefer adding structure over rewriting large study notes wholesale.
