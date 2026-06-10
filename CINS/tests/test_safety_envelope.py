# CINS Unit Tests — Safety Envelope Module
# Cognitive Integration & Navigation System — SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
#
# Covers: ConstraintRegistry, ViolationHandler, SafetyEnvelope
# Reference: docs/internal/safety-envelope-spec.md
#            docs/internal/safety-envelope-deep.md

import unittest


# ---------------------------------------------------------------------------
# ConstraintRegistry Tests
# ---------------------------------------------------------------------------

class TestConstraintRegistry(unittest.TestCase):

    def _make_registry(self):
        from CINS.modules.safety_envelope.constraint_registry import ConstraintRegistry
        return ConstraintRegistry()

    def test_default_constraints_loaded(self):
        reg = self._make_registry()
        self.assertGreaterEqual(len(list(reg.constraints())), 4)

    def test_valid_task_passes_all_defaults(self):
        reg = self._make_registry()
        task = {"deadline": 100, "priority": 2, "type": "compute",
                "within_envelope": True, "tier": "soft-rt", "cpu": 2}
        results = [fn(task) for _, fn in reg.constraints()]
        self.assertTrue(all(r == "PASS" for r in results))

    def test_out_of_range_priority_halts(self):
        reg = self._make_registry()
        task = {"deadline": 100, "priority": 99, "type": "compute",
                "within_envelope": True, "tier": "soft-rt", "cpu": 1}
        results = [fn(task) for _, fn in reg.constraints()]
        self.assertIn("HALT", results)

    def test_missing_deadline_warns(self):
        reg = self._make_registry()
        task = {"priority": 2, "type": "compute", "within_envelope": True,
                "tier": "soft-rt", "cpu": 1}
        results = [fn(task) for _, fn in reg.constraints()]
        self.assertIn("WARN", results)

    def test_navigation_outside_envelope_escalates(self):
        reg = self._make_registry()
        task = {"deadline": 50, "priority": 1, "type": "navigation",
                "within_envelope": False, "tier": "hard-rt", "cpu": 2}
        results = [fn(task) for _, fn in reg.constraints()]
        self.assertIn("ESCALATE", results)

    def test_hard_rt_cpu_ceiling_breach_halts(self):
        reg = self._make_registry()
        task = {"deadline": 50, "priority": 1, "type": "compute",
                "within_envelope": True, "tier": "hard-rt", "cpu": 9}
        results = [fn(task) for _, fn in reg.constraints()]
        self.assertIn("HALT", results)

    def test_register_custom_constraint(self):
        reg = self._make_registry()
        reg.register("custom_check", lambda t: "HALT" if t.get("banned") else "PASS")
        task = {"deadline": 50, "priority": 2, "type": "compute",
                "within_envelope": True, "tier": "soft-rt", "cpu": 1, "banned": True}
        results = [fn(task) for _, fn in reg.constraints()]
        self.assertIn("HALT", results)


# ---------------------------------------------------------------------------
# ViolationHandler Tests
# ---------------------------------------------------------------------------

class TestViolationHandler(unittest.TestCase):

    def _make_handler(self):
        from CINS.modules.safety_envelope.violation_handler import ViolationHandler
        return ViolationHandler()

    def test_record_appends_to_trail(self):
        handler = self._make_handler()
        task = {"id": "v001"}
        handler.record("priority_range", task, "HALT")
        self.assertEqual(len(handler.history()), 1)

    def test_history_contains_correct_fields(self):
        handler = self._make_handler()
        handler.record("deadline_present", {"id": "v002"}, "WARN")
        entry = handler.history()[0]
        self.assertEqual(entry["constraint"], "deadline_present")
        self.assertEqual(entry["task_id"], "v002")
        self.assertEqual(entry["action"], "WARN")

    def test_multiple_violations_accumulate(self):
        handler = self._make_handler()
        handler.record("c1", {"id": "t1"}, "WARN")
        handler.record("c2", {"id": "t2"}, "HALT")
        handler.record("c3", {"id": "t3"}, "ESCALATE")
        self.assertEqual(len(handler.history()), 3)


# ---------------------------------------------------------------------------
# SafetyEnvelope Tests
# ---------------------------------------------------------------------------

class TestSafetyEnvelope(unittest.TestCase):

    def _make_envelope(self):
        from CINS.modules.safety_envelope.safety_envelope import SafetyEnvelope
        from CINS.modules.safety_envelope.constraint_registry import ConstraintRegistry
        from CINS.modules.safety_envelope.violation_handler import ViolationHandler
        return SafetyEnvelope(ConstraintRegistry(), ViolationHandler())

    def test_valid_task_passes(self):
        env = self._make_envelope()
        task = {"id": "s001", "deadline": 50, "priority": 2, "type": "compute",
                "within_envelope": True, "tier": "soft-rt", "cpu": 2}
        result = env.evaluate(task)
        self.assertEqual(result, "PASS")
        self.assertFalse(env.safe_hold)

    def test_halt_sets_safe_hold(self):
        env = self._make_envelope()
        task = {"id": "s002", "deadline": 50, "priority": 99, "type": "compute",
                "within_envelope": True, "tier": "soft-rt", "cpu": 1}
        result = env.evaluate(task)
        self.assertEqual(result, "HALT")
        self.assertTrue(env.safe_hold)

    def test_tasks_rejected_in_safe_hold(self):
        env = self._make_envelope()
        env.safe_hold = True
        task = {"id": "s003", "deadline": 50, "priority": 1, "type": "compute",
                "within_envelope": True, "tier": "hard-rt", "cpu": 1}
        result = env.evaluate(task)
        self.assertEqual(result, "HALT")

    def test_reset_clears_safe_hold(self):
        env = self._make_envelope()
        env.safe_hold = True
        env.reset()
        self.assertFalse(env.safe_hold)

    def test_warn_on_missing_deadline(self):
        env = self._make_envelope()
        task = {"id": "s004", "priority": 2, "type": "compute",
                "within_envelope": True, "tier": "soft-rt", "cpu": 1}
        result = env.evaluate(task)
        self.assertEqual(result, "WARN")

    def test_escalate_on_nav_outside_envelope(self):
        env = self._make_envelope()
        task = {"id": "s005", "deadline": 50, "priority": 1, "type": "navigation",
                "within_envelope": False, "tier": "hard-rt", "cpu": 2}
        result = env.evaluate(task)
        self.assertEqual(result, "ESCALATE")


if __name__ == "__main__":
    unittest.main()
