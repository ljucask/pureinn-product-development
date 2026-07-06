---
name: pm-onboarding
description: Generate a role-specific Onboarding Brief for a new team member. Reads the existing workspace and distills the right subset of artifacts for the role (Developer, PM, Designer, Stakeholder/Investor). Produces a single navigable brief with product context, settled decisions, where-things-live map, current delivery state, and who to talk to. Run when a new person joins the team. Skip if solo builder with no team.
license: MIT
metadata:
  author: https://github.com/ljucask

  version: "1.0.0"
  domain: product-management
  triggers: onboarding, new team member, new developer, new designer, new pm, role brief, team brief, joining
  role: specialist
  scope: documentation
  output-format: document
  related-skills: pm-team-roster, pm-stakeholder-map, pm-comms-charter, pm-stripe
---

# PM - Onboarding Brief

## What this skill does

Generates a role-specific Onboarding Brief for a new team member joining mid-project. It reads the existing workspace and filters the relevant subset of artifacts for the person's role - so they get context without noise.

**Four role tracks:**

| Role | Gets |
|---|---|
| **Developer** | Domain model, entities + state transitions, business rules, current stripe/Feature Cards in queue, coding conventions, who to ask about what |
| **PM** | Product vision, PRD (problem + value prop + target customer), roadmap + phases, feature_list (KANO/VxC/phase), personas, open hypotheses, settled decisions |
| **Designer** | Personas, user flows, features in `2b_In_Design`, Figma links, design system reference, early adopter profile |
| **Stakeholder / Investor** | Executive brief: problem + market, value prop, MVP scope, traction/metrics, team, next milestone |

**Settled decisions section is mandatory for every role.** This is the list of things that have been decided and should not be re-opened without new evidence. Saves the team from re-litigating.

**Skip if:** solo builder with no team to onboard.

---

## Dependencies

**Required before running:**
- A workspace exists with at least some artifacts
- `pm-team-roster` - to know the team structure (recommended but not blocking)

The skill degrades gracefully if artifacts are missing - it reports what is absent rather than blocking.

---

## Step 0: Current state check

Inventory the workspace artifacts:

| Artifact | Present? |
|---|---|
| state.json | |
| PRD Master | |
| Product Roadmap | |
| Personas / Customer Segments | |
| Domain Model / Entities / Business Rules | |
| Feature List + Feature Cards | |
| Team Roster | |
| Stakeholder Map | |
| pureinn-variables.md (Notion URLs) | |

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask as plain text:

Who is joining the team? (name, role title)

What is their primary role?

```
[Use AskUserQuestion]
A) Developer / Engineer
B) Product Manager
C) Designer (UX/UI)
D) Stakeholder / Investor / Advisor
```

Is there anything specific they need to know or get up to speed on urgently? (optional - e.g. "they're taking over stripe-auth immediately", "they'll be reviewing the pitch deck this week")

What is their start date / when do you need this brief ready?

After answers: confirm role and urgency before generating.

---

## Step 2: Generate artifact

Generate in the product's working language (check PRD / existing artifacts for language convention).

---

### ARTIFACT: Onboarding Brief - [Name] ([Role])

```markdown
# Onboarding Brief - [Name]
**Role:** [Role title]
**Product:** [Product name]
**Date:** [date]
**Prepared by:** pm-onboarding (Pureinn v[version])

---

## Welcome - what you're joining

[3-4 sentences: what the product does, who it's for, what problem it solves, where the team is right now in the build. Factual, no fluff.]

---

## The product in one page

**Problem we're solving:**
[1-2 sentences from PRD §1]

**Who we're building for:**
[Primary segment + early adopter profile - from personas/customer-segments]

**Value we deliver:**
[Value proposition from PRD §3 - 1-2 sentences]

**Current phase:**
[Phase name from roadmap + what the exit criteria are]

**North Star Metric:**
[NSM from KPIs if available]

---

## Settled decisions (do not re-open without new evidence)

These have been decided. They can be changed - but only with new data or a specific argument, not preference.

| Decision | What was decided | Why |
|---|---|---|
| [e.g. Target segment] | [Primary segment: X, not Y] | [Market size + pain intensity evidence] |
| [e.g. Monetization] | [Transaction take-rate of X%] | [WTP evidence from research] |
| [e.g. MVP scope] | [Phase 0 = auto-match core loop in BA metro] | [Validated in pm-mvp-scope] |
| [e.g. Tech stack] | [Stack choice] | [pm-tech-feasibility rationale] |

[Add or remove rows based on what actually exists in the workspace. Only include genuinely settled decisions - not assumptions or open questions.]

---

## Where things live

[Adapt to role - only show what is relevant for this person's work]

| Artifact | Location | What it contains |
|---|---|---|
| PRD Master | `/product/PRD_master.md` | Problem, value prop, target customer, scope |
| Product Roadmap | `/artifacts/phase-5-planning/product-roadmap.md` (latest version; earlier drafts in `phase-3-define/`) | Phases, deliverables, exit criteria |
| Feature List | `/features/feature_list.md` | All features with KANO/VxC/phase/stripe |
| Feature Cards | `/features/cards/FEAT-[ID].md` | Per-feature spec, ACs, technical design |
| Domain Model | `/domain/entities.md` | Entities, state machines, guard conditions |
| Business Rules | `/domain/business_rules.md` | BR-IDs referenced in Feature Cards |
| Personas | `/artifacts/phase-2-discovery/personas.md` | Customer profiles + pains |
| Notion | [URL from pureinn-variables.md if present] | Feature Backlog, team collaboration |

---

## [ROLE-SPECIFIC SECTION - insert the relevant block below]
```

