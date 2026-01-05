# Python Core for Operators

## Theory

An *operator* is a small, deterministic unit of computation: it takes well-defined inputs and produces well-defined outputs. In operational Python work—especially in pipelines, tooling, and automation—operators are the foundation that allows systems to scale without becoming fragile.

The central idea is **purity at the core, side effects at the edges**. A pure operator has no hidden dependencies: no file access, no environment reads, no printing, no mutation of global state. Given the same inputs, it always returns the same output. This property makes reasoning, testing, and reuse straightforward.

In practice, Python encourages accidental impurity because it makes side effects easy. The discipline is therefore architectural, not syntactic. Inputs should arrive already parsed and validated; outputs should be returned as data structures, not written directly to disk or stdout. Operators can then be composed into pipelines where each step is independently testable.

Typing strengthens this discipline. By explicitly annotating inputs and outputs, you force yourself to define the operator’s contract. The goal is not exhaustive typing, but *meaningful typing* at the boundaries of each operator.

## Key Takeaways
- Operators should be deterministic and side-effect free.
- Parsing and I/O belong at boundaries, not inside operators.
- Explicit types make operator contracts visible and enforceable.
