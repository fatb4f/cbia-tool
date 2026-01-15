from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from types import MappingProxyType
from typing import Any, Dict, Mapping

from cbia_workbench.repl.session_logging import SessionLogger, SessionLoggingConfig
from cbia_workbench.repl.eofl import EOFL
from cbia_workbench.observe.algoctrl_adapter import AlgoCtrlAdapter
from cbia_workbench.p2_inference.operators import core_ops, io_json, errors


@dataclass(frozen=True)
class WorkbenchContext:
    log: SessionLogger
    eofl: EOFL
    obs: AlgoCtrlAdapter
    op: Mapping[str, Any]


_OP_REGISTRY: Mapping[str, Any] = MappingProxyType({"core": core_ops, "io": io_json, "errors": errors})


def bootstrap_ctx(
    *,
    log_dir: str | None = None,
    logging_config: SessionLoggingConfig | None = None,
) -> WorkbenchContext:
    """Build the REPL context as a typed object."""
    if logging_config is None:
        cfg = SessionLoggingConfig(log_dir=Path(log_dir) if log_dir else None)
    else:
        cfg = replace(logging_config, log_dir=Path(log_dir) if log_dir else logging_config.log_dir)
    log = SessionLogger(cfg).start()
    eofl = EOFL(log=log)
    obs = AlgoCtrlAdapter(log=log)

    return WorkbenchContext(log=log, eofl=eofl, obs=obs, op=_OP_REGISTRY)


def bootstrap(*, log_dir: str | None = None) -> Dict[str, Any]:
    """Build the REPL context.

    Side effects are allowed here (e.g. log directory creation).
    Keep other modules side-effect free on import.
    """
    ctx = bootstrap_ctx(log_dir=log_dir)

    return {
        "log": ctx.log,
        "eofl": ctx.eofl,
        "obs": ctx.obs,
        "op": ctx.op,
        "core": core_ops,
        "io": io_json,
        "E": errors,
    }
