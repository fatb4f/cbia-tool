#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from collections import defaultdict

def git_ls_files() -> list[str]:
    p = subprocess.run(
        ["git", "ls-files"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in p.stdout.splitlines() if line.strip()]

def main() -> int:
    files = git_ls_files()
    groups: dict[str, list[str]] = defaultdict(list)
    for f in files:
        groups[f.lower()].append(f)

    collisions = {k: v for k, v in groups.items() if len(v) > 1}
    if not collisions:
        print("OK: no case-insensitive filename collisions.")
        return 0

    print("ERROR: case-insensitive filename collisions detected:\n")
    for k, v in sorted(collisions.items()):
        print(f"{k}")
        for item in sorted(v):
            print(f"  - {item}")
        print()
    return 1

if __name__ == "__main__":
    raise SystemExit(main())

