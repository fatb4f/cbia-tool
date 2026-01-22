# Packet 00.1 — Template drift upstream (scaffold-only)

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
- docs/** (only if needed to document lockfile policy)
- .gitignore (only if needed for lockfile policy)

### Forbidden
- Any changes to src/** shared logic (that becomes `ctrl` later)
- Any change that requires network access
- Adding uv.lock to the template output

## Work
1) Port `--fast` option into `tools/sync_material.py` (from downstream drift).
2) Update `README.md` to document `--fast`.
3) Update `justfile` to include a `test` target (if missing).
4) Fix `tests/test_ramp1_purity.py` imports to be package-qualified consistently.
5) Remove `uv.lock` from template if present and document lockfile policy:
   - “Template must not ship lockfiles; downstream generates its own uv.lock”.

## Evidence (write to ./out/packet-00-1/)
- diffstat.txt (git diff --stat)
- tests.txt (test output)
- policy_note.txt (paths changed + summary)

## Acceptance criteria (binary)
- cbia-tool tests pass locally.
- Template output does not include uv.lock.
- Changes limited to the allowed paths.

