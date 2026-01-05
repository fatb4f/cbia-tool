from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass(frozen=True)
class MaterialCheck:
    ok: bool
    exit_code: int
    errors: List[str]
    warnings: List[str]
    notes: List[str]


def verify_material(
    *,
    repo_root: Path,
    material_rel: Path = Path("content") / "material",
    manifest_rel: Path = Path("content") / "manifest.json",
) -> MaterialCheck:
    """Verify the consumer-side material contract.

    - content/material must exist
    - should contain at least one .md file
    - content/manifest.json is optional (recommended)
    """
    material = repo_root / material_rel
    manifest = repo_root / manifest_rel

    errors: List[str] = []
    warnings: List[str] = []
    notes: List[str] = []

    if not material.exists():
        errors.append(f"missing: {material}")
        return MaterialCheck(ok=False, exit_code=2, errors=errors, warnings=warnings, notes=notes)

    if not any(material.rglob("*.md")):
        warnings.append("warning: no markdown files found under content/material/")
    else:
        notes.append("ok: markdown present")

    if manifest.exists():
        notes.append("ok: manifest present")
    else:
        notes.append("note: content/manifest.json not found (optional but recommended)")

    ok = len(errors) == 0
    return MaterialCheck(ok=ok, exit_code=0 if ok else 2, errors=errors, warnings=warnings, notes=notes)
