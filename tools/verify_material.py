from __future__ import annotations

from pathlib import Path

from cbia_workbench.p1_compute.contracts import verify_material


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    result = verify_material(repo_root=repo_root)

    for line in result.errors:
        print(line)
    for line in result.warnings:
        print(line)
    for line in result.notes:
        print(line)

    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
