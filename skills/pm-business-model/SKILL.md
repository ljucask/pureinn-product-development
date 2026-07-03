---
name: pm-business-model
description: Generate a Business Model Canvas from Phase 2 discovery outputs and founder knowledge. Phase 3b skill - runs after Go/No-Go = GO and Problem Validation Summary. Produces the commercial logic of the product.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.1.0"
  domain: product-management
  triggers: business model, revenue model, pricing strategy, monetization
  role: specialist
  scope: strategy
  output-format: document
  related-skills: pm-lean-canvas, pm-kpis, pm-business-case
---

# PM - Business Model Canvas

## What this skill does

Takes Phase 2 validated problem + market context + founder assumptions and produces a structured Business Model Canvas - the commercial logic that connects the product to revenue.

This is a synthesis skill. It combines what was learned in Phase 2 with strategic decisions about how the product will create, deliver, and capture value.

Output is used directly by `pm-kpis` (metrics follow from revenue model), `pm-business-case` (financial projections extend the model), and `pm-prd` (business model is a core PRD section).

---

## Dependencies

**Recommended before running:**
- `pm-problem-validation` - validated customer segments and core problem are the foundation
- `pm-market-analysis` - market size and competitor positioning inform revenue model choices
- `pm-personas` - personas clarify which customer relationships and channels make sense

**Produces artifacts used by:**
- `pm-kpis` - revenue model drives metric selection (AARRR, North Star)
- `pm-business-case` - business model is the commercial assumption set for financial modeling
- `pm-product-roadmap` - strategic context for roadmap prioritization
- `pm-prd` - business model is a required PRD section

---

## Step 0: Current state check

Check for existing artifacts:
- Business Model Canvas

Also check: does a Problem Validation Summary exist? Does a Market Analysis exist? Cross-reference customer segments and competitive whitespace identified there against the model being built here.

Look for: revenue streams without pricing evidence, value proposition not tied to validated pains, cost structure missing AI/infrastructure costs, no channel strategy defined, customer relationships undefined (self-serve vs. sales-led).

Apply the standard skill interaction pattern (CLAUDE.md).

---

### Re-run with new inputs (delta mode)

If a Business Model Canvas already exists and you are re-running it because new evidence arrived (WTP insights from user research, updated market analysis, re-prioritization), do NOT rewrite from scratch. Operate in delta mode (CLAUDE.md universal standard):

1. **Read the current canvas first** and capture its claims in the blocks most sensitive to the new input: Value Propositions, Customer Segments, Revenue Streams (pricing / take-rate), Channels, Cost Structure.
2. **Re-validate against the new sources:** WTP evidence in `personas.md` / research, `market-analysis.md` revenue potential, updated segments.
3. **Change only what the new evidence supports.** Mark each change `[UPDATED - previous: X / new: Y - reason: which input drove it]`; leave what the new input does not address `[UNCHANGED]`. Pricing/take-rate moves only on real WTP signal, not intuition.
4. **Show the delta and wait for confirmation before writing** - never silently overwrite a prior monetization decision.
5. **Surface the cascade:** after updating, name the downstream artifacts now possibly inconsistent - `/pm-prd` (Business Model section), `/pm-product-roadmap` (revenue assumptions), `/pm-features-list` (if monetization features shift priority) - and recommend `/pm-audit strategy` to verify the whole strategic layer still agrees.

---

## Step 1: Gather inputs

Ask questions in 3 groups. After each group show a summary and wait for confirmation before continuing.

---

### Group 1 of 3 - Value, customer, revenue

Use AskUserQuestion tool for these two questions:

Who is the primary paying customer?

  A) Individual consumer (B2C)
  B) Small business owner or solo professional (B2SMB)
  C) Mid-market company - buyer and user are often the same person (B2B)
  D) Enterprise - buyer and user are different (B2B, sales-led)

What is the primary revenue model?

  A) Subscription - flat monthly or annual fee
  B) Usage-based - pay per action, transaction, or volume
  C) Freemium - free tier with paid upgrade
  D) One-time purchase or marketplace cut

Then ask as plain text:

What is the core value you deliver? Describe the primary outcome the customer gets - not features, but what changes in their work or life.

