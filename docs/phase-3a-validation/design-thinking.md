# design-thinking

> Define + Ideate stages of Design Thinking - Problem Statement, POV, HMW questions, Ideation synthesis

**Phase:** 3a - Validation (Step 1)  
**Agent mode:** `never` - value is the live dialogue  
**Version:** 1.0.0  
**Triggers:** design thinking, HMW questions, problem statement, POV, ideation, elevator pitch, validation hypotheses

---

## When to use

Phase 3a, Step 1. Run after Phase 2 (Problem Validation Summary exists). This is the bridge between discovery (what we learned about the problem) and validation strategy (what we will test before committing to build).

In the Pureinn framework, Empathize is already done in Phase 2. This skill picks up at **Define** and runs through **Ideate**.

**Agent mode is not supported.** The value is in the live iterative dialogue - surfacing and challenging assumptions in real time. Invoking with `--agent` will warn once and proceed interactively.

---

## What it produces

**Design Thinking Synthesis** (`artifacts/phase-3a-validation/design-thinking.md`):

1. **Problem Statement** - precise articulation of the validated problem (from Define stage)
2. **Point of View (POV)** - User + Need + Insight framing: "[User] needs [need] because [insight]"
3. **How Might We (HMW) questions** - opportunity reframings derived from the POV and JTBD Forces Diagram
4. **Ideation synthesis** - promising solution directions from structured brainstorming (not feature lists - solution spaces)
5. **Elevator Pitch** - 30-second articulation of the problem and proposed solution direction
6. **Draft Validation Hypotheses** - input for `pm-hypotheses` Plan mode

---

## How to invoke

```bash
/design-thinking    # interactive only - --agent not supported
```

---

## Dependencies

**Required before running:**
- `pm-problem-validation` - Problem Validation Summary is the primary input
- `pm-personas` - persona and JTBD context frames the POV

**Recommended:**
- `jtbd-building` - Forces Diagram provides the HMW framing material
- `pm-market-analysis` - competitive whitespace informs ideation

**Produces for:**
- `pm-hypotheses` (Plan mode) - Draft Validation Hypotheses are the input
- `pm-business-model` - solution direction from ideation informs value proposition choices
- `pm-prd` - Problem Statement and POV are core PRD sections

**Related skills:** `pm-personas`, `jtbd-building`, `pm-problem-validation`, `pm-hypotheses`, `pm-kotler`
