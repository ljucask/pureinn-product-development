---
name: pm-stripe
description: JIT Delivery Stripe orchestrator. Manages the active development cycle in the FDD+SDD framework. Picks the next ready feature per stripe, routes to pm-feature-design (JIT spec) and build skills, tracks feature status in Feature Card frontmatter, runs Impact Analysis when business rules change. One stripe = one isolated development channel. Features are processed one at a time per stripe, in dependency order.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "2.0.0"
  domain: product-management
  triggers: stripe, delivery stripe, JIT cycle, feature design, build feature, impact analysis, Phase 6, Phase 7
  role: orchestrator
  scope: delivery
  output-format: document
  related-skills: pm-feature-design, pm-feature-card, pm-mvp-scope, pm-entity-registry
---

# PM - Delivery Stripe

## What this skill does

Orchestrates the JIT delivery cycle across all active Delivery Stripes.

**Division of responsibility:**
- `features/feature_list.md` - source of truth for feature inventory, priority, stripe assignment, dependency order
- `/features/cards/FEAT-*.md` - source of truth for feature status and spec content
- **This skill** - picks next ready feature per stripe, routes to the right skill, tracks status, runs Impact Analysis when registers change

**JIT cycle (per feature, per stripe):**
1. Feature selected (next in stripe, dependencies met, status: 1_Walkthrough)
2. Route to `/pm-feature-design` → populates Feature Card Sections 1-3, status: 2_Design
3. Design Inspection (human confirm or team review) → status: 3_Design_Inspection_Passed
4. Route to build skills → code + tests produced, Section 4 filled, status: 6_Promoted_to_Build
5. Feature Card becomes immutable history → next feature selected

**Impact Analysis** - runs when a business rule changes in `business_rules.md`:
- Scans all Feature Cards for references to the changed BR-ID in Section 1
- Identifies affected features by status (Promoted vs. in-progress)
- Routes to re-design or code update as appropriate

---

## Dependencies

**Required before running:**
- `pm-mvp-scope` - features must be assigned to stripes in feature_list.md and Feature Card frontmatter
- All Feature Cards must exist as stubs (status: 1_Walkthrough) in `/features/cards/`

**Produces artifacts used by:**
- Feature Cards (status updates throughout lifecycle)
- `feature_list.md` (status column updated)
- Build skills (fullstack-guardian, impeccable-craft, test-master, etc.)

---

## Step 0: Current state check

Read `features/feature_list.md` and scan `/features/cards/` directory.

Show stripe dashboard:

```
STRIPE DASHBOARD - [Product Name]

| Stripe | Active feature | Status | Queue (next 3) |
|---|---|---|---|
| stripe-checkout | FEAT-ORD-012 | 3_Design_Inspection_Passed | FEAT-ORD-013, FEAT-PAY-002 |
| stripe-auth | FEAT-USR-001 | 2_Design | FEAT-USR-002 |
| stripe-[name] | none | ready for first feature | FEAT-XXX-001, FEAT-XXX-002 |

Blocked features (dependencies not met):
  - FEAT-ORD-002: waiting for FEAT-ORD-001 (stripe-checkout, in build)
```

Use AskUserQuestion tool for this question:

```
What do you want to do?
  A) Advance next feature in a stripe - select stripe
  B) Run Impact Analysis - a business rule changed
  C) Check specific feature status
  D) Close a stripe - all features Promoted
```

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1A: Advance next feature in a stripe

**Selecting the next feature:**

A feature is READY when:
- Status: `1_Walkthrough`
- All dependencies have status: `6_Promoted_to_Build`
- No other feature in the same stripe is currently at status `2_Design` or `3_Design_Inspection_Passed` or `4_Build` (one at a time per stripe - prevents register conflicts)

Show:

```
Next feature in [stripe-name]:

  FEAT-[ID]: [title]
  Priority: [P1/P2/P3]
  Dependencies: [all met / list unmet]
  PRD reference: [prd_ref from frontmatter]

What to do:
  A) Start JIT design → run /pm-feature-design FEAT-[ID]
  B) Skip this feature (move to back of queue)
  C) Check a different stripe
```

---

## Step 1B: Mark Design Inspection passed

When user confirms design is approved after reviewing Feature Card Sections 1-3:

```
Design confirmed for FEAT-[ID]: [title]

Updating Feature Card status: 2_Design → 3_Design_Inspection_Passed
```

Update Feature Card frontmatter `status: 3_Design_Inspection_Passed`.

Then route to build:

