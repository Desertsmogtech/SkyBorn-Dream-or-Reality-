# Security & Separation Rules

## SkyBorn-Dream-or-Reality

This repository uses a strict three-tier separation model.

---

## 1. Public-Safe Layer

**Location:**
- `/docs/public/*`
- `/README.md`
- Non-sensitive examples

**Allowed:**
- High-level descriptions
- Conceptual overviews
- Public-facing documentation

**Restricted:**
- No internal logic
- No timing models
- No arbitration rules
- No operator-only content

---

## 2. NDA-Only Layer

**Location:**
- `/docs/internal/*`
- `/CINS/modules/*`
- Architecture specifications
- Timing & latency models
- Safety envelope definitions

**Access:**
- Requires explicit permission
- Must not be shared publicly
- Must not be referenced in public issues or PRs

---

## 3. Never-Disclosed Layer

**Location:**
- `/internal/*`
- `/operator-notes/*`
- Any file tagged operator-only

**Rules:**
- Never committed
- Never uploaded
- Never shared
- Never passed to AI systems

This layer contains operator identity, lineage, rituals, glyphs, and personal annotations.

---

## Enforcement

- CODEOWNERS restricts access
- .gitignore blocks never-disclosed content
- Branch protection required for internal paths
