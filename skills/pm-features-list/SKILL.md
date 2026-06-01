---
name: pm-features-list
description: Generate the complete Features List in FDD format, organized into the 3-level hierarchy (Subject Area > Feature Set > Feature). Runs Dependency Map, KANO Analysis, and Value vs. Complexity Matrix. Creates stub Feature Cards in /features/cards/ for each feature. After user approval, pushes features to Notion as the initial backlog. Output is the prioritized, dependency-mapped feature inventory and Live Register 4 ready for MVP scoping in pm-mvp-scope.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "2.0.0"
  domain: product-management
  triggers: features list, FDD format, feature list, KANO analysis, value complexity matrix, feature prioritization, Phase 5, feature hierarchy
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-mvp-scope, pm-entity-registry, pm-business-rules-library, pm-prd, pm-product-roadmap
---

# PM - Features List

## What this skill does

Phase 5 / Step 1-3. Takes the product scope from PRD Business Capabilities and produces:

1. **FDD Feature List** (`features/feature_list.md`) - Live Register 4. All features in FDD format (`[Action] [Result] [Object]`), organized in 3-level hierarchy: Subject Area -> Feature Set -> Feature. With actor, priority, dependencies, MVP flag, and stripe assignment.
2. **Dependency Map** - which features block which, critical path, parallelizable tracks
3. **KANO Analysis** - must-be / performance / delighter / indifferent classification per feature
4. **Value vs. Complexity Matrix** - Quick Win / Big Bet / Fill-in / Time Waster scoring per feature
5. **Stub Feature Cards** - one per feature, created automatically in `/features/cards/FEAT-[DOMAIN]-[NUMBER].md` with status `1_Walkthrough`

After user approval: push the complete feature inventory to Notion as the initial product backlog.

This is the direct input for `pm-mvp-scope`, which makes the MVP cut per feature and assigns features to Delivery Stripes.

---

## Dependencies

**Required before running:**
- `pm-prd` - PRD Business Capabilities section is the primary input for feature extraction
- `pm-entity-registry` - entities.md informs what operations are needed per domain

**Recommended before running:**
- `pm-personas` - user roles drive which features belong to which actor
- `pm-problem-validation` - validated pains confirm which features address real needs
- `pm-business-rules-library` - known compliance rules may constrain feature scope

**Produces artifacts used by:**
- `features/feature_list.md` - Live Register 4 of 4 (FDD Feature List)
- `/features/cards/FEAT-*.md` - stub Feature Cards (one per feature, status: 1_Walkthrough)
- `pm-mvp-scope` - feature list is the direct input for MVP cut + stripe assignment
- `pm-product-roadmap` v3 - features populate the delivery view
- Phase 6 skills - pm-feature-design reads Feature Cards JIT before each feature enters build

---

## Step 0: Current state check + mode detection

Check for existing artifacts:
- `features/feature_list.md` (Live Register 4)
- Dependency Map
- KANO Analysis
- Value vs. Complexity Matrix
- Stub Feature Cards in `features/cards/`

**Mode detection:**

| Condition | Mode | Behavior |
|---|---|---|
| `feature_list.md` does NOT exist | Create mode | Generate full feature list from PRD_master Business Capabilities |
| `feature_list.md` EXISTS + `initiatives/[slug]/` exists | FI Append mode | Add new initiative features, preserve existing list |
| `feature_list.md` EXISTS, no initiatives | Update mode | Refresh or extend the existing list (use Step 1 option C) |

**If FI Append mode detected**, inform user:

```
feature_list.md already exists with [N] features from the original product scope.

This session will APPEND new features for a new initiative.
Existing FEAT-* IDs will not be modified or renumbered.

Which initiative and domain code?
  Initiative: [e.g., ai-onboarding]
  Domain code: [e.g., ONB] → new features will be FEAT-ONB-001, FEAT-ONB-002, ...

Input source:
  A) Initiative PRD at initiatives/[slug]/prd.md (recommended)
  B) Paste Business Capabilities directly
```

Also check: does entities.md include the new domain entities? Without domain entities for the new initiative, feature-entity alignment will be guesswork.

Look for: features named as capabilities rather than actions, features too large for a single delivery cycle (split needed), missing user role attribution, duplicates, KANO classification without rationale. Subject Areas and Feature Sets are GROUPING ONLY.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

