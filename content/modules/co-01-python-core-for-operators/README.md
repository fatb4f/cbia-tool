# Write and refactor small, deterministic pipeline operators with clean module boundaries and safe IO at edges.

**Tags:** dev_practice, python_core, operators, io_edges

## Theory objectives

- **TH-01-operator-shape** — Define the operator as a deterministic transformation with explicit inputs/outputs and isolated side effects.
- **TH-02-io-boundary-rule** — Establish boundary discipline: parse/validate at edges; keep core logic pure.

## Skill objectives

- **1 SK-01-functions-and-return-types** — Implement 3 pure functions (transform/filter/aggregate) each with explicit type annotations. *(artefact: `src/operators/core_ops.py`)*
- **2 SK-02-exceptions-as-boundary** — Add explicit error handling at the boundary (raise domain errors; do not swallow exceptions). *(artefact: `src/operators/errors.py`)*
- **3 SK-03-safe-file-io** — Read/write JSON from disk using context managers; keep parsing in a single boundary function. *(artefact: `src/operators/io_json.py`)*
- **4 SK-04-modules-packages** — Split operators into a package with explicit exports and no circular imports. *(artefact: `src/operators/__init__.py`)*

## Generated artefacts (declared)

- `modules/co-01-python-core-for-operators/README.md` (kind=markdown, template=module_readme)
- `INDEX.md` (kind=index, template=project_index)

