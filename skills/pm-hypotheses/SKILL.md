---
name: pm-hypotheses
description: Structure validation hypotheses, design low-cost experiments, track results, and produce a Go/No-Go decision. Runs progressively in Phase 3: first to define hypotheses and plan experiments, then to record results and issue the verdict. Based on a 5-stage SaaS validation framework.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: hypotheses, hypothesis validation, go no go, experiment plan, ICP, assumption map, validation results
  role: specialist
  scope: validation
  output-format: document
  related-skills: design-thinking, pm-personas, pm-problem-validation, pm-lean-canvas
---

# PM - Hypothesis Validation

## What this skill does

Turns raw assumptions into structured, testable hypotheses. Assigns the right experiment to each hypothesis. Tracks evidence as experiments run. Produces a Go/No-Go decision with pre-defined success metrics.

This skill runs in two modes:

- **Plan mode** (first run): structure hypotheses from design-thinking outputs, rank by risk, assign experiment types, define success criteria before any experiment runs
- **Results mode** (follow-up run): record experiment outcomes, update hypothesis status, issue Go / Pivot / Stop decision

Both modes use the same artifact - the Hypothesis Register - which is updated progressively.

---

## Why validate this way

Most startups fail not because of bad ideas but because they build solutions for problems that are not painful enough. Skipping structured validation means:

- Months of engineering for a product nobody buys
- No ability to distinguish signal from noise in early feedback
- Confirmation bias: founders hear what they want to hear

The goal of validation is not to get a yes or no. It is to learn. Every experiment is a clue that reduces uncertainty before capital and engineering time are committed.

---

## Validation stages

This skill covers the full 5-stage validation arc:

| Stage | Goal | Primary method |
|---|---|---|
| 1 - Hypothesis | Define riskiest assumptions about problem, customer, solution, market | Assumption map + hypothesis register |
| 2 - Qualitative | Understand pain points and context from real people | Customer discovery interviews (The Mom Test approach) |
| 3 - Quantitative | Measure real-world demand with low-cost experiments | Landing page, smoke test, pre-order, targeted ads |
| 4 - Lightweight MVP | Test value delivery with minimum build | Concierge MVP, Wizard of Oz, no-code prototype |
| 5 - Go/No-Go | Evidence-based decision: go, pivot, or stop | Success metric review, decision table |

Stage 2 (Qualitative) feeds from Phase 2 outputs - `pm-personas`, `jtbd-building`, `pm-problem-validation`. This skill does not re-run that work. It structures the insights into hypotheses and designs the remaining experiments.

---

## Dependencies

**Recommended before running:**
- `design-thinking` - outputs Validation Hypotheses draft, Value Proposition Canvas, HMW Questions
- `pm-personas` - ICP definition and pain intensity data
- `jtbd-building` - jobs and forces that inform what assumptions to test
- `pm-problem-validation` - Phase 2 evidence available as input

**Produces artifacts used by:**
- `pm-lean-canvas` - validated problem, customer, and solution feed into Lean Canvas inputs
- `pm-product-roadmap` - hypotheses and risks section (v1)
- `pm-prd` - validation evidence and Go/No-Go verdict are PRD inputs

---

## Step 0: Current state check

Check for an existing Hypothesis Register at `pureinn-workspace/[project-slug]/artifacts/phase-3/hypothesis-register.md`.

Show state table:

| Artifact | Status | Detail |
|---|---|---|
| Hypothesis Register | ✅ / ⚠️ / ❌ | [X hypotheses / X with experiments assigned / X with results] |
| design-thinking output | ✅ / ❌ | [available / not found - will need manual input] |
| Phase 2 evidence | ✅ / ⚠️ / ❌ | [interviews done / partial / missing] |

Apply the standard skill interaction pattern (CLAUDE.md).

**Options:**

