# CINS Resource Arbitration Module - Resource Pool
# Cognitive Integration & Navigation System - SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
import logging
logger = logging.getLogger("cins.resource_pool")

class ResourcePool:
    DEFAULTS = {"cpu_slots": 16, "memory_mb": 4096, "io_kbps": 100000}

    def __init__(self, **overrides):
        cfg = {**self.DEFAULTS, **overrides}
        self.cpu_total = cfg["cpu_slots"]
        self.mem_total = cfg["memory_mb"]
        self.io_total = cfg["io_kbps"]
        self.cpu_used = 0
        self.mem_used = 0

    def allocate(self, cpu: int, mem: int) -> bool:
        if self.cpu_used + cpu > self.cpu_total or self.mem_used + mem > self.mem_total:
            return False
        self.cpu_used += cpu
        self.mem_used += mem
        return True

    def release(self, cpu: int, mem: int):
        self.cpu_used = max(0, self.cpu_used - cpu)
        self.mem_used = max(0, self.mem_used - mem)

    def utilization(self) -> dict:
        return {"cpu_pct": round(self.cpu_used / self.cpu_total * 100, 1),
                "mem_pct": round(self.mem_used / self.mem_total * 100, 1)}

    def status(self) -> dict:
        return {"cpu_free": self.cpu_total - self.cpu_used,
                "mem_free": self.mem_total - self.mem_used}
