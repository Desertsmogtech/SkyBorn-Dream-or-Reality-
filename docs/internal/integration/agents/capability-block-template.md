# Capability Block Template

**Internal — NDA Required**

```yaml
capability_name: <string>
version: <float>
performance_rating: low | medium | high
constraints:
  - <constraint_key>: <value>
resource_cost: low | medium | high
timing_profile:
  window: hard | soft
  expected_latency_ms: <int>
```
