# CINS Unit Tests — Orchestration Module
# Cognitive Integration & Navigation System — SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
#
# Covers: Orchestrator, TaskRouter, PriorityQueue
# Reference: docs/internal/orchestration-layer-spec.md

import unittest
import time


# ---------------------------------------------------------------------------
# PriorityQueue Tests
# ---------------------------------------------------------------------------

class TestPriorityQueue(unittest.TestCase):

    def _make_queue(self):
        from CINS.modules.orchestration.priority_queue import PriorityQueue
        return PriorityQueue()

    def test_push_pop_single(self):
        q = self._make_queue()
        task = {"task_id": "t001", "payload": {}}
        q.push(task, priority=2)
        result = q.pop()
        self.assertEqual(result["task_id"], "t001")

    def test_priority_ordering(self):
        """Lower priority number must dequeue first (higher urgency)."""
        q = self._make_queue()
        q.push({"task_id": "low"}, priority=5)
        q.push({"task_id": "high"}, priority=1)
        q.push({"task_id": "mid"}, priority=3)
        self.assertEqual(q.pop()["task_id"], "high")
        self.assertEqual(q.pop()["task_id"], "mid")
        self.assertEqual(q.pop()["task_id"], "low")

    def test_pop_empty_returns_none(self):
        q = self._make_queue()
        self.assertIsNone(q.pop())

    def test_size_and_is_empty(self):
        q = self._make_queue()
        self.assertTrue(q.is_empty())
        q.push({"task_id": "x"}, priority=3)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())

    def test_peek_does_not_remove(self):
        q = self._make_queue()
        q.push({"task_id": "peek_me"}, priority=1)
        peeked = q.peek()
        self.assertEqual(peeked["task_id"], "peek_me")
        self.assertEqual(q.size(), 1)

    def test_fifo_within_same_priority(self):
        """Tasks with equal priority must dequeue in submission order."""
        q = self._make_queue()
        q.push({"task_id": "first"}, priority=2)
        q.push({"task_id": "second"}, priority=2)
        self.assertEqual(q.pop()["task_id"], "first")


# ---------------------------------------------------------------------------
# TaskRouter Tests
# ---------------------------------------------------------------------------

class TestTaskRouter(unittest.TestCase):

    def _make_router(self):
        from CINS.modules.orchestration.task_router import TaskRouter
        return TaskRouter()

    def test_known_task_type_stub(self):
        router = self._make_router()
        task = {"task_id": "r001", "task_type": "compute"}
        result = router.route(task)
        self.assertEqual(result["status"], "stub")
        self.assertEqual(result["subsystem"], "resource_arbitration")

    def test_unknown_task_type_raises(self):
        router = self._make_router()
        with self.assertRaises(ValueError):
            router.route({"task_id": "r002", "task_type": "unknown_xyz"})

    def test_registered_handler_called(self):
        router = self._make_router()
        called = []

        def handler(task):
            called.append(task["task_id"])
            return {"status": "ok"}

        router.register_handler("sensor", handler)
        router.route({"task_id": "r003", "task_type": "sensor"})
        self.assertIn("r003", called)

    def test_navigation_routes_to_safety_envelope(self):
        router = self._make_router()
        task = {"task_id": "r004", "task_type": "navigation"}
        result = router.route(task)
        self.assertEqual(result["subsystem"], "safety_envelope")


# ---------------------------------------------------------------------------
# Orchestrator Tests
# ---------------------------------------------------------------------------

class TestOrchestrator(unittest.TestCase):

    def _make_orchestrator(self):
        from CINS.modules.orchestration.orchestrator import Orchestrator
        return Orchestrator()

    def test_submit_task_returns_id(self):
        orch = self._make_orchestrator()
        task_id = orch.submit_task({"task_type": "compute", "priority": 2})
        self.assertIsNotNone(task_id)
        self.assertTrue(task_id.startswith("cins-task-"))

    def test_process_next_empty_returns_none(self):
        orch = self._make_orchestrator()
        self.assertIsNone(orch.process_next())

    def test_submit_then_process(self):
        orch = self._make_orchestrator()
        tid = orch.submit_task({"task_type": "comms", "priority": 3})
        result = orch.process_next()
        self.assertIn(result["status"], ("completed", "failed"))
        self.assertEqual(result["task_id"], tid)

    def test_get_status_after_process(self):
        orch = self._make_orchestrator()
        tid = orch.submit_task({"task_type": "compute", "priority": 1})
        orch.process_next()
        status = orch.get_status(tid)
        self.assertIsNotNone(status)
        self.assertIn(status["status"], ("completed", "failed"))

    def test_priority_respected_across_submissions(self):
        orch = self._make_orchestrator()
        orch.submit_task({"task_id": "low", "task_type": "compute", "priority": 5})
        orch.submit_task({"task_id": "high", "task_type": "compute", "priority": 1})
        result = orch.process_next()
        self.assertEqual(result["task_id"], "high")


if __name__ == "__main__":
    unittest.main()
