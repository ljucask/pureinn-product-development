---
name: pm-business-case
description: Generate a Business Case Draft for Phase 3. Synthesizes market size, business model, and KPIs into financial projections and investment rationale. Requires pm-business-model and pm-kpis.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: business case, financial projections, unit economics, ROI, go no go, investment rationale
  role: specialist
  scope: analysis
  output-format: document
  related-skills: pm-kpis, pm-lean-canvas, pm-market-analysis, pm-product-roadmap
---

# PM - Business Case

## What this skill does

Translates Phase 2 market data and Phase 3 business model + metrics into a structured business case:
1. Financial projections (3-year revenue model)
2. Investment requirements
3. Go/No-Go recommendation with explicit assumptions and risks

This is a synthesis skill. Projections are explicitly assumption-based, not predictions. Every number must trace to an assumption the user has stated or derived from Phase 2 research.

No invented financial data. Claude builds the structure and logic; user provides the commercial assumptions.

---

## Dependencies

**Recommended before running:**
- `pm-business-model` - revenue model, pricing, and cost structure are the input
- `pm-kpis` - conversion rate assumptions and ARPU from metrics feed the financial model
- `pm-market-analysis` - TAM/SAM/SOM defines the addressable opportunity ceiling

**Produces artifacts used by:**
- `pm-prd` - business case summary is a PRD section
- `pm-product-roadmap` - investment requirements inform phase sequencing

---

## Step 0: Current state check

Check for existing artifacts:
- Business Case

Also check: does a Business Model Canvas exist? Does a KPIs framework exist? Does a Market Analysis exist? These three are the source inputs. If Business Model Canvas is missing, the financial projections will be unsupported.

Look for: projections without explicit assumptions, cost model missing AI/infrastructure costs, runway calculation missing, no Go/No-Go recommendation, risks listed without mitigation.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask questions in 2 groups. After each group show a summary and wait for confirmation before continuing.

---

### Group 1 of 2 - Revenue and volume assumptions

Use AskUserQuestion tool for these two questions:

What is the funding situation?

  A) Bootstrapped - self-funded, no external investors
  B) Pre-seed / seed - raising or recently closed a round
  C) Series A or later - significant capital, scaling
  D) Grant or accelerator funding

What is the basis for your customer volume targets?

  A) Bottom-up - derived from channel capacity and conversion rates
  B) Top-down - percentage of TAM/SAM
  C) Both - cross-validated with bottom-up and top-down
  D) Intuition / comparable benchmarks only

Then ask as plain text:

What are your revenue assumptions? State: target ARPU (monthly, per paying customer), expected conversion rate (free to paid, or trial to paid), and target monthly churn rate.

What is your customer volume target? How many paying customers by end of Month 6, Year 1, and Year 3?

What growth rate do you expect month-over-month in Year 1 and Year 2?

After answers, confirm: "Do these revenue and volume numbers feel realistic based on your channel and market assumptions?"

---

### Group 2 of 2 - Costs, investment, and go/no-go

Ask all as plain text:

What is the expected team size at launch and monthly burn rate all-in? (salaries, infrastructure, tools, sales, marketing) What are the top 3 cost drivers? If AI-powered: what is the estimated AI cost per active user per month?

How much runway do you need to reach the key milestones? (first 10 customers, PMF signal, break-even) What is the target milestone before the next funding event or break-even if bootstrapped?

What would make you stop? What is the minimum success signal that justifies continuing past Month 3? What is the single biggest risk to this financial model?

After answers, show complete Business Case inputs summary. Ask for final confirmation before generating projections and investment rationale.

---

## Step 2: Generate artifact

Generate in English.

---

### ARTIFACT: Business Case

