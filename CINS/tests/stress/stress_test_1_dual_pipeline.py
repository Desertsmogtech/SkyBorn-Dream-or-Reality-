# CINS Stress Test #1  Dual-Pipeline Convergence
# Cognitive Integration & Navigation System  SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
#
# Scroll Number:      #148
# Codex Reference:    C.I.N.S. Codex Book v1.1  Section 3.6
# Event Date:         April 8, 2026
# Codified:           June 8, 2026
# Author:             Jason  Solo Tech Design Studio
# Classification:     Operator-Grade | Contributor-Ready | PG-13 Compliant
#
# Test Question:
#   If a single pipeline can fail under external interference, what happens
#   when two pipelines operate simultaneously? Can CINS hold coordination
#   fidelity without resource contention, signal drift, or false convergence?
#
# Configuration  Roko Triad:
#   Pipeline A   Active agent, divergent reasoning map
#   Pipeline B   Active agent, divergent reasoning map
#   Roko         Validator / Observer Layer (not a peer  a structural check)
#
# Result (April 8, 2026):
#   "All systems, one rhythm."
#   CINS sustained multi-agent coordination without shared memory,
#   cross-pipeline communication, or synchronization scaffolding.
#
# Reference: CINS/docs/CINS_Stress_Test_1_Convergence_Record.md

import unittest
import time
import threading


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_full_stack():
      """Build a complete isolated CINS stack for one pipeline instance."""
      from CINS.modules.orchestration.orchestrator import Orchestrator
      from CINS.modules.orchestration.task_router import TaskRouter
      from CINS.modules.resource_arbitration.resource_pool import ResourcePool
      from CINS.modules.resource_arbitration.allocation_policy import AllocationPolicy
      from CINS.modules.resource_arbitration.arbitrator import ResourceArbitrator
      from CINS.modules.safety_envelope.constraint_registry import ConstraintRegistry
      from CINS.modules.safety_envelope.violation_handler import ViolationHandler
      from CINS.modules.safety_envelope.safety_envelope import SafetyEnvelope
      from CINS.modules.timing_model.window_manager import WindowManager
      from CINS.modules.timing_model.deadline_monitor import DeadlineMonitor
      from CINS.modules.timing_model.timing_model import TimingModel

    pool   = ResourcePool()
    policy = AllocationPolicy()
    arb    = ResourceArbitrator(pool=pool, policy=policy)
    reg    = ConstraintRegistry()
    vh     = ViolationHandler()
    env    = SafetyEnvelope(reg, vh)
    wm     = WindowManager()
    dm     = DeadlineMonitor(wm)
    tm     = TimingModel()
    orch   = Orchestrator()

    return {
              "orchestrator": orch,
              "arbitrator":   arb,
              "envelope":     env,
              "timing":       tm,
              "window_mgr":   wm,
              "deadline_mon": dm,
    }


def _run_pipeline(stack: dict, task_batch: list, results: list):
      """
          Execute a batch of tasks through a CINS stack.
              Appends per-task result dicts to `results` (thread-safe by list append).
                  """
      orch  = stack["orchestrator"]
      arb   = stack["arbitrator"]
      env   = stack["envelope"]
      tm    = stack["timing"]
      wm    = stack["window_mgr"]

    for task in task_batch:
              # 1. Safety check
              safety = env.evaluate(task)
              if safety == "HALT":
                            results.append({"task_id": task["id"], "status": "halted",
                                                                         "pipeline": task.get("pipeline")})
                            continue

              # 2. Resource allocation
              alloc = arb.request(task)
              if alloc["status"] == "denied":
                            results.append({"task_id": task["id"], "status": "denied",
                                                                         "pipeline": task.get("pipeline")})
                            continue

              # 3. Timing window
              window = tm.assign_window(task)
              wm.register(window)

        # 4. Submit + process
              tid = orch.submit_task(task)
        orch.process_next()

        # 5. Release resources
        arb.release(alloc["rid"])
        wm.remove(task["id"])

        results.append({"task_id": task["id"], "status": "executed",
                                                "pipeline": task.get("pipeline"),
                                                "budget_ms": window["budget_ms"]})


# ---------------------------------------------------------------------------
# Module 1  Load Simulation
# Two pipelines run 20 tasks each concurrently. No contention expected.
# Expected: Both pipelines execute all tasks without denial or halt.
# ---------------------------------------------------------------------------

class TestModule1LoadSimulation(unittest.TestCase):
      """
          Stress Test #1 | Module 1  Load Simulation
              Result (April 8, 2026): No resource contention detected.
                  Both pipelines maintained stable execution.
                      """

    def test_dual_pipeline_no_contention(self):
              stack_a = _make_full_stack()
              stack_b = _make_full_stack()

        def make_batch(pipeline_label, count=20):
                      return [
                                        {
                                                              "id": f"{pipeline_label}-task-{i:03d}",
                                                              "pipeline": pipeline_label,
                                                    
