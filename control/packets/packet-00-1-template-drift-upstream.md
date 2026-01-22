# Packet 00.1 — Template drift upstream (scaffold-only)

## Pre-authorized changes (no STOP required)
Codex may proceed without additional approval for:
- Adding/removing dev/test dependencies in `pyproject.toml` ONLY as required to run the packet’s tests.
- Editing `.gitignore` ONLY to enforce “no lockfiles in template outputs”.
- Adding small mechanical scripts under `tools/` to produce evidence or enforce the packet invariants.
- Editing docs (`docs/**`) to document the packet’s policy changes.

## Hard prohibitions (must STOP)
- Touching `src/**` unless explicitly allowed.
- Committing or keeping `uv.lock` in the template repo (delete if generated).
- Any network calls.
- Broad refactors unrelated to the packet goal.

## Goal
Upstream the scaffold/tooling deltas that must be identical across downstream repos, and enforce “lockfile is downstream-only”.

## Repo
- cbia-tool (run Codex from repo root)

## Preconditions
- You have a local checkout of INF_1220 available for comparison (read-only).

 ## Scope
 ### Allowed paths (cbia-tool)
 - tools/sync_material.py
 - README.md
 - justfile
 - tests/test_ramp1_purity.py
+- pyproject.toml
 - docs/** (only if needed to document lockfile policy)
 - .gitignore (only if needed for lockfile policy)

 ### Forbidden
 - Any changes to src/** shared logic (that becomes `ctrl` later)
 - Any change that requires network access
-- Adding uv.lock to the template output
+- Adding uv.lock to the template output (uv.lock must remain downstream-only)


## Work
1) Port `--fast` option into `tools/sync_material.py` (from downstream drift).
2) Update `README.md` to document `--fast`.
3) Update `justfile` to include a `test` target (if missing).
4) Fix `tests/test_ramp1_purity.py` imports to be package-qualified consistently.
5) Remove `uv.lock` from template if present and document lockfile policy:
   - “Template must not ship lockfiles; downstream generates its own uv.lock”.
6) Ensure test runner availability:
   - If pytest is required to run tests and is not present, add `pytest` to `pyproject.toml`
     under the project’s dev/test dependency mechanism (use the existing convention in this repo).
   - Do NOT add or commit `uv.lock` as part of this packet; template must not ship lockfiles.

## Evidence (write to ./out/packet-00-1/)
- diffstat.txt (git diff --stat)
- tests.txt (test output)
- policy_note.txt (paths changed + summary)

## Acceptance criteria (binary)
- cbia-tool tests pass locally.
- Template output does not include uv.lock.
- Changes limited to the allowed paths.
- If `pyproject.toml` was modified, it only adds the minimal pytest dev/test dependency required.
- `uv.lock` is not added or modified in the template repo.

