# pm-feature-design

> Just-In-Time technical design for a single feature, written immediately before build

**Phase:** 6 - JIT Delivery  
**Agent mode:** `decision` - drafts, then requires your review before finalizing  
**Version:** 2.1.0  
**Triggers:** feature design, JIT design, design by feature, sequence diagram, feature spec, Phase 6

---

## When to use

Run once per feature, just before it enters build. Triggered by `/pm-stripe` when the feature is next in its Stripe and all dependencies are met (status: `1_Backlog` → becomes `2_Spec_Done`).

Do not run upfront for entire Feature Sets. This is JIT - one feature, right before build, not before.

---

## What it produces

Enriches three Live Registers and populates three Feature Card sections in two atomic commits:

**Commit 1** - register finalization:
- `domain/entities.md` - exact guard conditions added to state transitions for this feature
- `domain/business_rules.md` - rules this feature enforces moved from Draft → Final
- `domain/decision_models.md` - decision tables finalized

**Commit 2** - feature design:
- Feature Card Section 1 (Business Constraints) - entity IDs, BR-IDs, TBL-IDs linked
- Feature Card Section 2 (Acceptance Criteria) - derived from register state + business rules
- Feature Card Section 3 (JIT Technical Design) - Mermaid.js sequence diagram + files to modify
- Feature Card Subtasks - nuance helpers captured during discovery

Sets status to `2_Spec_Done` (or `2b_In_Design` for frontend features awaiting Figma design).

---

## How to invoke

```bash
/pm-feature-design FEAT-ORD-012       # standard run
/pm-feature-design FEAT-ORD-012 --agent   # autonomous draft, requires review after
```

---

## Dependencies

**Required before running:**
- Feature Card for this FEAT-ID (stub, created by `pm-features-list`)
- `pm-entity-registry` - `entities.md` must exist
- `pm-business-rules-library` - `business_rules.md` and `decision_models.md` must exist (at least Draft)

**Produces for:**
- Build skills (`/fullstack-guardian`, `/impeccable-craft`, etc.) - Section 3 is the build spec they read
- `pm-stripe` - Impact Analysis reads BR-IDs from Section 1
- `pm-feature-card` - populates the card sections

**Related skills:** `pm-feature-viability`, `pm-entity-registry`, `pm-business-rules-library`, `pm-decision-model`, `pm-process-flows`, `pm-feature-card`, `pm-stripe`

---

## How it works

1. **Detects mode from `state.json`** - reads `playbook` (Greenfield vs Feature Implementation) and `team_structure`, set once at Phase 1 setup, and states the detected mode rather than re-asking. Only falls back to a question if a value is genuinely missing (e.g. a hand-created workspace).
2. **Reads the Feature Card** (stub at entry - frontmatter + empty sections)
3. **Discovery Interrogation** - actively surfaces unknowns and ambiguities; calibrated to feature criticality; sorts findings into: new rules / new guard conditions / new ACs / subtasks
4. **Enriches `entities.md`** - adds exact guard conditions to state transitions relevant to this feature
5. **Enriches `business_rules.md` and `decision_models.md`** - finalizes rules this feature enforces (Draft → Final); adds brand-new rules via the single-rule helpers (`pm-business-rule-core/critical/governance`)
6. **Populates Section 1** (Business Constraints) - links entity IDs, BR-IDs, TBL-IDs; defines explicit scope exclusions
7. **Writes Section 2** (Acceptance Criteria) - minimum: AC-01 happy path, AC-02 guard failure, AC-03 feature flag OFF
8. **Writes Subtasks** - nuance/spec details for the developer (these are helpers, not sub-features)
9. **Generates Section 3** - Mermaid.js sequence diagram with real classes/methods from existing codebase; lists files to modify
10. **Pushes to Notion**, sets status to `2_Spec_Done`

**Atomic commit protocol** (registers committed before Feature Card - prevents merge conflicts in parallel Stripes):
```
Commit 1: "spec([FEAT-ID]): guard conditions + rule finalization"
Commit 2: "spec([FEAT-ID]): feature design complete"
```

**Existing codebase mode:** if the project has an existing codebase, Claude Code scans the relevant service files before generating the sequence diagram. The diagram must use only real existing classes and methods.

---

## Feature Card status after this skill

| Feature type | Path |
|---|---|
| Backend / system feature | `1_Backlog` → `2_Spec_Done` → `3_Ready_to_Build` |
| Frontend feature (Figma design needed) | `1_Backlog` → `2_Spec_Done` → `2b_In_Design` → `3_Ready_to_Build` |

---

## Key rules

- **Spec gate is hard.** Sections 1-3 must be complete before any feature enters build. No exceptions.
- **Register updates before code.** Commit 1 (registers) always precedes Commit 2 (Feature Card). This prevents merge conflicts when multiple Stripes run in parallel.
- **No invented interfaces.** In existing codebase mode, the sequence diagram uses only real classes/methods. Never fabricate a service or method that doesn't exist.
- **Flag OFF AC is mandatory.** Every feature must have AC-03 verifying the feature flag OFF behavior.

---

## Pitfalls

- Running pm-feature-design upfront for a whole Feature Set defeats the JIT principle - spec becomes stale before build.
- Skipping the Discovery Interrogation and going straight to the sequence diagram produces an incomplete spec that discovers edge cases during build instead of before it.
- Not committing register updates first creates merge conflicts when two Stripes are running simultaneously.
