---
name: pm-personas
description: Generate Customer Segments, Personas, and Early Adopter Profile from raw VOC data (interview transcripts, synthetic interviews, survey data). Use in Phase 2 (Track D, Step 1) before running jtbd-building.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: personas, customer segments, early adopters, VOC, customer profile, user research, interviews
  role: specialist
  scope: research
  output-format: document
  related-skills: jtbd-building, pm-market-analysis, pm-problem-validation, design-thinking
---

# PM - Customer Segments & Personas

## What this skill does

Takes raw VOC (Voice of Customer) data - interview transcripts, synthetic interview outputs, survey results, behavioral observations - and produces:
1. Customer Segments (distinct groups with shared needs)
2. Personas (1-2 per key segment)
3. Early Adopters Profile

This is a "bring your data" skill. Claude synthesizes, structures, and formalizes patterns from the input. No invented personas without data.

Run this before `jtbd-building` - JTBD analysis uses personas as input.

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - target customer direction and geography
- `pm-market-analysis` - segment data provides foundation for persona development

**Produces artifacts used by:**
- `jtbd-building` - personas are the input context for JTBD analysis
- `pm-problem-validation` - personas + segments are Track D input
- `design-thinking` - personas feed the Define stage
- `pm-prd` - customer segments and personas are core PRD sections

---

## Step 0: Current state check

Check for existing artifacts:
- Customer Segments
- Personas
- Early Adopters Profile

Also check: does a Market Analysis exist? Cross-reference segments identified there vs. personas here. Does a JTBD Analysis exist? Check for consistency between jobs and persona pains.

Look for: personas with no direct quotes (invented, not research-based), segments without pain intensity ranking, early adopter profile without "where to find them" and "what triggers adoption", missing empathy map or as-is journey.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask the user all questions at once:

```
I need VOC data for Customer Segments + Personas.

1. PRODUCT
   What does the product do? For whom? (1-2 sentences)

2. DATA SOURCES (paste what you have available)
   Interview transcripts (direct / synthetic from SynthFolk/ChatGPT):
   [paste here]

   Survey data / responses:
   [paste here]

   Observations / field research:
   [paste here]

   Other insights (forums, reviews, support tickets...):
   [paste here]

3. CONTEXT
   How many interviews / respondents do you have in total?
   What types of people did you talk to? (role, industry, experience level...)
   What were the key questions / topics in the interviews?

4. HYPOTHESES
   What segments are you already suspecting? (if you have a preliminary view)
   Who do you think is the ideal early adopter and why?
```

---

## Step 2: Generate artifacts

Generate in English.

---

### ARTIFACT 1: Customer Segments

```markdown
# Customer Segments - [Product Name]

> **Phase:** 2 - Discovery (Track D: VOC - Customer Discovery)
> **Date:** [date]
> **Data basis:** [X interviews / Y survey responses / Z synthetic interviews]

---

## Segmentation Overview

[1-2 sentences: how we segmented - what primary dimension drove the segmentation (behavior, need, role, context)]

---

## Segment Map

| Segment | Size (est.) | Primary Need | Key Differentiator from Other Segments |
|---|---|---|---|
| [Segment 1 name] | [X% of TAM / X,000 users] | [core job to be done] | [what makes them distinct] |
| [Segment 2 name] | | | |
| [Segment 3 name] | | | |

---

## Segment Profiles

### Segment 1: [Name]

**Who they are:** [2-3 sentences - role, context, scale, typical situation]

**Primary goal:** [What they're trying to achieve]

**Current solution:** [How they solve the problem today]

**Key frustrations with current solution:**
- [Frustration 1]
- [Frustration 2]

**What they'd pay for:** [what value they recognize and would buy]

**Revenue potential:** [size x ARPU estimate]

**Strategic priority:** High / Medium / Low - [one-line reason]

---

### Segment 2: [Name]

[same structure]

---

### Segment 3: [Name]

[same structure]

---

## Segment Prioritization

| Segment | Market Size | Pain Intensity | Willingness to Pay | Accessibility | Priority |
|---|---|---|---|---|---|
| [Segment 1] | H/M/L | H/M/L | H/M/L | H/M/L | **1** |
| [Segment 2] | H/M/L | H/M/L | H/M/L | H/M/L | **2** |
| [Segment 3] | H/M/L | H/M/L | H/M/L | H/M/L | **3** |

**Primary segment for MVP:** [Segment X] - [brief reason]
```

---

### ARTIFACT 2: Personas

```markdown
# Personas - [Product Name]

> **Phase:** 2 - Discovery (Track D: VOC - Customer Discovery)
> **Date:** [date]
> **Note:** Personas are composites based on research data, not fictional characters.

---

## Persona 1: [Name] ([Segment])

**Role:** [Job title / context]
**Age range:** [X-Y]
**Context:** [Brief description - company size, geography, experience level]

### Goals

| Goal | Priority |
|---|---|
| [Primary goal - what they're trying to achieve] | High |
| [Secondary goal] | Med |
| [Tertiary goal] | Low |

### Pains

| Pain | Intensity | Current Workaround |
|---|---|---|
| [Primary pain] | High / Med / Low | [what they do today] |
| [Secondary pain] | | |
| [Third pain] | | |

### Behaviors & Habits

- [Relevant behavior 1: e.g., Manages everything via spreadsheets]
- [Relevant behavior 2]
- [Relevant behavior 3]

### Tools They Use Today

[List tools relevant to the problem space]

### Quotes (from research)

> "[Direct quote illustrating their main pain]"

> "[Direct quote illustrating what they want]"

### What Success Looks Like for Them

[1-2 sentences: what does their life look like when this problem is solved]

### Why They'd Adopt Our Product

[1-2 sentences: the trigger + the value that converts them]

### Why They Might Not

[Main objection / friction / risk from their perspective]

---

## Persona 2: [Name] ([Segment])

[Same structure]

---

## Persona Usage Guide

| Persona | Use for | Don't use for |
|---|---|---|
| [Persona 1] | [MVP feature prioritization, onboarding design] | [Enterprise sales scenarios] |
| [Persona 2] | | |
```

