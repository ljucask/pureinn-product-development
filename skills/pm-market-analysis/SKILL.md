---
name: pm-market-analysis
description: Generate Market Size Analysis (TAM/SAM/SOM), Competitor Analysis, SWOT, and Market Timing Rationale from raw research inputs. Use in Phase 2 (Track C).
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.1.0"
  domain: product-management
  triggers: market analysis, TAM SAM SOM, competitor analysis, SWOT, market sizing, competitive landscape
  role: specialist
  scope: research
  output-format: document
  related-skills: pm-domain-analysis, pm-personas, pm-problem-validation, pm-business-case
---

# PM - Market Analysis


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Takes raw research input (Perplexity/ChatGPT market data, competitor research, manual observations) and produces four structured market artifacts:
1. Market Size Analysis (TAM/SAM/SOM)
2. Competitor Analysis
3. SWOT Analysis
4. Market Timing Rationale ("Why now?")

Three input paths: (A) paste your own research, (B) guided elicitation from domain knowledge, (C) AI-powered research via OpenAI web search (requires OPENAI_API_KEY in pureinn-variables.md).

Path A and C produce research-backed artifacts. Path B produces assumption-based output marked for validation.

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

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

### Re-run with new inputs (delta mode)

If market analysis already exists and you are re-running it because new research arrived (competitor teardown, bottom-up TAM, new sources), do NOT rewrite from scratch and do NOT duplicate existing content. Append + operate in delta mode (on re-run: compare against the prior artifact, update only what new evidence supports, and show the delta before finalizing; never silently overwrite - full standard in CLAUDE.md):

1. **Read the current analysis first** and capture its claims in the sections most sensitive to the new input: Market Definition, TAM/SAM/SOM, Competitor landscape, SWOT, "Why Now".
2. **Re-validate against the new sources:** new market research, competitor teardown, TAM build-up, any new pricing evidence.
3. **Change only what the new evidence supports.** Append genuinely new findings; where new data revises a prior figure or claim, mark `[UPDATED - previous: X / new: Y - reason: which source drove it]`; leave what the new input does not address `[UNCHANGED]`. Where sources conflict, surface `[CONFLICT]` rather than averaging.
4. **Show the delta and wait for confirmation before writing** - never silently overwrite a prior market conclusion or TAM figure.
5. **Surface the cascade:** after updating, name the downstream artifacts now possibly inconsistent - `/pm-prd` (Market Context), `/pm-product-roadmap` (Problem&Market), `/pm-business-model` (revenue potential + pricing/WTP) - and recommend `/pm-audit strategy` to verify the whole strategic layer still agrees.

---

## Step 1: Gather inputs

First, check `pureinn-workspace/[slug]/pureinn-variables.md` for `OPENAI_API_KEY`. If present and non-blank, Path C is available. Then ask:

How do you want to approach market research?

  A) I have research data - I'll paste Perplexity/ChatGPT output, reports, or competitor research
  B) No research yet - guide me through domain knowledge elicitation
  C) AI-powered research - use OpenAI to research the market automatically (requires OPENAI_API_KEY in pureinn-variables.md)

If user selects C and OPENAI_API_KEY is blank: tell the user to add their OpenAI API key to `pureinn-workspace/[slug]/pureinn-variables.md` under `AI Research > OPENAI_API_KEY`, then re-run. Do not proceed with Path C without the key.

---

### Path A - Research data available

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

### Path B - No research data (guided elicitation)

Guide the user through 3 rounds to reconstruct a market picture from domain knowledge. Flag explicitly what needs external validation. Output marked as assumption-based.

**Group 1 of 3 - Market definition**

Use AskUserQuestion tool for these two questions:

What is the target geography for this product?

  A) One country - focused single market
  B) Regional - 2 to 5 countries with similar characteristics
  C) Global from day one
  D) Other - describe

How would you describe the current state of the market?

  A) New category - no clear solution exists today, problem is underserved
  B) Emerging - solutions exist but no clear winner, market is consolidating
  C) Established - clear leaders exist, competing on differentiation
  D) Commoditized - price competition dominates

Then ask as plain text:

What market or industry is this? Describe it as a customer would, not as a tech category.

Name the 2-3 main competitors or alternatives customers use today. What do they do well and where do they fall short?

After answers, confirm and proceed.

