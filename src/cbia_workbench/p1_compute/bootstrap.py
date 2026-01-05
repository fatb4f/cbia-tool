from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

from cbia_workbench.repl.session_logging import SessionLogger, SessionLoggingConfig
from cbia_workbench.repl.eofl import EOFL
from cbia_workbench.observe.algoctrl_adapter import AlgoCtrlAdapter
from cbia_workbench.p2_inference.operators import core_ops, io_json, errors


@dataclass(frozen=True)
class WorkbenchContext:
    log: SessionLogger
    eofl: EOFL
    obs: AlgoCtrlAdapter


def bootstrap(*, log_dir: str | None = None) -> Dict[str, Any]:
    """Build the REPL context.

    Side effects are allowed here (e.g. log directory creation).
    Keep other modules side-effect free on import.
    """
    cfg = SessionLoggingConfig(log_dir=Path(log_dir) if log_dir else None)
    log = SessionLogger(cfg).start()
    eofl = EOFL(log=log)
    obs = AlgoCtrlAdapter(log=log)

    op = {"core": core_ops, "io": io_json, "errors": errors}
    ctx = WorkbenchContext(log=log, eofl=eofl, obs=obs)

    return {
        "log": ctx.log,
        "eofl": ctx.eofl,
        "obs": ctx.obs,
        "op": op,
        "core": core_ops,
        "io": io_json,
        "E": errors,
    }
