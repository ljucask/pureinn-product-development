---
name: pm-mvp-scope
description: Define MVP scope from the prioritized Features List. Makes the IN/POST-MVP/CUT decision, groups features into Feature Sets (MFS/FS hierarchy), and sequences them into Delivery Stripes. After user approval, creates MFS and FS entries in Notion and enriches existing Feature entries with Phase, Dev Stripe, and parent grouping. Phase 5 exit artifact. Required input for all Phase 6 skills.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: MVP scope, feature sets, delivery stripes, MFS, prioritization, in scope post MVP cut
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-features-list, pm-product-roadmap, pm-stripe, pm-brd
---

# PM - MVP Scope

## What this skill does

Phase 5 / Steps 4-5. Takes the prioritized, dependency-mapped Features List (output of `pm-features-list`) and produces the delivery structure:

1. **MVP Scope Decision** - what is IN (MVP), what is POST-MVP, what is CUT, with rationale
2. **Feature Sets** - logical domain groupings (MFS → FS hierarchy). One BRD + one FSD per Feature Set.
3. **Delivery Stripes** - 2-week time-boxed delivery blocks, sequenced by dependency + V×C priority

After user approval: update Notion with the full structure - create MFS and FS entries, assign Parent relations, enrich Feature entries with Phase and Dev Stripe.

This is the Phase 5 exit artifact. Everything in Phase 6 (spec, build) operates on Feature Sets and Delivery Stripes defined here.

---

## Dependencies

**Required before running:**
- `pm-features-list` - must include completed Dependency Map, KANO Analysis, and V×C Matrix
- All four artifacts from pm-features-list must be approved by user before running this skill

**Recommended before running:**
- `pm-kpis` - North Star and AARRR metrics validate MVP scope alignment
- `pm-business-case` - revenue model and runway inform how aggressive the MVP cut should be

**Produces artifacts used by:**
- `pm-product-roadmap` v3 - Delivery Stripes populate the delivery view
- `pm-brd` - one BRD per Feature Set
- `pm-fsd` - one FSD per Feature Set
- All Phase 6 skills - Feature Sets are the unit of design and specification
- Notion - MFS/FS entries created, Feature entries enriched

---

## Step 0: Current state check

Check for existing artifacts:
- MVP Scope
- Feature Sets definition
- Delivery Stripes plan

Also check: does a complete Features List exist with KANO and V×C? This skill cannot run without it. Is state.json available with Notion connection details?

Look for: MVP scope that's too large (more than 3-4 months of work), no explicit out-of-scope list, Feature Sets that are too broad (BRD would be unmanageable), Delivery Stripes longer than 2 weeks, critical path not respected in stripe sequencing.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask questions in 2 groups. Group 1 drives strategic alignment - Claude shows a preliminary MVP cut after it. Group 2 sets execution parameters.

---

### Group 1 of 2 - Strategic alignment

Ask all as plain text:

What is the single most important thing the MVP must prove? Complete this sentence: "We will consider MVP successful if we prove that..." (e.g., "hosts will pay for automated property management", "users can complete a booking end-to-end without human intervention")

Are there any features that must be in MVP regardless of KANO/V×C scoring? Why are they non-negotiable? (technical dependency, contractual requirement, customer commitment, other)

Are there any features that must NOT be in MVP - features explicitly excluded for technical, strategic, or resource reasons?

After receiving Group 1 answers, Claude does the following before asking Group 2:

1. Read the KANO + V×C output from pm-features-list in context
2. Apply the MVP hypothesis and non-negotiables to the prioritized feature list
3. Show a preliminary MVP cut:

```
Based on your hypothesis and the KANO/V×C data, here is my initial reading of MVP scope:

IN - Must-be features (KANO: M) that are Quick Wins or Big Bets (V×C):
  - [feature] - [reason]
  - [feature] - [reason]

BORDERLINE - Performance features with high value, low complexity:
  - [feature] - [reason why it's borderline]

OUT - Deferred to post-MVP:
  - [feature] - [reason]

Does this initial cut match your thinking? Anything you'd move in or out before we finalize?
```

Wait for response. Adjust the cut if needed. Then proceed to Group 2.

---

### Group 2 of 2 - Execution parameters

Ask these two together:

What is the approximate team size for development?

  A) Solo developer
  B) 2 developers
  C) 3-4 developers
  D) 5+ developers

What is the MVP timeline constraint?

  A) Hard deadline - specific date or event (describe)
  B) Runway-constrained - must launch before runway runs out (how many months?)
  C) Milestone-driven - launch when PMF signal is achieved, no fixed date
  D) No constraint - launch when it's ready

Then ask as plain text:

