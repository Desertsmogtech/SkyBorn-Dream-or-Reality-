# CINS Orchestration Module — Priority Queue
# Cognitive Integration & Navigation System — SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
"""
priority_queue.py
Min-heap based priority queue for CINS task scheduling.
Priority 1 = highest (critical/hard-RT), Priority 5 = lowest (background).
Ties are broken by submission timestamp (FIFO within same priority).
"""
import heapq
import time
import logging
logger = logging.getLogger("cins.priority_queue")

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0

    def push(self, task: dict, priority: int = 3):
        entry = (priority, self._counter, time.time(), task)
        heapq.heappush(self._heap, entry)
        self._counter += 1
        logger.debug(f"Enqueued task priority={priority} | queue_size={len(self._heap)}")

    def pop(self):
        if not self._heap:
            return None
        _, _, _, task = heapq.heappop(self._heap)
        logger.debug(f"Dequeued task id={task.get('task_id')} | queue_size={len(self._heap)}")
        return task

    def peek(self):
        if not self._heap:
            return None
        return self._heap[0][3]

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0
