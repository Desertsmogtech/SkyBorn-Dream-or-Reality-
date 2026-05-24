# Agent Capability Template

**Internal — NDA Required**

## Purpose

Defines how agents describe their abilities to C.I.N.S.

## Capability Block

- `capability_name` — name of the capability
- `version` — capability version
- `performance_rating` — quality metric (high/medium/low)
- `constraints` — operational limits
- `resource_cost` — resource intensity
- `timing_profile` — timing characteristics

## Example

```
capability_name: "analyze_payload"
version: 1.0
performance_rating: high
constraints:
  max_payload_size: 2MB
  forbidden_types: ["unsafe", "unbounded"]
resource_cost: medium
timing_profile:
  window: soft
  expected_latency_ms: 120
```
