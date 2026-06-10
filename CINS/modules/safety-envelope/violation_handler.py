# CINS Safety Envelope Module - Violation Handler
# Cognitive Integration & Navigation System - SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
import logging, time
logger = logging.getLogger("cins.violation_handler")

class ViolationHandler:
    def __init__(self):
        self.trail = []

    def record(self, constraint: str, task: dict, action: str):
        entry = {"constraint": constraint, "task_id": task.get("id", "unknown"),
                 "action": action, "ts": time.time()}
        self.trail.append(entry)
        logger.warning("VIOLATION [%s] task=%s -> %s", constraint, entry["task_id"], action)

    def history(self) -> list:
        return list(self.trail)
