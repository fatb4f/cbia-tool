"""Ramp 1: pure operators (no I/O, no prints, no env access)."""

from __future__ import annotations

from typing import Iterable


def normalize_numbers(xs: list[int]) -> list[int]:
    """Remove negatives, sort ascending, return a new list (no mutation)."""
    # filter first to avoid sorting negatives then dropping (clarity > micro-optimizations)
    ys = [x for x in xs if x >= 0]
    return sorted(ys)


def summarize(xs: list[int]) -> dict[str, int]:
    """Return count/min/max/sum for a list of ints.

    Precondition: xs must be non-empty.
    """
    if not xs:
        raise ValueError("summarize() requires a non-empty list")
    return {
        "count": len(xs),
        "min": min(xs),
        "max": max(xs),
        "sum": sum(xs),
    }
