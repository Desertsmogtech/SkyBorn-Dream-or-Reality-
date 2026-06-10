"""
CINS.modules.resource_arbitration.allocation_policy
----------------------------------------------------
Enforces per-tier CPU/memory ceiling policy.
"""


class AllocationPolicy:
    """
    Hard admission-control ceilings per scheduling tier.

    CEILINGS
    --------
    hard-rt      : 40% of pool
    soft-rt      : 45% of pool
    best-effort  : 15% of pool
    """

    CEILINGS: dict = {
        "hard-rt":     0.40,
        "soft-rt":     0.45,
        "best-effort": 0.15,
    }

    _DEFAULT_TIER = "best-effort"

    def check(self, tier: str, cpu: int, mem: int, pool) -> bool:
        """
        Evaluate whether allocating cpu slots and mem MB is permissible
        for the given tier given the current state of pool.

        Returns True if within policy limits, False if ceiling violated.
        """
        ceiling = self.CEILINGS.get(tier, self.CEILINGS[self._DEFAULT_TIER])
        cpu_limit = pool.cpu_total * ceiling
        mem_limit = pool.mem_total * ceiling
        new_cpu = pool.cpu_used + cpu
        new_mem = pool.mem_used + mem
        return new_cpu <= cpu_limit and new_mem <= mem_limit
