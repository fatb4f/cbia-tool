"""Ramp 1: boundary I/O for JSON (effects at edges)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .errors import InputShapeError


def load_json(path: str | Path) -> Any:
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: str | Path, obj: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")


def parse_numbers(obj: Any) -> list[int]:
    """Accept either:
    - a list[int]
    - {"numbers": list[int]}
    """
    if isinstance(obj, dict) and "numbers" in obj:
        obj = obj["numbers"]

    if not isinstance(obj, list):
        raise InputShapeError("Expected a list of integers or {'numbers': [...]}")

    out: list[int] = []
    for i, x in enumerate(obj):
        if isinstance(x, bool) or not isinstance(x, int):
            raise InputShapeError(f"numbers[{i}] must be int (got {type(x).__name__})")
        out.append(x)
    return out
