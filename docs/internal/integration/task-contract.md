# Task Contract Schema

**Internal — NDA Required**

## Purpose

Defines the structure and requirements of a valid task entering C.I.N.S.

## Required Fields

- `task_id` — unique identifier
- `task_type` — classification for routing
- `payload` — data required to execute the task
- `priority` — integer or weighted value
- `deadline` — optional timing constraint
- `requested_capabilities` — list of required agent abilities

## Optional Fields

- `metadata` — additional context
- `operator_notes` — operator annotations
- `safety_overrides` — controlled exceptions

## Validation Rules

- Must pass safety envelope
- Must fit within timing window
- Must match at least one agent capability set
- Must not violate system-level constraints

## Lifecycle

1. Submitted
2. Validated
3. Routed
4. Executed
5. Completed or escalated
