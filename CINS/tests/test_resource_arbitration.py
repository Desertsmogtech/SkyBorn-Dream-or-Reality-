# CINS Unit Tests — Resource Arbitration Module
# Cognitive Integration & Navigation System — SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
#
# Covers: ResourcePool, AllocationPolicy, ResourceArbitrator
# Reference: docs/internal/resource-arbitration-deep.md

import unittest


# ---------------------------------------------------------------------------
# ResourcePool Tests
# ---------------------------------------------------------------------------

class TestResourcePool(unittest.TestCase):

    def _make_pool(self, **kwargs):
        from CINS.modules.resource_arbitration.resource_pool import ResourcePool
        return ResourcePool(**kwargs)

    def test_default_pool_initializes(self):
        pool = self._make_pool()
        self.assertEqual(pool.cpu_total, 16)
        self.assertEqual(pool.mem_total, 4096)

    def test_allocate_success(self):
        pool = self._make_pool()
        ok = pool.allocate(cpu=2, mem=256)
        self.assertTrue(ok)
        self.assertEqual(pool.cpu_used, 2)
        self.assertEqual(pool.mem_used, 256)

    def test_allocate_exceeds_capacity_fails(self):
        pool = self._make_pool()
        ok = pool.allocate(cpu=100, mem=256)
        self.assertFalse(ok)

    def test_release_restores_resources(self):
        pool = self._make_pool()
        pool.allocate(cpu=4, mem=512)
        pool.release(cpu=4, mem=512)
        self.assertEqual(pool.cpu_used, 0)
        self.assertEqual(pool.mem_used, 0)

    def test_utilization_returns_percentages(self):
        pool = self._make_pool()
        pool.allocate(cpu=8, mem=2048)
        util = pool.utilization()
        self.assertAlmostEqual(util["cpu_pct"], 50.0)
        self.assertAlmostEqual(util["mem_pct"], 50.0)

    def test_sequential_allocations_accumulate(self):
        pool = self._make_pool()
        pool.allocate(cpu=4, mem=512)
        pool.allocate(cpu=4, mem=512)
        self.assertEqual(pool.cpu_used, 8)


# ---------------------------------------------------------------------------
# AllocationPolicy Tests
# ---------------------------------------------------------------------------

class TestAllocationPolicy(unittest.TestCase):

    def _make_policy_and_pool(self):
        from CINS.modules.resource_arbitration.allocation_policy import AllocationPolicy
        from CINS.modules.resource_arbitration.resource_pool import ResourcePool
        return AllocationPolicy(), ResourcePool()

    def test_hard_rt_within_ceiling_approved(self):
        policy, pool = self._make_policy_and_pool()
        ok = policy.check("hard-rt", cpu=4, mem=256, pool=pool)
        self.assertTrue(ok)

    def test_hard_rt_exceeds_ceiling_denied(self):
        policy, pool = self._make_policy_and_pool()
        ok = policy.check("hard-rt", cpu=10, mem=256, pool=pool)
        self.assertFalse(ok)

    def test_best_effort_within_ceiling_approved(self):
        policy, pool = self._make_policy_and_pool()
        ok = policy.check("best-effort", cpu=1, mem=64, pool=pool)
        self.assertTrue(ok)

    def test_unknown_tier_falls_back_to_best_effort(self):
        policy, pool = self._make_policy_and_pool()
        result = policy.check("unknown-tier", cpu=1, mem=64, pool=pool)
        self.assertIsInstance(result, bool)


# ---------------------------------------------------------------------------
# ResourceArbitrator Tests
# ---------------------------------------------------------------------------

class TestResourceArbitrator(unittest.TestCase):

    def _make_arbitrator(self):
        from CINS.modules.resource_arbitration.arbitrator import ResourceArbitrator
        from CINS.modules.resource_arbitration.resource_pool import ResourcePool
        from CINS.modules.resource_arbitration.allocation_policy import AllocationPolicy
        return ResourceArbitrator(pool=ResourcePool(), policy=AllocationPolicy())

    def test_request_granted(self):
        arb = self._make_arbitrator()
        result = arb.request({"id": "a001", "tier": "soft-rt", "cpu": 2, "memory": 128})
        self.assertEqual(result["status"], "granted")
        self.assertIn("rid", result)

    def test_request_denied_over_ceiling(self):
        arb = self._make_arbitrator()
        result = arb.request({"id": "a002", "tier": "hard-rt", "cpu": 12, "memory": 128})
        self.assertEqual(result["status"], "denied")

    def test_release_after_grant(self):
        arb = self._make_arbitrator()
        result = arb.request({"id": "a003", "tier": "best-effort", "cpu": 1, "memory": 64})
        rid = result["rid"]
        arb.release(rid)
        snap = arb.snapshot()
        self.assertEqual(snap["active"], 0)

    def test_snapshot_active_count(self):
        arb = self._make_arbitrator()
        arb.request({"id": "a004", "tier": "soft-rt", "cpu": 1, "memory": 64})
        arb.request({"id": "a005", "tier": "soft-rt", "cpu": 1, "memory": 64})
        snap = arb.snapshot()
        self.assertEqual(snap["active"], 2)


if __name__ == "__main__":
    unittest.main()
