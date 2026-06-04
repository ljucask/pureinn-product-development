---
name: pm-stripe
description: JIT Delivery Stripe session orchestrator. Run every time you sit down to work on Phase 6-7. Reads current state across all active stripes, detects where each feature is in the lifecycle, surfaces the right next action, and routes you to the correct skill. One stripe = one isolated development channel. Features process one at a time per stripe in dependency order.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "3.0.0"
  domain: product-management
  triggers: stripe, delivery stripe, JIT cycle, feature design, build feature, impact analysis, Phase 6, Phase 7, next feature
  role: orchestrator
  scope: delivery
  output-format: document
  related-skills: pm-feature-viability, pm-feature-design, pm-feature-card, pm-mvp-scope, pm-entity-registry
---

# PM - Delivery Stripe

## What this skill does

**Run this every time you sit down to work on Phase 6-7.** It is not a one-time setup skill - it is your session start point.

pm-stripe reads the current state of all active stripes, detects where each active feature is in the lifecycle, and tells you exactly what to do next. It routes you to the right skill at the right moment.

**Division of responsibility:**
- `features/feature_list.md` - source of truth for feature inventory, priority, stripe assignment, dependency order
- `/features/cards/FEAT-*.md` - source of truth for feature status and spec content
- **This skill** - session orchestrator: detects state, routes to right skill, tracks transitions, runs Impact Analysis

**Full feature lifecycle:**

| Status | Meaning | Who sets it |
|---|---|---|
| `1_Backlog` | In queue, design not started | pm-features-list (auto) |
| `2_Spec_Done` | JIT design complete (Sections 1-3 written), awaiting design inspection | pm-feature-design |
| `3_Ready_to_Build` | Design inspection approved, ready to enter build | pm-stripe (human confirms) |
| `4_In_Build` | Build skills actively working on this feature | pm-stripe |
| `5_In_Review` | Build complete, code review in progress | pm-stripe |
| `6_Shipped` | Complete - code reviewed, Section 4 filled, Feature Card immutable | pm-stripe |

**JIT cycle (per feature, per stripe):**
1. `1_Backlog` → run `/pm-feature-design FEAT-[ID]` → `2_Spec_Done`
2. `2_Spec_Done` → design inspection (human review of Sections 1-3) → `3_Ready_to_Build`
3. `3_Ready_to_Build` → run build skills → `4_In_Build`
4. `4_In_Build` → build complete → `5_In_Review`
5. `5_In_Review` → code review passed, Section 4 filled → `6_Shipped`

---

## Dependencies

**Required before running:**
- `pm-mvp-scope` - features must be assigned to stripes in feature_list.md and Feature Card frontmatter
- All Feature Cards must exist as stubs (status: `1_Backlog`) in `/features/cards/`

**Produces artifacts used by:**
- Feature Cards (status updates throughout lifecycle)
- `feature_list.md` (status column updated)
- Build skills (fullstack-guardian, impeccable-craft, test-master, etc.)

---

## Step 0: Session start - read state and detect context

Read `features/feature_list.md` and scan all `/features/cards/FEAT-*.md` files.

**Re-entry detection:** Before showing the dashboard, check each stripe for features NOT at `1_Backlog` or `6_Shipped`. These are mid-cycle features that need attention:

- Feature at `2_Spec_Done`: design was written but inspection hasn't happened yet
- Feature at `3_Ready_to_Build`: inspection passed but build hasn't started yet
- Feature at `4_In_Build`: build was started but hasn't been marked complete
- Feature at `5_In_Review`: build completed but code review hasn't concluded

If any mid-cycle feature is found, surface it prominently at the top of the dashboard with a clear action prompt.

**Show stripe dashboard:**

```
STRIPE DASHBOARD - [Product Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ ACTION NEEDED:
  [stripe-name] FEAT-[ID]: [title]
  Status: [current status] → [what to do next]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRIPE STATUS
| Stripe | Active feature | Status | Next in queue |
|---|---|---|---|
| stripe-checkout | FEAT-ORD-012 | 3_Ready_to_Build | FEAT-ORD-013 |
| stripe-auth | FEAT-USR-001 | 2_Spec_Done | FEAT-USR-002 |
| stripe-[name] | none | - | FEAT-XXX-001 |

BLOCKED (dependencies not met):
  FEAT-ORD-002: waiting for FEAT-ORD-001 (currently 4_In_Build)
```

Then use AskUserQuestion tool based on what's detected:

**If one clear action is obvious** (e.g., one feature at 3_Ready_to_Build):
```
What do you want to do?
  A) [Specific next action for the detected feature] (Recommended)
  B) Different stripe - choose which
  C) Impact Analysis - a business rule changed
  D) Something else
```