---

### ARTIFACT 3: Early Adopters Profile

```markdown
# Early Adopters Profile - [Product Name]

> **Phase:** 2 - Discovery (Track D: VOC - Customer Discovery)
> **Date:** [date]

---

## Definition

Early adopters are the first 10-50 customers. They are not average users - they are willing to use an imperfect product because the pain is intense enough.

---

## Early Adopter Profile

**Segment:** [Which segment they come from]
**Persona:** [Which persona best represents them, or custom description]

### Characteristics

| Characteristic | Description |
|---|---|
| Pain intensity | [Extremely high - they can't wait for a perfect solution] |
| Current situation | [e.g., Using 3-4 duct-taped tools, losing X hours/week] |
| Technical comfort | [High / Med - early adopters accept rough edges] |
| Decision speed | [Fast - can decide without lengthy procurement] |
| Feedback willingness | [High - actively want to shape the product] |
| Referral potential | [High - if they love it, they tell others in their network] |

### What Triggers Them to Try a New Solution

- [Trigger 1: e.g., Their current tool raised prices / shut down]
- [Trigger 2: e.g., They just hit a scaling wall]
- [Trigger 3: e.g., A peer recommended something new]

### What They Need from Us (Day 1)

**Must have:**
- [The single thing that makes it worth switching]
- [The table-stakes that can't be missing]

**Nice to have (but OK to lack at launch):**
- [Feature that matters but doesn't block adoption]

**What they'll tolerate:**
- [Rough edges they'll accept if core value is there]

### Where to Find Them

| Channel | Method | Est. Volume |
|---|---|---|
| [e.g., Slack communities] | [e.g., STR host communities in SK/CZ] | [X] |
| [e.g., LinkedIn] | [e.g., Search by title + geography] | [X] |
| [e.g., Referrals from interviewees] | [ask existing contacts] | [X] |

### Success Metric for Early Adopter Phase

**Target:** [X paying early adopters by [date]]
**Signal of success:** [e.g., Retention > 80% after 30 days, NPS > 8]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Customer Segments must cover:**
- [ ] Segmentation criteria defined (what dimension drove the split: behavior, need, role, context)
- [ ] Each segment: size estimate, primary need, key differentiator from other segments
- [ ] Pain intensity per segment compared (which segment hurts most)
- [ ] Revenue potential per segment estimated
- [ ] Primary segment for MVP selected with rationale
- [ ] For B2B SaaS: buyer vs. user distinction per segment (who signs, who uses)

**Personas must cover:**
- [ ] Goals: primary, secondary (what they're trying to achieve)
- [ ] Pains: with intensity and current workaround
- [ ] Behaviors and habits relevant to the problem space
- [ ] Tools they use today (integration expectations)
- [ ] Direct quotes from research (not invented)
- [ ] What success looks like for them (their definition)
- [ ] Why they would adopt / why they might not
- [ ] For SaaS/AI: technical sophistication level (affects onboarding design)
- [ ] For SaaS/AI: AI adoption readiness and trust level
- [ ] For B2B: procurement process and budget ownership (self-serve vs. sales-led)

**Empathy Map must cover (per key persona):**
- [ ] Says - direct quotes
- [ ] Thinks - internal thoughts, hopes, fears
- [ ] Does - observed behaviors
- [ ] Feels - emotional states
- [ ] Pains - frustrations, obstacles, risks
- [ ] Gains - wants, needs, success measures

**Current Journey (as-is) must cover:**
- [ ] Current process mapped step by step
- [ ] Biggest pain points in the current journey identified
- [ ] Emotional states at each stage captured
- [ ] Where customers lose time, money, or energy

**Early Adopters Profile must cover:**
- [ ] Characteristics that make them early adopters (pain intensity, tech comfort, decision speed)
- [ ] Triggers that would make them try a new solution
- [ ] Day 1 must-haves vs. what they'll tolerate
- [ ] Where to find them (specific channels, communities)
- [ ] Success metric for early adopter phase (target number, retention signal)

## Notion

Read `pureinn-variables.md` key "Customer Personas" → if URL present, remind user after saving:
`Personas saved locally. Update Notion: [Customer Personas URL]`

Read `pureinn-variables.md` key "Customer Interviews" → if DB URL present, check `state.json notion_ids.customer_interviews`. This DB can be used to log interview notes alongside persona generation. Remind user:
`Customer interviews can be logged to Notion DB: [Customer Interviews URL]`

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-2/customer-segments.md
pureinn-workspace/[project-slug]/artifacts/phase-2/personas.md
pureinn-workspace/[project-slug]/artifacts/phase-2/early-adopters-profile.md
```
