---
name: pm-stripe
description: Delivery Stripe orchestration. Kicks off a new Stripe by confirming which Feature Sets are in scope and whether spec is ready. Then acts as a routing hub - user brings a specific feature from Notion, Claude runs the right skill for it. Notion is the source of truth for feature status and backlog; this skill manages workflow context and spec gates.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: delivery stripe, stripe kickoff, stripe close, FDD cycle, sprint orchestration, Phase 6 7
  role: orchestrator
  scope: delivery
  output-format: document
  related-skills: pm-feature-set-overview, pm-brd, pm-fsd, pm-mvp-scope
---

# PM - Delivery Stripe

## What this skill does

Manages the active Delivery Stripe as a routing and coordination layer.

**Division of responsibility:**
- **Notion** - source of truth for feature backlog, status, and assignment. The user assigns features to Stripes in Notion and picks what to work on next.
- **Claude (this skill)** - tracks which Feature Sets are in the current Stripe and whether their specs are complete. Routes the user to the right skills when they bring a feature to work on.

A Stripe in this workflow has two modes:
1. **Kickoff** - confirm scope (which FSs), confirm spec readiness per FS, establish the Stripe goal
2. **Active** - user says "I want to work on [feature from Notion]" → Claude routes to the right skill and generates the artifact

This skill does NOT replace Notion for backlog tracking. It does NOT track individual feature status - Notion does that. It ensures the spec gate is enforced and the user gets to the right skill quickly.

---

## Dependencies

**Required before running:**
- `pm-mvp-scope` - Delivery Stripes and Feature Sets must already be defined
- Notion backlog set up with features assigned to this Stripe

**Spec gate (must be complete before build starts for a Feature Set):**
- `pm-feature-set-overview` - Feature Set overview written
- `pm-brd` - BRD complete for this FS
- `pm-fsd` - FSD complete for this FS
- `pm-feature-card` - Feature Cards written for features in this Stripe

**Produces:**
- Stripe plan written to state.json
- Spec status per FS tracked in state.json
- Artifact files saved per skill invocation (in phase-6/ and phase-7/)

---

## Step 0: Current state check

Read `pureinn-workspace/[slug]/state.json`. Check `current_stripe` and `delivery_stripes`.

| Item | Status | Detail |
|---|---|---|
| Active Stripe | ✅ Active / 🔲 None | [stripe name or "not started"] |
| Feature Sets in Stripe | [list] | [spec status per FS] |
| Spec gate | ✅ / ⚠️ / ❌ | [which FSs are spec-complete] |

**Verdict:** [one sentence - what phase the Stripe is in and what to do next]

```
What do you want to do?
  A) Kick off a new Stripe - define scope, confirm spec readiness
  B) Work on a specific feature - bring a feature from Notion
  C) Check spec status for a Feature Set
  D) Close this Stripe - mark complete, note what shipped
```

If no Stripe is active: go to Step 1A (Kickoff).
If Stripe is active and user brings a feature: go to Step 1B (Feature routing).

---

## Step 1A: Stripe Kickoff

```
Kicking off Delivery Stripe [N]

1. STRIPE GOAL
   What is the single outcome this Stripe delivers?
   (e.g., "Users can register, log in, and manage their account")

2. FEATURE SETS IN THIS STRIPE
   Which Feature Sets are included?
   List FS IDs and names.
   (These should match what you've set up in Notion.)

3. SPEC STATUS PER FEATURE SET
   For each FS, is spec complete?
   - Feature Set Overview: done / in progress / not started
   - BRD: done / in progress / not started
   - FSD: done / in progress / not started
   - Feature Cards: done / in progress / not started

   Any FS without complete spec cannot have its features built yet.
   Spec work happens first within the Stripe.

4. NOTION MASTER FEATURE SET
   What is the top-level grouping in Notion for this Stripe's features?
   (e.g., "Core Platform", "Authentication & Access")
   Used for aligning outputs to your Notion hierarchy.

5. STRIPE TIMELINE
   Week dates or sprint number for reference.
```

---

## Step 2A: Stripe Kickoff Output

```markdown
# Stripe [N] - [Name]

**Goal:** [single sentence outcome]
**Timeline:** [weeks/sprint]
**Status:** Active

---

## Feature Sets in This Stripe

| FS ID | Feature Set | Overview | BRD | FSD | Cards | Can build? |
|---|---|---|---|---|---|---|
| FS-[ID] | [Name] | ✅ | ✅ | ✅ | ✅ | ✅ Yes |
| FS-[ID] | [Name] | ✅ | ✅ | ⚠️ partial | ❌ | ❌ Spec first |

**Notion Master Feature Set:** [name]

---

## Spec Work Queue (if any FS is not spec-complete)

For FS-[ID] [name] - run in order:
  1. /pm-fsd FS-[ID]          → complete FSD
  2. /pm-feature-card [F-ID]  → generate Feature Cards (one per feature)

---

## Build Gate

Build starts only when for the Feature Set:
- [ ] BRD complete
- [ ] FSD complete
- [ ] Feature Card exists for the specific feature
```

Write stripe to state.json.

---

## Step 1B: Feature Routing

User brings a feature from Notion. They say something like:
- "I want to work on F-001 Register user account"
- "Let's write the spec for the Auth Feature Set"
- "Ready to build the login feature"

