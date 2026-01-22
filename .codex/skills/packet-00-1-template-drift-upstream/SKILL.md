# SKILL — Packet 00.1: Template drift upstream (scaffold-only)

## Intent
Apply scaffold/tooling updates that must be identical across downstream repos, and enforce lockfile policy.

## Working directory
Run from the root of the **cbia-tool** repo.

## Constraints (hard)
- Only modify the allowed paths listed in the packet contract.
- Do not edit src/** (shared logic refactor is a later phase).
- Do not add uv.lock to template outputs.
- No network calls.

## Procedure (mechanical)
1) Inspect current files:
   - tools/sync_material.py
   - README.md
   - justfile
   - tests/test_ramp1_purity.py
   - uv.lock presence (if any)

2) Implement:
   - Add/port `--fast` to tools/sync_material.py
   - Update README.md with usage example showing `--fast`
   - Add `just test` target
   - Fix tests/test_ramp1_purity.py import style

3) Lockfile policy:
   - Ensure uv.lock is not included in template.
   - If needed: add a short note in docs/ or README.md.
   - If needed: add uv.lock to .gitignore in template repo.

4) Verify:
   - Run tests (whatever is canonical for cbia-tool).
   - Confirm `git diff` touches only allowed paths.

## Evidence outputs (required)
Write these files under `./out/packet-00-1/`:
- diffstat.txt
- tests.txt
- policy_note.txt

## Done definition
All acceptance criteria in the packet contract are satisfied.