```markdown
# Business Case - [Product Name]

> **Phase:** 3 - Define & Validation
> **Date:** [date]
> **Version:** Draft v1 - assumption-based projections, not audited forecasts
> **Status:** For internal decision-making only

---

## Executive Summary

**The opportunity:** [2-3 sentences: problem, market, why now]

**The solution:** [1-2 sentences: what we build, for whom, primary differentiation]

**The ask:** [What is needed - investment, decision, resources]

**The return:** [Key financial milestone - e.g., "Break-even at X customers, target MRR of $XK by Month 18"]

**Recommendation:** ✅ Proceed / ⚠️ Proceed with conditions / ❌ Do not proceed
[1-2 sentences: the recommendation and primary rationale]

---

## Market Opportunity

| Metric | Value | Source / Confidence |
|---|---|---|
| TAM | $[X]M | [Market Analysis - High/Med/Low] |
| SAM | $[X]M | [Market Analysis - High/Med/Low] |
| SOM (Year 3) | $[X]M | [Assumption: X% penetration - Low confidence] |
| Market CAGR | [X%] | [Source] |

**Why now (timing):** [1-2 sentences from Market Timing Rationale]

---

## Revenue Model

**Model type:** [Subscription / Usage-based / Marketplace / Freemium + upgrade]

**Pricing:**
- [Tier 1]: $[X]/month - [for whom]
- [Tier 2]: $[X]/month - [for whom]

**Blended ARPU assumption:** $[X]/month

---

## 3-Year Financial Projections

> All projections are assumption-based. Assumptions listed explicitly below.

### Customer Growth

| Period | Free Users | Paying Customers | MoM Growth Rate |
|---|---|---|---|
| Month 3 | [X] | [X] | [X%] |
| Month 6 | [X] | [X] | [X%] |
| Month 12 (EOY1) | [X] | [X] | [X%] |
| Month 24 (EOY2) | [X] | [X] | [X%] |
| Month 36 (EOY3) | [X] | [X] | [X%] |

### Revenue

| Period | MRR | ARR | MoM Growth |
|---|---|---|---|
| Month 3 | $[X]K | $[X]K | - |
| Month 6 | $[X]K | $[X]K | [X%] |
| Month 12 (EOY1) | $[X]K | $[X]K | [X%] |
| Month 24 (EOY2) | $[X]K | $[X]K | [X%] |
| Month 36 (EOY3) | $[X]K | $[X]K | [X%] |

### Cost Structure

| Cost Category | Monthly (Year 1) | Monthly (Year 2) | Monthly (Year 3) | Notes |
|---|---|---|---|---|
| Team (salaries) | $[X]K | $[X]K | $[X]K | [X FTEs] |
| AI / LLM API | $[X] | $[X] | $[X] | [$X/user/month × users] |
| Infrastructure | $[X] | $[X] | $[X] | |
| Sales & Marketing | $[X] | $[X] | $[X] | |
| Operations / Legal | $[X] | $[X] | $[X] | |
| **Total Burn** | **$[X]K** | **$[X]K** | **$[X]K** | |

### Profitability

| Milestone | Period | MRR Required |
|---|---|---|
| Contribution margin positive | [Month X] | $[X]K |
| Operating break-even | [Month X] | $[X]K |
| Cash flow positive | [Month X] | $[X]K |

**Gross margin target:** [X%] (SaaS benchmark: >70% healthy, >80% excellent)

---

## Unit Economics

| Metric | Target | Basis |
|---|---|---|
| ARPU (monthly) | $[X] | [Pricing model] |
| Monthly churn | < [X%] | [Retention target] |
| Customer LTV | $[X] | [ARPU / churn rate] |
| CAC (blended) | < $[X] | [Channel mix assumption] |
| LTV/CAC ratio | > [3:1] | [Target threshold] |
| CAC payback period | < [X] months | [LTV/CAC basis] |
| AI cost / user / month | $[X] | [API rate card × usage estimate] |
| Gross margin per customer | [X%] | [ARPU - COGS] / ARPU |

---

## Investment Requirements

**Total investment required:** $[X]K / $[X]M

**Use of funds:**

| Category | Amount | % | Purpose |
|---|---|---|---|
| Product development | $[X]K | [X%] | [MVP build + Phase 1 features] |
| Team / salaries | $[X]K | [X%] | [X months runway for X FTEs] |
| Sales & Marketing | $[X]K | [X%] | [First acquisition campaigns] |
| Infrastructure + tooling | $[X]K | [X%] | |
| Legal + compliance | $[X]K | [X%] | |
| Buffer / contingency | $[X]K | [X%] | |

**Runway:** [X months at stated burn rate]

**Key milestone this investment must reach:**
[The specific, measurable condition that either justifies the next round or proves viability for bootstrapped continuation]

---

## Financial Assumptions (explicit)

| Assumption | Value | Confidence | Source |
|---|---|---|---|
| Blended ARPU | $[X]/month | Med | [Competitor pricing + 3 interviews] |
| Free → Paid conversion | [X%] | Low | [Industry benchmark for freemium SaaS] |
| Monthly churn | [X%] | Low | [Target - no empirical data yet] |
| CAC (inbound) | $[X] | Low | [Early estimate - to validate in Month 1-2] |
| MoM growth rate (Year 1) | [X%] | Low | [Conservative: founder-led sales assumption] |
| AI cost / user / month | $[X] | Med | [API rate card calculation] |
| Team fully loaded cost | $[X]K/month | High | [Known salaries + benefits] |
| Break-even at | [X] customers | Med | [Fixed costs / contribution margin] |

**Highest-impact assumption (if wrong, model breaks):**
[Identify the single assumption that, if incorrect, changes the recommendation most dramatically]

---

## Scenario Analysis

| Scenario | Key Difference from Base | MRR (Month 12) | Runway Impact |
|---|---|---|---|
| Conservative | [Churn 2x higher, growth 50% lower] | $[X]K | [Runway extends / shortens by X months] |
| Base (this plan) | - | $[X]K | [X months runway] |
| Optimistic | [Viral growth kicks in, churn < 1%] | $[X]K | [Break-even at Month X] |

**What would make the optimistic scenario real:**
[Specific conditions - not "if everything goes well"]

**What would trigger the conservative scenario:**
[Specific conditions - not "if things go badly"]

---

## Key Risks to the Business Case

| Risk | Probability | Impact on Plan | Mitigation |
|---|---|---|---|
| [e.g., Churn higher than assumed] | Med | Extends break-even by [X months] | [Tighter activation, onboarding investment] |
| [e.g., CAC higher than assumed] | High (early) | Reduces runway by [X months] | [Founder-led sales, community-first channel] |
| [e.g., AI API cost increase] | Low-Med | Reduces gross margin by [X%] | [Cost optimization roadmap, model fine-tuning] |
| [e.g., Competitor enters market] | Med | Reduces SAM capture, increases CAC | [Faster speed to market, niche focus] |

---

## Go / No-Go Criteria

**Proceed conditions (all must hold):**
- [ ] [e.g., Problem validation: ≥10 interviews confirm pain with High intensity]
- [ ] [e.g., Willingness to pay: ≥5 potential customers indicate readiness to pay $X+]
- [ ] [e.g., Technical feasibility: no blockers identified in Tech Feasibility Report]
- [ ] [e.g., Legal: no regulatory showstoppers in target markets]
- [ ] [e.g., Funding: $X secured or committed]

**Stop conditions (any one = stop or pivot):**
- [ ] [e.g., Churn > X% monthly after Month 3 with no improvement signal]
- [ ] [e.g., Free → paid conversion < X% after Month 2 of optimization]
- [ ] [e.g., CAC > $X with no improvement path identified]
- [ ] [e.g., Regulatory blocker identified with no workaround]

**Minimum viable success signal (by Month 3 post-launch):**
[The specific, observable signal that justifies continuing to Month 6 and beyond]

---

## Recommendation

**Recommendation:** ✅ Proceed / ⚠️ Proceed with conditions / ❌ Do not proceed

**Rationale:**
[3-5 bullet points: the primary reasons for the recommendation]

**Conditions (if ⚠️):**
[What must be resolved before full commitment]

**Immediate next actions:**
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Financial projections must cover:**
- [ ] 3-year projection horizon (Month 3, 6, 12, 24, 36)
- [ ] Customer count AND revenue at each milestone
- [ ] Cost structure itemized (not just total burn)
- [ ] Gross margin calculated and stated
- [ ] Break-even milestone identified (at what customer count / MRR)

**Unit economics must cover:**
- [ ] ARPU defined and stated
- [ ] Monthly churn rate target
- [ ] LTV calculated (ARPU / monthly churn)
- [ ] CAC target stated
- [ ] LTV/CAC ratio target (minimum 3:1)
- [ ] CAC payback period

**Assumptions must cover:**
- [ ] All major revenue assumptions explicitly listed
- [ ] All cost assumptions explicitly listed
- [ ] Confidence level per assumption
- [ ] Highest-impact assumption identified ("if this is wrong, the model breaks")

**Scenario analysis must cover:**
- [ ] Conservative, Base, Optimistic scenarios
- [ ] Each scenario has a named trigger condition
- [ ] Runway impact per scenario stated

**Investment requirements must cover:**
- [ ] Total amount requested
- [ ] Use of funds breakdown
- [ ] Runway duration
- [ ] Key milestone the investment must reach

**Go/No-Go must cover:**
- [ ] Explicit proceed conditions (measurable, not vague)
- [ ] Explicit stop conditions
- [ ] Minimum viable success signal by Month 3

**For SaaS/AI products:**
- [ ] AI/LLM API cost per user modeled explicitly (not bundled into "infrastructure")
- [ ] Gross margin sensitivity to AI cost increase assessed
- [ ] Freemium conversion economics modeled (cost of free users is real)
- [ ] NRR (Net Revenue Retention) target - the SaaS growth health indicator
- [ ] Annual vs monthly billing mix (annual = better cash, better LTV)
- [ ] Infrastructure cost scaling profile (does it scale linearly or sub-linearly?)

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3-define/business-case.md
```
