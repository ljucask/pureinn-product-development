---
name: pm-prd
description: Two modes. (1) Product PRD - Phase 3 consolidation artifact synthesizing all Phase 2+3 outputs. Saves to product/PRD_master.md. Frozen after creation. (2) Initiative PRD - Feature Implementation context, after Track B discovery for a large new domain. Leaner document focused on Business Capabilities for that domain only. Saves to initiatives/[slug]/prd.md.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: PRD, product requirements document, Phase 3 exit, product consolidation, product specification
  role: specialist
  scope: documentation
  output-format: document
  related-skills: pm-lean-canvas, pm-kpis, pm-domain-model, pm-product-roadmap
---

# PM - Product Requirements Document (PRD)

## What this skill does

**Two modes - detected automatically in Step 0:**

| Mode | Context | Inputs | Output | Frozen? |
|---|---|---|---|---|
| **Product PRD** | Greenfield Phase 3 | All Phase 2+3 outputs | `product/PRD_master.md` | Yes - frozen after creation |
| **Initiative PRD** | Feature Implementation after Track B | `initiatives/[slug]/discovery/` | `initiatives/[slug]/prd.md` | No - living for that initiative |

**Product PRD_master** is the original product scope document. It does NOT change after creation. New scope, new functionality, changed assumptions → new Initiative PRD for that initiative. PRD_master remains as the stable historical record.

**Initiative PRD** is a leaner document scoped to one domain/initiative. It contains Business Capabilities for that domain only - the entry point for pm-entity-registry (append mode), pm-business-rules-library (append mode), and pm-features-list (FI append mode) for this initiative.

---

**Product PRD** synthesizes all Phase 2 and Phase 3 outputs into a single coherent product-level document:

**Phase 2 inputs:**
- Tech Feasibility Report (Track A)
- Domain Analysis + Legal Requirements (Track B)
- Market Size Analysis, Competitor Analysis, SWOT, Market Timing (Track C)
- Customer Segments, Personas, Early Adopters Profile, JTBD Analysis (Track D)
- Problem Validation Summary (convergence)

**Phase 3 inputs:**
- Business Model Canvas
- KPIs & Metrics Framework (North Star, AARRR, OKRs)
- Business Case
- Product Roadmap v1

The PRD is not a requirements spec and it does NOT contain User Stories. User Stories belong to Scrum/XP methodology and are incompatible with FDD. The PRD is a product-level document that answers: who is this for, what problem does it solve, why does it matter, what does success look like, what are the commercial assumptions.

**Critical PRD rule in FDD+SDD framework:** The PRD must include a **Business Capabilities** section - a list of what the product must enable, written in business language. This section is the direct input for Phase 4 (pm-entity-registry extracts entities from it) and Phase 5 (pm-features-list decomposes capabilities into FDD features). Without Business Capabilities, the AI decomposition into entities and features is guesswork.

**Modular PRD for large products:** If the product covers multiple distinct business domains, split the PRD into domain-specific files to prevent context window overload during Phase 4-5:
- `product/PRD_master.md` - high-level router: goals, personas, KPIs, links to domain sub-PRDs (this IS the frozen master)
- `product/PRD_[Domain].md` - Business Capabilities per domain (e.g., PRD_Billing.md, PRD_Auth.md)

Feature Cards reference specific PRD sections via `prd_ref` frontmatter field - Claude Code reads only the referenced section during JIT design, not the full PRD.

No new research. Pure synthesis.

---

## Dependencies

**Required before running (all of these):**
- `pm-problem-validation` - validated problem, customer, evidence
- `pm-business-model` - commercial logic and revenue model
- `pm-kpis` - North Star, AARRR, OKRs
- `pm-business-case` - financial projections and investment rationale
- `pm-product-roadmap` (v1) - strategic phases and roadmap direction

**Strongly recommended (Phase 2 artifacts):**
- `pm-personas` - customer segments and personas
- `pm-market-analysis` - market context
- `pm-domain-analysis` - domain constraints and regulatory landscape
- `pm-tech-feasibility` - technical context

**Produces artifacts used by:**
- Phase 4 entity extraction (`pm-entity-registry` reads Business Capabilities → entities.md)
- Phase 5 feature decomposition (`pm-features-list` reads Business Capabilities → feature_list.md)
- Phase 5 rules init (`pm-business-rules-library` reads known constraints from Domain Analysis)
- Feature Cards (`prd_ref` field points to specific PRD sections for JIT context)
- External stakeholders, investors, team onboarding

