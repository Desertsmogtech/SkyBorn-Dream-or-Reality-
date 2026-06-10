"""
CINS.modules.safety_envelope.constraint_registry
-------------------------------------------------
Maintains a named catalogue of safety constraint functions.

Each constraint is a callable of the form:

    fn(task: dict) -> bool

Returning False triggers a violation in SafetyEnvelope.evaluate().

Four default constraints are registered at construction:

    deadline_present    -- task must carry a non-None "deadline" field
    priority_range      -- priority must be an integer in [1, 10]
    nav_envelope        -- navigation tasks must include "nav_params" key
    hard_rt_cpu_ceiling -- hard-rt tasks may not request > 6 CPU slots
"""


class ConstraintRegistry:
    """
    Registry of named safety predicates.
    """

    # Maximum CPU slots a hard-rt task may claim (policy constant).
    _HARD_RT_CPU_MAX = 6

    def __init__(self):
        self._constraints: dict = {}
        self._register_defaults()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _register_defaults(self) -> None:
        self.register(
            "deadline_present",
            lambda task: task.get("deadline") is not None,
        )
        self.register(
            "priority_range",
            lambda task: isinstance(task.get("priority"), int)
                         and 1 <= task.get("priority", 0) <= 10,
        )
        self.register(
            "nav_envelope",
            lambda task: task.get("task_type") != "navigation"
                         or "nav_params" in task,
        )
        self.register(
            "hard_rt_cpu_ceiling",
            lambda task: task.get("tier") != "hard-rt"
                         or int(task.get("cpu", 0)) <= self._HARD_RT_CPU_MAX,
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def register(self, name: str, fn) -> None:
        """
        Add or replace a named constraint predicate.

        Parameters
        ----------
        name : str   -- unique identifier for this constraint
        fn   : callable(task: dict) -> bool
        """
        if not callable(fn):
            raise TypeError(f"Constraint '{name}' must be callable, got {type(fn)}")
        self._constraints[name] = fn

    def constraints(self):
        """
        Returns
        -------
        dict_items -- iterable of (name, fn) pairs, preserving insertion order.
        """
        return self._constraints.items()
