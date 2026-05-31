---
name: design-thinking
description: Synthesize Phase 2 discovery outputs through Design Thinking (Define + Ideate stages). Produces Problem Statement, POV, HMW questions, and Ideation synthesis. Run in Phase 3 as the first step before business model work. Takes Phase 2 outputs as input - no new research.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: design thinking, HMW questions, problem statement, POV, ideation, elevator pitch, validation hypotheses
  role: specialist
  scope: synthesis
  output-format: document
  related-skills: pm-personas, jtbd-building, pm-problem-validation, pm-hypotheses, pm-kotler
---

# PM - Design Thinking (Define + Ideate)

## What this skill does

Applies the Define and Ideate stages of Design Thinking to Phase 2 research outputs. In the context of this framework, Empathize is already done (Phase 2 discovery). This skill picks up at Define.

Produces:
1. Problem Statement - precise articulation of the validated problem
2. Point of View (POV) - user + need + insight framing
3. How Might We (HMW) questions - opportunity reframing
4. Ideation synthesis - promising solution directions from structured brainstorming

This skill runs once in Phase 3. It is the bridge between discovery (what we learned about the problem) and strategy (what we will build and how).

Output informs the Business Model Canvas, PRD framing, and product vision.

---

## Dependencies

**Required before running:**
- `pm-problem-validation` - the Problem Validation Summary is the primary input
- `pm-personas` - persona and JTBD context frames the POV

**Recommended before running:**
- `jtbd-building` - Forces Diagram provides the HMW framing material
- `pm-market-analysis` - competitive whitespace informs ideation

**Produces artifacts used by:**
- `pm-business-model` - solution direction from ideation informs value proposition choices
- `pm-prd` - Problem Statement and POV are core PRD sections
- `pm-product-roadmap` - product vision emerges from ideation synthesis

---

## Step 0: Current state check

Check for existing artifacts:
- Design Thinking synthesis (Define + Ideate output)
- Problem Statement
- POV Statement
- HMW Questions
- Ideation synthesis

Also check: does a Problem Validation Summary exist? Does a JTBD Analysis exist? These are required inputs. Without them, the Define stage will be built on unvalidated assumptions.

Look for: POV that describes features rather than user needs, HMW questions that are too broad ("HMW improve the experience") or too narrow ("HMW add a sync button"), ideation that jumped to solutions before framing, problem statement that describes symptoms rather than root cause.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

First, ask:

Do you have Phase 2 research outputs to work with?

  A) Yes - I have Problem Validation Summary and/or Personas + JTBD to paste or confirm in context
  B) No - I have not run formal Phase 2 research, guide me through what I know

---

### Path A - Phase 2 artifacts available

```
I need inputs for the Design Thinking synthesis.

1. PROBLEM VALIDATION SUMMARY
   Paste or confirm it's in context. I'll use:
   - The top validated pains
   - The primary customer
   - Evidence basis
   [paste or "in context"]

2. PERSONAS + JTBD
   Paste or confirm in context. I'll use:
   - Primary persona profile
   - Job story (When / I want to / So I can)
   - Dominant push and pull forces
   [paste or "in context"]

3. YOUR CURRENT THINKING
   What do you believe the core problem is? (your hypothesis)
   What solutions or directions are you already considering?
   What feels most exciting or most uncertain to you right now?

4. CONSTRAINTS ON SOLUTIONS
   Any hard constraints on what we can build?
   (e.g., no native mobile app in MVP, must integrate with Airbnb, budget limits,
    regulatory constraints, team skill constraints)
```

---

### Path B - No Phase 2 research (guided elicitation)

No Phase 2 artifacts exist. Guide the user through 3 rounds to build the input picture from founder knowledge. The goal is to extract enough to run a meaningful Define + Ideate synthesis. Output marked as assumption-based.

**Group 1 of 3 - The person and their world**

Ask all as plain text:

Who is the primary person this product is for? Describe them concretely - role, context, a typical day. Be specific enough to picture a real human, not a demographic.

What is the most important job they are trying to get done - the outcome they want, not the feature? Finish this sentence: "When [situation], they want to [motivation] so they can [outcome]."