---

### Role block A: Developer

```markdown
## Current delivery state

**Active stripes:**
[Read feature_list.md + Feature Cards. List stripes with their active feature and status.]

| Stripe | Active feature | Status | Next in queue |
|---|---|---|---|
| [stripe-name] | [FEAT-ID]: [title] | [status] | [FEAT-ID] |

**Features in your immediate queue:**
[List 2-3 features by priority with FEAT-IDs + current status + what needs to happen next]

**Features recently shipped (last 2-3):**
[From 6_Shipped cards - gives context on what was just built]

---

## Domain you need to understand first

**Key entities and their states:**
[Read entities.md - extract the 3-5 most central entities (highest number of transitions/references in Feature Cards) with their state machines]

| Entity | States | Key guard conditions |
|---|---|---|
| [Entity] | [state1 → state2 → state3] | [key guard expressions] |

**Critical business rules (referenced in active Feature Cards):**
[Read business_rules.md - extract only rules referenced in active/upcoming Feature Cards]

| BR-ID | Rule | Enforcement point |
|---|---|---|
| [BR-ID] | [one-line summary] | [where it's enforced] |

---

## How we work (delivery conventions)

- **JIT design:** every feature goes through pm-feature-design before build. Do not start building from feature_list alone - the Feature Card Sections 1-3 are the spec.
- **Atomic commits:** register updates (entities, rules) committed before code. Two commits per feature: `spec([FEAT-ID]): registers` then `spec([FEAT-ID]): design`.
- **Feature flags:** every feature ships behind a flag (`domain.feature-name`, default OFF). Non-negotiable.
- **Status transitions:** update Feature Card frontmatter `status:` at every transition. `feature_list.md` status column must stay in sync.
- **Run `/pm-stripe` at the start of every dev session** - it reads current state and tells you exactly what to do next.

---

## Who to ask about what

[Read pm-team-roster if it exists. If not, fill from what is known.]

| Topic | Person | How |
|---|---|---|
| Product decisions / scope | [PM name] | [Slack/channel/meeting] |
| Domain model / business rules | [Lead dev or PM] | [how] |
| Design / Figma | [Designer] | [how] |
| Deployment / infra | [DevOps/lead dev] | [how] |
```

---

### Role block B: PM

```markdown
## Strategic context

**Roadmap phases:**
[Extract phase names, primary goals, exit criteria from roadmap]

| Phase | Goal | Exit criteria | Status |
|---|---|---|---|
| [Phase 0 / MVP] | [goal] | [criteria] | [current / next] |
| [Phase 1] | | | |

**Open hypotheses (to validate):**
[From pm-hypotheses if exists, or from PRD §9 Open Questions]

- [ ] [Hypothesis 1 - what we're testing + how]
- [ ] [Hypothesis 2]

**Current KANO distribution:**
[Summary from feature_list - how many Must-be / Performance / Delighter / Indifferent]

Must-be: [N] | Performance: [N] | Delighter: [N] | Indifferent: [N]

Phase 0 features: [N] | Phase 1: [N] | Post-MVP: [N]

---

## Decisions you own

[From Decision Rights Matrix in pm-team-roster if available]

| Decision type | You decide | You need sign-off from |
|---|---|---|
| Feature scope changes | ✓ | [Stakeholder / Lead dev if major] |
| Phase assignments | ✓ | [Team] |
| Priority changes | ✓ | [PM lead if junior] |

---

## How we work (PM conventions)

- **Delta mode re-runs:** when new research arrives, re-run the relevant skill in delta mode - never rewrite from scratch. Show changes explicitly.
- **Research → artifacts:** new user/market data flows into personas → jtbd → pm-prd → roadmap → features-list in that order.
- **Strategic consistency:** run `/pm-audit strategy` after any major re-check to surface cross-artifact conflicts.
- **Feature Card ownership:** Sections 1-3 are produced by `pm-feature-design` JIT (just before build). Do not populate them earlier.
```

