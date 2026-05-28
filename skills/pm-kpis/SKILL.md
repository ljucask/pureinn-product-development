---
name: pm-kpis
description: Generate AARRR funnel metrics, North Star Metric, and OKRs for Phase 3. Requires Business Model Canvas. Produces the measurement framework for the product.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: KPIs, OKRs, north star metric, AARRR, success metrics, funnel metrics
  role: specialist
  scope: strategy
  output-format: document
  related-skills: pm-lean-canvas, pm-business-case, pm-prd, pm-product-roadmap
---

# PM - KPIs & Metrics Framework

## What this skill does

Translates the business model and validated problem into a structured measurement framework:
1. North Star Metric - the single metric that best captures value delivered to customers
2. AARRR Funnel Metrics - acquisition through revenue measurement chain
3. OKRs - Objectives and Key Results for the first 2 quarters post-launch

This is a decision skill, not a data skill. Claude derives metrics from the business model logic and validates their coherence. No invented benchmarks without basis.

---

## Dependencies

**Recommended before running:**
- `pm-business-model` - revenue model and customer relationship type determine the right metrics
- `pm-problem-validation` - validated pains define what "value delivered" means (North Star input)
- `pm-personas` - customer behavior patterns inform leading indicators

**Produces artifacts used by:**
- `pm-prd` - KPIs are a required PRD section
- `pm-business-case` - metrics inform financial model assumptions (conversion rates, retention)
- `pm-product-roadmap` - success metrics anchor roadmap phases

---

## Step 0: Current state check

Check for existing artifacts:
- KPIs & Metrics Framework
- North Star Metric definition
- OKRs

Also check: does a Business Model Canvas exist? Cross-reference the revenue model type - subscription SaaS needs different metrics than marketplace or usage-based. Does a Problem Validation Summary exist? The North Star must connect to the core validated problem.

Look for: North Star that measures activity not value (e.g., "DAU" vs. "properties actively managed"), AARRR metrics without conversion rate benchmarks, OKRs without measurable Key Results (vague KRs like "improve retention" are invalid), missing leading indicators.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask the user all questions at once:

```
I need inputs for the KPIs & Metrics Framework.

1. BUSINESS MODEL CONTEXT
   What is the revenue model? (subscription / usage-based / marketplace / freemium+upgrade)
   What does "active use" look like for your product? (daily? weekly? per booking? per property?)
   What is the core action that creates value for the customer? (the thing they come back to do)

2. GROWTH MODEL
   What is the primary growth motion? (product-led / sales-led / marketing-led / community-led)
   Is there a viral or referral component built in?
   What does the acquisition funnel look like end-to-end? (from awareness to paying customer)

3. RETENTION & ENGAGEMENT
   What does "retained" mean for your product? (logged in weekly? processed X bookings? synced calendar?)
   What is a realistic target for monthly churn? (do you have industry benchmarks?)
   What is the first "aha moment" - when does a new user first get real value?

4. BUSINESS GOALS (NEXT 6-12 MONTHS)
   What are the 2-3 most important outcomes for the business in the next 2 quarters?
   What does success look like at end of Q1 post-launch? Q2?
   Are there any external commitments (investor, pilot partner) that create hard targets?

5. CURRENT HYPOTHESES
   What conversion rates are you assuming? (visitor → signup, trial → paid, free → paid)
   What ARPU / LTV are you targeting?
   Do you have any data points from competitors or industry reports on benchmarks?
```

---

## Step 2: Generate artifacts

Generate in English.

---

### ARTIFACT 1: North Star Metric

```markdown
# North Star Metric - [Product Name]

> **Phase:** 3 - Define & Validation
> **Date:** [date]

---

## North Star Metric

**NSM:** [The one metric]

**Definition:** [Precise definition - what counts, what does not, measurement period]

**Why this metric:**
[2-3 sentences: why this metric best captures value delivered to customers AND predicts long-term business health. What behavior does optimizing this metric drive in the team?]

**What it is NOT:**
[Common trap metric that might be confused with NSM - and why we rejected it]

---

## NSM Decomposition

The North Star breaks into these input metrics (levers the team can pull):

| Input Metric | Lever Type | Who owns it | How it moves the NSM |
|---|---|---|---|
| [e.g., Properties connected per account] | Activation | Product | More properties = more managed = higher NSM |
| [e.g., Bookings processed per week] | Engagement | Product | Frequency of value delivery |
| [e.g., % accounts with 2+ active features] | Depth | Product | Breadth of adoption drives retention |

---

## NSM Targets

| Period | Target | Basis |
|---|---|---|
| End of Month 3 post-launch | [X] | [Early adopter cohort assumption] |
| End of Month 6 | [X] | [Growth model projection] |
| End of Month 12 | [X] | [Business case target] |
```

