# agents.md — tooling/workbench contract

This repo provides the **execution surface** (tools + helpers) for end users.

## Allowed changes by GPT
- Add/modify Python modules under `src/cbia_workbench/`
- Add/modify REPL config under `repl/`
- Add helper scripts under `tools/`
- Update docs and layouts

## Disallowed
- Generating or modifying CBIA learning material under `content/material/`
- Introducing schema generation or SSOT/CGP build logic (belongs to build repo)

## Invariants
- `content/material/` is treated as read-only and is populated externally.
- All runtime logic (except content consumption) lives under the uv project.
