# Routing Example (Public-Safe)

## Scenario

A task is submitted with:
- `task_type`: "analysis"
- `priority`: 3
- `requested_capabilities`: ["analyze_payload"]

## Flow

1. Task enters orchestration.
2. Safety envelope validates the task.
3. Timing model assigns a soft window.
4. Arbitration selects an agent with matching capability.
5. Orchestration routes the task.
