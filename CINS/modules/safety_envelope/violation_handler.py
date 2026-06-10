"""
CINS.modules.safety_envelope.violation_handler
-----------------------------------------------
Records constraint violations for audit and post-mortem analysis.

Each recorded entry captures:
    constraint : str   -- name of the failed constraint
    task_id    : str   -- ID of the offending task
    action     : str   -- response taken ("WARN", "HALT", "ESCALATE")
    ts         : float -- epoch timestamp of the violation
"""

import time


class ViolationHandler:
    """
    Append-only violation log for SafetyEnvelope decisions.
    """

    def __init__(self):
        self._history: list = []

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def record(self, constraint: str, task: dict, action: str) -> None:
        """
        Append a violation entry.

        Parameters
        ----------
        constraint : str  -- name of the constraint that failed
        task       : dict -- the offending task contract
        action     : str  -- enforcement action taken
        """
        self._history.append(
            {
                "constraint": constraint,
                "task_id":    task.get("task_id", "<unknown>"),
                "action":     action,
                "ts":         time.time(),
            }
        )

    def history(self) -> list:
        """
        Returns
        -------
        list of violation dicts, oldest first.
        Each dict: {"constraint": str, "task_id": str, "action": str, "ts": float}
        """
        return list(self._history)