First, ask this scoping question:

What is the goal for this session?

  A) Full extraction - map all features across the entire product scope, prioritize with KANO + V×C (Recommended for first run)
  B) Focused area - extract and prioritize features for one specific functional area only
  C) Refresh - update an existing list with new features or re-run prioritization
  D) Quick scan - extract a rough feature list without full KANO + V×C scoring

Then ask the remaining inputs as plain text:

```
I need inputs for the FDD Feature List (Live Register 4), Dependency Map, and KANO + V×C prioritization.

1. PRD BUSINESS CAPABILITIES
   Paste the Business Capabilities section from the PRD, or confirm it is in context.
   I will extract features from these capabilities using FDD grammar [Action] [Result] [Object].
   [paste or "in context"]

2. USER ROLES
   Who are the actors in the system? (e.g., Host, Guest, Admin, Property Manager)
   Which role is primary (most features serve them)?

3. ENTITY REGISTRY REFERENCE
   Is entities.md in context? (informs what operations are needed per domain entity)
   [confirm or "not yet"]

4. FEATURE IDEAS
   Do you have any feature ideas already written down?
   (Paste any list, notes - NO User Stories please, just capabilities or action descriptions)
   [paste or "nothing yet - extract from PRD only"]

5. KNOWN DEPENDENCIES
   Are there features you know depend on each other?
   (e.g., "payment must come before booking confirmation", "listing must exist before search")
   [describe or "none known yet"]

6. NOTION SETUP
   Read pureinn-variables.md, key "Feature Backlog". Skip this question if URL is present.
   If blank: do you have a Notion Product Features database to push features to after approval?
   [yes - paste URL / no - skip]
```

---

## Step 2: Generate FDD Feature List (Live Register 4)

Before generating:
1. Read PRD Business Capabilities - extract all nouns as potential Subject Areas and Feature Sets
2. Decompose each capability into FDD features: `[Action] [Result] [Object]`
3. Organize into 3-level hierarchy: Subject Area -> Feature Set -> Feature
4. Assign each feature: unique ID (FEAT-[DOMAIN]-[NUMBER], e.g., FEAT-ORD-001), user role, rough complexity
5. Flag features that are likely too large for 14 days (mark for atomic split)
6. Subject Areas and Feature Sets are GROUPING ONLY - no execution logic at those levels

**ID format:** `FEAT-[DOMAIN]-[NUMBER]`
Domain codes match business_rules.md: ORD (order), PAY (payment), USR (user/auth), INV (inventory), etc.

Generate in English.

---

### ARTIFACT 1: FDD Feature List (Live Register 4)

Save to: `pureinn-workspace/[project-slug]/features/feature_list.md`