Are Notion Feature entries already created from pm-features-list? (yes / no - if yes, I'll update existing entries; if no, Notion update is skipped)

After answers, show the finalized MVP scope proposal combining Group 1 alignment + Group 2 constraints. Ask for final confirmation before generating the full MVP Scope artifact with Feature Sets and Delivery Stripes.

---

## Step 2: Generate MVP Scope

---

### ARTIFACT 1: MVP Scope

```markdown
# MVP Scope - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]
> **MVP definition:** The minimum set of features that delivers the core value proposition
>                    to the primary persona and enables the first paying customers.

---

## MVP Definition

**What MVP must prove:** [Single hypothesis]

**Success signal:** [Specific, measurable - e.g., "20 paying customers, D30 retention > 40%, NPS > 30"]

**Primary persona served:** [Persona name from pm-personas]

---

## In MVP

| Feature | ID | KANO | V×C | Delivery Stripe |
|---|---|---|---|---|
| [Feature name] | F-001 | Must-be | Quick Win | Stripe 1 |
| [Feature name] | F-011 | Must-be | Big Bet | Stripe 2 |

**MVP total:** [X] features across [Y] stripes ([Z] weeks)

---

## Post-MVP

| Feature | ID | KANO | Reason deferred | Target phase |
|---|---|---|---|---|
| [Feature name] | F-006 | Performance | Not blocking core value | MVP+ |
| [Feature name] | F-040 | Performance | Nice-to-have | Phase 2 |

---

## Cut (Not building)

| Feature | ID | Reason |
|---|---|---|
| [Feature name] | F-050 | Indifferent per KANO - no customer asked for it |
```

---

## Step 3: Generate Feature Sets

---

### ARTIFACT 2: Feature Sets

```markdown
# Feature Sets - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]
> **Definition:** A Feature Set is a logical domain grouping of related features.
>                One BRD + One FSD per Feature Set.
>                Feature Sets are the spec unit. Delivery Stripes are the delivery unit.

---

## Feature Set Overview

| MFS | FS ID | Feature Set | Features (all, incl. post-MVP) | BRD/FSD status |
|---|---|---|---|---|
| [Domain A] | FS-01 | [e.g., Property Listing Management] | F-001, F-002, F-003, F-004, F-005, F-006 | To be written |
| [Domain A] | FS-02 | [e.g., Pricing & Availability] | F-007, F-008, F-009 | To be written |
| [Domain B] | FS-03 | [e.g., Booking Flow] | F-010, F-011, F-012, F-013, F-014 | To be written |
| [Domain B] | FS-04 | [e.g., Payment Processing] | F-015, F-016 | To be written |
| [Domain C] | FS-05 | [e.g., Guest-Host Messaging] | F-030, F-031, F-032 | To be written |
| [Domain C] | FS-06 | [e.g., Notifications] | F-020, F-021, F-022 | To be written |

---

## Feature Set Details

### [Domain A - MFS name]

#### FS-01: [Name]

**Purpose:** [What this FS enables - user value]
**Primary actor:** [Host / Guest / Admin / System]
**Domain(s):** [From Domain Model]
**All features in this set (MVP + post-MVP):**

| ID | Feature | Phase |
|---|---|---|
| F-001 | [Feature name] | MVP |
| F-006 | [Feature name] | MVP+ |

**Dependencies:** Needs: [None / FS-XX partial]. Enables: [FS-XX]
**Spec requirement:** BRD + FSD written before Stripe [X] starts.

---

[repeat per FS]
```

---

## Step 4: Generate Delivery Stripes

---

### ARTIFACT 3: Delivery Stripes

```markdown
# Delivery Stripes - [Product Name]

> **Phase:** 5 - Feature Planning
> **Date:** [date]
> **Definition:** A Delivery Stripe is a 2-week time-boxed delivery block.
>                Contains MVP features from one or more Feature Sets.
>                BRD + FSD must be complete before stripe build starts.

---

## Stripe Plan

| Stripe | Duration | MVP Features | Feature Sets | Goal | Spec ready by |
|---|---|---|---|---|---|
| Stripe 1 | Week 1-2 | F-001, F-002, F-003 | FS-01 (partial) | [Host can create and manage a listing] | Before Stripe 1 |
| Stripe 2 | Week 3-4 | F-010, F-011 | FS-03 (partial) | [Guest can search and request a booking] | During Stripe 1 |
| Stripe 3 | Week 5-6 | F-012, F-013, F-015 | FS-03 (done), FS-04 | [Full booking + payment flow] | During Stripe 2 |
| Stripe 4 | Week 7-8 | F-020, F-030, F-031 | FS-05, FS-06 | [Notifications and messaging] | During Stripe 3 |
| Stripe 5 | Week 9-10 | [Buffer: edge cases, polish] | All | [MVP ready for first users] | - |

**MVP completion:** Stripe [X] - estimated [date or week range]

---

## Spec Writing Schedule

Spec is written rolling - always ahead of build:

| When | Activity |
|---|---|
| Before Stripe 1 | Write BRD + FSD for FS-01 |
| During Stripe 1 | Write BRD + FSD for FS-03, FS-04 |
| During Stripe 2 | Write BRD + FSD for FS-05, FS-06 |

---

## Stripe Design Rules

- Max 2 weeks per stripe
- BRD + FSD complete before stripe build starts (spec-first)
- Each stripe has a named goal (testable outcome, not a feature list)
- Buffer stripe at end is mandatory for MVP
- Features span stripes only if intermediate state is testable
```

---

## Step 5: Notion update

**Runs after user approves all three artifacts.**

If user confirmed no Notion entries exist (Step 1, question 5 = "no"): skip this step.

If Notion Feature entries were created by pm-features-list:

### 5a. Get Notion connection

1. Read `pureinn-variables.md` key "Feature Backlog" → get URL
2. Check `state.json notion_ids.feature_backlog` → if set, use it directly
3. If not cached: call `mcp__claude_ai_Notion__notion-fetch` with the URL, extract data source ID, save to `state.json notion_ids.feature_backlog`
4. If URL blank in pureinn-variables.md: ask user, save URL to pureinn-variables.md, then proceed with 3

### 5b. Create MFS entries

For each MFS (domain cluster) from Artifact 2: call `mcp__claude_ai_Notion__notion-create-pages` with:
- `parent.type` = `"data_source_id"`
- `parent.data_source_id` = from 5a
- Per MFS entry: `Artefact Name` = MFS name, `Artefact Type` = `"MFS"`, `Status` = `"Backlog"`
- Use MFS Template ID from the database schema if available

Collect the returned page URLs (one per MFS) - needed for FS parent relations.

### 5c. Create FS entries

For each Feature Set from Artifact 2: call `mcp__claude_ai_Notion__notion-create-pages` with:
- Per FS entry: `Artefact Name` = FS name, `Artefact Type` = `"FS"`, `Status` = `"Backlog"`, `Parent` = URL of the corresponding MFS page from 5b
- Use FS Template ID from the database schema if available

Collect the returned page URLs (one per FS) - needed for Feature parent relations.

### 5d. Enrich Feature entries

For each Feature in Artifact 1 (MVP Scope - IN + POST-MVP + CUT), update the existing Notion entry:

Call `mcp__claude_ai_Notion__notion-update-page` with `command: "update_properties"` per feature:

| Property | Value | Source |
|---|---|---|
| `Phase` | `"MVP"` / `"MVP+"` / `"Phase 2"` / `"Enterprise"` | Artifact 1 scope decision |
| `Dev Stripe` | `"Stripe 1"` ... `"Stripe 7"` (MVP features only) | Artifact 3 stripe assignment |
| `Parent` | URL of the corresponding FS page from 5c | Artifact 2 feature set assignment |

Features marked CUT: update `Phase` to reflect cut status (use lowest phase option or leave blank); do not assign Dev Stripe.

### 5e. Confirm

After all updates: report counts (MFS created, FS created, Features enriched, errors). Remind user that BRD + FSD will be linked via FSD URL property as spec is written in Phase 6.

---

## Internal completeness checklist

<!-- Claude reference only -->

**MVP Scope must cover:**
- [ ] MVP hypothesis stated
- [ ] MVP success signal defined (measurable)
- [ ] In MVP list with stripe assignment
- [ ] Post-MVP list with reason for deferral and target phase
- [ ] Cut list with rationale
- [ ] MVP size is realistic vs. team and timeline

**Feature Sets must cover:**
- [ ] Logical/functional groupings (not too large - max ~8-10 features per FS)
- [ ] MFS → FS hierarchy clear
- [ ] Each FS has a purpose and primary actor
- [ ] All features (MVP + post-MVP) assigned to a FS
- [ ] Dependencies between FSs stated
- [ ] Spec requirement (BRD + FSD) noted per FS

**Delivery Stripes must cover:**
- [ ] Each stripe is max 2 weeks
- [ ] Each stripe has a named goal
- [ ] Spec-ready-by date specified per stripe
- [ ] Buffer stripe included at end
- [ ] Stripes sequenced by dependency (critical path respected)
- [ ] Spec-writing schedule defined

**For SaaS/AI products:**
- [ ] Onboarding flow is in Stripe 1 or 2
- [ ] Payment integration is in MVP stripes (if paid product)
- [ ] AI features have a fallback plan if AI output quality isn't ready
- [ ] Data pipeline features are before AI features in stripe order
- [ ] Account deletion (GDPR) is before launch stripe
- [ ] Admin/support tooling has at least a minimal stripe in MVP

---

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-5/mvp-scope.md
pureinn-workspace/[project-slug]/artifacts/phase-5/feature-sets.md
pureinn-workspace/[project-slug]/artifacts/phase-5/delivery-stripes.md
```
