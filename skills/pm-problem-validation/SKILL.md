---
name: pm-problem-validation
description: Generate a Problem Validation Summary by synthesizing all Phase 2 research outputs (Tech Feasibility, Domain Analysis, Market Analysis, Personas, JTBD). Use at end of Phase 2 as convergence artifact. No new research - pure synthesis.
license: MIT
metadata:
  agent-mode: decision
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


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments - after drafting, require the user's review before finalizing; do not close decisions autonomously.

---

## What this skill does

Synthesizes all Phase 2 Track outputs into one convergence document:
- Track A: Tech Feasibility Report
- Track B: Domain Analysis + Legal Requirements
- Track C: Market Analysis (TAM/SAM/SOM, Competitor Analysis, SWOT, Market Timing)
- Track D: Personas + JTBD Analysis

This is the Phase 2 exit artifact. Its output becomes the primary input to Phase 3a (Design Thinking - Define stage).

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

**Multi-source handling:** This skill synthesizes 4 tracks (A-D) at once. Where tracks agree, cite convergence as high-confidence signal. Where tracks conflict (e.g., Track C says market is small while Track D shows high pain intensity), do not silently pick one - surface as `[CONFLICT - Track X says A / Track Y says B → open question for Phase 3a]` in the Open Questions section. Never average or paper over a conflict.

**Re-run with new data (delta mode):** If a Problem Validation Summary already exists and a Track was updated, do not rewrite from scratch. Read the current summary first, re-validate against the updated track(s), update only what the new evidence supports (`[UPDATED - previous: X / new: Y]`), and mark what is unaddressed `[UNCHANGED]`. Show the delta before finalizing. Surface the cascade: `/pm-prd`, `/design-thinking`, `/pm-product-roadmap` may need re-check.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Gather inputs

First, ask:

Do you have Phase 2 research artifacts to work with?

  A) Yes - I have outputs from one or more Phase 2 tracks to paste or confirm in context
  B) No - I have not done formal Phase 2 research, guide me through what I know

---

### Path A - Phase 2 artifacts available

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

### Path B - No Phase 2 research (guided elicitation)

No Phase 2 artifacts exist. Guide the user through 3 rounds to reconstruct the validation picture from founder knowledge across all four tracks. Output will be marked as assumption-based and gaps will be flagged explicitly.

> **Path B - specific downstream risks by assumption type**
>
> This is the highest-leverage document in Phase 2 - every Phase 3a and Phase 3b artifact anchors to it. Knowing which parts are assumption vs. evidence matters more than completing the document.
>
> - **Problem urgency assumed (not confirmed by customers):** the Business Case will model conversion rates and pricing based on an urgency level the customer may not share. If real urgency is lower, pricing and CAC assumptions will not hold.
> - **Customer identity assumed:** if the primary customer turns out to be a different role or segment, the JTBD Analysis, Lean Canvas Customer Segment block, and KPI activation event definition will need to be revisited.
> - **Competitor landscape incomplete:** missing a key competitor means the positioning in Lean Canvas and PRD may be weaker than it appears - not necessarily fatal, but the team will not see it coming.
> - **Regulatory/legal gaps not surfaced here:** if Phase 4 Domain Analysis later identifies a compliance constraint (GDPR, licensing, sector-specific regulation), it may constrain technical architecture or MVP scope in ways that affect the roadmap timeline you set in Phase 3b.
>
> None of these require stopping. What matters: identify the highest-risk assumption before Phase 3a validation begins, and design at least one lightweight experiment to stress-test it before Phase 3b commercial work locks in the Business Case numbers.

**Group 1 of 3 - The problem and the customer**

Use AskUserQuestion tool for these two questions:

How confident are you that this problem is real and significant for your target customer?

  A) Very confident - I have spoken directly with people who experience this
  B) Somewhat confident - I have indirect evidence (forums, reviews, observation)
  C) Working from domain expertise - I know this world but haven't validated formally
  D) Mostly assumption - not yet tested with real people

How technically feasible is building your proposed solution, as far as you know?

  A) Proven stack - no significant technical unknowns
  B) Largely proven with some unknowns to validate
  C) Significant technical risks that need a spike or prototype to resolve
  D) Unknown - haven't assessed feasibility yet

Then ask as plain text:

Describe the problem in one specific sentence from the customer's perspective. Not what your product does - what pain they feel.

Who specifically experiences this problem? Describe the person: role, context, company size, how often the problem hits.

After answers, confirm and proceed.