```
Spec gate: PASSED
  Section 1 (Biznis Mantinely): populated
  Section 2 (Acceptance Criteria): populated
  Section 3 (JIT Technical Design): sequence diagram present

→ Ready for build.

Run: /fullstack-guardian FEAT-[ID]
     or /impeccable-craft FEAT-[ID] (frontend only)

Build instructions:
  Read /features/cards/FEAT-[ID].md - Section 3 defines what to build
  Read /domain/entities.md - guard conditions for state transitions
  Read /domain/business_rules.md - BR-IDs referenced in Section 1
  Read /domain/decision_models.md - TBL-IDs for edge case test generation
```

---

## Step 1C: Mark feature Promoted

When build is complete and Code Inspection passed:

1. Update Feature Card Section 4 (Realizacny Protokol):
   - Add commit links
   - Add test file paths
   - Add flag OFF verification
   - Add Code Inspection result + date

2. Update frontmatter: `status: 6_Promoted_to_Build`

3. Update `features/feature_list.md` - Status column for this feature

4. Announce:

```
FEAT-[ID]: [title] → PROMOTED TO BUILD

Feature Card is now immutable history.
Next feature in [stripe-name]: FEAT-[NEXT-ID]: [title]
  → Check dependencies: [met / waiting for FEAT-XXX]
```

---

## Step 1D: Impact Analysis

Triggered when a business rule changes in `business_rules.md`.

**User provides:** Which rule changed (BR-ID) and what changed.

**Analysis steps:**

1. Scan all `/features/cards/FEAT-*.md` files for references to the changed BR-ID in Section 1 (Biznis Mantinely)
2. Group affected features by status:

```
Impact Analysis: BR-[DOMAIN]-[NUMBER] changed

Affected features:
  Status 6_Promoted_to_Build (code must be updated):
    - FEAT-ORD-012: [title] → Section 4 has commit hash [hash] → files: [list from Section 4]
    - FEAT-ORD-015: [title] → Section 4 has commit hash [hash] → files: [list from Section 4]

  Status 2_Design or 3_Design_Inspection_Passed (re-design needed):
    - FEAT-PAY-002: [title] → re-run /pm-feature-design FEAT-PAY-002

  Status 1_Walkthrough (not yet designed - no action needed, JIT will pick up updated rule):
    - FEAT-ORD-020: [title] → will use updated rule when designed

Not affected: [N] features in other stripes (no BR-[ID] reference in Section 1)
```

3. For Promoted features: list exact files from Section 4 that need code update
4. For in-design features: re-run pm-feature-design to regenerate Section 1-3 with updated rule
5. Update business_rules.md: add this change to Changelog section

---

## Atomic commit protocol (parallel stripe safety)

When multiple stripes run in parallel, register updates can cause merge conflicts.

**Rule enforced by pm-feature-design (reinforced here):**
- Register updates (entities.md, business_rules.md, decision_models.md) are committed BEFORE any code generation
- Each feature gets exactly 2 atomic commits during design phase:
  1. `spec([FEAT-ID]): guard conditions + rule finalization` - registers only
  2. `spec([FEAT-ID]): feature design complete` - Feature Card Sections 1-3 only

**Stripe domain alignment guidance:**
- Stripes should cover coherent domain slices (stripe-checkout: Order + Payment, stripe-auth: User)
- Features in different stripes from different domains will not touch the same register sections
- Cross-domain features (rare): coordinate with human - one stripe processes at a time

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user -->

**Per-feature routing:**
- [ ] Feature selected is READY (status 1_Walkthrough, all deps Promoted)
- [ ] Only one feature per stripe in active design/build at any time
- [ ] Spec gate checked before routing to build (Sections 1-3 populated, status 3_Design_Inspection_Passed)
- [ ] Build skills receive Feature Card path as primary input

**Impact Analysis:**
- [ ] All Feature Cards scanned (not just active ones)
- [ ] Promoted features: exact files identified from Section 4
- [ ] In-design features: re-routed to pm-feature-design
- [ ] Walkthrough features: noted as no action needed
- [ ] business_rules.md Changelog updated

**Feature Card lifecycle:**
- [ ] Status updated at every transition
- [ ] feature_list.md Status column kept in sync
- [ ] Section 4 complete before 6_Promoted_to_Build is set
- [ ] After Promoted: no further edits to Feature Card

---

## State updates

Feature status in Feature Card frontmatter:
```
1_Walkthrough → 2_Design → 3_Design_Inspection_Passed → 4_Build → 5_Code_Inspection → 6_Promoted_to_Build
```

State update → `pureinn-workspace/[project-slug]/state.json`:
- `current_stripes`: list of active stripe names
- Per stripe: `active_feature`, `queue` (ordered list of FEAT-IDs)
