from __future__ import annotations

from cbia_workbench.p1_compute.bootstrap import WorkbenchContext, bootstrap_ctx
from cbia_workbench.repl.session_logging import SessionLoggingConfig


def bootstrap_notebook(*, log_dir: str | None = None, flush_every: int = 25) -> WorkbenchContext:
    """Notebook-friendly bootstrap with quiet logging defaults."""
    cfg = SessionLoggingConfig(console=False, flush_every=flush_every)
    return bootstrap_ctx(log_dir=log_dir, logging_config=cfg)