---

### ARTIFACT 2: AARRR Funnel Metrics

```markdown
# AARRR Metrics - [Product Name]

> **Phase:** 3 - Define & Validation
> **Date:** [date]

---

## Funnel Overview

```
[Acquisition] → [Activation] → [Retention] → [Revenue] → [Referral]
[X visitors]  → [X signups]  → [X active]  → [X paying] → [X referred]
```

---

## Acquisition

**Goal:** Bring the right people to the product.

| Metric | Definition | Target (Month 3) | Target (Month 6) | Channel |
|---|---|---|---|---|
| [e.g., Monthly website visitors] | Unique visitors/month | [X] | [X] | SEO + outreach |
| [e.g., Signups / month] | New accounts created | [X] | [X] | All channels |
| [e.g., CAC] | Total acq. cost / new paying customer | < $[X] | < $[X] | Blended |

**Primary acquisition channel:** [channel + rationale]

**Conversion: Visitor → Signup:** [X%] (basis: [competitor benchmark / assumption])

---

## Activation

**Goal:** Get new users to their first "aha moment" as fast as possible.

**Activation definition:** [Precise: what action = activated? e.g., "Connected first property and processed first booking within 7 days of signup"]

| Metric | Definition | Target |
|---|---|---|
| [Activation rate] | % of signups who complete activation event | [X%] |
| [Time to activation] | Median days from signup to activation event | < [X] days |
| [Onboarding completion rate] | % who complete full onboarding flow | [X%] |

**Activation bottleneck hypothesis:** [Where do you expect drop-off? What is the fix?]

---

## Retention

**Goal:** Keep customers coming back. Retained customers are the foundation of all other metrics.

**Retention definition:** [e.g., "Active in any given week = processed at least 1 booking or updated 1 property listing"]

| Metric | Definition | Target | Industry Benchmark |
|---|---|---|---|
| [Monthly active rate] | % of accounts active in last 30 days | [X%] | [SaaS benchmark: 40-70% depending on use case] |
| [Monthly churn rate] | % of paying customers who cancel | < [X%] | [SaaS: <2% monthly = good] |
| [Day 7 retention] | % of activated users still active Day 7 | [X%] | |
| [Day 30 retention] | % of activated users still active Day 30 | [X%] | |
| [Net Revenue Retention] | MRR from existing customers incl. expansion - churn | > [100%] | [SaaS: 110%+ = excellent] |

**Retention curve shape:** [Do you expect high early churn then flattening? Or gradual decline? Why?]

---

## Revenue

**Goal:** Convert value delivered into sustainable revenue.

| Metric | Definition | Target (Month 6) | Target (Month 12) |
|---|---|---|---|
| [MRR] | Monthly Recurring Revenue | $[X]K | $[X]K |
| [ARPU] | Average Revenue Per User (paying) | $[X]/month | $[X]/month |
| [Free → Paid conversion] | % of free users who upgrade | [X%] | [X%] |
| [Trial → Paid] | % of trials who convert | [X%] | [X%] |
| [LTV] | Average lifetime value per customer | $[X] | $[X] |
| [LTV/CAC ratio] | | > 3:1 | > 3:1 |
| [Payback period] | Months to recover CAC | < [X] months | |

---

## Referral

**Goal:** Turn satisfied customers into a growth channel.

| Metric | Definition | Target |
|---|---|---|
| [NPS] | Net Promoter Score | > [30] (baseline target) |
| [Referral rate] | % of customers who refer at least one other | [X%] |
| [Viral coefficient] | New customers per existing customer referral | [X] |

**Referral mechanism:** [Is there a built-in referral loop? If not, what triggers word of mouth?]

---

## Metric Ownership

| Metric area | Owner | Review cadence |
|---|---|---|
| Acquisition | [Marketing / Growth] | Weekly |
| Activation | [Product] | Weekly |
| Retention | [Product] | Weekly |
| Revenue | [CEO / Finance] | Weekly |
| NPS / Referral | [Customer Success] | Monthly |
```

---

### ARTIFACT 3: OKRs