---

### Role block C: Designer

```markdown
## What needs design right now

[Read Feature Cards with `2b_In_Design` status or frontend features approaching build]

| FEAT-ID | Feature | Status | Figma link | Notes |
|---|---|---|---|---|
| [ID] | [title] | [2b_In_Design / 2_Spec_Done] | [link or TBD] | [e.g. "ready for Figma"] |

**Layer-gated design:** only features with `frontend` in their `layer` field pass through `2b_In_Design`. Pure backend/system features skip design.

---

## Who we're designing for

[Condensed extract from personas.md - only most relevant for design decisions]

**Primary persona:** [Name] - [2-sentence who they are + top pain]
**Secondary persona:** [Name] - [2-sentence]

**Early adopter:** [1-sentence - who they are + what they'll tolerate at launch]

---

## Design conventions

- **Feature flow:** after Figma design is ready and approved, set Feature Card status `2b_In_Design → 3_Ready_to_Build` in Notion or in the `.md` frontmatter.
- **Design system:** [reference if it exists, or note TBD]
- **Figma workspace:** [link if exists]
- **How ACs relate to design:** Acceptance Criteria in Section 2 of each Feature Card define the observable outcomes. Design must satisfy the ACs - especially AC-03 (flag OFF behavior - the feature must degrade gracefully when its flag is off).
```

---

### Role block D: Stakeholder / Investor

```markdown
## Executive brief

**The problem:**
[PRD §1 - 2-3 sentences max]

**The market:**
[Market analysis headline numbers: TAM/SAM/SOM + "why now" in 1-2 sentences]

**Our solution:**
[Value proposition from PRD §3 - what we do that others don't]

**MVP scope:**
[Phase 0 deliverables - what we are building first and why]

**Current status:**
[Where we are: phase, features shipped vs. in build vs. in queue]

**Next milestone:**
[Phase 0 exit criteria - what it looks like when MVP is done]

**Team:**
[Core team from pm-team-roster - names + roles, 1 line each]

**Key risks:**
[Top 2-3 from PRD §8 Constraints and Risks]
```

---

## Internal completeness checklist

<!-- Claude reference only -->

**Brief must cover for every role:**
- [ ] Product context (problem + who + value prop + current phase) - no fluff
- [ ] Settled decisions table - at least 3 real decisions, not placeholder rows
- [ ] Where things live - artifact map scoped to role
- [ ] Role-specific block fully populated from real workspace data
- [ ] Who to ask about what - real names from team-roster or confirmed by user

**Developer-specific:**
- [ ] Active stripe state read from real Feature Cards (not invented)
- [ ] Entity state machines from real entities.md
- [ ] Business rules from real business_rules.md (only those referenced in active cards)

**PM-specific:**
- [ ] Roadmap phases with real exit criteria
- [ ] Open hypotheses from real register or PRD Open Questions
- [ ] KANO distribution from real feature_list

**Designer-specific:**
- [ ] `2b_In_Design` features read from real Feature Cards
- [ ] Personas condensed from real personas.md

**Stakeholder-specific:**
- [ ] Market numbers from real market-analysis.md
- [ ] Current status from real stripe/feature state

**Never invented:** direct quotes, metric values, team names, feature counts, BR-IDs. Read them from real artifacts or mark `[TBD - check with PM]`.

---

## Save to

```
pureinn-workspace/[project-slug]/team/onboarding/[name]-[role]-onboarding.md
```

---

## Handoff

**Čo si teraz má:** Role-specific brief ktorý nový člen dostane deň 1 - produkt, rozhodnutia, kde čo nájsť, aktuálny stav delivery, s kým hovoriť.

**Ďalší krok:** `/pm-team-roster` — ak ešte nemáš zdokumentovaný tím, roles a decision rights.

**Môžeš preskočiť ak:** Solo builder bez tímu - nikto nie je na onboarding.