**Claude's job:** identify what stage the feature is in and route to the right skill.

Ask if not clear from context:
```
What do you want to do with [feature/FS name]?
  A) Write or complete the spec (BRD / FSD / Feature Card)
  B) Design work - UX brief or wireframe
  C) Build - backend, frontend, or both
  D) Quality and ship - tests, code review, or deploy
```

---

## Step 2B: Routing Output

Route to the appropriate skill based on intent. Show:

```
For [Feature / Feature Set]: [action]

Spec gate check:
  Overview  [✅ / ❌]
  BRD       [✅ / ❌]
  FSD       [✅ / ❌]
  Card      [✅ / ❌ for F-[ID]]

[If spec gate not met for build:]
⚠️  Cannot build yet - [artifact] is incomplete.
    Run /[skill] first.

[If spec gate met or intent is spec work:]
→ Run: /[skill-name]

Input to prepare:
  - [what to bring to that skill]
```

**Routing table:**

| Intent | Spec gate required? | Skill to run |
|---|---|---|
| Write Feature Set overview | No | `/pm-feature-set-overview` |
| Write BRD for this FS | No | `/pm-brd` |
| Write FSD for this FS | BRD done | `/pm-fsd` |
| Write business rule | BRD in progress | `/pm-business-rule-critical` / `core` / `governance` |
| Write Feature Card | FSD done | `/pm-feature-card` |
| Shape UX brief | Feature Card done | `/impeccable-shape` |
| Build backend | All spec done | `/fullstack-guardian` |
| Build frontend | All spec done | `/impeccable-craft` |
| Write tests | Feature built | `/test-master` + `/playwright-expert` |
| Review code | Tests passing | `/code-reviewer` + `/impeccable-audit` |
| Security review | Code reviewed | `/impeccable-harden` + `/security-reviewer` |
| Deploy | All above done | `/devops-engineer` |

After routing: update spec status in state.json if spec artifact was just completed.

---

## Step 1C: Close a Stripe

```
Closing Stripe [N] - [Name]

1. WHAT SHIPPED
   Which features from Notion were completed and deployed?

2. WHAT DID NOT SHIP
   Which features were planned but not completed?
   Will they carry into Stripe [N+1]?

3. RETRO (quick)
   - What slowed us down?
   - What worked well?
   - One change for Stripe [N+1]?
```

---

## Step 2C: Close Output

```markdown
# Stripe [N] Close - [Name]

**Closed:** [date]

## Summary
Shipped: [N] features
Not shipped: [N] features (carrying to Stripe [N+1])

## Retro
Slowed us: [answer]
Worked well: [answer]
Change next Stripe: [answer]

## Carryover to Stripe [N+1]
[List features carrying over - update in Notion]
```

Mark Stripe as `complete` in state.json. Move carryover features' target stripe in state.json if tracked.

```
Next step: Plan Stripe [N+1].
Run /pm-stripe to kick it off.
```

---

## state.json fields written by this skill

```json
"current_stripe": "stripe-1",
"delivery_stripes": [
  {
    "id": "stripe-1",
    "name": "Stripe 1 - Core Authentication",
    "goal": "Users can register, log in, and manage their account",
    "timeline": "Week 1-2",
    "status": "planning | active | complete",
    "notion_master_feature_set": "Core Platform",
    "feature_sets_in_stripe": ["FS-01", "FS-02"]
  }
],
"feature_sets": [
  {
    "id": "FS-01",
    "name": "User Authentication",
    "stripe": "stripe-1",
    "notion_master_feature_set": "Core Platform",
    "spec": {
      "overview": "done | in_progress | pending",
      "brd": "done | in_progress | pending",
      "fsd": "done | in_progress | pending",
      "cards": "done | in_progress | pending"
    }
  }
]
```

Note: individual feature status is tracked in Notion, not state.json.

---

## Notion alignment

When a Feature Card is generated by `/pm-feature-card`, output includes:

```
NOTION PAGE PROPERTIES (copy to Notion)
  Name:             [Feature name]
  Feature Set:      [FS name]
  Master FS:        [Master Feature Set name]
  Status:           In Spec / Ready for Dev / In Dev (set manually)
  Stripe:           Stripe [N]
  Priority:         [from KANO / MVP Scope]
  Acceptance:       [link to FSD section or paste key Given/When/Then]
```

The user creates/updates the Notion page using this output. Claude does not write to Notion directly - Notion is the user's operational workspace.

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user -->

**Stripe kickoff:**
- [ ] Goal is a single testable outcome, not a list
- [ ] Every FS has explicit spec status (per artifact)
- [ ] Build-blocked FSs are identified with what's missing
- [ ] Notion Master Feature Set is named

**Feature routing:**
- [ ] Spec gate is always checked before routing to build skills
- [ ] Route is specific (named skill, not "work on it")
- [ ] Input needed is listed so user knows what to prepare

**FDD discipline:**
- [ ] Build never starts without BRD + FSD + Feature Card complete
- [ ] "Done" = deployed, not code-complete

## Save to

Stripe plan:
```
pureinn-workspace/[project-slug]/artifacts/phase-6/stripe-[N]-plan.md
```

Stripe close:
```
pureinn-workspace/[project-slug]/artifacts/phase-7/stripe-[N]-close.md
```

State updates → `pureinn-workspace/[project-slug]/state.json`
