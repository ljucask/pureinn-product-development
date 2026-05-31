---
name: pm-features-list
description: Generate the complete Features List in FDD format, then run Dependency Map, KANO Analysis, and Value vs. Complexity Matrix. After user approval, push all features to Notion as the initial backlog. Output is the prioritized, dependency-mapped feature inventory ready for MVP scoping in pm-mvp-scope.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: features list, FDD format, KANO analysis, value complexity matrix, feature prioritization, Phase 5
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-mvp-scope, pm-domain-model, pm-prd, pm-product-roadmap
---

# PM - Features List

## What this skill does

Phase 5 / Step 1-3. Takes the product scope from the PRD and produces:

1. **Features List** - all features in FDD format (`<action> <result> <object>`), grouped by functional area, with actor and rough scope
2. **Dependency Map** - which features block which, critical path, parallelizable tracks
3. **KANO Analysis** - must-be / performance / delighter / indifferent classification per feature
4. **Value vs. Complexity Matrix** - Quick Win / Big Bet / Fill-in / Time Waster scoring per feature

After user approval of all four artifacts: push the complete feature inventory to Notion as the initial product backlog (flat list of Feature entries, Status = Backlog, Priority derived from KANO + V×C).

This is the direct input for `pm-mvp-scope`, which takes the prioritized list and makes the MVP cut, groups into Feature Sets, and sequences into Delivery Stripes.

---

## Dependencies

**Required before running:**
- `pm-prd` - product scope (in-scope functional areas) is the primary input
- `pm-domain-model` - entities inform what operations are needed per domain

**Recommended before running:**
- `pm-personas` - user roles drive which features belong to which actor
- `pm-problem-validation` - validated pains confirm which features address real needs

**Produces artifacts used by:**
- `pm-mvp-scope` - prioritized feature inventory is the direct input for MVP cut + Feature Sets + Stripes
- `pm-product-roadmap` v3 - features populate the delivery view
- Phase 6 skills - each feature eventually gets a Feature Card, BRD entry, and FSD section

---

## Step 0: Current state check

Check for existing artifacts:
- Features List
- Dependency Map
- KANO Analysis
- Value vs. Complexity Matrix

Also check: does a PRD exist? A Domain Model? Without the PRD, the feature scope will be undefined. Without the Domain Model, features may not align with the data structure.

Look for: features named as capabilities ("messaging system") rather than actions ("Send message to guest"), features too large for 2-week delivery (split needed), missing user role attribution, duplicates across functional areas, KANO classification without rationale.

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
I need inputs for the Features List, Dependency Map, and KANO + V×C prioritization.

1. PRODUCT SCOPE (from PRD)
   What are the in-scope functional areas for the product?
   Paste the "In Scope" section from the PRD, or describe it here.
   [paste or describe]

2. USER ROLES
   Who are the actors in the system? (e.g., Host, Guest, Admin, Property Manager)
   Which role is primary (most features serve them)?

3. DOMAIN MODEL REFERENCE
   Are the core entities defined? (paste Entity Catalogue or confirm in context)
   [paste or "in context"]

4. FEATURE IDEAS
   Do you have any feature ideas already written down?
   (Paste any list, notes, or user stories - even rough, any format)
   [paste or "nothing yet"]

5. KNOWN DEPENDENCIES
   Are there features you know depend on each other?
   (e.g., "payment must come before booking confirmation", "listing must exist before search")
   [describe or "none known yet"]

6. NOTION SETUP
   Read pureinn-variables.md, key "Feature Backlog". Skip this question if URL is present.
   If blank: do you have a Notion Product Features database to push features to after approval?
   If yes: paste the database URL - save it to pureinn-variables.md under "Feature Backlog".
   If no: skip - output will be Markdown only. Fill in pureinn-variables.md later to enable push.
```

---

## Step 2: Generate Features List

Before generating:
1. Identify all functional areas from the PRD scope
2. For each area, derive features using the FDD naming convention: `<action> <result> <object>`
3. Assign each feature a user role (who performs or benefits from it)
4. Flag features that are likely too large for 2 weeks (mark for splitting)
5. Every feature gets an ID (F-001, F-002...) - used in Dependency Map and KANO

Generate in English.

---

### ARTIFACT 1: Features List

```markdown
# Features List - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]
> **Format:** FDD - action + result + object
> **Based on:** PRD v[X], Domain Model v[X]

---

## Feature Naming Convention

Every feature follows: **`<action> <result> <object>`**

