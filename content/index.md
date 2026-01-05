# Python CBIA Contract Pipelines v1

## Modules

- [Write and refactor small, deterministic pipeline operators with clean module boundaries and safe IO at edges.](modules/co-01-python-core-for-operators/README.md)
- [Encode stable operator/pipeline contracts using modern typing primitives to reduce ambiguity and enable static checking.](modules/co-02-typed-boundary-contracts/README.md)
- [Use Pydantic v2 models as the primary contract layer for validation, parsing, and serialization across pipeline boundaries.](modules/co-03-pydantic-contract-layer/README.md)
- [Maintain scalable project structure with explicit boundaries: schemas, operators, pipelines, CLI.](modules/co-04-repo-structure-and-import-discipline/README.md)
- [Expose pipelines through a deterministic CLI interface that orchestrates validated stages without embedding logic.](modules/co-05-cli-orchestration-with-typer/README.md)
- [Generate Markdown artifacts from validated SSOT models using deterministic templates and stable rendering rules.](modules/co-06-content-generation-layer/README.md)
- [Enforce correctness and stability with ruff, mypy, and pytest; verify contracts and transformations.](modules/co-07-verification-and-tooling/README.md)

