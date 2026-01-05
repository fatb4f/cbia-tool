#!/usr/bin/env python3
"""
Sync generated material from cbia-builder into content/material/.

This is a *consumer-side* operation.
No building, no rendering, no mutation of the source.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
import sys


def die(msg: str) -> None:
    print(f"[sync-material] ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def sync_material(src: Path, dst: Path, *, clean: bool = False) -> None:
    if not src.exists():
        die(f"source does not exist: {src}")

    if not src.is_dir():
        die(f"source is not a directory: {src}")

    dst.parent.mkdir(parents=True, exist_ok=True)

    if dst.exists() and clean:
        shutil.rmtree(dst)

    if dst.exists():
        die(f"destination already exists: {dst} (use --clean to overwrite)")

    shutil.copytree(src, dst)
    print(f"[sync-material] synced {src} → {dst}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync material from cbia-builder into content/material/"
    )
    parser.add_argument(
        "--src",
        required=True,
        type=Path,
        help="Path to cbia-builder material directory (e.g. ../cbia-builder/dist/material)",
    )
    parser.add_argument(
        "--dst",
        default=Path("content/material"),
        type=Path,
        help="Destination directory (default: content/material)",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove destination before syncing",
    )

    args = parser.parse_args()
    sync_material(args.src, args.dst, clean=args.clean)


if __name__ == "__main__":
    main()
