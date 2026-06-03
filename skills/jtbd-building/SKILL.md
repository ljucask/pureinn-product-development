---
name: jtbd-building
description: Generate a JTBD Analysis using Bob Moesta's Jobs-to-be-Done framework. Produces job stories, Forces Diagram, and switching logic. Run in Phase 2 (Track D) after pm-personas. Output feeds pm-problem-validation and design-thinking.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: JTBD, jobs to be done, forces diagram, switching logic, job stories, customer motivation
  role: specialist
  scope: analysis
  output-format: document
  related-skills: pm-personas, pm-problem-validation, design-thinking
---

# PM - JTBD Analysis

## What this skill does

Applies Jobs-to-be-Done theory to the validated customer research and personas to produce:
1. Job Stories - When / I want to / So I can formulations per key persona
2. Forces Diagram - what pushes away from the current solution and pulls toward a new one
3. Switching logic - what triggers the decision to change, and what blocks it

JTBD analysis goes deeper than persona pain points. It explains the causal mechanism behind why someone would switch - the forces operating on their decision. This is the input for design decisions in Phase 3 (Design Thinking).

Run this after `pm-personas`. Personas give you who - JTBD gives you why.

---

## Dependencies

**Required before running:**
- `pm-personas` - personas and their pains are the foundation for JTBD analysis

**Recommended before running:**
- Raw interview transcripts - JTBD is most powerful when grounded in actual interview data, not synthesized personas alone

**Produces artifacts used by:**
- `pm-problem-validation` - JTBD analysis is a Track D input (synthesized there)
- `design-thinking` - Forces Diagram informs the Define stage and HMW framing
- `pm-prd` - JTBD core is a required PRD section

---

## Step 0: Current state check

Check for existing artifacts:
- JTBD Analysis
- Forces Diagram

Also check: does a Personas document exist? JTBD without personas context will produce generic output. Do interview transcripts exist in context or referenced?

Look for: job stories that describe features rather than motivations ("I want to sync my calendar" is a feature request, not a job), Forces Diagram without evidence from actual interviews, push forces that are really just product features of the new solution, switching trigger not identified.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

First, ask:

Do you have interview data or research notes to work with?

  A) Yes - I have transcripts or notes that capture switching triggers and hesitations
  B) No - I'm working from my own knowledge and assumptions about this person

---

### Path A - Research data available

```
I need inputs for the JTBD Analysis.

1. PERSONAS (from pm-personas)
   Paste the personas or confirm they are in context.
   Which persona is the primary focus for JTBD analysis?
   [paste or "in context" + primary persona name]

2. INTERVIEW DATA
   Do you have interview transcripts or notes that capture:
   - Why people were unhappy with their current solution?
   - What triggered them to start looking for something new?
   - What made them hesitate before switching?
   - What they expected the new solution to do for them?
   [paste relevant excerpts, or describe what you heard]

3. CURRENT SOLUTION
   What does the primary persona use today to get this job done?
   (could be a competitor product, spreadsheet, manual process, nothing)
   What do they hate most about it?

4. SWITCHING TRIGGER
   Was there a specific moment or event that made them start looking?
   (e.g., "my property count crossed 5 and spreadsheets broke down",
    "my property manager quit", "I lost money on a double-booking")

5. HESITATIONS
   What makes them nervous about switching to something new?
   What do they fear losing or breaking?
```

---

### Path B - No research data (guided elicitation)

Guide the user through 3 rounds of questions to reconstruct the JTBD picture from founder knowledge. The goal is to surface the forces that drive switching behavior without formal interview data. Output will be marked as assumption-based.

**Group 1 of 3 - The person and the job**

Use AskUserQuestion tool for these two questions:

Which persona are we analyzing? (name from pm-personas, or describe briefly if personas don't exist yet)

How often does this job need to get done?

  A) Daily - it's a recurring operational task
  B) Weekly - regular but not daily
  C) Monthly or less - periodic, project-based
  D) Triggered by events - happens when something specific occurs

Then ask these as plain text:

What is the job they are trying to get done? Describe the outcome they want, not what your product does. What changes in their work or life when the job is done well?

After answers, confirm: "Is this the right person and job to analyze?"

