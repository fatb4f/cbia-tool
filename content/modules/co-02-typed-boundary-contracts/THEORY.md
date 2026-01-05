# Typed Boundary Contracts

## Theory

In Python systems, ambiguity almost always enters through boundaries: reading files, parsing JSON, handling CLI arguments, or interacting with external systems. Typed boundary contracts exist to stop ambiguity at the door.

A boundary contract describes *exactly* what shape of data is allowed to cross into the core. This can be expressed using `TypedDict`, `dataclass`, or lightweight validation logic. The purpose is not to over-engineer, but to ensure that once data enters the core, it is trustworthy.

Typing is most valuable when applied asymmetrically: strict at the boundary, relaxed internally. Once data has been validated and normalized, operators can assume correctness and focus purely on transformation.

This approach mirrors real systems: APIs validate requests before invoking business logic; compilers type-check before execution; pipelines validate schemas before processing data.

## Key Takeaways
- Apply typing and validation at system boundaries.
- Convert raw inputs into structured, trusted forms early.
- Keep core logic simple by assuming validated inputs.
