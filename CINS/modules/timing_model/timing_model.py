"""
CINS.modules.timing_model.timing_model
---------------------------------------
Assigns real-time execution windows to incoming tasks based on their
scheduling tier.

Profiles
--------
    hard-rt      : budget_ms=5,   jitter_ms=0.5
    soft-rt      : budget_ms=50,  jitter_ms=5
    best-effort  : budget_ms=500, jitter_ms=50

Any unrecognised tier falls back to "best-effort".
"""

import time


class TimingModel:
    """
    Maps task scheduling tiers to timing window parameters.
    """

    PROFILES: dict = {
        "hard-rt":     {"budget_ms": 5,   "jitter_ms": 0.5},
        "soft-rt":     {"budget_ms": 50,  "jitter_ms": 5.0},
        "best-effort": {"budget_ms": 500, "jitter_ms": 50.0},
    }

    _DEFAULT_TIER = "best-effort"

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def assign_window(self, task: dict) -> dict:
        """
        Derive a timing window from the task's declared tier.

        Parameters
        ----------
        task : dict
            Must contain "task_id" and optionally "tier".

        Returns
        -------
        {
            "task_id":     str,
            "tier":        str,
            "budget_ms":   int   (or float),
            "jitter_ms":   float,
            "assigned_at": float  (epoch seconds)
        }
        """
        tier    = task.get("tier", self._DEFAULT_TIER)
        profile = self.PROFILES.get(tier, self.PROFILES[self._DEFAULT_TIER])

        return {
            "task_id":     task.get("task_id", ""),
            "tier":        tier,
            "budget_ms":   profile["budget_ms"],
            "jitter_ms":   profile["jitter_ms"],
            "assigned_at": time.time(),
        }
