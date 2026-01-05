# Encode stable operator/pipeline contracts using modern typing primitives to reduce ambiguity and enable static checking.

**Tags:** theory, typing, contracts, dev_practice

## Theory objectives

- **TH-03-types-as-contracts** — Treat types as executable documentation for boundary contracts; constrain shapes before validation.
- **TH-04-structural-interfaces** — Prefer structural typing (Protocols) for operator interfaces over inheritance.

## Skill objectives

- **1 SK-05-typeddict-input-shape** — Define a TypedDict for raw external input and use it in a parser signature. *(artefact: `src/schemas/raw_input.py`)*
- **2 SK-06-literal-enums** — Use Literal to constrain a field/value used for routing or mode selection. *(artefact: `src/schemas/literals.py`)*
- **3 SK-07-protocol-operator-interface** — Define a Protocol for an operator callable and type-check two implementations. *(artefact: `src/operators/protocols.py`)*
- **4 SK-08-annotated-metadata** — Introduce Annotated for a constrained value (e.g., non-empty string) as metadata used downstream. *(artefact: `src/schemas/annotated.py`)*

## Generated artefacts (declared)

- `modules/co-02-typed-boundary-contracts/README.md` (kind=markdown, template=module_readme)

