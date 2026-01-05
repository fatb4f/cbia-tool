# Generate Markdown artifacts from validated SSOT models using deterministic templates and stable rendering rules.

**Tags:** content_gen, jinja2, markdown, ssot

## Theory objectives

- **TH-09-rendering-rules** — Rendering is a pure function from validated models to artifacts; templates are part of the contract.

## Skill objectives

- **1 SK-19-jinja2-template** — Create a Jinja2 template that renders a model into Markdown. *(artefact: `templates/doc.md.j2`)*
- **2 SK-20-render-function** — Implement a render(model) -> str function; no IO inside. *(artefact: `src/pipelines/render.py`)*
- **3 SK-21-jupytext-pairing** — Add Jupytext pairing config for Markdown ↔ notebook workflow (optional layer). *(artefact: `jupytext config file`)*

## Generated artefacts (declared)

- `modules/co-06-content-generation-layer/README.md` (kind=markdown, template=module_readme)

