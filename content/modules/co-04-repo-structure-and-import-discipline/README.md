# Maintain scalable project structure with explicit boundaries: schemas, operators, pipelines, CLI.

**Tags:** architecture, repo_layout, imports, dev_practice

## Theory objectives

- **TH-07-import-direction** — Define import direction: CLI → pipelines → operators → schemas (no reverse dependencies).

## Skill objectives

- **1 SK-14-src-layout** — Implement src/ layout with packages for schemas/operators/pipelines/cli and a single public entry module. *(artefact: `src/ (package tree)`)*
- **2 SK-15-boundary-contracts-compiled** — Run mypy and eliminate Any leakage across module boundaries. *(artefact: `mypy config + passing check`)*

## Generated artefacts (declared)

- `modules/co-04-repo-structure-and-import-discipline/README.md` (kind=markdown, template=module_readme)

