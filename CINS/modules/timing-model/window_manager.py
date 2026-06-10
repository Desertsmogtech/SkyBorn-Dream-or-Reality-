# CINS Timing Model Module - Window Manager
# Cognitive Integration & Navigation System - SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
import logging
logger = logging.getLogger("cins.window_manager")

class WindowManager:
    def __init__(self):
        self._windows = {}

    def register(self, window: dict):
        tid = window.get("task_id")
        self._windows[tid] = window
        logger.debug("Window registered | task_id=%s", tid)

    def lookup(self, task_id: str) -> dict:
        return self._windows.get(task_id)

    def remove(self, task_id: str):
        self._windows.pop(task_id, None)
        logger.debug("Window removed | task_id=%s", task_id)

    def active(self) -> list:
        return list(self._windows.values())

    def count(self) -> int:
        return len(self._windows)
