# Composition and Pipelines

## Theory

Composition is the act of building larger behaviors by chaining smaller operators. A pipeline is a concrete expression of composition, where data flows through a sequence of transformations.

Well-designed pipelines have:
- Clear stages
- Explicit inputs and outputs
- No hidden coupling between steps

Each stage should do exactly one thing. When a pipeline becomes difficult to understand, it usually means one stage is doing too much or leaking concerns.

In Python, pipelines can be expressed simply: function calls, lists of callables, or small orchestration functions. Avoid premature abstraction—clarity beats cleverness.

## Key Takeaways
- Pipelines are sequences of small, focused operators.
- Each stage should have a single responsibility.
- Prefer explicit flow over implicit magic.
