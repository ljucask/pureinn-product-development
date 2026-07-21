# pm-prd

> Product Requirements Document - synthesizes all Phase 2-3b outputs into a single product-level document

**Phase:** 3b - Definition (closes Phase 3b); or Feature Implementation (Initiative PRD)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.1.0  
**Triggers:** PRD, product requirements, product spec, business capabilities, initiative PRD

---

## When to use

Phase 3b close. The PRD is the final synthesis step before Phase 4 begins. It does not contain new research - it assembles all Phase 2, 3a, and 3b outputs into one coherent product-level document.

Also used in Feature Implementation playbook to produce an **Initiative PRD** scoped to one domain or initiative.

---

## What it produces

Two distinct modes, detected automatically:

| Mode | Context | Output | Frozen? |
|---|---|---|---|
| **Product PRD** | Greenfield Phase 3b | `product/PRD_master.md` | Yes - frozen after creation |
| **Initiative PRD** | Feature Implementation after Track B | `initiatives/[slug]/prd.md` | No - living for that initiative |

### Product PRD

Synthesizes all upstream artifacts into `product/PRD_master.md`. **This file does not change for new scope.** New domain/feature scope after Phase 4 → a new Initiative PRD, never an edit to PRD_master. PRD_master is the stable historical record.

**Re-run with new evidence (delta mode):** if PRD_master already exists and new upstream evidence arrives *for the same scope* (updated personas, market analysis, re-prioritization) before it's fully consumed downstream, the skill does not rewrite from scratch - it reads the current PRD, re-validates the evidence-sensitive sections (Problem Statement, Target Customer, Value Proposition, Market Context, Business Model) against the new sources, changes only what the new evidence supports (marking each `[UPDATED - previous/new/reason]`, leaving the rest `[UNCHANGED]`), and shows the delta before writing. It then names downstream artifacts that may now be inconsistent (`pm-product-roadmap`, `pm-features-list`, `pm-business-model`) and recommends `/pm-audit strategy`.

**PRD sections:**
- Product vision and problem statement
- Customer segments, personas, early adopters
- JTBD core: jobs, forces, switching logic
- Market context: TAM/SAM/SOM, competitive landscape, timing
- Validation evidence: hypothesis register, Go/No-Go verdict
- Business model overview (Lean Canvas or BMC summary)
- KPIs: North Star, AARRR metrics, OKRs
- Business case summary
- **Business Capabilities** - what the product must enable, in business language (required for Phase 4)
- Roadmap reference (v1)
- Legal and compliance requirements
- Assumptions and open risks

**Modular PRD for large products:** If the product covers multiple distinct business domains:
- `product/PRD_master.md` - high-level router: goals, personas, KPIs, links to domain sub-PRDs (this IS the frozen master)
- `product/PRD_[Domain].md` - Business Capabilities per domain (e.g., PRD_Billing.md, PRD_Auth.md)

Feature Cards reference specific PRD sections via the `prd_ref` field - Claude reads only the referenced section during JIT design, not the full PRD.

### Initiative PRD

Scoped to one domain or business initiative. Entry point for:
- `pm-entity-registry` (append mode)
- `pm-business-rules-library` (append mode)
- `pm-features-list` (FI append mode)

---

## How to invoke

```bash
/pm-prd           # interactive - Step 0 detects Product vs. Initiative mode
/pm-prd --agent   # autonomous synthesis from available phase artifacts
```

---

## Critical rule: Business Capabilities section

The PRD must include a Business Capabilities section - a list of what the product must enable, written in business language. This is the direct input for Phase 4 (`pm-entity-registry` extracts entities from it) and Phase 5 (`pm-features-list` decomposes capabilities into FDD features). Without Business Capabilities, the AI decomposition into entities and features is guesswork.

---

## The PRD is not a spec

- No User Stories (those belong to Scrum/XP, incompatible with FDD)
- No technical implementation detail
- No wireframes or UI descriptions
- No feature-level acceptance criteria

The PRD answers: who is this for, what problem does it solve, why does it matter, what does success look like, what are the commercial assumptions.

---

## Dependencies

**Required before running (Product PRD):**
- All four Phase 2 tracks: `pm-tech-feasibility`, `pm-domain-analysis`, `pm-market-analysis`, `pm-personas` + `jtbd-building`
- `pm-problem-validation`
- `pm-hypotheses` (Results mode, Go/No-Go = GO)
- `design-thinking`
- `pm-lean-canvas` or `pm-business-model`
- `pm-kpis`
- `pm-business-case`
- `pm-product-roadmap` (v1)

**Produces for:**
- `pm-entity-registry` - Business Capabilities section is the decomposition input
- `pm-features-list` - Business Capabilities drive feature decomposition
- `pm-domain-model` - Phase 4 domain modeling references PRD business context
- All Phase 6 Feature Cards - `prd_ref` field links to specific PRD sections

**Related skills:** `pm-product-roadmap`, `pm-lean-canvas`, `pm-kpis`, `pm-business-case`, `pm-entity-registry`