---

## Step 0: Current state check + mode detection

**Mode detection (run first):**

1. Does `product/PRD_master.md` already exist?
   - Yes → **Product PRD already created.** Use AskUserQuestion: A) view it, B) switch to Initiative PRD mode (FI context), C) done.

2. Does `initiatives/` directory exist in the project workspace?
   - Yes → **Feature Implementation context detected.**
   - Use AskUserQuestion tool:
     - Option A: "Initiative PRD - new domain/initiative after Track B discovery (saves to initiatives/[slug]/prd.md)" (Recommended for FI)
     - Option B: "Product PRD - full Phase 3 consolidation (saves to product/PRD_master.md)" (Greenfield only)
   - No → **Greenfield context.** Proceed to Product PRD mode below.

3. If Initiative PRD mode selected → skip to **INITIATIVE PRD MODE** section at bottom of this skill.

---

**Product PRD mode - check inputs:**

Then map which inputs are available:

| Input | Artifact | Status |
|---|---|---|
| Phase 2 convergence | Problem Validation Summary | ✅ / ⚠️ / ❌ |
| Phase 2 Track D | Personas + JTBD | ✅ / ⚠️ / ❌ |
| Phase 2 Track C | Market Analysis | ✅ / ⚠️ / ❌ |
| Phase 2 Track B | Domain Analysis + Legal | ✅ / ⚠️ / ❌ |
| Phase 2 Track A | Tech Feasibility | ✅ / ⚠️ / ❌ |
| Phase 3 | Business Model Canvas | ✅ / ⚠️ / ❌ |
| Phase 3 | KPIs (NSM, AARRR, OKRs) | ✅ / ⚠️ / ❌ |
| Phase 3 | Business Case | ✅ / ⚠️ / ❌ |
| Phase 3 | Product Roadmap v1 | ✅ / ⚠️ / ❌ |

If critical inputs are missing (Problem Validation Summary, Business Model Canvas, KPIs), block until resolved. If secondary inputs are missing, inform user and generate with noted gaps.

Look for: PRD without a clear problem statement, value proposition not tied to validated pains, success criteria not tied to NSM, roadmap section not consistent with pm-product-roadmap v1, missing "out of scope" section, regulatory constraints not surfaced.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

### Step 1a - Confirm artifacts

Ask as plain text:

```
To generate the PRD I will synthesize your Phase 2 and Phase 3 artifacts.

Please confirm which are available in context (or paste them below):

PHASE 2:
- Problem Validation Summary: [available in context / paste here]
- Personas + JTBD Analysis: [available in context / paste here]
- Market Analysis (TAM/SAM/SOM, Competitor Analysis, SWOT, Market Timing): [available / paste]
- Domain Analysis + Legal Requirements: [available / paste]
- Tech Feasibility Report: [available / paste]

PHASE 3:
- Business Model Canvas: [available / paste]
- KPIs (North Star, AARRR, OKRs): [available / paste]
- Business Case: [available / paste]
- Product Roadmap v1: [available / paste]
```

After receiving artifact status, show a coverage table and note which sections of the PRD will have gaps due to missing inputs.

---

### Step 1b - Follow-up questions

Ask these two questions together:

Is this PRD for internal use only, or will it be shared externally?

  A) Internal only - full transparency on risks and assumptions
  B) Shared externally (investors, partners) - softer language on risks
  C) Both versions needed

Has anything changed or been revised since these artifacts were generated?

  A) No - artifacts are current
  B) Yes - minor updates (I'll describe them)
  C) Yes - significant changes (pricing, scope, segment, pivot)

Then ask as plain text:

Are there any open decisions that need to be flagged in the PRD as unresolved? List them - they will appear as explicit open items in the document.

After answers, confirm: "Ready to synthesize. Anything else before I generate the PRD?"

---

## Step 2: Synthesize

Before generating, Claude must:
1. Identify the core validated problem and primary customer (from Problem Validation Summary)
2. Check that the Business Model value proposition aligns with validated pains from Phase 2
3. Check that KPIs (NSM) connect logically to the problem and business model
4. Check that the Roadmap phases align with the business case investment staging
5. Surface any contradictions between artifacts (market size vs. business case targets, persona vs. revenue model, tech feasibility vs. roadmap timeline)
6. Flag any sections where inputs are weak or missing

---

## Step 3: Generate artifact

Generate in English.

---

### ARTIFACT: Product Requirements Document (PRD)