---

**Group 2 of 3 - Market size and dynamics**

Ask all as plain text:

How large do you estimate the addressable market to be? Give your best reasoning - rough orders of magnitude are fine. (e.g., "~50,000 property managers in Slovakia and Czech Republic based on housing data")

Is the market growing, stable, or shrinking? What is driving that? Is there a specific event, regulation, or technology shift creating a window right now?

What is the biggest failure of existing solutions? Why are customers not fully satisfied with what is available today?

What are the main barriers to entering this market? (regulatory, technical, long sales cycles, incumbent relationships, capital required)

After answers, confirm: "Does this match your understanding of the market?"

---

**Group 3 of 3 - Positioning and defensibility**

Use AskUserQuestion tool for these two questions:

How defensible is your position in this market once you launch?

  A) Strong moat - proprietary data, network effects, or regulatory advantage
  B) Moderate - first-mover advantage, deep domain expertise, or strong brand potential
  C) Thin - primarily execution advantage, replicable by well-funded competitor
  D) Unknown - too early to assess

What is your biggest uncertainty about this market?

  A) Whether the problem is large enough to build a business on
  B) Whether customers will actually pay for a solution
  C) Whether you can acquire customers at a sustainable cost
  D) Whether a larger player will enter and outcompete you

Then ask as plain text:

Why would a customer choose you over the alternatives you named? What is your key differentiator?

Why now? What has changed recently - in technology, regulation, customer behavior, or market conditions - that makes this the right moment?

After answers, show complete summary. Flag explicitly which claims need external data validation before using in investor materials or strategy decisions.

Note at the top of every generated artifact: `> Assumption-based - built from founder domain knowledge. Claims marked [NEEDS VALIDATION] should be verified with external sources before treating as reliable.`

---

### Path C - AI-powered research (OpenAI)

Ask these questions as plain text:

What does the product do? (1-2 sentences)
Who is the primary customer?
What is the target geography? (SK, CZ, EU, US, global...)
Who are the 2-3 main competitors or alternatives?
Is there a specific market segment or angle you want the research to focus on?

After receiving answers, read `OPENAI_API_KEY` from `pureinn-workspace/[slug]/pureinn-variables.md`.

Run the following research queries using the Bash tool (one call per query):

**Query 1 - Market size and growth:**
```bash
curl -s https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "tools": [{"type": "web_search_preview"}],
    "input": "Market size, TAM, growth rate and key trends for [product category] in [geography]. Include recent statistics, CAGR, and data sources."
  }'
```

**Query 2 - Competitor research:**
```bash
curl -s https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "tools": [{"type": "web_search_preview"}],
    "input": "Competitor analysis for [competitor names] in [product category]: pricing, target customers, key features, market position, funding stage, weaknesses. Include recent news."
  }'
```

**Query 3 - Market timing and enabling conditions:**
```bash
curl -s https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "tools": [{"type": "web_search_preview"}],
    "input": "What recent changes (regulation, technology, customer behavior, market events) are creating new opportunities in [product category] in [geography]? Why is now a good or bad time to enter this market?"
  }'
```

Replace `$OPENAI_API_KEY` with the actual key value read from pureinn-variables.md. Replace placeholders with the user's actual product, geography, and competitor names.

After running all three queries: extract the research content from the `output[].content[].text` field of each response. Show the user a brief summary of what was found and cite sources from `output[].content[].annotations[]` where available.

Then proceed to Step 2 using the AI research output as the data input (same as Path A, but sourced from the API responses).

Note at the top of every generated artifact: `> AI-researched - market data retrieved via OpenAI web search on [date]. Verify critical numbers against primary sources before using in investor materials.`

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
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/market-size-analysis.md
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/competitor-analysis.md
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/swot-analysis.md
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/market-timing-rationale.md
```

---

## Handoff

**Čo si teraz má:** Market Size (TAM/SAM/SOM), competitor analysis, SWOT - vieš veľkosť príležitosti a konkurenčný kontext.

**Ďalší krok:** Dokonči Phase 2 tracky, potom `/pm-problem-validation`. Trhové dáta neskôr vstúpia do `/pm-lean-canvas` a `/pm-business-case`.

**Môžeš preskočiť ak:** Trh a konkurenciu už máš zmapované z existujúcej analýzy.
