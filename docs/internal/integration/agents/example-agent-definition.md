# Example Agent Definition (Public-Safe)

**Internal — NDA Required**

```yaml
agent_id: "example_agent_01"
version: 1.0
description: "A demonstration agent used for illustrating C.I.N.S. integration."

capabilities:
  - capability_name: "analyze_payload"
    version: 1.0
    performance_rating: medium
    constraints:
      - max_payload_size: 1MB
    resource_cost: low
    timing_profile:
      window: soft
      expected_latency_ms: 150

health_profile:
  heartbeat_interval_ms: 1000
  load_reporting: enabled
  failure_modes:
    soft_failure_behavior: "retry"
    hard_failure_behavior: "escalate"

constraints:
  resource_limits:
    cpu: "low"
    memory: "low"
```