```markdown
# FDD Feature List
# Live Register 4 of 4 - FDD+SDD Framework

> **Product:** [Product Name]
> **Version:** 1.0
> **Last updated:** [date]
> **Based on:** PRD Business Capabilities v[X], entities.md v[X]

---

> **How to read this register:**
> - Subject Areas and Feature Sets are grouping only - no execution logic
> - All prioritization, dependencies, MVP cut, and stripe assignment is per Feature
> - Status reflects Feature Card status (updated by pm-stripe during JIT cycle)

---

## Feature Naming Convention

Every feature follows: **`[Action] [Result] [Object]`**

- Action: what happens (Submit, Calculate, Validate, Generate, Send, Approve, Cancel...)
- Result: the outcome or state change (order confirmation, payment status, availability...)
- Object: the entity being acted on (card, order, booking, invoice, user account...)

Features must be:
- Independently implementable and testable
- Deliverable in 14 days or less (if larger: split atomically)
- Expressed from the business/user value perspective (not technical implementation)
- NO User Stories format ("As a user I want...") - FDD grammar only

---

## [Subject Area 1: e.g., Order Management]

### Feature Set: [e.g., Order Processing]

| ID | Feature | Actor | Priority | MVP | Stripe | Status | Dependencies |
|---|---|---|---|---|---|---|---|
| FEAT-ORD-001 | [Create] [draft order] [from cart] | [Customer] | P1 | true | TBD | 1_Walkthrough | none |
| FEAT-ORD-002 | [Confirm] [order] [after payment] | [System] | P1 | true | TBD | 1_Walkthrough | FEAT-ORD-001, FEAT-PAY-001 |
| FEAT-ORD-003 | [Cancel] [order] [before fulfillment] | [Customer] | P2 | true | TBD | 1_Walkthrough | FEAT-ORD-001 |

### Feature Set: [e.g., Order Fulfillment]

| ID | Feature | Actor | Priority | MVP | Stripe | Status | Dependencies |
|---|---|---|---|---|---|---|---|
| FEAT-ORD-010 | [Track] [fulfillment status] [for order] | [Customer] | P2 | true | TBD | 1_Walkthrough | FEAT-ORD-002 |

---

## [Subject Area 2: e.g., Payments]

### Feature Set: [e.g., Card Payments]

| ID | Feature | Actor | Priority | MVP | Stripe | Status | Dependencies |
|---|---|---|---|---|---|---|---|
| FEAT-PAY-001 | [Validate] [card payment] [for order] | [System] | P1 | true | TBD | 1_Walkthrough | FEAT-ORD-001 |
| FEAT-PAY-002 | [Process] [refund] [for cancelled order] | [System] | P1 | true | TBD | 1_Walkthrough | FEAT-ORD-003 |

---

## Features Flagged for Splitting

| Feature ID | Reason | Suggested split |
|---|---|---|
| [FEAT-XXX-001] | Too broad - each part separately deliverable | [FEAT-XXX-001a: ..., FEAT-XXX-001b: ...] |

---

## Feature Count Summary

| Subject Area | Feature Sets | Features |
|---|---|---|
| [Area 1] | [X] | [X] |
| **Total** | **[X]** | **[X]** |

---

## Features Not in Scope (from PRD)

| Capability | Reason excluded | Reconsider when |
|---|---|---|
| [e.g., Native mobile app] | Web-first MVP | After PMF proven on web |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | [date] | Initial extraction from PRD Business Capabilities |
```

---

## Step 3: Generate Dependency Map

After Features List is approved, run dependency analysis.

---

### ARTIFACT 2: Dependency Map

```markdown
# Feature Dependency Map - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]

---

## Dependency Rules

A feature is **blocked** if another feature must be complete before it can be built or tested.
A feature is a **blocker** if other features depend on it.

---

## Dependency Matrix

| Feature | Depends on | Blocks | Dependency type |
|---|---|---|---|
| [F-011: Submit booking request] | [F-001: Create property listing] | [F-012: Approve booking request] | Hard - cannot test without it |
| [F-015: Process booking payment] | [F-011, F-012] | [F-016: Issue refund] | Hard - payment depends on confirmed booking |
| [F-020: Send booking confirmation] | [F-012, F-015] | None | Soft - can stub notification for testing |

---

## Critical Path

The longest sequence of hard dependencies that determines minimum delivery timeline.

```
[F-001] Create listing
  → [F-011] Submit booking request
    → [F-012] Approve booking request
      → [F-015] Process payment
        → [F-020] Send confirmation
```

**Critical path length:** [X features - estimated [Y] weeks]

---

## Parallelizable Tracks

| Track | Features | No dependency on |
|---|---|---|
| [Track A: Property management] | [F-001, F-002, F-003] | Track B, C |
| [Track B: Search] | [F-010] | Track A (partial) |
| [Track C: Messaging] | [F-030, F-031] | Track A + B complete |
```

---

## Step 4: Generate KANO + Value vs. Complexity

After Dependency Map is approved.

---

### ARTIFACT 3: KANO Analysis

```markdown
# KANO Analysis - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]

---

## KANO Categories

| Category | Definition | MVP implication |
|---|---|---|
| Must-be | Expected by default. Absence = dissatisfied. Presence is neutral. | Always in MVP |
| Performance | More = better. Linear satisfaction. | Prioritize highest-impact |
| Delighter | Unexpected. Delights when present. No dissatisfaction if absent. | Post-MVP unless very fast to build |
| Indifferent | Neither satisfied nor dissatisfied. | Cut or defer indefinitely |

---

## Feature KANO Classification

| Feature | KANO Category | Rationale |
|---|---|---|
| [F-001: Create property listing] | Must-be | Without this, hosts cannot use the product |
| [F-010: Search available properties] | Must-be | Without this, guests cannot book |
| [F-006: Configure seasonal pricing] | Performance | Better pricing = more host revenue, but basic pricing works |
| [F-025: AI-generated listing description] | Delighter | Unexpected value-add |
| [F-050: Multi-currency display] | Indifferent (for MVP market) | Single-market MVP |

---

## KANO Summary

| Category | Count | Notes |
|---|---|---|
| Must-be | [X] | All go into MVP |
| Performance | [X] | Highest-impact ones into MVP |
| Delighter | [X] | Post-MVP unless fast to build |
| Indifferent | [X] | Cut |
```

