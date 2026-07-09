# pm-stress-test

> Adversarial stakeholder pushback simulator - stress-tests a proposal BEFORE the real room

**Phase:** Cross-phase  
**Agent mode:** `never` - value is the live adversarial dialogue  
**Version:** 1.0.0  
**Triggers:** stress test, pushback, challenge my proposal, devil's advocate, red team, murder board, pre-mortem, investor grilling, board prep, exec review prep, defend my plan, poke holes, skeptical stakeholder, pitch prep

---

## When to use

Before any exec review, investor pitch, board meeting, budget defense, or contentious feature push. Identifies where your argument is thin before the real audience does. Cross-phase - run it whenever you need to pressure-test a proposal, decision, or plan.

**Agent mode is not supported.** The skill's value is the live multi-round adversarial dialogue. Invoking with `--agent` will warn once and proceed interactively.

---

## What it produces

1. **Multi-round adversarial questioning** - the skill plays a specific skeptical stakeholder and presses through multiple rounds, not one shot
2. **Prep summary** at the end of the session:
   - What held under pressure
   - What is thin (weak evidence, circular reasoning, unexplored assumptions)
   - Unresolved blind spots
   - Concrete pre-meeting checklist

---

## How it works

1. **Silent weakness diagnosis** - runs a first pass on your input before asking the first question; calibrates to the persona and focus area
2. **Persona selection** - you pick the skeptical stakeholder it will play
3. **Multi-round pressing** - fires the sharpest questions that stakeholder actually asks, follows up on weak answers, does not accept surface responses
4. **Prep summary** - structured debrief after the session

---

## Stakeholder personas available

- Investor (pre-seed / seed / Series A)
- CFO / finance lead
- Board member
- CTO / technical lead
- Legal / DPO
- Sales lead
- Product lead (internal review)
- Customer (enterprise procurement)
- Other (describe the skeptic)

---

## How to invoke

```bash
/pm-stress-test    # interactive only - --agent not supported
```

Paste the proposal, plan, decision, or document you want challenged. The skill asks which persona to play and which focus areas to target (financials, technical risk, market assumptions, legal, team, go-to-market, etc.).

---

## Dependencies

**Recommended input (any works):**
- `pm-business-case` - financial projections under scrutiny
- `pm-pitch-deck` - pitch prep before an investor meeting
- `pm-prd` - PRD decisions before a product review
- `pm-hypotheses` - validation plan before a board/exec review
- `pm-prioritize` - priority decisions before a planning defense

**Produces for:**
- Pre-meeting preparation (the session output is a checklist)
- `pm-hypotheses` - blind spots surface as new hypotheses to test

**Related skills:** `pm-stakeholder-map`, `pm-pitch-deck`, `pm-business-case`, `pm-prd`, `pm-hypotheses`
