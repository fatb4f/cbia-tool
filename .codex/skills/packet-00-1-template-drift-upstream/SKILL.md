---
name: packet-00-1-template-drift-upstream
description: Execute Packet 00.1 in cbia-tool—upstream scaffold/tooling deltas and enforce downstream-only uv.lock; write evidence to ./out/packet-00-1.
---

# Packet 00.1 — Template drift upstream (scaffold-only)

## When to use
Use when running **Packet 00.1** for the **cbia-tool** repo.

## Working directory
Run from the **cbia-tool repo root**.

## Inputs
- Packet contract: `control/packets/packet-00-1-template-drift-upstream.md`

## Hard constraints
- Mirror the codex-web sandbox network policy allowing outbound connections for mainstream tools and librairies. 
- Modify only paths allowed by the packet contract.
- Do not touch `src/**` unless explicitly allowed by the contract.
- Always write evidence to `./out/packet-00-1/`.

## Procedure
1) Read the packet contract and follow it exactly (Goal, Scope, Work, Forbidden, Acceptance).
2) Before changes, write baseline evidence:
   - `out/packet-00-1/status_before.txt` = `git status --porcelain=v1`
   - `out/packet-00-1/diff_before.txt`   = `git diff`
   - `out/packet-00-1/head_before.txt`   = `git rev-parse HEAD`
3) Apply the Work items from the contract.
4) After changes, write required evidence:
   - `out/packet-00-1/diffstat.txt`      = `git diff --stat`
   - `out/packet-00-1/diff_after.txt`    = `git diff`
   - `out/packet-00-1/status_after.txt`  = `git status --porcelain=v1`
   - `out/packet-00-1/head_after.txt`    = `git rev-parse HEAD`
   - `out/packet-00-1/changed_files.txt` = changed paths, one per line
   - `out/packet-00-1/tests.txt`         = full output of required tests
   - `out/packet-00-1/acceptance.txt`    = PASS/FAIL per acceptance criterion + brief justification
   - `out/packet-00-1/scope_check.txt`   = PASS/FAIL that only allowed paths were modified (list violations if any)
5) If scope/forbidden constraints block required work:
   - STOP and write `out/packet-00-1/stop.txt` with the blocking reason and minimal contract change needed.

## Commit discipline
Do not commit unless the packet contract explicitly requests it.

