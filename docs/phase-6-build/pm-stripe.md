# pm-stripe

> JIT Delivery Stripe session orchestrator - run every time you sit down to work on Phase 6-7

**Phase:** 6-7 - JIT Delivery (session start point)  
**Agent mode:** `never` - value is the live interactive session  
**Version:** 3.0.0  
**Triggers:** stripe, delivery stripe, JIT cycle, build feature, impact analysis, Phase 6, next feature

---

## When to use

**Run this every time you sit down to work on Phase 6-7.** It is not a one-time setup skill - it is your session start point. It reads current state, tells you exactly what to do next, and routes you to the right skill.

---

## What it does

Reads `features/feature_list.md` and all `features/cards/FEAT-*.md` files, then:

1. **Syncs status from Notion** (if Feature Backlog URL is configured) - Notion wins on status, markdown wins on content
2. **Detects mid-cycle features** (anything not at `1_Backlog` or `6_Shipped`) and surfaces them with a clear action prompt
3. **Shows the Stripe Dashboard** - active feature per stripe, status, next in queue, blocked features
4. **Routes you** to the right next action via AskUserQuestion

**Division of responsibility:**
- `feature_list.md` - source of truth for inventory, priority, stripe assignment, dependency order
- `features/cards/FEAT-*.md` - source of truth for feature status and spec content
- `pm-stripe` - session orchestrator: detects state, routes, tracks transitions, runs Impact Analysis

---

## How to invoke

```bash
/pm-stripe    # always the same - reads current state and routes
```

---

## Session flow

```
Session start → pm-stripe
  │
  ├─ 1_Backlog, deps met → /pm-feature-design [FEAT-ID]       → 2_Spec_Done
  ├─ 2_Spec_Done         → Design Inspection (human review)    → 3_Ready_to_Build
  ├─ 2b_In_Design        → Figma design complete?              → 3_Ready_to_Build
  ├─ 3_Ready_to_Build    → build skills                        → 4_In_Build
  ├─ 4_In_Build          → build complete                      → 5_In_Review
  ├─ 5_In_Review         → code review + Section 4             → 6_Shipped
  └─ all 6_Shipped       → Close Stripe
```

---

## Design Inspection (2_Spec_Done → 3_Ready_to_Build)

pm-stripe presents a checklist for human review of Sections 1-3:

**Section 1 - Business Constraints:**
- BR-IDs referenced and correct
- Entity guard conditions specified
- Edge cases covered

**Section 2 - Acceptance Criteria:**
- ACs are observable (Given/When/Then)
- Happy path covered
- Guard failures covered

**Section 3 - JIT Technical Design:**
- Sequence diagram present and logical
- All actors/services match real codebase
- Files to modify listed

Approval transitions the feature to `3_Ready_to_Build`.

---

## Impact Analysis

Triggered when a business rule in `business_rules.md` changes. Provide the changed BR-ID and what changed - pm-stripe scans all Feature Cards and groups affected features by status:

| Feature status | Action |
|---|---|
| `6_Shipped` | Code must be updated - pm-stripe lists exact files from Section 4 |
| `2_Spec_Done` / `3_Ready_to_Build` / `4_In_Build` / `5_In_Review` | Reset to `1_Backlog`, re-run `pm-feature-design` |
| `1_Backlog` | No action - JIT design will use the updated rule when reached |

---

## Atomic commit protocol

When multiple Stripes run in parallel, register updates (entities.md, business_rules.md, decision_models.md) must be committed before any code to prevent merge conflicts. pm-stripe reinforces the rule established by `pm-feature-design`.

**Stripe domain alignment:** stripes should cover coherent domain slices (e.g. stripe-checkout: Order + Payment, stripe-auth: User). Features from different domains in different stripes won't conflict on registers. Cross-domain features: coordinate manually, one stripe processes at a time.

---

## Dependencies

**Required before running:**
- `pm-mvp-scope` - features must be assigned to stripes
- All Feature Cards exist as stubs (status: `1_Backlog`)

**Related skills:** `pm-feature-viability`, `pm-feature-design`, `pm-feature-card`, `pm-mvp-scope`, `pm-entity-registry`