```markdown
# Product Requirements Document - [Product Name]

> **Phase:** 3 - Define & Validation (Phase 3 exit artifact)
> **Date:** [date]
> **Version:** 1.0
> **Status:** [Draft / Final / Approved]
> **Owner:** [PM name]
> **Audience:** Internal team, [investors / advisors / partners if external]

---

## Document Purpose

This PRD is the consolidation of Phase 2 (Discovery) and Phase 3 (Define) outputs. It captures the validated product-market fit hypothesis and serves as the stable reference for Phase 4+ execution.

It is NOT a feature spec. Feature specifications are generated per Feature Set in Phase 6 (BRD + FSD).

---

## 1. Problem Statement

**The core problem:**
[2-3 sentences: What is the problem? Who has it? When does it occur? What does it cost them?]

**Evidence basis:**
- [X] customer interviews conducted
- [X] distinct JTBD identified
- Problem urgency: High / Medium / Low

**Why this problem is not solved well today:**
[Current alternatives and why they fall short - tied to competitor analysis and JTBD forcing functions]

---

## 2. Target Customer

### Primary Segment

**Segment:** [Name]
**Description:** [2-3 sentences: who they are, their context, scale]
**Size (SAM):** [X,000 / $XM]

**Primary Persona: [Name]**
- Role: [Job title / context]
- Core goal: [What they're trying to achieve]
- Top pain: [Primary pain with current solution]
- What triggers them to seek a new solution: [switching trigger]

### Early Adopter Profile

[2-3 sentences: who specifically will be the first 10-50 customers, what makes them different from the average segment member, how to find them]

### Secondary Segment (if applicable)

[Brief profile - segment name, size, difference from primary, timing of when we address them]

---

## 3. Product Vision and Value Proposition

**Vision (3 years):**
[One sentence: what does the world look like if this product succeeds?]

**Value proposition:**
[2-3 sentences: what outcome does the customer get, what pain disappears, why choose us over alternatives]

**For [Primary Persona]:**
- Primary outcome: [What they achieve]
- Pain eliminated: [What disappears]
- Differentiation: [Why this vs. the status quo or competitors]

---

## 4. Market Context

**Market opportunity:**

| Metric | Value | Confidence |
|---|---|---|
| TAM | $[X]M | [High/Med/Low] |
| SAM | $[X]M | [High/Med/Low] |
| SOM (Year 3) | $[X]M | [Low - assumption-based] |
| Market CAGR | [X%] | [Source] |

**Why now:**
[2-3 sentences: the specific conditions (tech, regulation, behavior change) that open this window now]

**Competitive position:**
[2-3 sentences: who the key competitors are, where we win, what is defensible]

**Competitive whitespace:**
[Where no competitor is covering well that we can own]

---

## 5. Business Model

**Revenue model:** [Subscription / Usage-based / Marketplace / Freemium + upgrade]

**Pricing:**
| Tier | Price | For whom |
|---|---|---|
| [Tier 1] | $[X]/month | [Target] |
| [Tier 2] | $[X]/month | [Target] |

**Unit economics targets:**
| Metric | Target |
|---|---|
| ARPU | $[X]/month |
| Monthly churn | < [X%] |
| LTV/CAC | > 3:1 |
| Gross margin | > [X%] |

**Acquisition model:** [Primary channel + approach]

---

## 6. Success Metrics

**North Star Metric:** [NSM definition]
**NSM Target (Month 12):** [X]

**Phase 1 exit criteria (Month [X] post-launch):**
- [ ] [Measurable condition - e.g., 20 paying customers]
- [ ] [Measurable condition - e.g., Day 30 retention > 40%]
- [ ] [NPS > 30 with first cohort]

**Phase 2 targets (Month [X]-[Y]):**
- [ ] [MRR target]
- [ ] [Churn target]
- [ ] [Growth rate]

**AARRR summary:**

| Stage | Key Metric | Target |
|---|---|---|
| Acquisition | [Metric] | [Target] |
| Activation | [Metric - activation event] | [X%] |
| Retention | [Day 30 retention] | [X%] |
| Revenue | [MRR Month 6] | $[X]K |
| Referral | [NPS] | > [X] |

---

## 7. Product Scope

### Business Capabilities (FDD+SDD input)

What the product must enable, written as business capabilities. This section is the primary input for entity extraction (Phase 4) and feature decomposition (Phase 5).

**Format:** "The system must enable [actor] to [business outcome]." No User Stories. No technical implementation. No "As a user I want..." format.

**[Domain 1: e.g., Order Management]**
- The system must enable customers to create, confirm, and manage orders.
- The system must enable customers to track order fulfillment status in real time.
- The system must enforce payment validation before any order is confirmed.

**[Domain 2: e.g., Payments]**
- The system must enable secure card payment processing for orders.
- The system must enable automated refund processing for cancelled orders within 5 business days.

**[Domain N: ...]**
- [capability]

> This section is referenced by Feature Cards via `prd_ref` - write with section anchors so individual capabilities can be linked directly.

### In Scope (MVP)

[High-level summary of which capability domains are in MVP]

1. [Domain 1: e.g., Order Management - full capability set]
2. [Domain 2: e.g., Payments - card processing only, no crypto]

> Feature-level detail defined in Phase 5 (pm-features-list) and Phase 6 JIT design (pm-feature-design).

### Out of Scope (MVP)

These items are explicitly excluded from the MVP. This is a strategic decision.

| Item | Reason | Reconsider when |
|---|---|---|
| [Feature / capability] | [Not validated / wrong segment / too complex] | [Phase 2 / after X customers] |
| [Feature 2] | | |

### Deferred (Post-MVP)

| Item | Target phase | Trigger |
|---|---|---|
| [Feature] | Phase 2 of product | [Condition] |
| [Feature] | Phase 3 of product | [Condition] |

---

## 8. Constraints and Risks

### Technical Constraints

| Constraint | Impact | Source |
|---|---|---|
| [e.g., Airbnb API rate limits] | [Affects sync frequency] | Tech Feasibility Report |
| [e.g., AI API cost ceiling] | [Gross margin constraint] | Tech Feasibility Report |

**Technical feasibility verdict:** 🟢 Feasible / 🟡 Feasible with risks / 🔴 Not feasible
[Key risks from Tech Feasibility Report]

### Regulatory Constraints

| Regulation | Jurisdiction | Requirement | Timeline |
|---|---|---|---|
| GDPR | EU | [Key requirements] | Before launch |
| [Local regulation] | [SK/CZ/...] | [Requirement] | [When] |

**Regulatory showstoppers:** [None / List]

**Compliance requirements to address before launch:**
- [ ] [Requirement 1]
- [ ] [Requirement 2]

### Business Constraints

| Constraint | Impact |
|---|---|
| [e.g., Budget: $XK for 12 months] | [Limits team size and marketing spend] |
| [e.g., Founding team = 2 people] | [Sequencing: cannot build everything in parallel] |
| [e.g., Must reach X customers by date Y for funding] | [Hard deadline on Phase 1 exit] |

---

## 9. Open Questions and Assumptions

### Open Questions (not yet resolved)

| Question | Priority | Owner | Target date |
|---|---|---|---|
| [What we don't know yet] | High / Med / Low | [Who resolves] | [When] |
| ... | | | |

### Critical Assumptions (that could invalidate the product)

| Assumption | Confidence | How to validate | By when |
|---|---|---|---|
| [e.g., Customers will pay $X/month] | Med | [Pricing test] | [Month X] |
| [e.g., Self-serve onboarding will work] | Low | [5-user test] | [Before launch] |
| [e.g., CAC < $X via inbound] | Low | [First campaign] | [Month 2] |

---

## 10. Product Roadmap (summary)

> Full roadmap in Product Roadmap v1 artifact.

**Phase 1 - [Name]:** [Timeframe] - [Goal in one sentence]
**Phase 2 - [Name]:** [Timeframe] - [Goal in one sentence]
**Phase 3 - [Name]:** [Timeframe] - [Goal in one sentence]

---

## 11. Artifact Input Map

This PRD synthesizes the following Phase 2 and Phase 3 artifacts:

| Artifact | Status | Key contribution to PRD |
|---|---|---|
| Problem Validation Summary | ✅ / ⚠️ / ❌ | Problem statement, evidence, validated pains |
| Customer Segments + Personas | ✅ / ⚠️ / ❌ | Target customer, early adopter profile |
| JTBD Analysis | ✅ / ⚠️ / ❌ | Customer motivation, switching forces |
| Market Analysis | ✅ / ⚠️ / ❌ | Market size, competitive position, timing |
| Domain Analysis + Legal | ✅ / ⚠️ / ❌ | Domain constraints, regulatory requirements |
| Tech Feasibility Report | ✅ / ⚠️ / ❌ | Technical constraints and risks |
| Business Model Canvas | ✅ / ⚠️ / ❌ | Revenue model, pricing, channels |
| KPIs (NSM, AARRR, OKRs) | ✅ / ⚠️ / ❌ | Success metrics |
| Business Case | ✅ / ⚠️ / ❌ | Financial targets, investment |
| Product Roadmap v1 | ✅ / ⚠️ / ❌ | Strategic phases |

**Gaps noted:** [List any artifacts that were missing or partial and how it affected the PRD]

---

## 12. Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | [date] | [PM] | Initial - end of Phase 3 |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Problem Statement must cover:**
- [ ] Problem clearly stated with who, when, and what it costs
- [ ] Evidence basis: number of interviews, JTBD identified
- [ ] Why current alternatives fail - tied to JTBD analysis and competitor research
- [ ] Problem urgency level stated

**Target Customer must cover:**
- [ ] Primary segment identified with size
- [ ] Primary persona named and described
- [ ] Early adopter profile - who specifically are the first 10-50 customers
- [ ] B2B: buyer vs. user distinction

**Business Capabilities must cover:**
- [ ] Capabilities written in business language ("The system must enable X to do Y")
- [ ] NO User Stories format ("As a user I want...") - incompatible with FDD
- [ ] Capabilities grouped by domain (each domain = potential Subject Area in feature_list.md)
- [ ] Capabilities specific enough for AI to extract entities and features from them
- [ ] Section anchors present so Feature Cards can link to specific capabilities via prd_ref

**Product Scope must cover:**
- [ ] In-scope capability domains (MVP) - which domains are in MVP
- [ ] Out of scope explicitly listed (strategic decision, not omission)
- [ ] Deferred items with trigger conditions
- [ ] No feature-level detail in scope (that belongs in Phase 5-6)

**Business Model must cover:**
- [ ] Revenue model type stated
- [ ] Pricing structure
- [ ] Unit economics targets (ARPU, churn, LTV/CAC, gross margin)
- [ ] Primary acquisition model

**Success Metrics must cover:**
- [ ] North Star Metric defined
- [ ] Phase 1 exit criteria (measurable)
- [ ] AARRR summary table
- [ ] OKR period and key results

**Constraints must cover:**
- [ ] Technical constraints from Tech Feasibility Report
- [ ] Regulatory requirements from Domain Analysis
- [ ] Regulatory showstoppers explicitly addressed (None or Listed)
- [ ] Business constraints (budget, team size, hard deadlines)

**Synthesis quality must cover:**
- [ ] Value proposition aligned with top validated pains from Problem Validation Summary
- [ ] NSM connected to business model (what customers do = what drives revenue)
- [ ] Roadmap phases aligned with business case investment staging
- [ ] No internal contradictions between sections (market size vs. financial targets, persona vs. pricing)
- [ ] Open questions and critical assumptions surfaced, not hidden

**For SaaS/AI products:**
- [ ] AI product positioning: is AI a feature, the core product, or the infrastructure?
- [ ] AI trust and adoption risk addressed (will target customers trust AI for this task?)
- [ ] Data requirements for AI stated (what data does the AI need, who provides it?)
- [ ] EU AI Act risk category assessed if applicable
- [ ] AI cost impact on gross margin captured in business model section
- [ ] Freemium strategy clarified (free tier, upgrade trigger, cost of free users)
- [ ] SaaS-specific retention risks: single-user risk in B2B (what happens if champion leaves?), multi-seat expansion path

## Save to (Product PRD mode)

```
pureinn-workspace/[project-slug]/product/PRD_master.md
```

**PRD_master is frozen after creation.** Do not update it for new initiatives. New domain/feature scope → Initiative PRD in `initiatives/[slug]/prd.md`.

State update → `state.json`: set `registers.prd_master` to `done`.

---

## INITIATIVE PRD MODE

> Triggered when: Feature Implementation context + Track B discovery complete for a new domain.
> Inputs: `initiatives/[slug]/discovery/` + Viability Assessment outputs.
> Purpose: crystallize discovery for this domain into Business Capabilities → feeds pm-entity-registry (append), pm-business-rules-library (append), pm-features-list (FI append).

### Step 0 (Initiative mode): identify initiative

```
Which initiative is this PRD for?

  Initiative slug: [e.g., ai-onboarding]
  (This determines the save path: initiatives/[slug]/prd.md)

  Does the discovery folder exist at initiatives/[slug]/discovery/?
    A) Yes - I'll read the outputs from there
    B) No / different location - paste or describe discovery outputs below
