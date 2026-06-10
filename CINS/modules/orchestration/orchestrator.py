# CINS Orchestration Module — Orchestrator
# Cognitive Integration & Navigation System — SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
"""
orchestrator.py
Core orchestration controller for the CINS system.
Manages lifecycle of agent task execution: intake, routing, monitoring, resolution.
"""
import time
import logging
from typing import Optional
from .task_router import TaskRouter
from .priority_queue import PriorityQueue

logger = logging.getLogger("cins.orchestrator")

class Orchestrator:
    def __init__(self, config: Optional[dict] = None):
        self.config = config or {}
        self.router = TaskRouter()
        self.queue = PriorityQueue()
        self.active_tasks: dict = {}
        self.task_history: list = []
        logger.info("CINS Orchestrator initialized | v0.1.0")

    def submit_task(self, task_contract: dict) -> str:
        task_id = task_contract.get("task_id") or self._generate_task_id()
        task_contract["task_id"] = task_id
        task_contract["submitted_at"] = time.time()
        task_contract["status"] = "queued"
        priority = task_contract.get("priority", 3)
        self.queue.push(task_contract, priority)
        logger.info(f"Task queued | id={task_id} | priority={priority}")
        return task_id

    def process_next(self) -> Optional[dict]:
        task = self.queue.pop()
        if not task:
            return None
        task["status"] = "running"
        task["started_at"] = time.time()
        self.active_tasks[task["task_id"]] = task
        try:
            result = self.router.route(task)
            task["status"] = "completed"
            task["completed_at"] = time.time()
            task["result"] = result
        except Exception as e:
            task["status"] = "failed"
            task["error"] = str(e)
        finally:
            self.task_history.append(task)
            self.active_tasks.pop(task["task_id"], None)
        return task

    def get_status(self, task_id: str) -> Optional[dict]:
        if task_id in self.active_tasks:
            return self.active_tasks[task_id]
        for t in self.task_history:
            if t["task_id"] == task_id:
                return t
        return None

    def _generate_task_id(self) -> str:
        import uuid
        return f"cins-task-{uuid.uuid4().hex[:8]}"