```
What do you want to do in this session?
  A) Plan mode - structure hypotheses and design experiments (first run) (Recommended if register is empty)
  B) Results mode - record experiment outcomes and issue Go/No-Go verdict
  C) Add a new hypothesis to an existing register
  D) Review and update success criteria before experiments run
  E) Something specific: ...
```

---

## Step 1: Gather inputs

### Plan mode (Option A)

```
I need your current assumptions to structure the Hypothesis Register.

1. PRODUCT IDEA
   What does it do? For whom? (1-2 sentences)

2. PHASE 2 EVIDENCE (paste what exists)
   Key insights from customer interviews:
   [paste or summarize]

   Top pains identified (from JTBD / personas):
   [paste or summarize]

   Problem Validation Summary (if available):
   [paste]

3. DESIGN THINKING OUTPUTS (paste if available)
   Validation Hypotheses draft (from design-thinking skill):
   [paste]

   Value Proposition Canvas (core jobs, pains, gains):
   [paste or summarize]

4. YOUR RISKIEST ASSUMPTIONS
   What would have to be true for this business to work?
   What are you least confident about - problem, solution, customer, or market?
   [free text]

5. IDEAL CUSTOMER PROFILE
   Who specifically is this for? (role, company size, context, geography)
   Not "small businesses" - the specific person who feels the pain most acutely.
   [describe]
```

### Results mode (Option B)

```
I need the experiment results to update the register and issue a verdict.

For each completed experiment, provide:
  - Hypothesis ID (e.g., HYP-001)
  - Experiment type run
  - What you measured (metric, volume, time period)
  - Result (number or observation)
  - Pre-defined success criteria (from the register)
  - Did it pass? (Yes / No / Unclear)
  - Key quotes or evidence worth recording

Paste results below or describe what happened:
[free text]
```

---

## Step 2: Generate artifacts

Generate in English.

---

### Hypothesis types

| Type | What it tests | Example |
|---|---|---|
| Problem | Does the pain exist and is it severe enough to act on? | "Freelance designers consistently lose client feedback across 3+ tools and see this as a top 3 daily frustration" |
| Customer | Are the people we're targeting the right ICP, and can we reach them? | "Freelance designers with 3+ active clients are actively searching for consolidation tools and will engage with targeted outreach" |
| Solution | Does our proposed solution actually solve the problem in a way users value? | "A single inbox for Figma comments, email, and Slack messages reduces designer context-switching meaningfully" |
| Market | Is the market large enough and willing to pay? | "At least 10,000 freelance designers in our target geography would pay $29/month for this solution" |

---

### Experiment types

| Experiment | What it tests | Cost | Speed | Best for |
|---|---|---|---|---|
| Customer Interview | Problem severity, ICP validation, current workarounds | Low (time) | Medium | Problem + Customer hypotheses |
| Landing Page | Value prop appeal, demand signal, ICP reach | Low ($) | Fast | Problem + Market + Solution |
| Smoke Test / Fake Door | Feature demand, specific solution interest | Low ($) | Fast | Solution hypothesis |
| Targeted Ads | ICP reachability, value prop resonance, CAC estimate | Low-Medium ($100-300) | Fast | Market + Customer |
| Waitlist | Intent signal, ICP self-selection | Very low | Fast | Market hypothesis |
| Pre-order | Willingness to pay - strongest signal available | Low-Medium | Medium | Market + Solution |
| Concierge MVP | Full value delivery manually - learn and earn simultaneously | Medium (time) | Slow | Solution + Market |
| Wizard of Oz MVP | Simulate automation manually - test behavior without build | Medium | Medium | Solution hypothesis |
| No-code Prototype | Interactive test of core user flow | Medium | Medium | Solution + UX |
| Survey | Breadth of pattern confirmation after qualitative phase | Low | Fast | Customer + Market |

