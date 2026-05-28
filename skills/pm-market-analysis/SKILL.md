---
name: pm-market-analysis
description: Generate Market Size Analysis (TAM/SAM/SOM), Competitor Analysis, SWOT, and Market Timing Rationale from raw research inputs. Use in Phase 2 (Track C).
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: market analysis, TAM SAM SOM, competitor analysis, SWOT, market sizing, competitive landscape
  role: specialist
  scope: research
  output-format: document
  related-skills: pm-domain-analysis, pm-personas, pm-problem-validation, pm-business-case
---

# PM - Market Analysis

## What this skill does

Takes raw research input (Perplexity/ChatGPT market data, competitor research, manual observations) and produces four structured market artifacts:
1. Market Size Analysis (TAM/SAM/SOM)
2. Competitor Analysis
3. SWOT Analysis
4. Market Timing Rationale ("Why now?")

This is a "bring your data" skill - Claude structures and validates the logic. No hallucinated market numbers.

---

## Dependencies

**Recommended before running:**
- `pm-project-charter` - target segment and geography are defined there

**Produces artifacts used by:**
- `pm-problem-validation` - market analysis is Track C input
- `pm-personas` - segment data informs persona development
- `pm-prd` - market context is a key PRD section
- `pm-product-roadmap` - market sizing and timing feed into roadmap framing

---

## Step 0: Current state check

Check for existing artifacts:
- Market Size Analysis (TAM/SAM/SOM)
- Competitor Analysis
- SWOT Analysis
- Market Timing Rationale

Also check: does a Project Charter exist? Cross-reference target segment and geography stated there.

Look for: market size estimates with no source or low confidence, competitors without pricing data, SWOT without strategic implications, "Why now" not specifically argued.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask the user all questions at once:

```
I need inputs for the Market Analysis.

1. PRODUCT AND MARKET
   What does the product do? (1-2 sentences)
   For whom? (who is the primary customer)
   What is the target geography? (SK, CZ, EU, US, global...)

2. MARKET RESEARCH (paste raw output below)
   Perplexity / ChatGPT output on market data (TAM, volumes, segments...):
   [paste here]

   Competitor research / analysis:
   [paste here]

   Other sources (reports, studies, industry data):
   [paste here]

3. YOUR PERSPECTIVE
   What is your key differentiator vs. existing solutions?
   Why now? What changes (tech, regulation, behavior) are opening this opportunity?
   Which competitors are most dangerous to you? Why?

4. WEAKNESSES AND RISKS
   Where does the market have bigger problems? What don't you know yet?
   What are the barriers to entry in this market?
```

---

## Step 2: Generate artifacts

Generate in English.

---

### ARTIFACT 1: Market Size Analysis

```markdown
# Market Size Analysis - [Product Name]

> **Phase:** 2 - Discovery (Track C: Market Discovery)
> **Date:** [date]
> **Geography:** [target markets]

---

## Market Definition

**Product category:** [e.g., Property management software for short-term rentals]
**Primary customer:** [e.g., Independent hosts with 1-10 properties in Slovakia + Czech Republic]

---

## TAM / SAM / SOM

| Level | Definition | Size | Source / Method |
|---|---|---|---|
| **TAM** (Total Addressable Market) | [All potential customers globally / in category] | $[X]M / [X]M users | [source] |
| **SAM** (Serviceable Addressable Market) | [Subset we can realistically serve - geography, segment] | $[X]M / [X]K users | [source / calculation] |
| **SOM** (Serviceable Obtainable Market) | [Realistic capture in 3-5 years] | $[X]M / [X]K users | [assumption: X% of SAM] |

### Key Assumptions

| Assumption | Value | Confidence |
|---|---|---|
| [e.g., Active STR hosts in Slovakia] | [X,000] | High / Med / Low |
| [e.g., Average revenue per host / year] | $[X] | Med |
| [e.g., Market penetration Year 3] | [X%] | Low - aspirational |

### Calculation Methodology

[Brief explanation of how the numbers were derived - top-down / bottom-up, which data sources]

---

## Market Growth

**CAGR (historical):** [X%] ([source])
**Growth drivers:**
- [Driver 1: e.g., STR regulation creating demand for compliance tools]
- [Driver 2]
- [Driver 3]

**Key market trends:**
- [Trend 1]
- [Trend 2]

---

## Revenue Potential

| Scenario | Year 1 | Year 3 | Assumptions |
|---|---|---|---|
| Conservative | $[X]K | $[X]M | [X% SOM penetration, $X ARPU] |
| Base | $[X]K | $[X]M | [X% SOM penetration, $X ARPU] |
| Optimistic | $[X]M | $[X]M | [X% SOM penetration, $X ARPU] |
```

---

### ARTIFACT 2: Competitor Analysis

```markdown
# Competitor Analysis - [Product Name]

> **Phase:** 2 - Discovery (Track C: Market Discovery)
> **Date:** [date]

---

## Competitive Landscape Map

**Category:** [product category]

| Competitor | Type | Geography | Core Value Prop | Target Segment | Est. Size / Stage |
|---|---|---|---|---|---|
| [Name] | Direct / Indirect / Substitute | [markets] | [what they offer] | [who they serve] | [funded / public / bootstrapped / est. revenue] |
| ... | | | | | |

---

## Head-to-Head Comparison

| Feature / Dimension | [Our Product] | [Competitor 1] | [Competitor 2] | [Competitor 3] |
|---|---|---|---|---|
| [Key capability 1] | ✅ / ❌ / 🔧 | ✅ / ❌ / 🔧 | | |
| [Key capability 2] | | | | |
| [Pricing model] | | | | |
| [Target segment] | | | | |
| [Geographic focus] | | | | |
| [Differentiator] | | | | |

Legend: ✅ = strong / 🔧 = partial / ❌ = absent

---

## Our Competitive Position

**Primary differentiation:** [1-2 sentences - what we do differently and why it matters]

**Defensible advantage:** [what is hard to copy and why]

**Weaknesses vs. competition:** [honest assessment of where we lose today]

---

## Competitive Risks

| Risk | Probability | Mitigation |
|---|---|---|
| [e.g., Competitor X enters our target geography] | High / Med / Low | [response strategy] |
| [e.g., Large player adds our core feature] | | |
```