- Action: what happens (Submit, Calculate, Sync, Generate, Send, Approve, Cancel...)
- Result: the outcome or state change (booking request, pricing update, availability...)
- Object: the entity or thing being acted on (calendar, listing, invoice, message...)

Features must be:
- Independently implementable
- Deliverable in 2 weeks or less
- Testable with clear acceptance criteria (defined later in Phase 6)

---

## Features by Functional Area

### [Functional Area 1: e.g., Property Management]

| ID | Feature | Actor | Notes |
|---|---|---|---|
| F-001 | [e.g., Create property listing] | [Host] | |
| F-002 | [e.g., Edit property details] | [Host] | |
| F-003 | [e.g., Upload property photos] | [Host] | |
| F-004 | [e.g., Set base nightly price] | [Host] | |
| F-005 | [e.g., Define availability rules] | [Host] | |
| F-006 | [e.g., Configure seasonal pricing] | [Host] | |

---

### [Functional Area 2: e.g., Booking Flow]

| ID | Feature | Actor | Notes |
|---|---|---|---|
| F-010 | [e.g., Search available properties] | [Guest] | |
| F-011 | [e.g., Submit booking request] | [Guest] | |
| F-012 | [e.g., Approve booking request] | [Host] | |
| F-013 | [e.g., Decline booking request] | [Host] | |
| F-014 | [e.g., Cancel confirmed booking] | [Guest / Host] | Cancellation policy applies |
| F-015 | [e.g., Process booking payment] | [System] | Via payment provider |
| F-016 | [e.g., Issue booking refund] | [System] | Triggered by cancellation |

---

### [Functional Area N: ...]

[same structure]

---

## Features Flagged for Splitting

| Feature | Reason | Suggested split |
|---|---|---|
| [F-XXX: name] | Too broad - each part is separately deliverable | [F-XXX-a: ..., F-XXX-b: ...] |

---

## Feature Count Summary

| Functional Area | Feature count |
|---|---|
| [Area 1] | [X] |
| [Area N] | [X] |
| **Total** | **[X]** |

---

## Actor Coverage

| Actor | Feature count | Primary functional areas |
|---|---|---|
| [Host] | [X] | [Property mgmt, pricing] |
| [Guest] | [X] | [Search, booking, payment] |
| [System] | [X] | [Automated: notifications, payments] |

---

## Features Not in Scope

| Feature idea | Reason excluded | Reconsider when |
|---|---|---|
| [e.g., Native mobile app] | Web-first MVP | After PMF proven on web |

---

## Open Items

| Item | Decision needed | Owner |
|---|---|---|
| [Unclear feature] | [What needs clarification] | [PM / stakeholder] |
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

## Step 5: Notion push

**Runs after user approves all four artifacts.**

If no Notion database is configured (state.json `notion.product_features_data_source_id` is null and user did not provide a URL in Step 1): skip this step, output Markdown files only.

### 5a. Get data source ID

1. Read `pureinn-variables.md` key "Feature Backlog" → get URL
2. Check `state.json notion_ids.feature_backlog` → if set, use it directly
3. If not cached: call `mcp__claude_ai_Notion__notion-fetch` with the URL, extract data source ID from `<data-source url="collection://...">`, save to `state.json notion_ids.feature_backlog`

### 5b. Push Feature entries

Call `mcp__claude_ai_Notion__notion-create-pages` with:
- `parent.type` = `"data_source_id"`
- `parent.data_source_id` = ID from 5a

Create one entry per feature with:

| Notion property | Value | Source |
|---|---|---|
| `Artefact Name` | Feature name (FDD format) | Features List |
| `Artefact Type` | `"Feature"` | Fixed |
| `Short Description` | 1-sentence description of what the feature does | Features List |
| `Status` | `"Backlog"` | Fixed |
| `Priority` | P1 / P2 / P3 / P4 | KANO + V×C mapping (see Artifact 4) |
| `template_id` | Feature Template ID from database schema | From notion-fetch result |

Push features in batches of up to 100 per call if the list is large.

### 5c. Confirm

After push: report how many entries were created and surface any errors. Remind the user that Phase, Dev Stripe, and Feature Set grouping (MFS/FS) will be added after `pm-mvp-scope` completes the MVP cut.

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

```
pureinn-workspace/[project-slug]/artifacts/phase-5/features-list.md
pureinn-workspace/[project-slug]/artifacts/phase-5/feature-dependency-map.md
pureinn-workspace/[project-slug]/artifacts/phase-5/kano-analysis.md
pureinn-workspace/[project-slug]/artifacts/phase-5/value-complexity-matrix.md
```