**Decision rule for experiment selection:**
- Problem hypothesis → Customer Interview first. If insufficient evidence: Survey.
- Customer hypothesis → Targeted Ads + Landing Page. Measure: conversion rate, cost per sign-up.
- Solution hypothesis → Smoke Test (fake door click rate) or Concierge MVP (payment + retention).
- Market hypothesis → Pre-order or Waitlist. Only strong signal: credit card pulled or explicit commitment.

**What counts as commitment (in order of strength):**
1. Credit card / pre-payment - strongest
2. Letter of intent (B2B) or signed pilot agreement
3. Email sign-up from targeted ICP (not friends)
4. Click-through from paid traffic (shows intent, not commitment)
5. Verbal agreement - weakest, do not count as validation

---

### ARTIFACT 1: Hypothesis Register

```markdown
# Hypothesis Register - [Product Name]

> **Phase:** 3 - Define & Validation
> **Last updated:** [date]
> **Status:** [X hypotheses / X validated / X rejected / X in progress]

---

## ICP Definition

> The Ideal Customer Profile is the razor-sharp definition of who we are validating with.
> "Small businesses" is not an ICP. Define role, context, company size, and specific pain context.

**ICP:** [Role] at [company type/size] who [specific situation/context] and [specific pain/trigger].

**Example:** "Freelance UX/UI designers with 3+ active client projects who manage feedback via email and Figma comments and spend 1+ hour/day chasing scattered input."

---

## Assumption Map

Before hypotheses: the core beliefs that must be true for this business to work.

| Assumption | Type | Riskiest? | Why |
|---|---|---|---|
| [Belief 1] | Problem / Customer / Solution / Market | Yes / No | [What breaks if this is wrong] |
| [Belief 2] | | | |
| [Belief 3] | | | |

**Most dangerous assumption:** [The one that, if false, makes everything else pointless. Test this first.]

---

## Hypothesis Register

| ID | Type | Hypothesis | Riskiest | Experiment | Success Criteria | Status | Result | Decision |
|---|---|---|---|---|---|---|---|---|
| HYP-001 | Problem | We believe [specific pain] exists for [ICP] at [frequency/intensity] | Yes / No | [Experiment type] | [Pre-defined measurable target] | Not started / Running / Complete | [Evidence] | Confirmed / Rejected / Unclear |
| HYP-002 | Customer | | | | | | | |
| HYP-003 | Solution | | | | | | | |
| HYP-004 | Market | | | | | | | |

---

## Experiment Plans

### [HYP-001] - [Short hypothesis name]

**Experiment type:** [Customer Interview / Landing Page / Pre-order / ...]
**What we're testing:** [The specific belief being tested - one sentence]
**Method:** [How: target channel, message, call to action, budget if applicable]
**ICP targeting:** [Who specifically, where to find them]
**Duration:** [X days / X interviews]
**Budget:** [€X or time only]

**Success criteria (defined before running):**
- Quantitative: [e.g., ≥5% landing page conversion from targeted traffic]
- Qualitative: [e.g., ≥7/10 interviewees confirm pain without prompting]
- Financial: [e.g., ≥10 pre-orders at €29 within 30 days]

**Signals to watch for:**
- Positive: [e.g., unprompted workaround descriptions, immediate follow-up interest]
- Negative: [e.g., polite agreement but no sign-up, "I'd use it if it were free"]

**Interview approach (if applicable):**
Do not pitch. Ask about past behavior and specific experiences, not hypothetical reactions to your solution.
- "Walk me through the last time you had to deal with [the specific problem]."
- "What was the most frustrating part of that?"
- "Have you tried to solve this before? What happened?"
- "What do you do now when you don't have a solution for this?"

---

### [HYP-002] - [Short hypothesis name]

[same structure]
```

---

### ARTIFACT 2: Go/No-Go Decision

Generate after results are in. Do not generate in Plan mode.

