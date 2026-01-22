# Packet 00.2 — Naming SSOT + case hygiene

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
Freeze naming conventions in one SSOT doc and prevent case-only filename hazards (e.g., AGENTS.md vs agents.md).

## Repo
- cbia-tool (run Codex from repo root)

## Scope
### Allowed paths
- docs/NAMING.md
- AGENTS.md (and/or agents.md normalization)
- tools/** (only for a small case-check script)
- .github/workflows/** (optional CI gate; if present)
- README.md (optional pointer to NAMING.md)

### Forbidden
- Any changes to shared logic (src/**)
- Any unrelated formatting sweep

## Work
1) Create docs/NAMING.md (SSOT) that defines:
   - Repo names (kebab-case)
   - Distribution names (kebab-case)
   - Import modules (snake_case)
   - Reserved file casing: prefer AGENTS.md (uppercase)
   - “Template is scaffold-only” rule (no shared logic, no lockfile)
   - Downstream policy: generated lockfile is downstream-only

2) Normalize AGENTS.md casing in cbia-tool:
   - Choose AGENTS.md as canonical
   - Remove or rename agents.md if present

3) Add a mechanical case-collision check:
   - Detect case-insensitive duplicates in tracked files.
   - Fail CI (or at minimum provide a local script + documented command).

## Evidence (write to ./out/packet-00-2/)
- naming_doc.txt (path + short excerpt/headings list)
- case_check.txt (output from the collision check)
- diffstat.txt

## Acceptance criteria (binary)
- docs/NAMING.md exists and is referenced from README or docs index.
- Repo contains only AGENTS.md (no case-only duplicates).
- Case-collision check exists and is runnable (CI gate if workflow exists).

