---
name: pm-lean-canvas
description: Generate a Lean Canvas. Phase 3b - one-page business model optimized for validation-stage products. Runs after Go/No-Go = GO. Replaces Business Model Canvas for Greenfield and Feature Implementation.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: lean canvas, business model, UVP, channels, cost structure, revenue streams, one-page business model
  role: specialist
  scope: strategy
  output-format: document
  related-skills: pm-kotler, pm-kpis, pm-business-case, pm-prd
---

# PM - Lean Canvas


## Agent mode (`--agent`)

Podporuje `--agent`: beží autonómne v subagentovi, nadraftuje artefakt z existujúcich vstupov, vráti krátky súhrn + coverage note.

- **Bez flagu** → interaktívne (default); pri ťažkých vstupoch ponúkni agent režim.
- **`--agent`** → poslúchni. Najprv over úplnosť vstupov. Čo chýba: NEVYMÝŠĽAJ - označ `[ASSUMED - čo/prečo]` vo výstupe aj v súhrne. Nikdy nehalucinuj medzeru.
- **Review povinný:** artefakt obsahuje záväzky - po drafte vynúť review používateľa pred finalizáciou; nezavieraj rozhodnutia autonómne.

---

## What this skill does

Produces a one-page business model focused on problem-solution fit and early traction. Lean Canvas is optimized for the validation stage - it forces explicit problem/solution pairing, early adopter definition, and unfair advantage thinking before scaling.

Unlike the Business Model Canvas (which maps an established business), Lean Canvas maps a hypothesis. Each block is a bet that needs validation.

No invented market data or assumptions. Claude structures the canvas; user provides the business knowledge from Phase 2 research and Phase 3a Go/No-Go outcomes.

---

## Dependencies

**Recommended before running:**
- `pm-hypotheses` (Results mode) - Go/No-Go verdict must be GO before running this skill
- `design-thinking` - Problem, UVP, and Solution blocks draw directly from design thinking synthesis
- `pm-personas` - Customer Segments and Early Adopters block requires validated persona work
- `pm-market-analysis` - Channels and Revenue Streams informed by market research

**Produces artifacts used by:**
- `pm-prd` - Lean Canvas is a PRD section (business model overview)
- `pm-business-case` - Revenue Streams and Cost Structure from canvas feed financial projections
- `pm-product-roadmap` - channels and key metrics inform roadmap priorities

---

## Step 0: Current state check

Check for existing artifact:
- `pureinn-workspace/[slug]/artifacts/phase-3-define/lean-canvas.md`

Also check: Go/No-Go verdict. If PIVOT or STOP, flag before proceeding - canvas assumptions may need to change.

Check for Design Thinking synthesis and Personas - these are the primary inputs. Note missing inputs in the state table.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask questions in 3 groups. After each group show a summary and wait for confirmation before continuing.

---

### Group 1 of 3 - Problem, customer, solution

Ask all as plain text:

What are the top 3 problems your product solves? Rank them by severity for the customer. For each, name what customers use today as an alternative (competitor, workaround, manual process, or nothing).

Who is your primary target customer? Be specific - not "SMBs" but "ops managers at 10-50 person logistics companies." Who are the early adopters within that segment, and what makes them different from the broader segment? (more pain, more budget, earlier tech adoption, specific trigger event?)

In one sentence: what is the single most compelling reason your target customer should use this product? What outcome do you promise?

What are the top 3 features or capabilities that directly address the top 3 problems? Match each solution to the problem it solves.

After answers, confirm: "Is this problem-solution fit clear and specific enough to build on?"

---

### Group 2 of 3 - Channels, revenue, costs

Use AskUserQuestion tool for these two questions:

What is the primary channel to reach your early adopters?

  A) Product-led - product itself drives acquisition (self-serve, viral, free tier)
  B) Content / inbound - SEO, community, thought leadership
  C) Outbound / sales - direct outreach, demos, relationship selling
  D) Partnership or ecosystem - integrations, resellers, platform distribution

What is the revenue model?

  A) Subscription - flat monthly or annual
  B) Usage-based - pay per action, transaction, or volume
  C) Freemium - free tier with paid upgrade trigger
  D) One-time or marketplace cut

Then ask as plain text:

What is the expected price point for the primary tier and revenue per customer per year at target scale?

What are the top 3 cost drivers and the estimated monthly burn at launch? What cost scales with usage?

After answers, confirm: "Does this revenue and cost model hold together?"

---

### Group 3 of 3 - Metrics and advantage

Ask all as plain text:

What is the one metric that best indicates you are on track? (North Star) What are 2-3 leading indicators you will track weekly in the first 6 months?

What do you have that cannot be easily copied or bought? (proprietary data, domain expertise, regulatory relationships, exclusive partnerships, network effects, brand, unique technology) If nothing yet, say so honestly - "not yet established" is a valid answer that flags a risk to address.

After answers, show complete Lean Canvas summary across all 3 groups. Ask for final confirmation before generating the artifact.

---

## Step 2: Build the Lean Canvas

Generate the canvas in two formats: table view (for quick reference) and expanded view (with notes and gaps).

