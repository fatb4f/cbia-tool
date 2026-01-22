# SKILL — Packet 00.2: Naming SSOT + case hygiene

## Intent
Create a single naming SSOT and prevent cross-platform case-only file conflicts.

## Working directory
Run from the root of the **cbia-tool** repo.

## Constraints (hard)
- Do not touch src/**.
- No broad refactors.
- Ensure AGENTS.md casing is canonical and unique.

## Procedure
1) Write docs/NAMING.md with:
   - naming conventions (repo/dist/module)
   - casing rules (AGENTS.md)
   - scaffold vs shared logic boundary
   - lockfile policy

2) Normalize AGENTS.md:
   - Rename agents.md -> AGENTS.md if needed
   - Remove duplicates

3) Add case collision check:
   - Provide tools/check_case_collisions.py (or equivalent)
   - Optionally wire into CI if workflows exist

## Evidence outputs (required)
Write these under `./out/packet-00-2/`:
- naming_doc.txt
- case_check.txt
- diffstat.txt

## Done definition
All acceptance criteria in the packet contract are satisfied.

