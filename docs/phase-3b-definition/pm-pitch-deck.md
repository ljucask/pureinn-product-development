# pm-pitch-deck

> Slide-by-slide pitch deck content brief - built from Pureinn artifacts, delivered via Gamma MCP

**Phase:** 3b - Definition (optional, skip if not fundraising or pitching)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** pitch deck, investor pitch, fundraising, presentation, Gamma deck, slide content

---

## When to use

Phase 3b, after Lean Canvas, Business Case, and Market Analysis are complete. Optional - **skip if not raising capital and not pitching to partners or investors.**

Quality rules are derived from analysis of 82 reviewed pre-seed/seed pitch decks and 590 investor Reddit comments. Applied as constraints to every slide, not as suggestions.

**Skip condition:** Not fundraising, not pitching to external stakeholders, and not applying to an accelerator. This skill adds no value for internal-only product work.

---

## What it produces

Two outputs:

1. **Pitch Deck Content Brief** (`artifacts/phase-3b-definition/pitch-deck-brief.md`) - slide-by-slide structured content ready for Gamma
2. **Visual deck via Gamma MCP** - if Gamma MCP is connected (`claude.ai Gamma` via `/mcp`), the content brief is passed to Gamma to produce the visual presentation

If Gamma is not connected, the skill stops after the content brief and outputs it as a standalone artifact.

---

## How to invoke

```bash
/pm-pitch-deck           # interactive
/pm-pitch-deck --agent   # autonomous draft from existing phase artifacts
```

---

## Deck types

The intake determines which slide structure applies:

| Type | Goal | Key difference |
|---|---|---|
| Investor pitch (pre-seed/seed/Series A) | Raise capital | Ask, traction, unit economics |
| Demo Day | Be remembered, get follow-up | Ultra-short, one memorable hook |
| Sales / partnership pitch | Customer trial, contract, strategic partner | Problem-solution fit, proof |
| Internal / grant / accelerator | Budget approval, program acceptance | ROI framing, milestones |

**Company stage also matters:** the slide emphasis shifts across Idea / MVP / Early Traction / Revenue stage.

---

## Slide structure (Investor pitch, base template)

| Slide | Content |
|---|---|
| 1 - Cover | Company name, tagline, presenter |
| 2 - Problem | The pain, who has it, how often, what it costs them |
| 3 - Solution | What you built, for whom, how it works (no feature lists) |
| 4 - Why Now | Market timing - what changed that makes this possible today |
| 5 - Market | TAM/SAM/SOM, bottom-up preferred |
| 6 - Product | Demo or screenshot - show, don't describe |
| 7 - Business Model | Revenue model, ARPU, pricing |
| 8 - Traction | Evidence: customers, revenue, interviews, waitlist, NPS |
| 9 - Go-to-Market | First 100 customers plan; channels |
| 10 - Competition | Honest landscape + defensible position |
| 11 - Team | Why this team; relevant expertise |
| 12 - Ask | How much, what for, runway |
| 13 - Appendix | Unit economics, financial model, technical detail (on request) |

---

## Quality rules (applied to every slide)

- No market size statements without a source
- No "we have no competition" claims
- Problem slide must name a specific person with a specific cost (time or money) - not a vague pain category
- Traction slide must show a number with a date, not a testimonial quote
- Ask must include runway in months and next milestone
- Team slide must answer: why are you the right people for this specific problem?

---

## Dependencies

**Recommended before running:**
- `pm-lean-canvas` - business model, UVP, channels, revenue
- `pm-problem-validation` - problem evidence and interview quotes for problem slide
- `pm-personas` - specific customer profile for problem story
- `pm-market-analysis` - market size data (bottom-up preferred)
- `pm-business-case` - financial projections and ask
- `pm-hypotheses` - traction evidence and validation results
- `pm-kotler` - differentiation and positioning for competition slide

**Produces for:**
- External investors / partners / customers (primary audience)
- Accelerator applications

**Related skills:** `pm-lean-canvas`, `pm-business-case`, `pm-problem-validation`, `pm-kotler`
