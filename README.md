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

## Notebook usage (optional)

Install notebook extras:

```bash
pip install -e '.[notebook]'
```

Or with uv:

```bash
uv sync --extra notebook
```

Bootstrap in a notebook:

```python
from cbia_workbench.notebook import bootstrap_notebook

ctx = bootstrap_notebook()
globals().update({"ctx": ctx, "log": ctx.log, "eofl": ctx.eofl, "obs": ctx.obs, "op": ctx.op})
```

Templates live in `notebooks/templates/` (Jupytext Markdown format) and are intended
for lightweight drills and exercises. Notebooks are optional; the core install stays lean.

Date: 2026-01-04
