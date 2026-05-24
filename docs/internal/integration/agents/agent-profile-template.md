# Agent Profile Template

**Internal — NDA Required**

## Agent Identity

- `agent_id` — unique identifier
- `version` — agent version
- `description` — agent purpose

## Capabilities

List of capability blocks (see capability template).

## Health Profile

- `heartbeat_interval_ms` — health check frequency
- `load_reporting` — enabled/disabled
- `failure_modes`:
  - `soft_failure_behavior` — retry/fallback/escalate
  - `hard_failure_behavior` — shutdown/escalate

## Constraints

- `resource_limits` — CPU, memory, etc.
- `forbidden_operations` — blocked actions
- `timing_constraints` — deadline requirements

## Metadata

- `author` — creator
- `creation_date` — timestamp
- `notes` — additional context
