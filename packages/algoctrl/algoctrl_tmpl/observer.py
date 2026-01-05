"""observer.py — stage logging helpers for ramps (v2).

Adds:
- Stage enum for fixed vocabulary: GEN/STRUCT/SELECT/FLOW/EVAL
- Decorators: @stage_fn(Stage.GEN) to wrap functions
- Better type hints

Emits JSON lines by default to keep logs machine-readable.
"""

from __future__ import annotations

import json
import logging
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum
from functools import wraps
from typing import Any, Callable, Dict, Iterator, ParamSpec, TypeVar, Union


def _now_ms() -> int:
    return int(time.time() * 1000)


class Stage(str, Enum):
    GEN = "GEN"
    STRUCT = "STRUCT"
    SELECT = "SELECT"
    FLOW = "FLOW"
    EVAL = "EVAL"


P = ParamSpec("P")
R = TypeVar("R")

StageLike = Union[Stage, str]


@dataclass
class StageObserver:
    run_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    logger_name: str = "ramp"
    level: str = "INFO"
    enabled: bool = True
    emit_json: bool = True
    log_path: str | None = None

    def __post_init__(self) -> None:
        self.log = logging.getLogger(self.logger_name)
        if not self.log.handlers:
            if self.log_path:
                h = logging.FileHandler(self.log_path, encoding="utf-8")
            else:
                h = logging.StreamHandler()
            fmt = logging.Formatter("%(message)s")
            h.setFormatter(fmt)
            self.log.addHandler(h)
        self.log.setLevel(getattr(logging, self.level.upper(), logging.INFO))

    def _stage_val(self, stage: StageLike) -> str:
        return stage.value if isinstance(stage, Stage) else str(stage)

    def event(self, stage: StageLike, kind: str, **fields: Any) -> None:
        if not self.enabled:
            return
        payload: Dict[str, Any] = {
            "ts_ms": _now_ms(),
            "run": self.run_id,
            "stage": self._stage_val(stage),
            "kind": kind,
            **fields,
        }
        msg = (
            json.dumps(payload, ensure_ascii=False) if self.emit_json else str(payload)
        )
        self.log.info(msg)

    @contextmanager
    def stage(self, stage: StageLike, note: str = "", **fields: Any) -> Iterator[None]:
        """Context manager that logs stage start/end + elapsed time."""
        if not self.enabled:
            yield
            return

        t0 = time.perf_counter()
        self.event(stage, "start", note=note, **fields)
        try:
            yield
        except Exception as e:
            dt_ms = int((time.perf_counter() - t0) * 1000)
            self.event(stage, "error", note=note, elapsed_ms=dt_ms, err=repr(e))
            raise
        else:
            dt_ms = int((time.perf_counter() - t0) * 1000)
            self.event(stage, "end", note=note, elapsed_ms=dt_ms)

    def metric(self, stage: StageLike, name: str, value: Any, **fields: Any) -> None:
        self.event(stage, "metric", name=name, value=value, **fields)


def stage_fn(
    stage: StageLike, *, note: str = ""
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator wrapping a function in observer stage logs.

    Convention:
    - Wrapped function should accept `obs: StageObserver` as a kwarg.
    - If no observer is provided, function runs normally (no logs).
    """

    def deco(fn: Callable[P, R]) -> Callable[P, R]:
        @wraps(fn)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            obs = kwargs.get("obs")
            if not isinstance(obs, StageObserver):
                return fn(*args, **kwargs)
            with obs.stage(stage, note=note or fn.__name__):
                return fn(*args, **kwargs)

        return wrapped

    return deco


def configure_root_logging(level: str = "INFO") -> None:
    logging.basicConfig(level=getattr(logging, level.upper(), logging.INFO))
