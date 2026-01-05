# Testing and Determinism

## Theory

Testing is easiest when code is deterministic. Deterministic code produces the same result every time for the same input, making failures meaningful and reproducible.

Unit tests should target operators, not pipelines. When operators are pure, tests are fast, isolated, and expressive. Integration tests can then focus on verifying wiring and boundaries.

In operational systems, determinism is also a safety feature. It allows you to reproduce failures, reason about changes, and trust automation.

## Key Takeaways
- Test pure operators first.
- Favor many small tests over few large ones.
- Determinism makes failures diagnosable.

---

# CLI and I/O Boundaries

## Theory

Command-line interfaces and file I/O are classic boundary layers. They translate human or system input into structured data and translate results back into artifacts or messages.

A clean CLI layer:
- Parses arguments
- Validates inputs
- Calls core logic
- Handles errors and exit codes

The CLI should not contain business logic. Its job is orchestration, not computation. This separation allows you to reuse the same core logic in scripts, services, or tests.

## Key Takeaways
- Treat CLI and I/O as boundary layers.
- Keep core logic reusable and independent.
- Use clear exit codes and error messages.