What frustrates them most about how they handle this today? What breaks, slows them down, or costs them the most?

After answers, confirm: "Is this the person we're designing for? Anything to sharpen?"

---

**Group 2 of 3 - Evidence and solution space**

Ask these two questions together:

How solid is your evidence that this problem is real and this is the right person?

  A) Strong - I have spoken directly with people matching this profile
  B) Medium - indirect evidence (forums, observation, secondhand accounts)
  C) Domain expertise - I know this world well but haven't formally validated
  D) Assumption only - no external evidence yet

Are you already thinking about specific solution directions?

  A) Yes - I have a clear hypothesis about what to build
  B) Partially - some directions but nothing concrete
  C) No - completely open, need the ideation process
  D) Yes but I want to challenge my assumptions before committing

Then ask as plain text:

What are the 2-3 most painful moments in this person's experience with the current solution? Be specific - describe situations, not generalizations.

After answers, confirm and proceed.

---

**Group 3 of 3 - Solution constraints and direction**

Ask all as plain text:

What solutions or directions are you already considering? List them - even rough ideas are useful input for ideation.

What hard constraints exist on what you can build? (e.g., no native mobile app in MVP, must integrate with a specific system, budget limits, team skill gaps, regulatory constraints)

What feels most uncertain or risky about the solution space right now? What would you most need to get right?

After answers, show complete summary. Note explicitly which insights are validated vs. assumed before proceeding to Define stage.

Note at the top of every generated artifact: `> Assumption-based - no formal Phase 2 research conducted. Problem Statement and POV reflect founder hypotheses. HMW questions and ideation directions should be treated as starting points for validation, not confirmed insights.`

---

## Step 2: Generate artifacts

Structure: Define first (Problem Statement → POV → HMW), then Ideate (solution directions).

Generate in English.

---

### ARTIFACT: Design Thinking Synthesis