---

### ARTIFACT 4: Value vs. Complexity Matrix

```markdown
# Value vs. Complexity Matrix - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]
> **Purpose:** Determine delivery priority and sequencing

---

## Quadrants

| Quadrant | Value | Complexity | Action |
|---|---|---|---|
| Quick Win | High | Low | Do first |
| Big Bet | High | High | Plan carefully, phase |
| Fill-in | Low | Low | Only if fits naturally |
| Time Waster | Low | High | Cut |

---

## Feature Scoring

| Feature | Value (1-5) | Complexity (1-5) | Quadrant | Notion Priority |
|---|---|---|---|---|
| [F-001: Create property listing] | 5 | 3 | Big Bet | P1 - Critical |
| [F-010: Search available properties] | 5 | 2 | Quick Win | P1 - Critical |
| [F-004: Set base nightly price] | 4 | 1 | Quick Win | P1 - Critical |
| [F-025: AI listing description] | 4 | 2 | Quick Win | P2 - High |
| [F-006: Configure seasonal pricing] | 3 | 2 | Fill-in | P3 - Medium |
| [F-040: Analytics dashboard] | 2 | 4 | Time Waster | P4 - Low |

**Notion Priority mapping:**
- Must-be (KANO) → P1 - Critical
- Performance (KANO) + Quick Win (V×C) → P2 - High
- Performance (KANO) + Big Bet (V×C) → P2 - High
- Delighter + Fill-in → P3 - Medium
- Indifferent + Time Waster → P4 - Low

---

## Sequencing Signal

```
First in delivery: Quick Wins from Must-be category
Then: Big Bets (high value, plan carefully)
Later: Fill-ins alongside other work
Cut: Time Wasters + Indifferent
```
```

---

## Step 5: Create stub Feature Cards

**Runs after user approves all four artifacts (Feature List, Dependency Map, KANO, V×C).**

For every feature in the Feature List, create a stub Feature Card file at:
`pureinn-workspace/[project-slug]/features/cards/[FEAT-ID].md`

Stub content (frontmatter only, sections as empty placeholders):

```markdown
---
id: [FEAT-ID]
title: "[Action] [Result] [Object]"
status: 1_Walkthrough
stripe: TBD
owner: unassigned
priority: [P1/P2/P3 from V×C]
prd_ref: /product/PRD.md#[relevant-section]
feature_flag: [domain.feature-name]
flag_default: off
---

# Feature Card: {{title}}

## 1. Biznis Mantinely (SDD Input)
*Populated by pm-feature-design (JIT) - not yet.*

## 2. Acceptance Criteria
*Populated by pm-feature-design (JIT) - not yet.*

## 3. JIT Technical Design (FDD Design)
*Populated by pm-feature-design (JIT) - not yet.*

## 4. Realizacny Protokol (Build Verification)
*Populated after build - not yet.*
```

After creating all stub cards: confirm count and remind user that:
- Stripe assignment happens in pm-mvp-scope (updates `stripe:` field in each card)
- JIT design (Sections 1-3) happens in pm-feature-design just before each feature enters build
- Feature flags follow format: `[product-domain].[feature-name]` (e.g., `orders.draft-order`)

---

## Step 6: Notion push

**Runs after stub Feature Cards are created.**

If no Notion database is configured (state.json `notion.product_features_data_source_id` is null and user did not provide a URL in Step 1): skip this step, output Markdown files only.

### 5a. Get data source ID

1. Read `pureinn-variables.md` key "Feature Backlog" → get URL
2. Check `state.json notion_ids.feature_backlog` → if set, use it directly
3. If not cached: call `mcp__claude_ai_Notion__notion-fetch` with the URL, extract data source ID from `<data-source url="collection://...">`, save to `state.json notion_ids.feature_backlog`

