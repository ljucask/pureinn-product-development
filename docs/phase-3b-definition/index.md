# Phase 3b - Commercial Definition

Synthesize validated inputs into commercial strategy: value proposition, business model, metrics, and the PRD that drives everything downstream.

**Duration:** Hours to a few sessions (AI-assisted synthesis sprint) · **Gate type:** Implicit gate - entry requires Phase 3a GO verdict · **Playbooks:** Greenfield

---

## How to read this page

Steps run mostly in sequence, with one branch point (Lean Canvas vs. Business Model Canvas) and one full-phase alternative (commissioned builds → `pm-scope-brief`).

---

## When to enter this phase

Enters **only after** a GO verdict from Phase 3a - no workaround.

**Exception - commissioned builds:** when the mandate is already given (a client commissioned the build, an exec directed it), Phase 3a is skipped and this phase reduces to `/pm-scope-brief` - the market risk sits with the commissioner, and the definition (not a Go/No-Go) is what you owe them. Canvas/KPI/business-case skills are optional in that mode.

**"Done elsewhere" rule:** if you have an existing Lean Canvas or business model from prior work, bring it via Path A in the relevant skill - you don't need to rebuild from scratch.

**What you need before entering:** Phase 3a GO verdict, Phase 2 outputs (market analysis, personas, JTBD, problem validation), and optionally existing business model artifacts to import.

---

## Step 1 - Product Definition

- **When to run / skip:** always run - this frames everything after it.
- **Gather first:** Phase 2 outputs.
- **Command:** `/pm-kotler`
- **What you get:** the product defined through Kotler's Five Levels (core benefit → augmented/potential product).
- **What it does NOT give you:** a business model - that's Step 2.
- **Done when:** all five levels are filled with product-specific content, not generic placeholders.

---

## Step 2 - Business Model (branch: Lean Canvas vs. Business Model Canvas)

- **When to run / skip:** always run one of the two. **Decision point:**

| | Lean Canvas | Business Model Canvas |
|---|---|---|
| Focus | Problem-solution fit | Full business operations |
| Best for | Early-stage startups validating PMF | Established or operationally complex businesses |
| Command | `/pm-lean-canvas` | `/pm-business-model` |

**Default: Lean Canvas** for most products at this stage - use Business Model Canvas only if operational complexity (multi-sided market, complex partnerships, regulated operations) genuinely requires the fuller model.

- **Gather first:** Product Definition (Step 1), any existing business model to import.
- **What you get:** one-page business model - problem, solution, channels, revenue, cost structure.
- **What it does NOT give you:** metrics or financial projections - those are Steps 3-4.
- **Done when:** every block has real content, not "TBD".

---

## Step 3 - KPI Framework

- **When to run / skip:** always run.
- **Gather first:** Business Model (Step 2).
- **Command:** `/pm-kpis`
- **What you get:** North Star Metric, AARRR Funnel Metrics, OKRs.
- **What it does NOT give you:** the financial case - that's Step 4. KPIs measure product health, not investment viability.
- **Done when:** the North Star Metric is a single, unambiguous number you can track from day one.

---

## Step 4 - Business Case

- **When to run / skip:** run for every product where a financial commitment is being made. Skip only in commissioned-build mode with no independent financial stake.
- **Gather first:** Business Model + KPIs.
- **Command:** `/pm-business-case`
- **What you get:** 3-year financial projections, unit economics, a Go/No-Go investment decision.
- **What it does NOT give you:** a market-validated demand signal - that already happened in Phase 3a. This is the financial math on top of validated demand.
- **Done when:** unit economics are positive under stated assumptions, or the gap is named explicitly.

---

## Step 5 - Product Roadmap (v1)

- **When to run / skip:** always run.
- **Gather first:** Business Case.
- **Command:** `/pm-product-roadmap`
- **What you get:** a strategic roadmap - the first of three versions (v2 in Phase 4, v3 in Phase 5).
- **What it does NOT give you:** feature-level detail - that arrives in v3, after Phase 5.
- **Done when:** major milestones are dated or sequenced, not just listed.

---

## Step 6 - PRD (phase exit)

- **When to run / skip:** always run - this is the phase's exit artifact.
- **Gather first:** all of Phase 2 + 3a + Steps 1-5 above.
- **Command:** `/pm-prd`
- **What you get:** the PRD - synthesizes Phase 2+3a+3b into the primary product specification. **Frozen immediately after this phase** - all subsequent changes go through a formal change request tracked in the PRD changelog.
- **What it does NOT give you:** domain/entity detail - Phase 4 builds the Live Registers from this PRD's Business Capabilities.
- **Done when:** the PRD is complete and you're ready to freeze it - there's no partial-freeze state.

**Commissioned-build alternative:** `/pm-scope-brief` replaces the PRD when the mandate is already given - Business Capabilities, edge-case register, non-goals, acceptance criteria + Change Log. Phase 4-5 consume it exactly like a PRD.

---

## Optional - Pitch Deck

- **When to run / skip:** run only if raising capital or pitching to partners. **Skip if neither** - this produces no delivery value otherwise.
- **Command:** `/pm-pitch-deck`
- **What you get:** slide-by-slide pitch deck content brief.

---

## What you exit with

- **Product Definition** (Kotler) - five-level product structure
- **Lean Canvas or Business Model Canvas** - one-page business model
- **KPI Framework** - North Star Metric, AARRR, OKRs
- **Business Case** - financial projections and unit economics
- **Product Roadmap v1** - strategic roadmap
- **PRD** - the master product specification; frozen after this phase

---

## Phase exit gate

**Exit criteria:** PRD frozen + Business Case complete + Roadmap v1 complete.

Run `/pureinn` to check the Phase 3b exit gate and advance to Phase 4.
