"""
CINS.modules.timing_model.deadline_monitor
-------------------------------------------
Polls all active timing windows and reports any that have overrun their
allocated budget.

An overrun is defined as:

    (current_time - assigned_at) * 1000  >  budget_ms

Overruns are appended to the persistent `violations` list so that
post-mortem analysis can review every deadline miss in the session.
"""

import time


class DeadlineMonitor:
    """
    Scans WindowManager entries for deadline violations.

    Parameters
    ----------
    window_manager : WindowManager
    """

    def __init__(self, window_manager):
        self._wm = window_manager
        self.violations: list = []

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def check_all(self) -> list:
        """
        Iterate over all active windows and collect any that have exceeded
        their budget_ms allocation.

        Returns
        -------
        list of dicts -- one entry per overrun::

            {
                "task_id":    str,
                "elapsed_ms": float,
                "limit_ms":   float,
            }

        Side effect: each overrun entry is also appended to
        ``self.violations`` for session-level audit.
        """
        now = time.time()
        overruns = []

        for window in self._wm.active():
            elapsed_ms = (now - window["assigned_at"]) * 1000.0
            limit_ms = float(window["budget_ms"])

            if elapsed_ms > limit_ms:
                entry = {
                    "task_id": window["task_id"],
                    "elapsed_ms": elapsed_ms,
                    "limit_ms": limit_ms,
                }
                overruns.append(entry)
                self.violations.append(entry)

        return overruns
