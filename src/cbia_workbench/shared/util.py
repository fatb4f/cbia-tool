from __future__ import annotations

from pathlib import Path


def repo_root_from(file: str) -> Path:
    """Resolve repository root given a file path inside the repo."""
    return Path(file).resolve().parents[2]
