# Subsystem Relationship Model

**Internal — NDA Required**

## Overview

C.I.N.S. is composed of four primary subsystems:

- Orchestration
- Safety Envelope
- Timing Model
- Resource Arbitration

These subsystems interact through deterministic pathways.

## Relationship Graph (Text-Based)

```
Orchestration → Safety Envelope → Timing Model → Arbitration → Orchestration
```

## Explanation

### Orchestration → Safety Envelope

Before routing a task, orchestration checks safety boundaries.

### Safety Envelope → Timing Model

If safe, the task is evaluated for timing feasibility.

### Timing Model → Arbitration

Timing windows inform resource allocation decisions.

### Arbitration → Orchestration

Arbitration returns the final decision to orchestration for execution.

## Notes

- All subsystems report health to the operator.
- Operator overrides bypass the loop but must be logged.