```markdown
# Lean Canvas

**Product:** [product name]
**Date:** [date]
**Status:** Phase 3b - Commercial Definition (Go/No-Go: GO)

---

## Canvas Overview

| Block | Content |
|---|---|
| **Problem** | 1. [problem 1] / 2. [problem 2] / 3. [problem 3] |
| **Existing alternatives** | [what customers use today] |
| **Customer segments** | [primary segment] |
| **Early adopters** | [specific early adopter profile] |
| **Unique value proposition** | [one sentence UVP] |
| **High-level concept** | [X for Y or category claim] |
| **Solution** | 1. [solution 1] / 2. [solution 2] / 3. [solution 3] |
| **Channels** | [primary channel] + [secondary] |
| **Revenue streams** | [pricing model] at [price point] |
| **Cost structure** | [top 3 cost drivers] / burn: [monthly estimate] |
| **Key metrics** | North Star: [metric] / Leading: [metric 1, metric 2] |
| **Unfair advantage** | [what cannot be easily copied] |

---

## Expanded View

### Problem

| # | Problem | Severity (1-5) | Existing alternative |
|---|---|---|---|
| 1 | [problem] | [score] | [what they use today] |
| 2 | [problem] | [score] | [what they use today] |
| 3 | [problem] | [score] | [what they use today] |

**Source:** [Phase 2 interviews / analytics / support tickets / other]

---

### Customer Segments

**Primary segment:** [specific description]

**Early adopters:**
- Who: [specific profile]
- Why early adopter: [what makes them different - higher pain, more budget, trigger event]
- Where to find them: [specific channel or community]

---

### Unique Value Proposition

**UVP:** [one sentence]

**High-level concept:** [X for Y / category claim]

**Promise:** [specific outcome the customer gets]

---

### Solution

| Problem | Solution | MDP scope |
|---|---|---|
| [problem 1] | [solution 1] | [what is the minimum to solve this] |
| [problem 2] | [solution 2] | [minimum scope] |
| [problem 3] | [solution 3] | [minimum scope] |

---

### Channels

| Channel | Stage | CAC estimate | Priority |
|---|---|---|---|
| [channel] | [awareness / acquisition / activation] | [estimate or unknown] | Primary / Secondary |

---

### Revenue Streams

**Model:** [subscription / usage-based / one-time / freemium / other]

| Tier | Price | Target customer | Revenue per year |
|---|---|---|---|
| [tier name] | [price/month] | [who buys this] | [ARR per customer] |

**Path to first revenue:** [first paid customer target: when and how]

---

### Cost Structure

| Cost driver | Type | Monthly estimate |
|---|---|---|
| [cost] | Fixed / Variable / Step-function | [estimate] |

**Monthly burn at launch:** [total]
**Runway needed to PMF signal:** [months / milestones]

---

### Key Metrics

**North Star metric:** [metric] - measures [what exactly]

| Leading indicator | Frequency | Target (Month 3) | Target (Month 6) |
|---|---|---|---|
| [metric] | Weekly / Monthly | [target] | [target] |

---

### Unfair Advantage

[What cannot be easily copied or bought. If not yet established, state that explicitly and note what will become the advantage as the business grows.]

---

## Canvas health check

| Block | Status | Risk |
|---|---|---|
| Problem | [validated / assumed / weak] | [note] |
| Customer segments | [validated / assumed / weak] | [note] |
| UVP | [strong / generic / unclear] | [note] |
| Solution | [validated / assumed] | [note] |
| Channels | [tested / assumed] | [note] |
| Revenue | [tested / assumed] | [note] |
| Unfair advantage | [real / aspirational / none yet] | [note] |

**Overall:** [1-2 sentence verdict on canvas strength and biggest open bet]

---

## Open items

| Item | Block | Action needed |
|---|---|---|
| [gap or assumption] | [canvas block] | [what to do / validate] |
```

---

## Step 3: Validate and close

After generating, surface the three most important tensions:

1. **UVP vs. Problem match:** Does the UVP directly address Problem 1 (the highest severity)? If not, the positioning is misaligned.
2. **Segment vs. Channel match:** Can you actually reach the early adopter profile via the primary channel at a reasonable cost?
3. **Unfair advantage:** If the unfair advantage block is empty or generic, flag it explicitly. A business with no unfair advantage is one that anyone can copy once validated. Ask the user to pressure-test this block.

---

## Notion

Read `pureinn-variables.md` key "Lean Canvas" → if URL present, remind user after saving:
`Lean Canvas saved locally. Update Notion: [Lean Canvas URL]`

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3-define/lean-canvas.md
```

---

## Handoff

**Čo si teraz má:** Lean Canvas - one-page biznis model s problémom, riešením, kanálmi a ekonomikou na jednej strane.

**Ďalší krok:** `/pm-kpis` — North Star + AARRR + OKRs, aby si vedel čo merať.
Ak potrebuješ plnší operačný model (etablovaný/komplexný biznis), najprv `/pm-business-model` (Business Model Canvas).

**Môžeš preskočiť ak:** Pre startup vo validačnej fáze Lean Canvas stačí - `/pm-business-model` preskoč.
