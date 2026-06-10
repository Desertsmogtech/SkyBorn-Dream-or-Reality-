# CINS Test Suite — Shared Fixtures (pytest conftest)
# Cognitive Integration & Navigation System — SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
#
# Fixtures available to all test modules automatically.

import pytest
import time


# ---------------------------------------------------------------------------
# Full CINS stack fixture — one isolated stack per test function
# ---------------------------------------------------------------------------

@pytest.fixture
def cins_stack():
    """
    Returns a fully initialized, isolated CINS stack.
    Each test gets a fresh instance with no shared state.
    """
    from CINS.modules.orchestration.orchestrator import Orchestrator
    from CINS.modules.orchestration.task_router import TaskRouter
    from CINS.modules.orchestration.priority_queue import PriorityQueue
    from CINS.modules.resource_arbitration.resource_pool import ResourcePool
    from CINS.modules.resource_arbitration.allocation_policy import AllocationPolicy
    from CINS.modules.resource_arbitration.arbitrator import ResourceArbitrator
    from CINS.modules.safety_envelope.constraint_registry import ConstraintRegistry
    from CINS.modules.safety_envelope.violation_handler import ViolationHandler
    from CINS.modules.safety_envelope.safety_envelope import SafetyEnvelope
    from CINS.modules.timing_model.timing_model import TimingModel
    from CINS.modules.timing_model.window_manager import WindowManager
    from CINS.modules.timing_model.deadline_monitor import DeadlineMonitor

    pool   = ResourcePool()
    policy = AllocationPolicy()
    arb    = ResourceArbitrator(pool=pool, policy=policy)
    reg    = ConstraintRegistry()
    vh     = ViolationHandler()
    env    = SafetyEnvelope(reg, vh)
    wm     = WindowManager()
    dm     = DeadlineMonitor(wm)
    tm     = TimingModel()
    pq     = PriorityQueue()
    router = TaskRouter()
    orch   = Orchestrator()

    return {
        "orchestrator":  orch,
        "router":        router,
        "priority_queue": pq,
        "pool":          pool,
        "policy":        policy,
        "arbitrator":    arb,
        "registry":      reg,
        "violation_handler": vh,
        "envelope":      env,
        "timing":        tm,
        "window_mgr":    wm,
        "deadline_mon":  dm,
    }


# ---------------------------------------------------------------------------
# Shared task factories
# ---------------------------------------------------------------------------

@pytest.fixture
def valid_compute_task():
    return {
        "id": "fixture-compute-001",
        "task_id": "fixture-compute-001",
        "task_type": "compute",
        "deadline": 100,
        "priority": 2,
        "type": "compute",
        "within_envelope": True,
        "tier": "soft-rt",
        "cpu": 1,
        "memory": 64,
    }


@pytest.fixture
def valid_navigation_task():
    return {
        "id": "fixture-nav-001",
        "task_id": "fixture-nav-001",
        "task_type": "navigation",
        "deadline": 50,
        "priority": 1,
        "type": "navigation",
        "within_envelope": True,
        "tier": "hard-rt",
        "cpu": 2,
        "memory": 128,
    }


@pytest.fixture
def expired_window():
    return {
        "task_id": "fixture-expired-001",
        "tier": "hard-rt",
        "budget_ms": 5,
        "jitter_ms": 0.5,
        "assigned_at": time.time() - 60,
    }


@pytest.fixture
def fresh_window():
    return {
        "task_id": "fixture-fresh-001",
        "tier": "soft-rt",
        "budget_ms": 60000,
        "jitter_ms": 6000,
        "assigned_at": time.time(),
    }