---

### ARTIFACT 3: SWOT Analysis

```markdown
# SWOT Analysis - [Product Name]

> **Phase:** 2 - Discovery (Track C: Market Discovery)
> **Date:** [date]

---

## SWOT Matrix

| | Positive | Negative |
|---|---|---|
| **Internal** | **Strengths** | **Weaknesses** |
| | [S1: e.g., Deep domain expertise of founders] | [W1: e.g., No existing customer base] |
| | [S2] | [W2] |
| | [S3] | [W3] |
| **External** | **Opportunities** | **Threats** |
| | [O1: e.g., Regulation creating compliance gap] | [T1: e.g., Well-funded competitor entering market] |
| | [O2] | [T2] |
| | [O3] | [T3] |

---

## Strategic Implications

**SO Strategies (Strengths + Opportunities):**
- [How to use strengths to capture opportunities]

**WO Strategies (Weaknesses + Opportunities):**
- [How to overcome weaknesses to capture opportunities]

**ST Strategies (Strengths + Threats):**
- [How to use strengths to mitigate threats]

**WT Strategies (Weaknesses + Threats):**
- [How to minimize weaknesses and avoid threats]

---

## Priority Actions (from SWOT)

1. [Most important strategic move]
2. [Second priority]
3. [Third priority]
```

---

### ARTIFACT 4: Market Timing Rationale

```markdown
# Market Timing Rationale - [Product Name]

> **Phase:** 2 - Discovery (Track C: Market Discovery)
> **Date:** [date]

---

## "Why Now?" Statement

[2-3 sentences: The specific conditions that make this the right time to build this product. What changed recently that opens the window?]

---

## Enabling Conditions

| Condition | Change | Since When | Impact on Our Opportunity |
|---|---|---|---|
| Technology | [e.g., LLM cost dropped 10x, enabling AI features at SMB price point] | [2023] | [High - makes core feature viable] |
| Regulation | [e.g., EU DSA compliance requirements for marketplaces] | [2024] | [Med - creates new need] |
| Behavior | [e.g., Post-COVID normalization of remote work driving STR demand] | [2021-ongoing] | [High - expanded customer base] |
| Market | [e.g., Airbnb pulling back from certain markets, gap created] | [2023] | [Med - reduced competition] |
| Competition | [e.g., No well-funded player in SK/CZ specifically] | [now] | [High - whitespace] |

---

## Window of Opportunity

**Opens:** [when / what triggered it]
**Closes:** [what could close it - competition, regulation, tech shift]
**Estimated window:** [X months / years]

**Urgency:** [High / Medium / Low] - [brief reason]

---

## Risk of Being Early / Late

| Scenario | Probability | Consequence |
|---|---|---|
| Too early (market not ready) | [Low / Med / High] | [what happens] |
| Right timing | | [expected outcome] |
| Too late (window closes) | | |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Market Size Analysis must cover:**
- [ ] TAM defined with source and methodology (top-down or bottom-up)
- [ ] SAM defined (geography + segment filter applied)
- [ ] SOM defined with realistic penetration assumption and timeline
- [ ] Market penetration target stated (% of SAM we aim to capture)
- [ ] Key assumptions behind numbers listed with confidence level
- [ ] Revenue scenarios (conservative / base / optimistic)

**Market Timing Rationale must cover:**
- [ ] "Why now" stated with specific enabling conditions (tech, regulation, behavior, market)
- [ ] Window of opportunity defined (opens when, closes when, estimated duration)
- [ ] Risk of being too early assessed
- [ ] Risk of being too late assessed
- [ ] Long-term viability: will the problem exist in 5+ years?

**Competitor Analysis must cover:**
- [ ] Direct competitors identified and profiled
- [ ] Indirect competitors and substitutes identified
- [ ] Key functionalities per competitor mapped
- [ ] Competitor weaknesses / gaps identified (our opportunity)
- [ ] Competitor pricing models documented
- [ ] Customer feedback on competitors captured (reviews, forums, interviews)
- [ ] Competitor GTM strategy assessed
- [ ] Our competitive position and defensible advantage stated
- [ ] For SaaS/AI: AI commoditization risk assessed (is the core AI feature becoming table stakes?)
- [ ] For SaaS/AI: platform risk assessed (are any competitors also our suppliers - e.g., Microsoft, Google, OpenAI?)

**SWOT Analysis must cover:**
- [ ] Strengths (internal, positive)
- [ ] Weaknesses (internal, negative - honest assessment)
- [ ] Opportunities (external, positive)
- [ ] Threats (external, negative)
- [ ] Strategic implications per quadrant (SO, WO, ST, WT)
- [ ] Priority actions derived from SWOT

## Notion

Read `pureinn-variables.md` for keys "Competitor Analysis" and "SWOT Analysis" → if URLs present, remind user after saving:
`Competitor Analysis saved locally. Update Notion: [Competitor Analysis URL]`
`SWOT Analysis saved locally. Update Notion: [SWOT Analysis URL]`

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-2/market-size-analysis.md
pureinn-workspace/[project-slug]/artifacts/phase-2/competitor-analysis.md
pureinn-workspace/[project-slug]/artifacts/phase-2/swot-analysis.md
pureinn-workspace/[project-slug]/artifacts/phase-2/market-timing-rationale.md
```