```markdown
# Design Thinking Synthesis - [Product Name]

> **Phase:** 3 - Define & Validation
> **Date:** [date]
> **Stages covered:** Define + Ideate (Empathize = Phase 2 discovery)
> **Input:** Problem Validation Summary, Personas, JTBD Analysis

---

## DEFINE STAGE

### Problem Statement

[2-3 sentences: The precise problem we are solving. Specific, not generic.
Grounded in evidence from Phase 2. Describes the root cause, not just symptoms.]

**Problem statement:** [Clear, specific, evidence-backed statement]

**What makes this problem worth solving:**
- Pain intensity: [High / Medium / Low - from Problem Validation Summary]
- Frequency: [How often does this problem occur for the primary customer]
- Current alternatives: [Why existing solutions fail to solve it]
- Economic impact: [What it costs the customer - time, money, stress]

---

### Point of View (POV)

The POV frames the problem from the perspective of the primary user.

**Format:** [User] needs to [need - verb phrase] because [insight - non-obvious finding].

**POV Statement:**

> [Primary persona role] needs to [specific need - what they must be able to do]
> because [insight - the non-obvious reason why this matters to them, from JTBD research].

**Deconstructed:**

| Element | Content |
|---|---|
| User | [Specific persona - role, context] |
| Need | [The job to be done - not a feature, an action] |
| Insight | [The non-obvious finding from research that explains the need] |

**Why this POV:** [1 sentence: why this framing captures the most important design challenge]

---

### How Might We (HMW) Questions

HMW questions transform the POV and validated pains into opportunity spaces for ideation.
Each HMW opens a direction, not a solution.

**Source pains → HMW reframes:**

| Validated pain | HMW question |
|---|---|
| [Pain from Problem Validation Summary] | HMW [opportunity reframe]? |
| [Pain 2] | HMW [opportunity reframe]? |
| [Pain 3] | HMW [opportunity reframe]? |

**Additional HMW lenses:**

| Lens | HMW question |
|---|---|
| Amplify what's working | HMW do more of [what customers already value in current solutions]? |
| Remove the pain | HMW eliminate [the dominant push force] entirely? |
| Flip the assumption | HMW if [core assumption about the problem] wasn't true? |
| Change who does it | HMW shift [manual effort] to [system / other actor]? |
| Reduce anxiety | HMW make [switching trigger] feel safe and reversible? |

**Priority HMW (to ideate on):**

1. [HMW question 1 - most promising direction]
2. [HMW question 2]
3. [HMW question 3]

**Selection rationale:** [Why these 3 HMW questions are the most important to explore]

---

## IDEATE STAGE

Ideation explores solution directions for the priority HMW questions. Output is directions and concepts, not final features.

### Ideation Results

**Priority HMW being explored:** [The selected HMW question]

**Ideas generated (clustered by theme):**

#### Theme 1: [Name - e.g., "Unification"]
[Ideas that converge on this approach]
- [Idea 1]
- [Idea 2]
- [Idea 3]
**Core hypothesis:** [If we did this, what would change for the user?]

#### Theme 2: [Name - e.g., "Automation"]
- [Idea 1]
- [Idea 2]
**Core hypothesis:** [If we did this, what would change for the user?]

#### Theme 3: [Name - e.g., "Insight / Intelligence"]
- [Idea 1]
- [Idea 2]
**Core hypothesis:** [If we did this, what would change for the user?]

---

### Promising Directions

After ideation, these are the solution directions that best address the validated problem and the priority HMW:

| Direction | Core concept | Why promising | Risks / constraints |
|---|---|---|---|
| [Direction 1] | [What it is in 1 sentence] | [What validated pain it eliminates, what pull force it activates] | [Key risk or constraint] |
| [Direction 2] | | | |
| [Direction 3] | | | |

**Recommended direction to pursue:**
[Which direction and why - this informs the Business Model Canvas and PRD]

---

### What We Are Not Doing

Ideas that came up in ideation but are explicitly ruled out:

| Idea | Why ruled out |
|---|---|
| [Idea that seemed good but doesn't fit] | [Reason: outside constraints, wrong timing, unvalidated demand, etc.] |

---

## Define → Strategy Bridge

How this Define + Ideate output connects to what comes next:

| Design Thinking output | Used by |
|---|---|
| Problem Statement | PRD Section 1, Business Case rationale |
| POV | PRD Section 3 (Value Proposition framing) |
| HMW questions | Product Roadmap - what each phase must answer |
| Recommended direction | Business Model Canvas - Value Proposition |

**Open questions for Phase 3 strategy work:**
1. [Question the Design Thinking stage couldn't answer - needs business model / financial analysis]
2. [Question 2]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Problem Statement must cover:**
- [ ] Specific (not generic - "users struggle with productivity" is not specific)
- [ ] Evidence-backed (references validated pains from Problem Validation Summary)
- [ ] Root cause, not symptoms
- [ ] Quantified where possible (frequency, intensity, cost)

**POV Statement must cover:**
- [ ] User is a specific persona (not "users")
- [ ] Need is an action/verb, not a feature request
- [ ] Insight is non-obvious (not just restating the pain)
- [ ] Full sentence: [User] needs to [need] because [insight]

**HMW Questions must cover:**
- [ ] Each HMW maps to a validated pain from Problem Validation Summary
- [ ] HMW questions are not too broad (not "HMW improve the product")
- [ ] HMW questions are not too narrow (not "HMW add a button to sync calendars")
- [ ] Multiple lenses used (amplify good, remove bad, flip assumption, automation)
- [ ] Priority HMW selected with rationale

**Ideation must cover:**
- [ ] Ideas clustered by theme (not just a flat list)
- [ ] Each theme has a core hypothesis
- [ ] Promising directions evaluated against: validated pain fit, feasibility, constraints
- [ ] Recommended direction stated with rationale
- [ ] What we are not doing is explicit

**For SaaS/AI products:**
- [ ] AI as solution direction evaluated: where does AI create the most leverage?
- [ ] AI ideation includes non-AI fallback: what is the manual/simple version if AI isn't ready?
- [ ] Trust and transparency HMW considered: HMW make the AI output trustworthy?
- [ ] Automation direction evaluated: what can be automated vs. what needs human judgment?

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3/design-thinking-synthesis.md
```
