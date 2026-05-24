# Agent Health Profile Template

**Internal — NDA Required**

## Health Signals

- `heartbeat_timestamp` — last checkin
- `load_percentage` — current utilization
- `error_state` — error status
- `drift_detected` — true/false

## Failure Modes

### Soft Failure

- `retry_count` — retry attempts
- `fallback_agent` — backup agent
- `escalation_threshold` — escalation trigger

### Hard Failure

- `immediate_shutdown` — true/false
- `operator_notification` — required/optional
