# CINS Timing Model Module - Deadline Monitor
# Cognitive Integration & Navigation System - SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
import logging, time
logger = logging.getLogger("cins.deadline_monitor")

class DeadlineMonitor:
      def __init__(self, window_manager):
                self.wm = window_manager
                self.violations = []

      def check_all(self) -> list:
                now = time.time()
                overruns = []
                for w in self.wm.active():
                              elapsed = (now - w["assigned_at"]) * 1000
                              if elapsed > w["budget_ms"] + w["jitter_ms"]:
                                                entry = {"task_id": w["task_id"], "elapsed_ms": round(elapsed, 2),
                                                                                  "limit_ms": w["budget_ms"] + w["jitter_ms"]}
                                                overruns.append(entry)
                                                self.violations.append(entry)
                                                logger.warning("DEADLINE OVERRUN: %s", entry)
                                        return overruns
