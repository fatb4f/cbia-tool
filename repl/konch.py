"""Konch config (workbench).

Bootstraps:
- session logging
- EOFL helpers
- algoctrl adapter (if installed/available)
- operators namespace
"""

from __future__ import annotations

from cbia_workbench.repl.bootstrap import bootstrap

def context():
    return bootstrap()