**If no active features or multiple stripes need attention:**
```
What do you want to do?
  A) Advance next feature - pick a stripe (Recommended)
  B) Impact Analysis - a business rule changed
  C) Close a completed stripe
  D) Check specific feature or stripe status
```

---

## Step 1A: Start JIT design (1_Backlog → 2_Spec_Done)

Feature is at `1_Backlog`, all dependencies met, no other feature in stripe is active.

**READY check before routing:**
- Status: `1_Backlog` ✓
- All dependencies: `6_Shipped` ✓
- No other feature in same stripe at `2_Spec_Done`, `3_Ready_to_Build`, `4_In_Build`, or `5_In_Review` ✓

Show:
```
Next feature in [stripe-name]:

  FEAT-[ID]: [title]
  Priority: [P1/P2/P3]
  Dependencies: all met ✓
  PRD reference: [prd_ref from frontmatter]

→ Starting JIT design. Run:
  /pm-feature-design FEAT-[ID]
```

After pm-feature-design completes: Feature Card status becomes `2_Spec_Done`.

---

## Step 1B: Design Inspection (2_Spec_Done → 3_Ready_to_Build)

Feature Sections 1-3 are written. Human reviews before build starts.

Show what to review:
```
Design Inspection - FEAT-[ID]: [title]

Review Feature Card /features/cards/FEAT-[ID].md:

  Section 1 - Biznis Mantinely
    [ ] BR-IDs referenced and correct
    [ ] Entity guard conditions specified
    [ ] Edge cases covered

  Section 2 - Acceptance Criteria
    [ ] ACs are observable (Given/When/Then format)
    [ ] Happy path covered
    [ ] Guard failures covered (what happens when AC fails)

  Section 3 - JIT Technical Design
    [ ] Sequence diagram present and logical
    [ ] All actors/services match real codebase
    [ ] Files to modify listed

  UX/UI context (if UI feature)
    [ ] Placement in app described
    [ ] Design system reference present or Figma link provided
```

Use AskUserQuestion tool:
```
Design Inspection result for FEAT-[ID]?
  A) Approved - all sections complete and correct (Recommended if reviewed)
  B) Changes needed - I'll describe what to fix
  C) Re-run pm-feature-design - significant rework needed
```

If approved: update Feature Card frontmatter `status: 3_Ready_to_Build`.

```
✅ Design inspection passed. FEAT-[ID] is ready to build.

Spec gate: PASSED
  Section 1 (Biznis Mantinely): ✓
  Section 2 (Acceptance Criteria): ✓
  Section 3 (JIT Technical Design): ✓

→ Next: start build (Step 1C)
```

---

## Step 1C: Start Build (3_Ready_to_Build → 4_In_Build)

Spec gate passed. Route to build skills.

Update Feature Card frontmatter `status: 4_In_Build`.

```
Build started for FEAT-[ID]: [title]
Status: 4_In_Build

Build instructions - read in this order:
  1. /features/cards/FEAT-[ID].md - Section 3 defines what to build
  2. /domain/entities.md - guard conditions for state transitions
  3. /domain/business_rules.md - BR-IDs referenced in Section 1
  4. /domain/decision_models.md - TBL-IDs for edge case test generation

Run build skills:
  /fullstack-guardian FEAT-[ID]    → full-stack implementation
  /impeccable-craft FEAT-[ID]      → frontend UI (if UI feature)
  /test-master FEAT-[ID]           → unit + integration tests
  /playwright-expert FEAT-[ID]     → E2E tests

When build is complete, run /pm-stripe and mark build done.
```

---

## Step 1D: Mark Build Complete (4_In_Build → 5_In_Review)

Build skills finished. Moving to code review phase.

Update Feature Card frontmatter `status: 5_In_Review`.

```
Build complete for FEAT-[ID]: [title]
Status: 5_In_Review

Code review:
  /code-reviewer FEAT-[ID]     → code correctness review
  /impeccable-audit FEAT-[ID]  → code quality review
  /security-reviewer FEAT-[ID] → security check (if applicable)

When code review passes, run /pm-stripe and mark review complete.
```

---

## Step 1E: Ship Feature (5_In_Review → 6_Shipped)

Code review passed. Fill Section 4 and ship.

```
Marking FEAT-[ID] as shipped.

Please provide (or confirm already recorded):
  1. Commit hash(es) for this feature
  2. Test file paths (unit / integration / E2E)
  3. Feature flag OFF verification (if applicable)
  4. Code Inspection result and reviewer name/date
```