---

**Group 2 of 3 - Current solution and pain**

Ask all as plain text:

What do they use today to get this job done? Name specific tools, processes, or workarounds - even if the answer is "nothing formal" or "they do it manually."

What frustrates them most about the current solution? What breaks, slows them down, or costs them the most?

Describe a specific moment or event that would push someone to start actively looking for a better solution. What needs to go wrong - or right - for them to say "I need to fix this now"?

What do they expect a new solution to deliver? What outcome would make them feel the switch was worth it?

After answers, confirm: "Does this match what you'd expect from this type of person?"

---

**Group 3 of 3 - Switching forces**

Use AskUserQuestion tool for these two questions:

What is their biggest anxiety about switching to something new?

  A) Risk of losing data or breaking current processes
  B) Learning curve and time investment to get up to speed
  C) Cost or budget approval required
  D) Fear that the new solution won't actually solve the problem

What keeps them stuck with the current solution even when they're unhappy?

  A) Habit - they know it, it works well enough, change feels risky
  B) Switching cost - migration effort, data locked in, integrations
  C) Social inertia - team uses it, hard to change alone
  D) No clear alternative - nothing obviously better exists

Then ask as plain text:

What would need to happen - or what would the new solution need to show - for them to overcome those hesitations and commit to switching?

After answers, show complete summary of all forces collected. Confirm before proceeding.

Note at the top of every generated artifact: `> Assumption-based - built from founder knowledge, not validated research. Treat as hypotheses to be tested.`

---

## Step 2: Generate artifact

Before generating, Claude must:
1. Identify the core functional, emotional, and social dimensions of the job
2. Check that push forces are about the current solution (not features of the new one)
3. Check that pull forces are about expected outcomes (not product features)
4. Identify the switching trigger - the specific moment that broke the status quo
5. Identify the anxiety - what makes switching feel risky

Generate in English.

---

### ARTIFACT: JTBD Analysis

```markdown
# JTBD Analysis - [Product Name]

> **Phase:** 2 - Discovery (Track D: VOC - Customer Discovery)
> **Date:** [date]
> **Primary persona:** [Persona name]
> **Data basis:** [X interviews / synthesized from personas / mixed]

---

## The Core Job

**When** [specific situation that creates the need],
**I want to** [motivation - what progress they want to make],
**So I can** [expected outcome - what success looks like for them].

**The job in plain language:**
[2-3 sentences: what is this person really trying to accomplish in their life or work? Not what feature they want - what progress are they trying to make?]

---

## Three Dimensions of the Job

| Dimension | The job | Why it matters |
|---|---|---|
| Functional | [What needs to get done - the task] | [Practical outcome] |
| Emotional | [How they want to feel while doing it] | [Internal state they're seeking] |
| Social | [How they want to be perceived by others] | [Identity or status outcome] |

---

## Forces Diagram

The four forces that operate on the switching decision:

```
                    TOWARD NEW SOLUTION
                           ↑
              PULL (attraction to new)
         ┌─────────────────────────────────┐
         │ [Expected benefit 1]            │
         │ [Expected benefit 2]            │
         │ [Expected benefit 3]            │
         └─────────────────────────────────┘
                           ↑
PUSH ──────────────── DECISION ──────────────── ANXIETY
(away from current)    POINT       (hesitation about new)
         │                               │
┌────────┴──────────┐         ┌──────────┴────────┐
│ [Pain 1 with      │         │ [Fear 1:           │
│  current solution]│         │  "What if..."]    │
│ [Pain 2]          │         │ [Fear 2]           │
│ [Pain 3]          │         │ [Switching cost]   │
└───────────────────┘         └───────────────────┘
                           ↓
              HABIT (inertia - staying with current)
         ┌─────────────────────────────────┐
         │ [Current habit 1]               │
         │ ["It works well enough"]        │
         │ [Effort to switch]              │
         └─────────────────────────────────┘
                    TOWARD STATUS QUO
