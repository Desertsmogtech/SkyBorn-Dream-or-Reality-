"""
CINS.modules.resource_arbitration.arbitrator
--------------------------------------------
Coordinates resource requests from the Orchestrator.

Flow
----
1. Policy check  -> tier ceiling respected?
2. Pool check    -> physical capacity available?
3. Grant / Deny  -> return structured response dict.
4. Release       -> caller returns resources by rid.
"""

import uuid
import time


class ResourceArbitrator:
    """
    Top-level resource broker for CINS task submissions.

    Parameters
    ----------
    pool   : ResourcePool
    policy : AllocationPolicy
    """

    def __init__(self, pool, policy):
        self._pool   = pool
        self._policy = policy
        self._active: dict = {}

    def request(self, task: dict) -> dict:
        """
        Attempt to grant resources for task.
        Returns dict with status 'granted' or 'denied'.
        """
        tier = task.get("tier", "best-effort")
        cpu  = int(task.get("cpu", 0))
        mem  = int(task.get("mem", 0))

        if not self._policy.check(tier, cpu, mem, self._pool):
            return {"status": "denied", "reason": "policy_ceiling", "rid": None}

        if not self._pool.allocate(cpu=cpu, mem=mem):
            return {"status": "denied", "reason": "insufficient_capacity", "rid": None}

        rid = str(uuid.uuid4())
        self._active[rid] = {"cpu": cpu, "mem": mem, "tier": tier, "ts": time.time()}

        return {
            "status": "granted",
            "rid":    rid,
            "cpu":    cpu,
            "mem":    mem,
            "ts":     self._active[rid]["ts"],
        }

    def release(self, rid: str) -> None:
        """Return allocated resources to the pool. Silently ignores unknown rids."""
        entry = self._active.pop(rid, None)
        if entry:
            self._pool.release(cpu=entry["cpu"], mem=entry["mem"])

    def snapshot(self) -> dict:
        """Returns active allocation count and pool status."""
        return {
            "active": len(self._active),
            "pool":   self._pool.status(),
        }