```

### Step 1 (Initiative mode): gather inputs

```
I need the following for the Initiative PRD:

1. DISCOVERY OUTPUTS
   What did Track B discovery produce? (paste summaries or confirm in context)
   - User interview insights: [paste or "in context"]
   - Competitive analysis: [paste or "none"]
   - Tech feasibility for this domain: [paste or "none"]

2. VIABILITY ASSESSMENT
   From the Feature Viability Assessment, confirm:
   - Target segment / persona for this initiative: [answer]
   - KANO classification: [Must-be / Performance / Delighter]
   - Success metrics (defined before build): [answer]

3. DOMAIN SCOPE
   Which business domain does this initiative cover?
   e.g., "AI-assisted employee onboarding (ONB domain)"

4. EXISTING PRODUCT CONTEXT
   Confirm that product/PRD_master.md exists and is in context.
   This initiative PRD references but does not replace the master.
```

### Step 2 (Initiative mode): generate artifact

Generate a focused PRD for this domain only. No market sizing sections. No full persona rebuild - reference existing personas from PRD_master.

### ARTIFACT: Initiative PRD

Save to: `pureinn-workspace/[project-slug]/initiatives/[slug]/prd.md`

```markdown
# Initiative PRD - [Initiative Name]

> **Initiative:** [slug]
> **Domain:** [e.g., ONB - Employee Onboarding]
> **Date:** [date]
> **Version:** 1.0
> **Status:** Draft
> **Parent PRD:** product/PRD_master.md
> **Discovery source:** initiatives/[slug]/discovery/

