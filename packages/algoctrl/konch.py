# konch.py (project root)
#
# Provides:
# - XDG-aware session log
# - EOFL-ish helpers: snapshot / gate / note / promote / end
# - Traceback capture via sys.excepthook
# - StageObserver wired to the SAME log (no duplicate handlers)
#
# Usage:
#   uv run konch

from __future__ import annotations

import logging
import os
import sys
import time
import traceback
from pathlib import Path
from uuid import uuid4

from algoctrl_tmpl.observer import Stage, StageObserver

# -----------------------------------------------------------------------------
# Log location (XDG-aware)
# Prefer XDG_STATE_HOME for session logs (vs cache).
# -----------------------------------------------------------------------------

state_home = Path(os.environ.get("XDG_STATE_HOME", "~/.local/state")).expanduser()
log_dir = state_home / "algoctrl-tmpl" / "repl"
log_dir.mkdir(parents=True, exist_ok=True)

session_id = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid4().hex[:6]
log_path = log_dir / f"repl-{session_id}.log"

# -----------------------------------------------------------------------------
# Logging setup (single sink)
# We configure root logging to write to log_path, and we make StageObserver use
# the root logger to avoid duplicate file handlers.
# -----------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
    handlers=[logging.FileHandler(log_path, encoding="utf-8")],
)

log = logging.getLogger("repl")


def _emit(tag: str, msg: str = "") -> None:
    msg = msg.replace("\n", "\\n").strip()
    log.info(f"{tag:<8} | {msg}")


# -----------------------------------------------------------------------------
# EOFL-ish helpers
# -----------------------------------------------------------------------------


def snapshot(intent: str, deliverable: str, constraints=None) -> None:
    _emit(
        "SNAPSHOT",
        f"intent={intent} | deliverable={deliverable} | constraints={constraints or []}",
    )


def gate(
    goal: str, success: list[str], rollback: str, bounded_inputs: list[str]
) -> None:
    _emit(
        "GATE",
        f"goal={goal} | success={success} | rollback={rollback} | inputs={bounded_inputs}",
    )


def note(msg: str) -> None:
    _emit("NOTE", msg)


def promote(artifact: str, why: str = "") -> None:
    _emit("PROMOTE", artifact + (f" | {why}" if why else ""))


def end(result: str) -> None:
    _emit("END", result)


# -----------------------------------------------------------------------------
# Exception hook (tracebacks go into the session log)
# -----------------------------------------------------------------------------


def _log_excepthook(exc_type, exc, tb):
    _emit("ERROR", "".join(traceback.format_exception(exc_type, exc, tb)).strip())


sys.excepthook = _log_excepthook

# -----------------------------------------------------------------------------
# Stage observer (same log file; no duplicate handlers)
# Root logger already has FileHandler from basicConfig above.
# -----------------------------------------------------------------------------

obs = StageObserver(
    run_id=session_id,
    level="INFO",
    logger_name="",  # root logger (inherits the FileHandler we configured)
    log_path=None,  # critical: do not add another FileHandler
)

_emit("START", f"log={log_path} | run={obs.run_id}")

# -----------------------------------------------------------------------------
# Konch context (names injected into the shell)
# -----------------------------------------------------------------------------

context = {
    # session
    "session_id": session_id,
    "log_path": log_path,
    # EOFL helpers
    "snapshot": snapshot,
    "gate": gate,
    "note": note,
    "promote": promote,
    "end": end,
    # stage observer
    "Stage": Stage,
    "StageObserver": StageObserver,
    "obs": obs,
}
