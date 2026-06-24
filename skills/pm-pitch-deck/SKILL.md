---
name: pm-pitch-deck
description: Generate a structured pitch deck content brief. Determines presentation type, audience, and style via questionnaire. Applies validated investor feedback guidelines (82 + 590 deck analyses) to every slide. Outputs slide-by-slide content spec ready for Gamma.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: pitch deck, investor pitch, fundraising, presentation, Gamma deck, slide content
  role: specialist
  scope: communication
  output-format: document
  related-skills: pm-lean-canvas, pm-business-case, pm-problem-validation, pm-kotler
---

# PM - Pitch Deck

## What this skill does

Produces a slide-by-slide content brief for a pitch deck. Does not generate slides directly - it generates structured content that Gamma uses to build the visual presentation.

Two-step process:
1. Intake questionnaire - determines type, audience, style, maintenance model
2. Content generation - maps existing Pureinn artifacts to slides, applies quality rules per slide

Quality rules are derived from analysis of 82 reviewed pre-seed/seed pitch decks and 590 investor Reddit comments. These are constraints, not suggestions - every slide is generated to pass them.

**Gamma integration:** Once content brief is complete, the skill passes it to Gamma MCP to produce the visual deck. Requires Gamma MCP connected (`claude.ai Gamma` via `/mcp`). If Gamma is not connected, the skill stops after Step 5 and outputs the content brief as a standalone artifact.

---

## Dependencies

**Recommended before running:**
- `pm-lean-canvas` - business model, UVP, channels, revenue
- `pm-problem-validation` - problem evidence and interview quotes
- `pm-personas` - specific customer profile for the problem story
- `pm-market-analysis` - market size data (bottom-up preferred)
- `pm-business-case` - financial projections and ask
- `pm-hypotheses` - traction evidence, validation results
- `pm-kotler` - differentiation and positioning

**Produces artifacts used by:**
- External investors / partners / customers (primary audience)
- `pm-product-roadmap` - milestone and ask should match roadmap

---

## Step 0: Current state check

Check for existing artifact:
- `pureinn-workspace/[slug]/artifacts/phase-3-define/pitch-deck-brief.md`

Check which Pureinn artifacts exist (these will be pulled into slides):
- Lean Canvas, Problem Validation, Personas, Market Analysis, Business Case, Hypothesis Register, Kotler Five Levels

Flag missing artifacts - they represent gaps Claude cannot fill from thin air. User must provide the missing data manually during Step 2.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Intake questionnaire

Questions are grouped into 2 rounds. Ask option-based questions together via interactive call, open-text questions as plain text. Show a confirmation summary after each group.

Do not proceed without answers to Group 1 questions 1-4. Group 2 questions have defaults if skipped.

---

### Group 1 of 2 - What you're creating

Use AskUserQuestion tool for these two questions:

What type of presentation is this?

  A) Investor pitch (pre-seed, seed, or Series A)
  B) Demo Day (short slot, goal: be remembered, get follow-up)
  C) Sales or partnership pitch (goal: customer trial, contract, or strategic partner)
  D) Internal / grant / accelerator (goal: budget approval or program acceptance)

Where is the company right now?

  A) Idea / pre-product (no users yet)
  B) MVP / prototype (first users, no revenue)
  C) Early traction (paying customers or strong engagement signals)
  D) Revenue-stage (consistent MRR, growing)

Then ask these three questions as plain text:

Who will read or watch this? Describe their background, how much they know about your market, and what they care about most.

What is the presentation context? Live pitch or sent ahead (self-read)? If live: how many minutes? If sent: teaser or follow-up?

After receiving all Group 1 answers, output a summary:

```
Here's what I understand:
- Deck type: [type]
- Company stage: [stage]
- Audience: [summary]
- Context: [live/sent, timing]

Is this correct, or anything to adjust before we continue?
```

Wait for confirmation. If corrections needed, update and re-confirm. Then proceed to Group 2.

---

### Group 2 of 2 - Style and maintenance (optional, defaults apply if skipped)

Ask as plain text:

