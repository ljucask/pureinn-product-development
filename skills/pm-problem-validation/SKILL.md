---
name: pm-problem-validation
description: Generate a Problem Validation Summary by synthesizing all Phase 2 research outputs (Tech Feasibility, Domain Analysis, Market Analysis, Personas, JTBD). Use at end of Phase 2 as convergence artifact. No new research - pure synthesis.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: problem validation, validation summary, Phase 2 exit, discovery synthesis, problem confirmed
  role: specialist
  scope: validation
  output-format: document
  related-skills: pm-personas, jtbd-building, pm-market-analysis, pm-tech-feasibility, pm-domain-analysis
---

# PM - Problem Validation Summary

## What this skill does

Synthesizes all Phase 2 Track outputs into one convergence document:
- Track A: Tech Feasibility Report
- Track B: Domain Analysis + Legal Requirements
- Track C: Market Analysis (TAM/SAM/SOM, Competitor Analysis, SWOT, Market Timing)
- Track D: Personas + JTBD Analysis

This is the Phase 2 exit artifact. Its output becomes the primary input to Phase 3 (Design Thinking - Define stage).

No new research. Claude reads all inputs and synthesizes patterns, validates consistency, and surfaces contradictions.

---

## Dependencies

**Strongly recommended before running (this skill synthesizes all of them):**
- `pm-tech-feasibility` - Track A
- `pm-domain-analysis` - Track B
- `pm-market-analysis` - Track C
- `pm-personas` - Track D (Step 1)
- `jtbd-building` - Track D (Step 2)

**Produces artifacts used by:**
- `pm-prd` - Problem Validation Summary is a primary PRD input
- `design-thinking` - feeds the Define stage (problem statement, POV)
- `pm-product-roadmap` - problem and market context for roadmap framing

---

## Step 0: Current state check

Check for existing artifacts:
- Problem Validation Summary

Then check which Track inputs are available:

| Track | Artifact | Status |
|---|---|---|
| A - Tech | Tech Feasibility Report | ✅ / ⚠️ / ❌ |
| B - Domain | Domain Analysis + Legal Requirements | ✅ / ⚠️ / ❌ |
| C - Market | Market Analysis (all 4 artifacts) | ✅ / ⚠️ / ❌ |
| D - VOC | Personas + JTBD Analysis | ✅ / ⚠️ / ❌ |

If tracks are incomplete, inform the user which are missing and let them decide whether to proceed with partial inputs or complete the missing tracks first.

Look for (in existing summary): problem statement not specific enough, pains without evidence count, open questions not listed, Phase 1 assumption status not updated.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask the user to provide the outputs from all Phase 2 tracks:

```
For the Problem Validation Summary I need outputs from all Tracks A-D.

Paste below (or confirm they are already in context):

TRACK A - Tech Feasibility Report:
[paste here or "already in context"]

TRACK B - Domain Analysis + Legal Requirements:
[paste here or "already in context"]

TRACK C - Market Analysis (TAM/SAM/SOM, Competitor Analysis, SWOT, Market Timing):
[paste here or "already in context"]

TRACK D - Customer Segments + Personas + Early Adopters Profile + JTBD Analysis:
[paste here or "already in context"]

Additional questions:
1. Did your view of the problem change during discovery? Any surprises?
2. Are you revising any initial assumptions from Phase 1 (Project Charter / Assumptions Register)?
3. What is the biggest uncertainty that remains?
```

---

## Step 2: Synthesize

Before generating, Claude must:
1. Identify the strongest validated pains (cross-referenced across tracks)
2. Check for contradictions between tracks (e.g., market too small vs. high customer pain)
3. Confirm the JTBD matches the identified personas
4. Flag any track that is incomplete or has low confidence

---

## Step 3: Generate artifact

Generate in English.

---

### ARTIFACT: Problem Validation Summary