---

**Group 2 of 3 - Evidence and market**

Ask all as plain text:

What evidence do you have that this problem is real? Be specific - even anecdotal is useful. (e.g., "I managed 8 properties myself and felt this pain", "Three friends in this industry confirmed it", "I found 50+ complaints on Reddit")

What do people use today to cope with this problem? Name specific solutions - tools, workarounds, manual processes, or nothing at all. What is wrong with each?

Who are the 2-3 main competitors or close alternatives in this space? Why are customers not fully satisfied with them?

Are there any legal, regulatory, or compliance factors relevant to this market or product that you are aware of?

After answers, confirm: "Is this a fair summary of what you know about the market and problem?"

---

**Group 3 of 3 - Confidence and gaps**

Use AskUserQuestion tool for these two questions:

What is your biggest uncertainty right now?

  A) Whether the problem is painful enough to justify a paid solution
  B) Whether you are targeting the right customer segment
  C) Whether the solution you have in mind is technically feasible
  D) Whether the market is large enough to build a business on

Did your thinking about the problem or customer shift as you answered these questions?

  A) No - my original assumptions held up
  B) Yes - I realized I need to refine who the customer is
  C) Yes - I realized the problem framing needs adjustment
  D) Yes - significant doubts emerged that I need to address before continuing

Then ask as plain text:

What would need to happen for you to feel confident enough to move forward to strategy and business model work?

After answers, show complete summary across all groups. Flag which areas have zero validation evidence and recommend which should be addressed before treating the Problem Validation Summary as reliable.

Note at the top of every generated artifact: `> Assumption-based - no formal Phase 2 research conducted. Treat this summary as a hypothesis map, not validated evidence. Items marked [NO EVIDENCE] carry highest risk.`

---

## Step 2: Synthesize

Before generating, Claude must:
1. Identify the strongest validated pains (cross-referenced across tracks)
2. Check for contradictions between tracks (e.g., market too small vs. high customer pain)
3. Confirm the JTBD matches the identified personas
4. Flag any track that is incomplete or has low confidence

**Verdict discipline (this is the single most consequential judgment in Phase 2):**
- "✅ Validated" requires all three: (1) evidence from real customers, not only founder knowledge; (2) the top pain confirmed by multiple independent sources; (3) no unresolved `[CONFLICT]` on problem, customer, or urgency. Missing any one → the honest verdict is ⚠️ Partially validated, and that is a normal, useful outcome - not a failure.
- Do not soften a deserved ❌ to ⚠️ out of politeness. A ❌ verdict here saves more money than any other single output in the framework - it stops months of Phase 3-6 work on an unvalidated premise. State plainly what evidence would be needed to change it.
- Watch for confirmation bias in the inputs themselves: if every track was authored from the same founder assumptions (all Path B), convergence between tracks is NOT independent confirmation - say so in the Evidence basis.

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

[2-3 sentences: clear statement of what was validated, what wasn't, and whether proceeding to Phase 3a is justified]

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

**Top validated pain (focus for Phase 3a Design Thinking):**
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

## Open Questions Going into Phase 3a

| Question | Priority | Who resolves |
|---|---|---|
| [What we still don't know] | High / Med / Low | [Human research / Phase 3a Design Thinking / next discovery loop] |
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

## Phase 2 → Phase 3a Recommendation

**Recommendation:** ✅ Proceed to Phase 3a / ⚠️ Proceed with gaps noted / ❌ Do not proceed - revisit [area]

**Reason:** [1-2 sentences]

**What Phase 3a must answer:**
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
- [ ] Open questions going into Phase 3a listed with priority
- [ ] Phase 2 → Phase 3a recommendation stated with reasoning

**For SaaS/AI products:**
- [ ] Would customers trust an AI-based solution for this problem?
- [ ] Do customers have the data required for AI to work (if AI-dependent solution)?
- [ ] Is there already an adequate AI solution - why would customers switch?
- [ ] What is the switching cost from current solution?

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/problem-validation-summary.md
```

---

## Handoff

**Čo si teraz má:** Problem Validation Summary - Phase 2 je uzavretá, máš validovaný problém ako základ pre validáciu a commercial definition.

**Ďalší krok:** `/design-thinking` (Phase 3a) — ideácia a validačné hypotézy. Alebo `/pureinn` pre Phase 2 gate.

**Môžeš preskočiť ak:** Problém je už silne validovaný reálnymi dátami - choď rovno na `/pm-hypotheses` [Plan mode].