What is the pricing model and target price point? (per seat, per property, flat monthly, tiered - and what number are you targeting based on research or competitor benchmarks?)

Is there a free tier planned? If yes, what is the trigger that makes a free user upgrade to paid?

After answers, confirm: "Does this commercial logic make sense as a starting point?"

---

### Group 2 of 3 - Channels, relationships, resources

Use AskUserQuestion tool for these two questions:

What is the primary customer acquisition motion?

  A) Product-led - product itself drives acquisition and conversion (self-serve, viral loops)
  B) Content / inbound - SEO, community, thought leadership drives leads
  C) Outbound / sales-led - direct outreach, demos, relationship selling
  D) Partnership or channel - resellers, integrations, ecosystem distribution

What type of relationship do customers expect with this product?

  A) Self-serve tool - they figure it out themselves, low-touch
  B) Assisted onboarding - guided setup, then self-serve
  C) Ongoing managed relationship - CSM, regular check-ins, high-touch
  D) Community-led - peer support and network is the core relationship

Then ask as plain text:

How will you acquire the first 10 to 50 customers specifically? Name the channel and the action.

What is hardest to replicate about your business? What is the defensible core - technology, data, brand, domain expertise, network effects, regulatory position?

After answers, confirm: "Does this match your go-to-market thinking?"

---

### Group 3 of 3 - Operations and economics

Ask all as plain text:

What must you do continuously to deliver value? What are the 2-3 key activities that the business breaks without?

Who do you depend on to operate? Name key partners, APIs, data providers, or integrations that are essential. Are any of these also potential competitors?

What are the primary cost drivers? (team salaries, AI/infrastructure costs, sales, support, compliance) Does the cost per unit go up or down as you scale?

If AI-powered: what is your estimate for AI cost per active user or per transaction per month?

After answers, show complete Business Model summary across all 3 groups. Ask for final confirmation before proceeding to artifact generation.

---

## Step 2: Generate artifact

Generate in English.

---

### ARTIFACT: Business Model Canvas

