from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional

from cbia_workbench.repl.session_logging import SessionLogger


@dataclass
class EOFLState:
    intent: Optional[str] = None
    current_state: Optional[str] = None
    next_deliverable: Optional[str] = None
    constraints: Optional[str] = None
    goal: Optional[str] = None
    success: Optional[str] = None
    rollback: Optional[str] = None
    bounded_inputs: Optional[str] = None


class EOFL:
    """External-Observer Feedback Loop helpers."""

    def __init__(self, *, log: SessionLogger) -> None:
        self.log = log
        self.state = EOFLState()

    def start(self, *, intent: str, current_state: str, next_deliverable: str, constraints: str = "") -> None:
        self.state.intent = intent
        self.state.current_state = current_state
        self.state.next_deliverable = next_deliverable
        self.state.constraints = constraints
        self.log.event("eofl_start", {
            "intent": intent,
            "current_state": current_state,
            "next_deliverable": next_deliverable,
            "constraints": constraints,
        })

    def pre_action(self, *, goal: str, success: str, rollback: str, bounded_inputs: str) -> None:
        self.state.goal = goal
        self.state.success = success
        self.state.rollback = rollback
        self.state.bounded_inputs = bounded_inputs
        self.log.event("eofl_pre_action", {
            "goal": goal,
            "success": success,
            "rollback": rollback,
            "bounded_inputs": bounded_inputs,
        })

    def post_action(self, *, outcome: str, notes: str = "", metrics: Optional[Mapping[str, Any]] = None) -> None:
        self.log.event("eofl_post_action", {
            "outcome": outcome,
            "notes": notes,
            "metrics": dict(metrics) if metrics else {},
        })
