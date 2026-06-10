# CINS Resource Arbitration Module - Allocation Policy
# Cognitive Integration & Navigation System - SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
import logging
logger = logging.getLogger("cins.allocation_policy")

class AllocationPolicy:
    CEILINGS = {"hard-rt": 0.40, "soft-rt": 0.45, "best-effort": 0.15}

    def check(self, tier: str, cpu: int, mem: int, pool) -> bool:
        ceiling = self.CEILINGS.get(tier, self.CEILINGS["best-effort"])
        max_cpu = int(pool.cpu_total * ceiling)
        max_mem = int(pool.mem_total * ceiling)
        if cpu > max_cpu or mem > max_mem:
            logger.warning(
                "Policy denied: tier=%s cpu=%d mem=%d ceiling=%.0f%%",
                tier, cpu, mem, ceiling * 100
            )
            return False
        return True
