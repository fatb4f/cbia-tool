# CBIA Workbench (tooling skeleton)

This repo is a **workbench** that **consumes** generated CBIA material and provides:
- Konch/ptpython REPL surface
- session logging
- EOFL (External-Observer Feedback Loop) helpers
- algoctrl adapter hooks
- operators (learning-side code)

## Layout

- `content/material/` — populated externally (sparse-checkout); treated as read-only
- `src/cbia_workbench/` — all executable/helpers code (uv project)
- `tools/` — small entrypoint scripts (thin wrappers)

## Quickstart

```bash
uv venv
uv sync --all-extras
uv run konch -c repl/konch.py
```

Date: 2026-01-04