```markdown
# Problem Validation Summary - [Product Name]

> **Phase:** 2 - Discovery (Convergence)
> **Date:** [date]
> **Input artifacts:** Tech Feasibility Report, Domain Analysis, Legal Requirements, Market Size Analysis, Competitor Analysis, SWOT, Market Timing Rationale, Customer Segments, Personas, Early Adopters Profile, JTBD Analysis

---

## Validation Verdict

**Overall verdict:** ✅ Validated / ⚠️ Partially validated / ❌ Not validated

[2-3 sentences: clear statement of what was validated, what wasn't, and whether proceeding to Phase 3 is justified]

---

## The Problem (Validated)

**Problem statement:**
[1-2 sentences: What is the core problem? Who has it? When does it occur?]

**Evidence basis:**
- [X] interviews conducted
- [X] data sources reviewed
- [X] JTBD identified

**Problem urgency:** High / Medium / Low
**Basis for urgency:** [why people need this solved now, not later]

---

## Validated Customer Pains

| Pain | Segment | Frequency | Intensity | Evidence |
|---|---|---|---|---|
| [Pain 1] | [Segment X] | High / Med / Low (X of Y interviewees) | High / Med / Low | [interview quotes / survey stat] |
| [Pain 2] | | | | |
| [Pain 3] | | | | |

**Top validated pain (focus for Phase 3):**
[The single most validated, most intense pain to solve first]

---

## Primary Customer (Validated)

**Segment:** [name]
**Persona:** [name]
**Early adopter archetype:** [1-2 sentences describing the ideal first customer]

---

## JTBD Core (Summary)

**The Job:**
When [situation], I want to [motivation], so I can [expected outcome].

**Dominant force (what drives switching):**
- Push: [top pain with current solution]
- Pull: [strongest attraction to new solution]

---

## Market Opportunity (Summary)

| Metric | Value | Confidence |
|---|---|---|
| SAM | $[X]M | High / Med / Low |
| SOM (Year 3) | $[X]M | Low (assumption-heavy) |
| Market timing | [Strong / Moderate / Weak] | [brief reason] |

**Competitive whitespace:** [where we can win that competitors are not covering]

---

## Technical Feasibility (Summary)

**Verdict:** 🟢 Feasible / 🟡 Feasible with risks / 🔴 Not feasible

**Key risks:**
- [Risk 1]
- [Risk 2]

**Critical blockers:** [None / List blockers]

---

## Regulatory Summary

**Showstoppers:** [None / List any blocking requirements]
**Key compliance requirements to address:** [list top 2-3]

---

## Assumptions Confirmed / Invalidated

| Assumption (from Phase 1) | Status | Finding |
|---|---|---|
| [Assumption from Project Charter] | ✅ Confirmed / ❌ Invalidated / ⚠️ Partially | [what we found] |
| [Assumption 2] | | |

---

## Open Questions Going into Phase 3

| Question | Priority | Who resolves |
|---|---|---|
| [What we still don't know] | High / Med / Low | [Human research / Phase 3 Design Thinking / next discovery loop] |
| ... | | |

---

## Track Completeness Check

| Track | Status | Confidence | Notes |
|---|---|---|---|
| A: Tech Feasibility | ✅ Complete / ⚠️ Partial / ❌ Missing | High / Med / Low | |
| B: Domain + Legal | ✅ Complete / ⚠️ Partial / ❌ Missing | High / Med / Low | |
| C: Market Analysis | ✅ Complete / ⚠️ Partial / ❌ Missing | High / Med / Low | |
| D: VOC + JTBD | ✅ Complete / ⚠️ Partial / ❌ Missing | High / Med / Low | |

---

## Phase 2 → Phase 3 Recommendation

**Recommendation:** ✅ Proceed to Phase 3 / ⚠️ Proceed with gaps noted / ❌ Do not proceed - revisit [area]

**Reason:** [1-2 sentences]

**What Phase 3 must answer:**
1. [Key design/strategy question remaining]
2. [Second key question]
3. [Third key question]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Problem Validation Summary must cover:**
- [ ] Overall verdict stated clearly (Validated / Partially / Not validated) with rationale
- [ ] Problem statement: who has it, when, what it costs them - specific and concrete
- [ ] Evidence basis: number of interviews, data sources, confidence level
- [ ] Problem is real and significant - confirmed by data, not assumption
- [ ] Problem is painful enough that customers actively seek a solution
- [ ] Problem is solvable with available resources (feasibility link)
- [ ] Top validated pains ranked by frequency AND intensity
- [ ] Primary customer identified (segment + persona)
- [ ] JTBD core summarized (When / I want to / So I can)
- [ ] Dominant switching forces identified (what pushes away from current, what pulls toward new)

**Track completeness must be verified:**
- [ ] Track A (Tech Feasibility) - complete or gaps noted
- [ ] Track B (Domain + Legal) - complete or gaps noted
- [ ] Track C (Market Analysis) - complete or gaps noted
- [ ] Track D (VOC + JTBD) - complete or gaps noted
- [ ] Minimum interview threshold met (≥10 interviews)
- [ ] JTBD identified (≥3 distinct jobs)

**Synthesis quality must be verified:**
- [ ] Assumptions from Phase 1 (Project Charter) confirmed or invalidated - explicitly stated
- [ ] Contradictions between tracks surfaced and addressed
- [ ] Open questions going into Phase 3 listed with priority
- [ ] Phase 2 → Phase 3 recommendation stated with reasoning

**For SaaS/AI products:**
- [ ] Would customers trust an AI-based solution for this problem?
- [ ] Do customers have the data required for AI to work (if AI-dependent solution)?
- [ ] Is there already an adequate AI solution - why would customers switch?
- [ ] What is the switching cost from current solution?

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-2/problem-validation-summary.md
```
