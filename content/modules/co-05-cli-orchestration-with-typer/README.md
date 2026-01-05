# Expose pipelines through a deterministic CLI interface that orchestrates validated stages without embedding logic.

**Tags:** cli, typer, orchestration, dev_practice

## Theory objectives

- **TH-08-thin-cli** — CLI is a control surface: it wires stages, loads settings, and handles IO; it does not contain transformation logic.

## Skill objectives

- **1 SK-16-typer-single-command** — Create a Typer command that loads settings, parses inputs, runs pipeline, writes outputs. *(artefact: `src/cli/app.py`)*
- **2 SK-17-subcommands** — Add subcommands for validate-only, render-only, and full-run. *(artefact: `src/cli/commands.py`)*
- **3 SK-18-exit-codes** — Implement explicit exit codes for validation failure vs runtime failure. *(artefact: `src/cli/errors.py`)*

## Generated artefacts (declared)

- `modules/co-05-cli-orchestration-with-typer/README.md` (kind=markdown, template=module_readme)