Style preferences: Visual-heavy or content-balanced? Data-driven or story-driven? Formal or conversational tone? Any visual references or brands you want to match? (Skip any you don't have strong preferences on - defaults will be used.)

Maintenance: One-time deck or living document? If living: what version is this?

---

## Step 2: Artifact mapping

Before generating content, map available Pureinn artifacts to slides.

Show the user this mapping table:

| Slide | Source artifact | Status |
|---|---|---|
| Cover / one-liner | Lean Canvas (UVP) | [found / missing] |
| Why Now | Market Analysis, Problem Validation | [found / missing] |
| Problem | Problem Validation, Personas, JTBD | [found / missing] |
| Solution | Lean Canvas (Solution), Kotler (Level 2-3) | [found / missing] |
| Product | [user must provide screenshots or mockup links] | [always manual] |
| Market size | Market Analysis (bottom-up) | [found / missing] |
| Business model | Lean Canvas (Revenue Streams, Cost) | [found / missing] |
| Traction | Hypothesis Register (Results), Business Case | [found / missing] |
| Go-to-market | Lean Canvas (Channels), Business Case | [found / missing] |
| Competition | Market Analysis (Competitor Analysis) | [found / missing] |
| Team | [user must provide] | [always manual] |
| Ask | Business Case (Investment section) | [found / missing] |
| Financials (appendix) | Business Case (projections) | [found / missing] |

For any missing artifact, ask the user to provide the data in plain text before continuing.

---

## Step 3: Slide structure by presentation type

Use the correct structure based on the answer to Question 1.

### Investor pitch - pre-seed / seed (10-12 slides)

```
1.  Cover
2.  Why Now
3.  Problem
4.  Solution
5.  Product (screenshots / demo)
6.  Market size
7.  Business model
8.  Traction
9.  Go-to-market
10. Competition
11. Team
12. Ask
    [Appendix: financials, additional product screens, supporting data]
```

### Investor pitch - Series A (12-14 slides)

```
1.  Cover
2.  Company snapshot (traction summary at-a-glance)
3.  Why Now
4.  Problem
5.  Solution
6.  Product
7.  Market size
8.  Business model + unit economics
9.  Traction (growth, retention, cohorts)
10. Go-to-market (proven channels + expansion plan)
11. Competition
12. Team
13. Financial projections (P&L, path to break-even)
14. Ask
    [Appendix: detailed financials, customer case studies, market deep-dive]
```

### Demo Day (5-7 slides)

```
1. Hook + company one-liner
2. Problem (30 seconds, emotional)
3. Solution + product (screenshot mandatory)
4. Traction (one number, one chart)
5. Ask + contact
   [optional: 6. Why Now, 7. Team]
```

### Sales pitch (8-10 slides)

```
1.  Cover
2.  Their problem (specific to this customer's context)
3.  Why existing solutions fall short
4.  Our solution (outcome, not features)
5.  Product walkthrough (screenshots)
6.  Customer results / proof
7.  Why us (differentiation)
8.  Pricing and packaging
9.  Next steps
10. Contact
```

### Partnership pitch (6-8 slides)

```
1. Cover
2. Who we are (one-liner + traction signal)
3. Market opportunity (shared)
4. Why this partnership (mutual benefit)
5. What we bring
6. What we need
7. Proposed terms / structure
8. Next steps + contact
```

### Internal / stakeholder pitch (8-15 slides)

```
1.  Cover
2.  Executive summary (recommendation + ask upfront)
3.  Problem / opportunity
4.  Current state vs. desired state
5.  Proposed solution
6.  Business case (costs, benefits, ROI)
7.  Risks and mitigations
8.  Implementation roadmap
9.  Success metrics
10. Ask (decision, budget, resources)
11. Contact
```

### Grant / accelerator (follows program template)

If program has a defined template, ask user to provide it. Apply quality rules to each section. Do not invent grant-specific criteria.

---

## Step 4: Content quality rules

These rules apply to every slide. They are derived from analysis of 82 investor-reviewed pre-seed/seed decks and 590 Reddit investor comments.

Apply these as hard constraints when generating content in Step 5.

### Universal rules (every slide)

- **One message per slide.** If a slide tries to say two things, split it or cut one.
- **No jargon.** Assume the reader does not know your industry acronyms or technical architecture details.
- **No text walls.** Each slide should be readable in under 10 seconds.
- **Grammar.** Every line of text must be proofread. Typos signal poor attention to detail.
- **Contact info.** Appears on cover and last slide. Deck gets forwarded - make it findable.
- **Send as PDF.** Note in the content brief: always export to PDF before sending. Fonts and layouts break in .pptx across systems.

### Cover slide

- Include: company name, one-liner (what / for whom / what outcome), contact email, logo if exists.
- One-liner format: "[Product] helps [specific customer] [specific outcome]." No buzzwords.
- Do not waste the cover with generic taglines or abstract imagery without text.

### Why Now slide

- Must answer: what changed in the world that makes this problem more urgent today than 2 years ago?
- Valid triggers: behavior shift, regulation change, technology enabler, market collapse of incumbent, generational transition.
- "Because AI" is not a Why Now unless paired with a specific capability that did not exist before and a specific customer behavior that has changed.
- Source: Market Analysis (market timing rationale) if available.

### Problem slide

- Tell a story. Give the customer a name. Describe one specific moment where the problem hit them hard.
- If the founder has personally lived this problem: lead with that. It is the strongest possible signal.
- Use own evidence: "We talked to 47 people in this role. 39 listed this as a top-3 pain point." Do not cite Statista or industry report PDFs.
- One slide only. Do not add solution or market size here.
- Existing alternatives: name what customers do today (competitor, workaround, manual process, doing nothing).

### Solution slide

- Describe what the product does, not how it works.
- Benefits, not features. "Cuts reconciliation from 4 hours to 20 minutes" not "AI-powered multi-tenant architecture."
- The grandma test: can someone who knows nothing about your industry understand the outcome in 30 seconds?
- Do not explain the technical implementation here.

### Product slide

- Show screenshots. Real product if it exists, mockups if it does not.
- Add one line under each screenshot explaining what the viewer is seeing.
- Demo beats explanation. If presenting live, this is where you show the product running.
- Show the product early in the deck - do not save it for slide 8.

### Market size slide

- Do not use top-down Statista numbers. Investors know you did this and it signals lazy thinking.
- Bottom-up calculation: [number of specific people or companies with this problem] x [realistic price per year] = your target market.
- If TAM is too broad, it signals you do not know who your customer is. Niche down.
- Show the math. One slide with the formula and the numbers.

### Business model slide

- Show 1-3 revenue streams maximum. More than 3 signals lack of focus.
- Make it clear: who pays, what they pay, how often.
- If freemium: show conversion rate assumption. If usage-based: show unit economics.

### Traction slide

- Most important chart: retention. How many users are still active at week 1, 2, 4, 8, 12?
- A retention curve that flattens signals PMF. A curve that drops to zero says users tried once and left.
- Context is everything. "10K users" means nothing. "10K users, 23% MoM growth over 6 months, 68% still active after 3 months" tells a story.
- Explain anomalies. If there is a spike, say why. If growth slowed, say why and what changed.
- Show evidence of demand even if pre-revenue: early adopters, beta testers, pre-orders, LOIs, waitlist size with conversion signal.

### Go-to-market slide

- Pick one channel. Not a list. Not "SEO, partnerships, and paid ads."
- Show what acquiring one customer through that channel actually looks like in concrete steps.
- Example: "30 cold emails per week → 3 replies → 1 customer." Show evidence this is working, even at small scale.
- Include CAC (cost to acquire one customer) and LTV if known. Show CAC < LTV.
- If using influencers or partnerships: name specific people or companies, not categories.
- Weak GTMs ("we will leverage social media") are the most common failure mode on this slide.

### Competition slide

- Use an X-Y positioning map. Two axes that your customers actually care about (not axes that conveniently make you look best).
- Name all competitors. Including large ones. Avoiding them looks like you do not understand the market.
- Be honest about positioning. Investors who know the space will see through a misleading map.

### Team slide

- Answer one question: why is THIS team uniquely suited for THIS problem right now?
- Lead with lived experience, domain expertise, unfair access, or track record in this specific problem.
- Do not include advisors, wealthy friends, or one-time mentors on the main team slide.
- If advisors are genuinely notable, they go on a separate slide.
- Names + titles + one sentence of relevant proof per person. Not a LinkedIn dump.

### Ask slide

- One sentence: [$ amount] gets us to [specific milestone] with [runway in months].
- Bad: "We need $2M for hiring and marketing."
- Good: "$2M gets us to $100K MRR with 18 months of runway."
- Use of funds: 2-3 lines maximum. Shows you have thought about how the money translates to outcomes.
- If raising equity: include valuation if you have one, or note "open to discuss" if not.

### First and last slide rule

- First slide (cover) and last slide (ask or contact) stay on screen longest during a live pitch - before you start and during Q&A.
- Both must work standalone. Contact info on both.
- Do not waste either slide on abstract visuals or logos without substance.

---

## Step 5: Generate slide-by-slide content brief

For each slide in the selected structure, generate:

```markdown
## Slide [N]: [Slide name]

**Headline:** [The one message of this slide - 8 words max]

**Body content:**
[Bullet points or short paragraphs - what goes on this slide]

**Data / proof to include:**
[Specific numbers, quotes, or evidence from Pureinn artifacts]

**Visual suggestion:**
[What type of visual element would work: chart, screenshot, photo, X-Y map, table, icon set]

**Source artifact:**
[Which Pureinn artifact this content is drawn from, or "Manual input required"]

**Quality check:**
[Flags: anything on this slide that violates the quality rules above]
```

After all slides, add:

```markdown
## Common mistakes check

| Rule | Status | Note |
|---|---|---|
| One message per slide | Pass / Fail | [which slide violates this] |
| No top-down market sizing | Pass / Fail | |
| GTM = one channel with specifics | Pass / Fail | |
| Team = unfair advantage, not CV | Pass / Fail | |
| Ask = $ → milestone → runway | Pass / Fail | |
| Traction has retention data | Pass / Fail | |
| Contact info on cover + last slide | Pass / Fail | |
| Product shown early (before slide 6) | Pass / Fail | |
| Why Now is substantive (not just AI) | Pass / Fail | |
| Problem slide has own evidence | Pass / Fail | |

**Open items before sending to Gamma:**
[List any slides where user still needs to provide data, screenshots, or team bios]
```

---

## Step 6: Gamma integration

**Requires:** Gamma MCP connected (`claude.ai Gamma` via `/mcp`).

If Gamma MCP tools are not available:
```
Gamma MCP is not connected. The content brief above is your pitch deck spec.
To generate the visual deck:
1. Run /mcp in Claude Code
2. Select "claude.ai Gamma" and complete authentication
3. Re-run /pm-pitch-deck - it will detect the existing brief and proceed to Gamma directly
```

If Gamma MCP is connected, proceed as follows:

### 6a. Select theme (if user specified a style preference in Step 1)

Call `mcp__claude_ai_Gamma__get_themes` to retrieve available themes.
Match the user's style description (e.g. "professional", "modern", "minimal", "bold") against theme tone and color keywords.
If user did not specify a style → omit themeId and let Gamma use its default.

### 6b. Prepare the inputText

Format the content brief as one section per slide, separated by `---`. Use the Slide Name as a heading.
Each section should contain: headline + bullet points (body content from Step 5).
Do NOT include visual suggestions, source artifact notes, or quality check lines - these are for Claude's reference only, not for Gamma.

Example structure:
```
## Cover
[company name] - [one-liner]
Contact: [email]

---

## Why Now
[headline]
- [bullet 1]
- [bullet 2]

---

## Problem
[story headline]
[narrative sentence]
- Evidence: [quote or data point]
- Existing alternative: [what they use today]

---
[...continue for all slides...]
```

### 6c. Call generate

Use `mcp__claude_ai_Gamma__generate` with these parameters:

| Parameter | Value | Source |
|---|---|---|
| `inputText` | Formatted content brief (see 6b) | Step 5 output |
| `cardSplit` | `"inputTextBreaks"` | Always - honors `---` slide separators |
| `textMode` | `"generate"` | Lets Gamma expand bullets into natural slide text |
| `numCards` | Based on presentation type (investor: 12, demo day: 6, sales: 9, partnership: 7, internal: 10) | Step 1 answer |
| `textOptions.tone` | `"professional"` or `"conversational"` per Step 1 style | Step 1 answer |
| `textOptions.amount` | `"brief"` | Always for pitch decks - one message per slide |
| `textOptions.audience` | Audience description from Step 1 | Step 1 answer |
| `cardOptions.dimensions` | `"16x9"` | Always for presentations |
| `imageOptions.stylePreset` | `"illustration"` (default) or `"photorealistic"` if specified | Step 1 style |
| `themeId` | From 6a if user specified style, otherwise omit | Step 1 style |

After Gamma returns the `gammaUrl`:
1. Share the link with the user immediately.
2. Note: **Gamma decks cannot be edited via MCP after generation.** All refinements (slide order, design, text edits) happen in the Gamma editor at the returned URL.
3. Recommend the user export to PDF from the Gamma editor before sharing with investors or partners.

### 6d. Template option (if user has an existing pitch deck template in Gamma)

If the user references an existing template ("use my seed deck template", "use the same format as last time"):
1. Call `mcp__claude_ai_Gamma__get_gammas` with `type: "template"` to list available templates.
2. Identify the matching template by name.
3. Call `mcp__claude_ai_Gamma__generate_from_template` with the template `id` and the formatted content brief as `prompt`.
4. This preserves the template's layout and structure while filling it with the new content.

Do NOT attempt to use a regular (non-template) gamma as a template - it will fail.

---

## Maintenance mode

If an existing `pitch-deck-brief.md` is found in Step 0, offer:

```
A pitch deck brief already exists for this project.

What do you want to do?
  A) Update specific slides (tell me which ones changed)
  B) Create a new version (e.g. post-traction update, Series A version)
  C) Full review against the quality rules checklist
  D) Regenerate from scratch
```

For updates: apply the quality rules to the changed slides only. Note the version and what changed.

---

## Notion

Read `pureinn-variables.md` key "Investor Pitch" → if URL present, remind user after saving:
`Pitch deck brief saved locally. Update Notion: [Investor Pitch URL]`

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-3-define/pitch-deck-brief.md
```

---

## Handoff

**Čo si teraz má:** Pitch Deck content brief - štruktúrovaný príbeh pre investorov alebo partnerov.

**Ďalší krok:** `/pm-prd` (ak ešte nie je) na uzavretie Phase 3b, potom Phase 4 (`/pm-domain-model` → `/pm-entity-registry`).

**Môžeš preskočiť ak:** Nezháňaš kapitál a nepitchuješ partnerom - tento skill je voliteľný, preskoč ho.
