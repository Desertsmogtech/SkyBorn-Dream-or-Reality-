"""
CINS.modules.safety_envelope.safety_envelope
--------------------------------------------
Core safety evaluator.

Runs every registered constraint against an incoming task and escalates
according to the number and severity of failures.

Decision table
--------------
  0 violations               -> "PASS"
  1 non-critical violation   -> "WARN"   (logged, task continues)
  1 critical violation       -> "HALT"   (safe_hold set, task blocked)
  2+ violations of any kind  -> "ESCALATE" (safe_hold set, human loop required)

Critical constraints (halt on first failure):
    hard_rt_cpu_ceiling, nav_envelope

All others are non-critical (warn on single failure).
"""


class SafetyEnvelope:
    """
    Evaluates a task contract against all registered safety constraints.

    Parameters
    ----------
    registry : ConstraintRegistry
    handler  : ViolationHandler
    """

    _CRITICAL = {"hard_rt_cpu_ceiling", "nav_envelope"}

    def __init__(self, registry, handler):
        self._registry = registry
        self._handler  = handler
        self.safe_hold: bool = False

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def evaluate(self, task: dict) -> str:
        """
        Run all constraints and return the aggregate verdict.

        Returns
        -------
        "PASS"     -- all constraints satisfied
        "WARN"     -- exactly one non-critical violation
        "HALT"     -- one critical violation (safe_hold activated)
        "ESCALATE" -- two or more violations (safe_hold activated)
        """
        failures: list = []

        for name, fn in self._registry.constraints():
            try:
                passed = bool(fn(task))
            except Exception:
                # A constraint that throws is treated as a failure.
                passed = False

            if not passed:
                failures.append(name)

        if not failures:
            return "PASS"

        if len(failures) >= 2:
            self.safe_hold = True
            for name in failures:
                self._handler.record(name, task, "ESCALATE")
            return "ESCALATE"

        # Exactly one failure
        name = failures[0]
        if name in self._CRITICAL:
            self.safe_hold = True
            self._handler.record(name, task, "HALT")
            return "HALT"

        self._handler.record(name, task, "WARN")
        return "WARN"

    def reset(self) -> None:
        """
        Clear the safe_hold flag, re-enabling task evaluation.
        Does NOT clear the violation history.
        """
        self.safe_hold = False
