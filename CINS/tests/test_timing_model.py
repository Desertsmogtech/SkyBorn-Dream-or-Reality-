# CINS Unit Tests  Timing Model Module
# Cognitive Integration & Navigation System  SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
#
# Covers: TimingModel, WindowManager, DeadlineMonitor
# Reference: docs/internal/timing-and-latency-model.md
#            docs/internal/timing-model-deep.md

import unittest
import time


# ---------------------------------------------------------------------------
# TimingModel Tests
# ---------------------------------------------------------------------------

class TestTimingModel(unittest.TestCase):

      def _make_timing(self):
                from CINS.modules.timing_model.timing_model import TimingModel
                return TimingModel()

      def test_assign_window_hard_rt(self):
                tm = self._make_timing()
                task = {"id": "tm001", "tier": "hard-rt"}
                window = tm.assign_window(task)
                self.assertEqual(window["budget_ms"], 5)
                self.assertEqual(window["jitter_ms"], 0.5)

      def test_assign_window_soft_rt(self):
                tm = self._make_timing()
                window = tm.assign_window({"id": "tm002", "tier": "soft-rt"})
                self.assertEqual(window["budget_ms"], 50)

      def test_assign_window_best_effort(self):
                tm = self._make_timing()
                window = tm.assign_window({"id": "tm003", "tier": "best-effort"})
                self.assertEqual(window["budget_ms"], 500)

      def test_assign_window_unknown_tier_defaults_to_best_effort(self):
                tm = self._make_timing()
                window = tm.assign_window({"id": "tm004", "tier": "unknown"})
                self.assertEqual(window["budget_ms"], 500)

      def test_window_contains_assigned_at(self):
                tm = self._make_timing()
                before = time.time()
                window = tm.assign_window({"id": "tm005", "tier": "soft-rt"})
                after = time.time()
                self.assertGreaterEqual(window["assigned_at"], before)
                self.assertLessEqual(window["assigned_at"], after)

      def test_window_contains_task_id(self):
                tm = self._make_timing()
                window = tm.assign_window({"id": "tm006", "tier": "hard-rt"})
                self.assertEqual(window["task_id"], "tm006")


# ---------------------------------------------------------------------------
# WindowManager Tests
# ---------------------------------------------------------------------------

class TestWindowManager(unittest.TestCase):

      def _make_wm(self):
                from CINS.modules.timing_model.window_manager import WindowManager
                return WindowManager()

      def _make_window(self, task_id, budget_ms=50):
                return {
                              "task_id": task_id,
                              "tier": "soft-rt",
                              "budget_ms": budget_ms,
                              "jitter_ms": 5,
                              "assigned_at": time.time()
                }

      def test_register_and_lookup(self):
                wm = self._make_wm()
                w = self._make_window("w001")
                wm.register(w)
                found = wm.lookup("w001")
                self.assertIsNotNone(found)
                self.assertEqual(found["task_id"], "w001")

      def test_lookup_missing_returns_none(self):
                wm = self._make_wm()
                self.assertIsNone(wm.lookup("nonexistent"))

      def test_remove_clears_window(self):
                wm = self._make_wm()
                wm.register(self._make_window("w002"))
                wm.remove("w002")
                self.assertIsNone(wm.lookup("w002"))

      def test_active_returns_all_registered(self):
                wm = self._make_wm()
                wm.register(self._make_window("w003"))
                wm.register(self._make_window("w004"))
                active = wm.active()
                ids = [w["task_id"] for w in active]
                self.assertIn("w003", ids)
                self.assertIn("w004", ids)

      def test_count_tracks_registrations(self):
                wm = self._make_wm()
                self.assertEqual(wm.count(), 0)
                wm.register(self._make_window("w005"))
                self.assertEqual(wm.count(), 1)
                wm.remove("w005")
                self.assertEqual(wm.count(), 0)


# ---------------------------------------------------------------------------
# DeadlineMonitor Tests
# ---------------------------------------------------------------------------

class TestDeadlineMonitor(unittest.TestCase):

      def _make_monitor(self):
                from CINS.modules.timing_model.window_manager import WindowManager
                from CINS.modules.timing_model.deadline_monitor import DeadlineMonitor
                wm = WindowManager()
                return DeadlineMonitor(wm), wm

      def test_no_overrun_when_fresh(self):
                monitor, wm = self._make_monitor()
                wm.register({
                    "task_id": "dm001",
                    "tier": "soft-rt",
                    "budget_ms": 5000,
                    "jitter_ms": 500,
                    "assigned_at": time.time()
                })
                overruns = monitor.check_all()
                self.assertEqual(len(overruns), 0)

      def test_overrun_detected_on_expired_window(self):
                monitor, wm = self._make_monitor()
                # Set assigned_at far in the past so it's definitely overrun
                wm.register({
                    "task_id": "dm002",
                    "tier": "hard-rt",
                    "budget_ms": 5,
                    "jitter_ms": 0.5,
                    "assigned_at": time.time() - 10  # 10 seconds ago = definitely overrun
                })
                overruns = monitor.check_all()
                self.assertEqual(len(overruns), 1)
                self.assertEqual(overruns[0]["task_id"], "dm002")

      def test_violations_accumulate(self):
                monitor, wm = self._make_monitor()
                past = time.time() - 10
                wm.register({"task_id": "dm003", "tier": "hard-rt",
                              "budget_ms": 5, "jitter_ms": 0.5, "assigned_at": past})
                wm.register({"task_id": "dm004", "tier": "soft-rt",
             
