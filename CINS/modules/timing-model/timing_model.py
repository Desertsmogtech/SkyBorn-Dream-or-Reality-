# CINS Timing Model Module - Core
# Cognitive Integration & Navigation System - SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
import logging, time
logger = logging.getLogger("cins.timing_model")

class TimingModel:
    PROFILES = {
        "hard-rt": {"budget_ms": 5, "jitter_ms": 0.5},
        "soft-rt": {"budget_ms": 50, "jitter_ms": 5},
        "best-effort": {"budget_ms": 500, "jitter_ms": 50},
    }

    def assign_window(self, task: dict) -> dict:
        tier = task.get("tier", "best-effort")
        profile = self.PROFILES.get(tier, self.PROFILES["best-effort"])
        return {"task_id": task.get("id"), "tier": tier,
                "budget_ms": profile["budget_ms"], "jitter_ms": profile["jitter_ms"],
                "assigned_at": time.time()}