```

---

## Forces Detail

### Push Forces (what drives them away from the current solution)

| Force | Description | Intensity | Evidence |
|---|---|---|---|
| [e.g., Calendar sync breaks] | [Managing 5+ properties manually causes double bookings] | High | [3 of 8 interviewees mentioned this] |
| [e.g., No financial overview] | [Tracking income across platforms requires manual export] | High | |
| [e.g., Guest communication scattered] | [Messages across Airbnb + WhatsApp + email] | Med | |

**Dominant push force:** [The single biggest frustration that most drives dissatisfaction with the status quo]

### Pull Forces (what attracts them to a new solution)

| Force | Description | What they imagine it will do |
|---|---|---|
| [e.g., Single dashboard] | [All properties, bookings, revenue in one place] | [Feel in control, professional] |
| [e.g., Automated messaging] | [Guest communication handled without manual effort] | [Save hours per week] |
| [e.g., Financial reporting] | [Monthly income without manual export] | [Stop worrying about tax season] |

**Dominant pull force:** [The benefit that most attracts them to switching]

### Anxiety Forces (what makes switching feel risky)

| Force | Description | Mitigation in our product |
|---|---|---|
| [e.g., "What if I miss a booking during migration?"] | [Fear of downtime during transition] | [Import existing bookings before going live] |
| [e.g., "What if it's complicated to set up?"] | [Fear of technical complexity] | [Onboarding flow, guided setup] |
| [e.g., "What if I pay and it doesn't work?"] | [Financial risk of subscription] | [Free trial, no card required] |

### Habit Forces (what keeps them doing what they do today)

| Force | Description | How to overcome |
|---|---|---|
| [e.g., Spreadsheet is "good enough"] | [Current state works, no crisis yet] | [Show cost of near-misses - double bookings, missed tax] |
| [e.g., Existing Airbnb routine] | [Established workflow, muscle memory] | [Replicate familiar patterns in new product] |
| [e.g., Learning curve fear] | [Investment to learn new tool] | [Familiar UX patterns, short time-to-value] |

---

## Switching Trigger

**The moment everything changed:**
[1-2 sentences: the specific event, threshold, or situation that broke the status quo and forced the person to start looking for a new solution. This is the "first thought" moment.]

**Examples of triggers in this market:**
- [Specific trigger 1 - with evidence from research]
- [Specific trigger 2]

**Design implication:** [What this means for acquisition strategy or onboarding - meet them at the trigger moment]

---

## Job Stories (per persona)

### [Primary Persona: Name]

**Job story:**
When [specific situation that creates the job],
I want to [motivation - progress to be made],
So I can [expected outcome].

**Secondary job stories:**

| Situation | Motivation | Expected outcome |
|---|---|---|
| [When I have a new booking inquiry] | [want to respond quickly without checking 3 apps] | [look professional and not lose the booking] |
| [When month ends] | [want to see total income across all properties] | [prepare accurate numbers for tax without manual work] |

---

## Key Insight for Product Design

**What the customer is really hiring our product for:**
[1-2 sentences: the core insight that should guide feature prioritization and product design. What is the deeper progress they want to make?]

**What this means for our MVP:**
[Implication: which features directly serve the dominant job, and which are secondary]

**What this means for our messaging:**
[How to talk about the product - what outcome to lead with, what fear to address]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Job Story must cover:**
- [ ] When / I want to / So I can formulation is correct (not a feature request)
- [ ] The job describes progress to be made, not a product feature
- [ ] Three dimensions addressed: functional, emotional, social
- [ ] Job story is grounded in research data, not invented

**Forces Diagram must cover:**
- [ ] Push forces are about the CURRENT solution (not features of the new one)
- [ ] Pull forces are about expected OUTCOMES (not product features)
- [ ] Anxiety forces include the specific fears heard in interviews
- [ ] Habit forces include the switching cost and inertia
- [ ] Dominant force identified per category
- [ ] Evidence cited for at least the top push and pull forces

**Switching analysis must cover:**
- [ ] Switching trigger identified (the specific moment that broke status quo)
- [ ] Design implication from the trigger stated

**For SaaS/AI products:**
- [ ] AI-specific anxiety addressed: "what if the AI makes mistakes?" / "do I trust it?"
- [ ] Data anxiety addressed: "what happens to my data?" / "who sees it?"
- [ ] Platform dependency anxiety: "what if the company shuts down?"

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/jtbd-analysis.md
```
