# Use Pydantic v2 models as the primary contract layer for validation, parsing, and serialization across pipeline boundaries.

**Tags:** pydantic, contracts, validation, serialization

## Theory objectives

- **TH-05-boundary-validation** — Validate at boundaries; inside the pipeline operate on already-validated models.
- **TH-06-serialization-is-contract** — Treat model_dump output as a stable API between stages and for generated artifacts.

## Skill objectives

- **1 SK-09-basemodel-minimal** — Create a BaseModel with field constraints; validate valid/invalid inputs. *(artefact: `src/schemas/models.py`)*
- **2 SK-10-model-validate** — Parse raw dict input using model_validate and return a model from the boundary function. *(artefact: `src/operators/parse.py`)*
- **3 SK-11-model-dump** — Serialize models using model_dump in a pipeline output function; ensure stable keys. *(artefact: `src/operators/serialize.py`)*
- **4 SK-12-custom-validator** — Implement a custom validator for a cross-field invariant (e.g., start <= end). *(artefact: `src/schemas/validators.py`)*
- **5 SK-13-settings-model** — Define a BaseSettings model for pipeline configuration and load it via environment variables. *(artefact: `src/schemas/settings.py`)*

## Generated artefacts (declared)

- `modules/co-03-pydantic-contract-layer/README.md` (kind=markdown, template=module_readme)