### 6b. Push Feature entries

Call `mcp__claude_ai_Notion__notion-create-pages` with:
- `parent.type` = `"data_source_id"`
- `parent.data_source_id` = ID from 6a

Create one entry per feature with:

| Notion property | Value | Source |
|---|---|---|
| `Artefact Name` | Feature name (FDD format) | Feature List |
| `Artefact Type` | `"Feature"` | Fixed |
| `Short Description` | 1-sentence description of what the feature does | Feature List |
| `Status` | `"Backlog"` | Fixed |
| `Priority` | P1 / P2 / P3 | KANO + V×C mapping (see Artifact 4) |
| `Feature ID` | FEAT-[DOMAIN]-[NUMBER] | Feature List |
| `template_id` | Feature Template ID from database schema | From notion-fetch result |

Push features in batches of up to 100 per call if the list is large.

### 6c. Confirm

After push: report how many entries were created, how many stub Feature Cards were written locally, and surface any errors. Remind the user that MVP cut, stripe assignment, and Subject Area / Feature Set grouping will be finalized after `pm-mvp-scope`.

---

## Internal completeness checklist

<!-- Claude reference only -->

**Feature naming must comply with FDD:**
- [ ] Every feature follows action + result + object format
- [ ] No feature named as a capability ("messaging system", "admin panel")
- [ ] Features are discrete actions, not multi-step processes

**Feature granularity:**
- [ ] Each feature deliverable in 2 weeks or less
- [ ] Features too broad are flagged for splitting

**Coverage:**
- [ ] All in-scope functional areas from PRD have features
- [ ] All user roles have features assigned
- [ ] System-automated features included (notifications, scheduled jobs, payments)
- [ ] Admin/back-office features included

**Dependency Map:**
- [ ] All hard dependencies identified
- [ ] Critical path identified
- [ ] Parallelizable tracks identified
- [ ] No circular dependencies

**KANO:**
- [ ] Every feature classified
- [ ] Classification rationale stated
- [ ] All Must-be features are in MVP

**V×C Matrix:**
- [ ] Every feature scored on Value (1-5) and Complexity (1-5)
- [ ] Quadrant assigned
- [ ] Notion Priority assigned per mapping

**For SaaS/AI products:**
- [ ] AI features named correctly (e.g., "Generate listing description draft", not "AI module")
- [ ] Onboarding features included
- [ ] Billing and subscription management features included (if paid)
- [ ] Settings and configuration features included
- [ ] Data export / account deletion features included (GDPR)
- [ ] Notification features included per channel
- [ ] API/webhook features included if integrations are in scope

---

## Save to

**Create mode (first run - Greenfield):**
```
pureinn-workspace/[project-slug]/features/feature_list.md          (Live Register 4 - created)
pureinn-workspace/[project-slug]/features/cards/FEAT-[DOMAIN]-[NUMBER].md  (one stub per feature)
pureinn-workspace/[project-slug]/artifacts/phase-5/feature-dependency-map.md
pureinn-workspace/[project-slug]/artifacts/phase-5/kano-analysis.md
pureinn-workspace/[project-slug]/artifacts/phase-5/value-complexity-matrix.md
```

**FI Append mode (new initiative):**
```
pureinn-workspace/[project-slug]/features/feature_list.md          (APPENDED - new domain section added)
pureinn-workspace/[project-slug]/features/cards/FEAT-[NEW-DOMAIN]-[NUMBER].md  (stub cards for new features only)
pureinn-workspace/[project-slug]/initiatives/[slug]/kano-analysis.md  (initiative-scoped KANO)
pureinn-workspace/[project-slug]/initiatives/[slug]/value-complexity-matrix.md  (initiative-scoped V×C)
```

**FI Append rules:**
- Existing FEAT-* entries in feature_list.md are not modified, renumbered, or removed
- New initiative features are appended as a new Subject Area section at the bottom
- Stub Feature Cards created only for new FEAT-[NEW-DOMAIN]-* features
- KANO + V×C saved to initiative folder (not overwriting master phase-5/ analysis)
- Dependency map section in feature_list.md updated with cross-initiative dependencies (if any)
