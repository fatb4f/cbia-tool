# Validation and Invariants

## Theory

Validation ensures that data satisfies *invariants*: conditions that must always be true for the system to behave correctly. Invariants are stronger than type checks—they encode domain rules.

Examples of invariants include:
- IDs must be unique
- Paths must exist
- Lists must not be empty
- Numeric values must fall within a defined range

A common mistake is scattering validation logic throughout the codebase. Instead, validation should be centralized and explicit. Once invariants are checked, downstream code can rely on them without defensive programming.

In operational pipelines, validation failures are not exceptional—they are expected and informative. Good validation produces clear error messages that explain *which invariant failed and why*.

## Key Takeaways
- Validation enforces domain rules, not just types.
- Check invariants once, early.
- Fail loudly and descriptively when invariants are violated.
