"""
CINS.modules.resource_arbitration.resource_pool
-----------------------------------------------
Tracks physical resource availability (CPU slots, memory, I/O bandwidth).
All allocate/release operations are synchronous and deterministic.
"""


class ResourcePool:
    """
    Manages a finite pool of computational resources.

    Defaults
    --------
    cpu_slots : 16
    memory_mb : 4096
    io_kbps   : 100 000
    """

    _DEFAULTS = {
        "cpu_slots": 16,
        "memory_mb": 4096,
        "io_kbps": 100_000,
    }

    def __init__(self, **overrides):
        cfg = {**self._DEFAULTS, **overrides}
        self.cpu_total: int = cfg["cpu_slots"]
        self.mem_total: int = cfg["memory_mb"]
        self.io_total: int  = cfg["io_kbps"]
        self.cpu_used: int  = 0
        self.mem_used: int  = 0
        self.io_used: int   = 0

    def allocate(self, cpu: int = 0, mem: int = 0, io: int = 0) -> bool:
        if (
            self.cpu_used + cpu > self.cpu_total
            or self.mem_used + mem > self.mem_total
            or self.io_used  + io  > self.io_total
        ):
            return False
        self.cpu_used += cpu
        self.mem_used += mem
        self.io_used  += io
        return True

    def release(self, cpu: int = 0, mem: int = 0, io: int = 0) -> None:
        self.cpu_used = max(0, self.cpu_used - cpu)
        self.mem_used = max(0, self.mem_used - mem)
        self.io_used  = max(0, self.io_used  - io)

    def utilization(self) -> dict:
        return {
            "cpu_pct": self.cpu_used / self.cpu_total if self.cpu_total else 0.0,
            "mem_pct": self.mem_used / self.mem_total if self.mem_total else 0.0,
        }

    def status(self) -> dict:
        return {
            "cpu_free": self.cpu_total - self.cpu_used,
            "mem_free": self.mem_total - self.mem_used,
        }