Fill Feature Card Section 4 (Realizacny Protokol) with the above.

Update Feature Card frontmatter `status: 6_Shipped`.
Update `features/feature_list.md` - Status column for this feature.

```
✅ FEAT-[ID]: [title] → SHIPPED

Feature Card is now immutable history.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Next in [stripe-name]:
  FEAT-[NEXT-ID]: [title]
  Dependencies: [all met ✓ / waiting for FEAT-XXX]

→ Ready to start. Run /pm-stripe to advance.
```

---

## Step 1F: Impact Analysis

Triggered when a business rule changes in `business_rules.md`.

**User provides:** Which rule changed (BR-ID) and what changed.

**Analysis steps:**

1. Scan all `/features/cards/FEAT-*.md` files for references to the changed BR-ID in Section 1 (Biznis Mantinely)
2. Group affected features by status:

```
Impact Analysis: BR-[DOMAIN]-[NUMBER] changed

Affected features:
  Status 6_Shipped (code must be updated):
    - FEAT-ORD-012: [title] → files: [list from Section 4]
    - FEAT-ORD-015: [title] → files: [list from Section 4]

  Status 2_Spec_Done, 3_Ready_to_Build, 4_In_Build, or 5_In_Review (re-design needed):
    - FEAT-PAY-002: [title] → re-run /pm-feature-design FEAT-PAY-002

  Status 1_Backlog (no action - JIT design will use updated rule when reached):
    - FEAT-ORD-020: [title]

Not affected: [N] features (no BR-[ID] reference in Section 1)
```

3. For Shipped features: list exact files from Section 4 that need code update
4. For in-progress features: reset to `1_Backlog`, re-run pm-feature-design
5. Update `business_rules.md`: add entry to Changelog section

---

## Step 1G: Close Stripe

All features in the stripe are at `6_Shipped`.

```
Closing [stripe-name]:

  Features shipped: [N]
  Last feature: FEAT-[ID] - [title]

Verification:
  [ ] All Feature Cards in stripe at 6_Shipped
  [ ] feature_list.md Status column up to date
  [ ] No features blocked waiting for this stripe

Stripe [stripe-name] → CLOSED ✅

Remaining active stripes: [list]
```

Update `state.json`: remove closed stripe from `current_stripes`.

---

## Atomic commit protocol (parallel stripe safety)

When multiple stripes run in parallel, register updates can cause merge conflicts.

**Rule enforced by pm-feature-design (reinforced here):**
- Register updates (entities.md, business_rules.md, decision_models.md) are committed BEFORE any code
- Each feature gets exactly 2 atomic commits during design phase:
  1. `spec([FEAT-ID]): guard conditions + rule finalization` - registers only
  2. `spec([FEAT-ID]): feature design complete` - Feature Card Sections 1-3 only

**Stripe domain alignment guidance:**
- Stripes should cover coherent domain slices (stripe-checkout: Order + Payment, stripe-auth: User)
- Features from different domains in different stripes will not conflict on registers
- Cross-domain features (rare): coordinate manually - one stripe processes at a time

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user -->

**Per-feature routing:**
- [ ] READY check: status 1_Backlog + all dependencies 6_Shipped + no active feature in same stripe
- [ ] One feature per stripe in active design/build at any time (no parallel features in same stripe)
- [ ] Spec gate verified before 3_Ready_to_Build → 4_In_Build transition (Sections 1-3 present)
- [ ] Build skills receive Feature Card FEAT-ID as context parameter
- [ ] Section 4 complete before 6_Shipped is set

**Status transitions:**
- [ ] Feature Card frontmatter `status:` updated at every transition
- [ ] `feature_list.md` Status column kept in sync at every transition
- [ ] Re-entry: mid-cycle features (2-5) detected and surfaced on dashboard

**Impact Analysis:**
- [ ] All Feature Cards scanned, not just active ones
- [ ] Shipped features: exact files identified from Section 4
- [ ] In-progress features: reset to 1_Backlog, re-routed to pm-feature-design
- [ ] business_rules.md Changelog updated

**Stripe closure:**
- [ ] All features at 6_Shipped before closing
- [ ] state.json current_stripes updated

---

## State updates

Feature status in Feature Card frontmatter:
```
1_Backlog → 2_Spec_Done → 3_Ready_to_Build → 4_In_Build → 5_In_Review → 6_Shipped
```

State update → `pureinn-workspace/[project-slug]/state.json`:
- `current_stripes`: list of active stripe names (remove on closure)
- Per stripe: `active_feature`, `queue` (ordered FEAT-ID list)
