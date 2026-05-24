# Timing Window Example (Public-Safe)

## Scenario

A task requires completion within 500ms.

## Flow

- Timing model assigns a hard window.
- Drift detector monitors execution.
- If drift exceeds threshold, arbitration is triggered.