```markdown
# OKRs - [Product Name]

> **Phase:** 3 - Define & Validation
> **Date:** [date]
> **Period:** [Q1 / Q2 post-launch] — [Start date] to [End date]

---

## OKR Design Principles

- Objectives: qualitative, inspiring, directional - describes what we want to achieve
- Key Results: quantitative, measurable, binary (hit or miss) - describes how we know we achieved it
- Target: ambitious but achievable - 70% completion = success (not 100%)
- Max 3 OKRs per quarter, max 3-4 KRs per Objective

---

## Q1 OKRs (Post-Launch)

### O1: [e.g., Prove product-market fit with early adopters]

| Key Result | Target | Current | Status |
|---|---|---|---|
| KR1: [e.g., Reach X paying customers] | [X] | 0 | Not started |
| KR2: [e.g., Achieve Day 30 retention of X%] | [X%] | - | Not started |
| KR3: [e.g., NPS > X with first cohort] | [X] | - | Not started |

### O2: [e.g., Validate acquisition channel efficiency]

| Key Result | Target | Current | Status |
|---|---|---|---|
| KR1: [e.g., CAC < $X via inbound] | $[X] | - | Not started |
| KR2: [e.g., Activation rate > X%] | [X%] | - | Not started |
| KR3: [e.g., Time to activation < X days] | [X] days | - | Not started |

### O3: [e.g., Build operational foundation for Q2 growth]

| Key Result | Target | Current | Status |
|---|---|---|---|
| KR1: [e.g., Onboarding completion rate > X%] | [X%] | - | Not started |
| KR2: [e.g., Support ticket volume < X per 10 customers] | [X] | - | Not started |

---

## Q2 OKRs (Growth Phase)

### O1: [e.g., Achieve sustainable growth trajectory]

| Key Result | Target | Basis |
|---|---|---|
| KR1: [e.g., MRR of $X] | $[X]K | [From business case] |
| KR2: [e.g., Monthly churn < X%] | < [X%] | [Retention target] |
| KR3: [e.g., NRR > 100%] | > 100% | [Expansion revenue hypothesis] |

### O2: [e.g., Establish primary growth channel]

| Key Result | Target | Basis |
|---|---|---|
| KR1: | | |
| KR2: | | |

---

## What We Are NOT Measuring (Yet)

[List metrics that are tempting but premature - and why we're explicitly deferring them]

- [e.g., Enterprise pipeline - not the segment for Q1-Q2]
- [e.g., International traffic - single market focus for now]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**North Star Metric must cover:**
- [ ] NSM is a value metric (measures value to customer), not a vanity metric (page views, signups)
- [ ] NSM definition is precise - what counts, what doesn't, measurement window
- [ ] NSM decomposition: 2-4 input metrics that drive the NSM
- [ ] NSM targets set for Month 3, 6, 12 post-launch
- [ ] NSM is tied to the core validated pain from Problem Validation Summary

**AARRR must cover:**
- [ ] Activation event defined precisely (not "uses the product" - specific action)
- [ ] Conversion rates estimated for each funnel stage (with confidence level)
- [ ] Retention definition stated (what = active)
- [ ] Day 7 and Day 30 retention targets set
- [ ] Monthly churn target set with basis
- [ ] LTV/CAC ratio target stated (minimum 3:1)
- [ ] Primary acquisition channel identified with CAC target

**OKRs must cover:**
- [ ] Max 3 Objectives per quarter
- [ ] Each KR is measurable and binary (you either hit the number or not)
- [ ] OKRs for Q1 AND Q2 drafted
- [ ] "What we are not measuring yet" section prevents metric sprawl
- [ ] OKRs connected to NSM (at least one KR per quarter moves the NSM)

**For SaaS/AI products:**
- [ ] MRR and ARR targets set
- [ ] Net Revenue Retention (NRR) target set (>100% is the SaaS health indicator)
- [ ] Free → Paid conversion rate target stated (industry: 2-5% freemium, 15-25% trial)
- [ ] AI-specific metrics if applicable: output quality score, AI usage rate, AI cost per user
- [ ] Time to value metric defined (SaaS: faster TTValue = better retention)
- [ ] Product-led growth metrics if PLG motion: PQL (Product Qualified Lead) definition

## Notion push

**Runs after user approves the KPI artifacts.**

Read `pureinn-variables.md` key "KPIs" → get DB URL.
If blank: skip Notion push, output Markdown only.
Check `state.json notion_ids.kpis` for cached ID. Fetch and cache if missing.

Push one entry per metric (North Star + each AARRR metric + each OKR key result) to the KPIs DB.
Use actual schema from notion-fetch to map: metric name → title, target → value field, category (North Star / Acquisition / Activation / Retention / Revenue / Referral / OKR) → type or tag field.

After push: report counts (created, errors).

**Notion page links (OKRs page):**
Read `pureinn-variables.md` key "OKRs" → if URL present, remind user:
```
OKRs artifact saved locally. Paste content into Notion: [OKRs URL]
```

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3/north-star-metric.md
pureinn-workspace/[project-slug]/artifacts/phase-3/aarrr-metrics.md
pureinn-workspace/[project-slug]/artifacts/phase-3/okrs.md
```
