# CINS Resource Arbitration Module - Arbitrator
# Cognitive Integration & Navigation System - SkyBorn Dream or Reality
# Desertsmogtech | v0.1.0
import logging, uuid, time
logger = logging.getLogger("cins.resource_arbitration")

class ResourceArbitrator:
    def __init__(self, pool, policy):
        self.pool = pool
        self.policy = policy
        self._ledger = {}

    def request(self, task: dict) -> dict:
        tier = task.get("tier", "best-effort")
        cpu = task.get("cpu", 1)
        mem = task.get("memory", 64)
        allowed = self.policy.check(tier, cpu, mem, self.pool)
        if not allowed:
            return {"status": "denied", "reason": "policy ceiling reached"}
        ok = self.pool.allocate(cpu, mem)
        if not ok:
            return {"status": "denied", "reason": "insufficient resources"}
        rid = str(uuid.uuid4())[:8]
        self._ledger[rid] = {"task": task, "cpu": cpu, "mem": mem, "ts": time.time()}
        return {"status": "granted", "rid": rid}

    def release(self, rid: str):
        rec = self._ledger.pop(rid, None)
        if rec:
            self.pool.release(rec["cpu"], rec["mem"])

    def snapshot(self) -> dict:
        return {"active": len(self._ledger), "pool": self.pool.status()}
