from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Optional

try:
    from rich.console import Console
except Exception:  # pragma: no cover
    Console = None  # type: ignore


@dataclass(frozen=True)
class SessionLoggingConfig:
    log_dir: Optional[Path] = None
    prefix: str = "cbia"
    include_pid: bool = True
    console: bool = True
    flush_every: int = 1


class SessionLogger:
    """Minimal session logger (ndjson)."""

    def __init__(self, cfg: SessionLoggingConfig) -> None:
        self.cfg = cfg
        self.session_id: str | None = None
        self.path: Path | None = None
        self._fp = None
        self._console = Console() if Console and cfg.console else None
        self._event_count = 0

    def start(self) -> "SessionLogger":
        ts = time.strftime("%Y%m%d-%H%M%S")
        pid = os.getpid()
        self.session_id = f"{self.cfg.prefix}-{ts}" + (f"-{pid}" if self.cfg.include_pid else "")
        log_dir = self.cfg.log_dir or Path.cwd() / ".logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        self.path = log_dir / f"{self.session_id}.ndjson"
        self._fp = self.path.open("a", encoding="utf-8", buffering=1)
        self._event_count = 0
        self.event("session_start", {"session_id": self.session_id, "path": str(self.path)})
        return self

    def close(self) -> None:
        if self._fp:
            self.event("session_end", {})
            self._fp.close()
            self._fp = None

    def event(self, kind: str, data: Mapping[str, Any]) -> None:
        payload = {"t": time.time(), "kind": kind, "data": dict(data)}
        line = json.dumps(payload, ensure_ascii=False)
        if self._fp:
            self._fp.write(line + "\n")
            self._event_count += 1
            flush_every = max(1, self.cfg.flush_every)
            if self._event_count % flush_every == 0:
                self._fp.flush()

        if self.cfg.console:
            msg = f"[{kind}]"
            if "note" in data:
                msg += f" {data['note']}"
            if self._console:
                self._console.print(msg)
            else:
                print(msg)

    def kv(self, **items: Any) -> None:
        self.event("kv", items)