---

## 1. Initiative Context

**Why this initiative:**
[2-3 sentences: what customer/business problem prompted this? What changed or was validated?]

**Relationship to existing product:**
[Which existing domains does this touch? What new domain does it introduce?]

**Target users:**
[Reference personas from PRD_master. Note if this initiative serves a different sub-segment.]

---

## 2. Business Capabilities (FDD+SDD input)

What this initiative must enable. Primary input for pm-entity-registry (append), pm-business-rules-library (append), and pm-features-list (FI append).

**Format:** "The system must enable [actor] to [business outcome]." No User Stories.

**[Domain: e.g., Employee Onboarding]**
- The system must enable HR Admins to create role-based onboarding templates with task lists.
- The system must enable the system to generate a personalized onboarding plan for each new employee based on their role.
- The system must enable employees to track their onboarding progress and complete assigned tasks.
- The system must enable line managers to monitor the onboarding status of their direct reports.
- The system must integrate with the HRIS system to receive new hire data automatically.

> Section anchors here - Feature Cards will link to specific capabilities via prd_ref.

---

## 3. Success Metrics

Defined in Viability Assessment - reproduced here for traceability.

| Metric | Target | Measurement method |
|---|---|---|
| [e.g., Time-to-productivity] | [Reduced by X%] | [How measured] |
| [e.g., Onboarding completion rate] | [>X%] | [How measured] |
| [e.g., HR admin time per hire] | [Reduced by X h] | [How measured] |

