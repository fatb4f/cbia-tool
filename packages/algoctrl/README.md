# algoctrl-tmpl

Algorithmic ramp template using an explicit control pipeline and lightweight observer hooks.

Core pipeline: GEN → STRUCT → SELECT → FLOW → EVAL


- **GEN**: generate candidate state
- **STRUCT**: organize state / enforce invariants
- **SELECT**: prune state space
- **FLOW**: control progression over time
- **EVAL**: decide / score / terminate

## Repo layout

**Mechanism**
  [observer](src/observer.py)
  [observer](src/example_solution.py)
**Templates**
  [Problem](.github/template/PROBLEM_TEMPLATE.md)
  [Readme](.github/template/README_TEMPLATE.md)
  [Settings](.github/template/GITHUB_SETTINGS.md)
**Versioning**
  [Ramp](.github/versioning/RAMP_VERSIONING.md)
**Docs**
  [Diagram](.github/docs/diagram.png)
  [Minimal Pattern](.github/docs/minimal_usage_pattern.md)
  [Control-Checklist](.github/docs/ctrl-checklist.md)


## Quickstart (uv)

Create an isolated environment and install tools:

```bash
uv venv
source .venv/bin/activate
uv pip install -U ptpython konch # tools for REPL + ramp work
```

Run the example with stage logs:
```bash
python src/example_solution.py
```

Optional: run a REPL in this environment with konch

```bash
konch \
  --config-file .konshrc
```

## Using this as a template repo

1. GitHub → Use this template
2. In the new repo, copy .github/template/problem.md into a new ramp folder:
  - e.g. ramps/ramp-00/problem.md
3. Fill problem.md before coding
4. Implement with explicit stage boundaries and log metrics with StageObserver

## Design rules (non-negotiable)

- State must be observable
- Feedback must be bounded
- Termination must be explicit
- Prefer pruning over cleverness


---

## `uv` bootstrap (recommended shape)

### Minimal (tooling only; no packaging decisions)
```bash
uv venv
source .venv/bin/activate
uv pip install -U ptpython konch
```