```markdown
# Validation Go/No-Go - [Product Name]

> **Date:** [date]
> **Phase:** 3 - Define & Validation exit
> **Hypotheses tested:** [X total / X confirmed / X rejected / X unclear]

---

## Evidence Summary

| Hypothesis | Type | Result | Pre-defined criteria met? |
|---|---|---|---|
| HYP-001 | Problem | [1-sentence result] | Yes / No / Partial |
| HYP-002 | Customer | | |
| HYP-003 | Solution | | |
| HYP-004 | Market | | |

**Strongest signal:** [The most compelling evidence collected - quote or number]
**Weakest signal:** [Where evidence was thin or mixed]

---

## Decision

**Verdict: GO / PIVOT / STOP**

---

### GO - confirmed signals across problem, customer, and market

All three of the following must be true:
- Problem hypothesis confirmed: ICP describes the pain without prompting, rates it high-priority
- Customer hypothesis confirmed: ICP exists, is reachable, engages with targeted outreach
- Market hypothesis confirmed: meaningful commitment signal (pre-order, letter of intent, or waitlist conversion ≥5% from targeted ICP traffic)

→ Proceed to Phase 4 (Domain Modeling). Solution hypothesis can remain partially open - it gets tested further in the MVP phase.

---

### PIVOT - mixed signals, clear direction to change

Something specific is not working but the evidence points at what to change:
- Problem hypothesis confirmed but ICP was wrong → redefine target segment, re-run Customer + Market tests
- ICP confirmed but problem is different than assumed → reframe solution, run new Solution hypothesis
- Strong problem + customer signal but no willingness to pay → reprice, reframe value prop, or reassess market

**What changes:** [Specific assumption being revised]
**New experiment:** [What runs next and with what success criteria]

---

### STOP - weak or absent signals across critical hypotheses

One of the following is true:
- Problem hypothesis not confirmed after 10+ ICP interviews: pain is not severe enough to act on
- Market hypothesis failed: no meaningful commitment signal after quantitative test with adequate ICP traffic
- Willingness to pay not demonstrated after pre-order or concierge MVP test

This is not failure. It is a successful experiment that prevented years of wasted effort. Negative validation data has real value - it redirects attention to a problem worth solving.

**Key learnings:** [What was discovered that can inform the next idea]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps. Use in Step 2 to verify output before finalizing. -->

**Hypothesis Register (Plan mode) must cover:**
- [ ] ICP defined with specificity: role, context, company size, pain trigger (not "small businesses")
- [ ] Assumption map complete: at least one hypothesis per type (Problem / Customer / Solution / Market)
- [ ] Riskiest assumption identified and marked - the one that, if false, invalidates everything else
- [ ] Every hypothesis has a pre-defined success criterion (quantitative OR qualitative + financial) set BEFORE the experiment runs
- [ ] Experiment type matches hypothesis type (see decision rule above)
- [ ] Interview questions follow The Mom Test principle: past behavior, not hypothetical future

**Go/No-Go (Results mode) must cover:**
- [ ] Every hypothesis has a result recorded (even "no data" is a result)
- [ ] Verdict is one of three: GO / PIVOT / STOP - not "promising" or "needs more time"
- [ ] If PIVOT: specific assumption named and new experiment defined
- [ ] If STOP: learnings recorded (what was discovered, not just what failed)
- [ ] Evidence includes at least one concrete signal (a number, a quote, or a payment)

## Notion

Read `pureinn-variables.md` key "Hypothesis Validation" → if URL present, remind user after saving:
`Hypothesis Register saved locally. Update Notion: [Hypothesis Validation URL]`

Read `pureinn-variables.md` key "Open Questions" → if DB URL present, check `state.json notion_ids.open_questions`. Open questions and decisions from the hypothesis process can be pushed as entries to this DB. Remind user:
`Open questions can be logged to Notion DB: [Open Questions URL]`

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3/hypothesis-register.md
pureinn-workspace/[project-slug]/artifacts/phase-3/go-no-go.md
```
