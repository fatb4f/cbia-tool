# Packet XX — <title>

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
<one sentence>

## Repos
- <repo>

## Scope
Allowed paths:
- ...

Forbidden:
- network access
- lockfiles in template outputs

## Outputs
- files added/changed list

## Invariants
- stage_enter/stage_exit schema unchanged
- template contains scaffold only
- downstream consumes shared logic via dependency pin

## Evidence
- out/packet-XX/diffstat.txt
- out/packet-XX/tests.txt
- out/packet-XX/schema_assertions.txt (if applicable)

## Acceptance criteria
- <binary checks>

