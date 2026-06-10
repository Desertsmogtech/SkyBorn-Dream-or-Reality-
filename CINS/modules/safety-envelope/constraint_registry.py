# CINS Safety Envelope Module - Constraint Registry
# Cognitive Integration & Navigation System - SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
import logging
logger = logging.getLogger("cins.constraint_registry")

class ConstraintRegistry:
    def __init__(self):
        self._store = {}
        self._load_defaults()

    def _load_defaults(self):
        self.register("deadline_present", lambda t: "PASS" if t.get("deadline") else "WARN")
        self.register("priority_range", lambda t: "PASS" if 1 <= t.get("priority", 3) <= 5 else "HALT")
        self.register("nav_envelope", lambda t: "PASS" if t.get("type") != "navigation" or t.get("within_envelope", True) else "ESCALATE")
        self.register("hard_rt_cpu_ceiling", lambda t: "PASS" if t.get("tier") != "hard-rt" or t.get("cpu", 1) <= 8 else "HALT")

    def register(self, name: str, fn):
        self._store[name] = fn

    def constraints(self):
        return self._store.items()
