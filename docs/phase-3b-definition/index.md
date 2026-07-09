# Phase 3b - Commercial Definition

Synthesize validated inputs into commercial strategy: value proposition, business model, metrics, and the PRD that drives everything downstream.

**Duration:** Hours to a few sessions (AI-assisted synthesis sprint)  
**Gate type:** Implicit gate - entry requires Phase 3a GO verdict  
**Playbooks:** Greenfield

---

## When to enter this phase

Enters **only after** a GO verdict from Phase 3a. The GO verdict is required - there is no workaround.

**"Done elsewhere" rule:** if you have an existing Lean Canvas or business model from prior work, bring it via Path A in the relevant skill. You don't need to rebuild from scratch.

---

## What you need before entering

- Phase 3a GO verdict
- Phase 2 outputs (market analysis, personas, JTBD, problem validation)
- (Optional) existing business model artifacts to import

---

## Skills in this phase

| Skill | What it does | Output |
|---|---|---|
| [pm-kotler](pm-kotler.md) | Defines the product through Kotler's Five Levels of a Product | Product Definition |
| [pm-lean-canvas](pm-lean-canvas.md) | One-page business model focused on the problem (default for startups) | Lean Canvas |
| [pm-business-model](pm-business-model.md) | Fuller Business Model Canvas focused on operations (alternative to Lean Canvas for complex models) | Business Model Canvas |
| [pm-kpis](pm-kpis.md) | North Star Metric, AARRR Funnel Metrics, OKRs | KPI Framework |
| [pm-business-case](pm-business-case.md) | 3-year financial projections, unit economics, Go/No-Go investment decision | Business Case |
| [pm-product-roadmap](pm-product-roadmap.md) | Phase 3b version: product roadmap based on validated strategy | Product Roadmap v1 |
| [pm-prd](pm-prd.md) | Synthesizes Phase 2+3a+3b into the PRD - the primary product specification | PRD (Phase 3b exit artifact) |
| [pm-pitch-deck](pm-pitch-deck.md) | Pitch deck content brief (optional - only if raising capital or pitching to partners) | Pitch Deck brief |

**Recommended order:**
```
pm-kotler → pm-lean-canvas (or pm-business-model) → pm-kpis → pm-business-case
→ pm-product-roadmap (v1) → pm-prd
```

`pm-pitch-deck` is optional - skip if not raising capital and not pitching to partners.

---

## Lean Canvas vs. Business Model Canvas

Both produce a business model artifact. Choose one:

| | Lean Canvas | Business Model Canvas |
|---|---|---|
| Focus | Problem-solution fit | Full business operations |
| Best for | Early-stage startups validating PMF | Established or operationally complex businesses |
| Size | 1 page, 9 blocks | 1 page, 9 blocks (different blocks) |

Default recommendation: **Lean Canvas** for most products at this stage.

---

## What you exit with

- **Product Definition** (Kotler) - five-level product structure
- **Lean Canvas or Business Model Canvas** - one-page business model
- **KPI Framework** - North Star Metric, AARRR, OKRs
- **Business Case** - financial projections and unit economics
- **Product Roadmap v1** - strategic roadmap
- **PRD** - the master product specification; frozen after this phase

**PRD note:** `PRD_master.md` is immutable after Phase 3b. It is the baseline. All subsequent changes go through a formal change request process tracked in the PRD changelog.

---

## Phase exit gate

**Exit criteria:** PRD frozen + Business Case complete + Roadmap v1 complete.

Run `/pureinn` to check the Phase 3b exit gate and advance to Phase 4.