```markdown
# Business Model Canvas - [Product Name]

> **Phase:** 3 - Define & Validation
> **Date:** [date]
> **Version:** v1 (initial - based on Phase 2 discovery)
> **Status:** Draft - validated against Problem Validation Summary, not yet market-tested

---

## Canvas Overview

| | | |
|---|---|---|
| **Key Partners** | **Key Activities** | **Value Propositions** |
| [partners] | [activities] | [value props] |
| | **Key Resources** | |
| | [resources] | |
| **Cost Structure** | | **Revenue Streams** |
| [costs] | **Customer Relationships** | [revenue] |
| | [relationships] | |
| | **Channels** | **Customer Segments** |
| | [channels] | [segments] |

---

## 1. Value Propositions

**Primary value proposition:**
[1-2 sentences: What outcome does the customer get? What pain disappears?]

**For [Segment 1]:**
- [Specific value delivered]
- [Pain eliminated]
- [Outcome created]

**For [Segment 2] (if applicable):**
- [Specific value delivered]

**Differentiation from alternatives:**
[Why this and not competitor X or status quo - tied to competitive whitespace from Market Analysis]

---

## 2. Customer Segments

| Segment | Type | Size (SAM) | Priority |
|---|---|---|---|
| [Primary segment] | [B2B / B2C / B2B2C] | [X,000 / $XM] | Primary |
| [Secondary segment] | | | Secondary |

**Primary segment decision:** [1-2 sentences on why this is the segment to focus on first]

**B2B specifics (if applicable):**
- Buyer: [who signs / pays]
- User: [who uses daily]
- Champion: [who drives internal adoption]
- Decision process: [self-serve / procurement / executive buy-in]

---

## 3. Channels

**Acquisition channels:**

| Channel | Type | Priority | Estimated CAC | Notes |
|---|---|---|---|---|
| [e.g., Inbound SEO / content] | Inbound | High | Low (long-term) | [detail] |
| [e.g., Direct outreach to hosts] | Outbound | High (early) | Med | [detail] |
| [e.g., Partner referrals] | Partnership | Med | Low | [detail] |

**First 10-50 customer strategy:**
[Specific approach to get the first paying customers - founder-led, direct outreach, community, etc.]

**Onboarding model:** Self-serve / Assisted / Sales-led
[Brief rationale - driven by customer sophistication and price point]

---

## 4. Customer Relationships

**Relationship type:** [e.g., Self-serve SaaS / Community-led / High-touch onboarding]

**Retention mechanism:**
- [What creates stickiness - data lock-in, network effects, habit, contract...]
- [What switching cost does the customer face after 6 months of use]

**Support model:**
- Phase 1 (early): [e.g., Founder-led, email, Intercom]
- Scale: [e.g., Self-serve docs + async support]

**Community / expansion:**
[Is there a community element planned? Referral program? Expansion revenue (upsell/cross-sell)?]

---

## 5. Revenue Streams

**Primary revenue model:** [Subscription / Usage-based / Marketplace / Freemium / Hybrid]

| Revenue Stream | Model | Price Point | Trigger | Est. % of Revenue |
|---|---|---|---|---|
| [Primary: e.g., Monthly subscription] | [Recurring] | [$X/month per property] | [Signup + first property added] | [80%] |
| [Secondary: e.g., Booking fee] | [Transactional] | [X% per booking] | [Booking confirmed] | [20%] |

**Pricing tiers (if applicable):**

| Tier | Price | For whom | Key limits / features |
|---|---|---|---|
| [Free / Starter] | $0 | [Early traction, lead gen] | [X properties, limited features] |
| [Pro] | $X/mo | [Core target customer] | [Full features] |
| [Business] | $X/mo | [Larger operators] | [Multi-user, API access...] |

**Freemium upgrade trigger (if applicable):**
[The specific limit or feature that converts free to paid - must be concrete]

**Unit economics direction:**
- ARPU: $[X]/month
- Estimated churn target: < [X]% monthly
- LTV/CAC target ratio: [3:1 minimum]

---

## 6. Key Resources

| Resource | Type | Own / Partner / Build | Strategic Importance |
|---|---|---|---|
| [e.g., Product + tech stack] | Technology | Build | Core |
| [e.g., AI model / LLM access] | Technology | Partner (API) | Critical dependency |
| [e.g., Domain data / dataset] | Data | Build / Accumulate | Defensible moat |
| [e.g., Founder domain expertise] | Human | Own | High (early stage) |
| [e.g., Brand + community] | Intangible | Build | Long-term moat |

**Defensible core:**
[What resource, once built, is hard to replicate and creates durable advantage]

---

## 7. Key Activities

| Activity | Frequency | Owner | Why it matters |
|---|---|---|---|
| [e.g., Product development] | Continuous | CTO / team | Core value delivery |
| [e.g., Customer success / onboarding] | Per new customer | Founder | Retention driver (early) |
| [e.g., Content / SEO] | Weekly | PM / Marketing | Inbound acquisition |
| [e.g., AI model tuning / prompt engineering] | Ongoing | ML / PM | Output quality maintenance |

---

## 8. Key Partners

| Partner | Role | Dependency Level | Risk |
|---|---|---|---|
| [e.g., Stripe] | Payment processing | High | Low - commodity |
| [e.g., OpenAI / Anthropic] | AI inference | High | Medium - pricing, policy changes |
| [e.g., Airbnb / Booking.com] | Channel / data source | Med | High - platform risk |
| [e.g., Legal counsel] | Compliance | Low-Med | Low |

**Platform risk assessment:**
[Are any key partners also competitors or could become competitors? What is the mitigation?]

---

## 9. Cost Structure

**Cost model type:** Fixed-dominant / Variable-dominant / Mixed

| Cost Category | Type | Est. Scale | Notes |
|---|---|---|---|
| Engineering team | Fixed | [X FTEs] | |
| AI / LLM API costs | Variable | [$X per active user/month] | Critical for SaaS margin |
| Infrastructure (hosting, DB, storage) | Variable + Fixed | [$X/month base + usage] | |
| Customer acquisition | Variable | [$X CAC target] | |
| Compliance / legal | Fixed | [$X/year] | |
| Customer support | Semi-variable | [grows with user count] | |

**Unit economics - COGS:**
[What is included in cost of goods sold? What is gross margin target at scale? (SaaS target: >70%)]

**AI cost sensitivity:**
[If AI usage scales with usage: what happens to margin at 10x users? Is there a cost ceiling or optimization path?]

---

## Business Model Assumptions (to validate)

| Assumption | Current Belief | Confidence | How to validate |
|---|---|---|---|
| [e.g., Customers will pay $X/month] | [Based on competitor pricing + 3 interviews] | Med | [Pricing experiment / waitlist signup] |
| [e.g., Self-serve onboarding will work] | [Based on persona tech sophistication] | Low | [Onboarding test with 5 early adopters] |
| [e.g., CAC < $X via inbound] | [Industry benchmark] | Low | [First campaign results] |
| [e.g., AI cost < $X per user/month] | [API rate card estimate] | Med | [Load testing] |

---

## Business Model Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| [e.g., Pricing too high for SMB segment] | Med | High | [Freemium entry tier / annual discount] |
| [e.g., AI API costs erode margin at scale] | Med | High | [Cost optimization roadmap / model fine-tuning] |
| [e.g., Platform dependency on Airbnb API] | High | High | [Multi-channel strategy, direct booking support] |
| [e.g., Sales cycle too long for B2B] | Low-Med | Med | [Self-serve motion for SMB, sales-assist for enterprise] |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Value Proposition must cover:**
- [ ] Core outcome stated (not features - what the customer achieves)
- [ ] Pain eliminated is the top validated pain from Problem Validation Summary
- [ ] Differentiation from status quo and direct competitors stated
- [ ] Value proposition per segment if multiple segments

**Customer Segments must cover:**
- [ ] Primary segment confirmed and prioritized
- [ ] B2B: buyer / user / champion distinction made
- [ ] Segment size tied to Market Analysis SAM

**Revenue Streams must cover:**
- [ ] Revenue model explicitly chosen (subscription / usage / marketplace / hybrid)
- [ ] Pricing model defined (per seat, per unit, flat, tiered)
- [ ] Price point grounded in research (competitor pricing, interview willingness to pay)
- [ ] Freemium trigger defined if freemium model (must be specific - not vague)
- [ ] Unit economics direction: ARPU, churn target, LTV/CAC target

**Channels must cover:**
- [ ] Acquisition channels identified with CAC estimate
- [ ] First 10-50 customer strategy concrete (not "social media" - specific actions)
- [ ] Onboarding model chosen (self-serve / assisted / sales-led) with rationale

**Cost Structure must cover:**
- [ ] All major cost categories identified
- [ ] AI/LLM API cost per user estimated (for AI products)
- [ ] Gross margin target stated
- [ ] COGS defined (what's in it, what's not)

**Key Partners must cover:**
- [ ] Critical dependencies identified
- [ ] Platform risk assessed (partner = potential competitor?)
- [ ] Single points of failure noted

**Business Model Assumptions:**
- [ ] Key assumptions that could invalidate the model are listed
- [ ] Each assumption has a validation approach
- [ ] Confidence level assigned per assumption

**For SaaS/AI products:**
- [ ] AI inference cost modeled per active user per month
- [ ] Gross margin sensitivity to AI cost increase assessed
- [ ] Freemium conversion rate assumption stated (industry baseline: 2-5%)
- [ ] Annual vs monthly pricing split considered (annual: better LTV, harder early sales)
- [ ] Multi-tenant architecture cost implications noted
- [ ] Network effect potential assessed (does value grow with more users/data?)
- [ ] AI commoditization risk: if core AI feature becomes table stakes, what is the durable differentiator?

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3-define/business-model-canvas.md
```

---

## Handoff

**Čo si teraz má:** Business Model Canvas - plnší operačný pohľad (partneri, aktivity, zdroje, nákladová štruktúra) nad rámec Lean Canvas.

**Ďalší krok:** `/pm-kpis` — North Star + AARRR + OKRs.

**Môžeš preskočiť ak:** Tento skill je sám voliteľný - ak ti stačil `/pm-lean-canvas`, BMC nerob a choď na `/pm-kpis`.