---

## 4. Scope

### In Scope (MVP for this initiative)

[High-level: which capabilities from Section 2 are in MVP]

### Out of Scope (MVP)

| Item | Reason | Reconsider when |
|---|---|---|
| [capability excluded] | [reason] | [condition] |

---

## 5. Constraints

**Technical constraints specific to this domain:**
[e.g., AI API cost per onboarding plan, HRIS integration limitations]

**Dependencies on existing product:**
[Which existing entities, APIs, or Feature Sets this initiative depends on]

**Regulatory / compliance:**
[Any new compliance requirements introduced by this domain - e.g., data retention for employee data]

---

## 6. Open Questions

| Question | Priority | Owner | Target date |
|---|---|---|---|
| [unresolved] | High / Med | [who] | [when] |

---

## 7. Revision History

| Version | Date | Change |
|---|---|---|
| 1.0 | [date] | Initial - after Track B discovery |
```

### Save to (Initiative mode)

```
pureinn-workspace/[project-slug]/initiatives/[slug]/prd.md
```

**Next steps after Initiative PRD:**
1. `/pm-entity-registry` - append mode: extract ONB entities from Business Capabilities, append to domain/entities.md
2. `/pm-business-rules-library` - append mode: extract ONB rules, append to domain/business_rules.md + decision_models.md
3. `/pm-features-list` - FI append mode: extract FEAT-ONB-* features, append to features/feature_list.md
