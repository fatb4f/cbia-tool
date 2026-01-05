from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from cbia_workbench.repl.session_logging import SessionLogger

try:
    from algoctrl_tmpl.observer import Stage, StageObserver  # type: ignore
except Exception:  # pragma: no cover
    Stage = None  # type: ignore
    StageObserver = None  # type: ignore


@dataclass
class AlgoCtrlAdapter:
    """Bridge between the workbench and algoctrl.

    Works as:
    - real adapter if algoctrl is installed
    - ndjson-only logger if not
    """

    log: SessionLogger
    _obs: Any = None

    def __post_init__(self) -> None:
        if StageObserver is not None:
            self._obs = StageObserver()

    def available(self) -> bool:
        return self._obs is not None

    def stage(self, name: str, *, note: str = ""):
        if self._obs is not None and Stage is not None:
            try:
                st = getattr(Stage, name)
            except Exception:
                st = Stage.FLOW
            return self._obs.stage(st, note=note)
        return _LogStage(self.log, name=name, note=note)


class _LogStage:
    def __init__(self, log: SessionLogger, *, name: str, note: str) -> None:
        self.log = log
        self.name = name
        self.note = note

    def __enter__(self):
        self.log.event("stage_enter", {"stage": self.name, "note": self.note})
        return self

    def __exit__(self, exc_type, exc, tb):
        self.log.event("stage_exit", {"stage": self.name, "exc": str(exc) if exc else ""})
        return False
