# GitHub Copilot Usage Boundaries

## Allowed with Copilot

- Public documentation
- High-level scaffolding
- Non-sensitive code
- Public-safe examples

## Use With Caution

- `docs/internal/*`
- C.I.N.S. module stubs
- Architecture descriptions

Only reference these when comfortable with abstraction.

## Never Send to Copilot

- `/internal/*`
- `/operator-notes/*`
- Operator identity
- Lineage, rituals, glyphs
- Timing budgets
- Arbitration logic
- Safety envelope thresholds

If it would compromise the operator or system integrity, it must not be shared.
