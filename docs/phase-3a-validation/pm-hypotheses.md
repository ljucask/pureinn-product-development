# pm-hypotheses

> Structure validation hypotheses, design low-cost experiments, track results, and issue a Go/No-Go decision

**Phase:** 3a - Validation (Hard Gate)  
**Agent mode:** `never` - value is the live dialogue  
**Version:** 1.0.0  
**Triggers:** hypotheses, hypothesis validation, go no go, experiment plan, ICP, assumption map, validation results

---

## When to use

Phase 3a hard gate. Runs after `design-thinking`. The only skill in the framework that produces a formal Go/No-Go verdict. No Phase 3b work begins until this verdict is GO.

**Agent mode is not supported.** The skill's value is the live iterative dialogue around assumptions and evidence. Invoking with `--agent` will warn once and proceed interactively.

---

## What it produces

Two artifacts under `pureinn-workspace/[project-slug]/artifacts/phase-3-define/`:

1. **Hypothesis Register** (`hypothesis-register.md`) - ICP definition, assumption map, structured hypotheses, experiment plans with pre-defined success criteria
2. **Go/No-Go Decision** (`go-no-go.md`) - evidence summary per hypothesis, verdict (GO / PIVOT / STOP)

---

## How to invoke

```bash
/pm-hypotheses    # interactive only - --agent not supported
```

At the start of every session, the skill asks which mode to run:

**Plan mode** (first run, or after a PIVOT):
- Structures hypotheses from `design-thinking` outputs + Phase 2 evidence
- Ranks by risk, assigns experiment type, defines success criteria before any experiment runs
- Output: complete Hypothesis Register with experiment plans

**Results mode** (after experiments complete):
- Records experiment outcomes against pre-defined success criteria
- Issues the Go/No-Go verdict
- Output: Go/No-Go decision with evidence summary

Both modes use the same Hypothesis Register - it is updated progressively, not recreated.

---

## Go/No-Go decision logic

| Verdict | Condition |
|---|---|
| **GO** | Problem + Customer + Market hypotheses all confirmed (at least one payment/commitment signal) |
| **PIVOT** | Mixed signals - evidence points at what to change; new experiment defined with new success criteria |
| **STOP** | Problem not confirmed after 10+ ICP interviews, or no willingness-to-pay signal after quantitative test |

**PIVOT escalation rule:** After PIVOT 2, if all four hypothesis types (Problem / Customer / Solution / Market) have each been revised at least once, a structured review is triggered before more experiments run. The pattern indicates the original premise was fundamentally wrong, not misaligned on one dimension.

---

## Hypothesis types

| Type | What it tests |
|---|---|
| Problem | Does the pain exist and is it severe enough to act on? |
| Customer | Are the people we're targeting the right ICP, and can we reach them? |
| Solution | Does our proposed solution solve the problem in a way users value? |
| Market | Is the market large enough and willing to pay? |

---

## Experiment types (summary)

| Experiment | Best for | Signal strength |
|---|---|---|
| Customer Interview (Mom Test) | Problem + Customer | High (qualitative) |
| Landing Page | Problem + Market + Solution | Medium |
| Smoke Test / Fake Door | Solution | Medium |
| Targeted Ads | Market + Customer | Medium (reach + CAC) |
| Pre-order | Market + Solution | Highest (financial commitment) |
| Concierge MVP | Solution + Market | Highest (delivery + payment) |
| Waitlist | Market | Low-Medium |
| Survey | Customer + Market | Low (breadth confirmation only) |

**Commitment hierarchy (strongest to weakest):**
1. Credit card / pre-payment
2. Letter of intent (B2B) or signed pilot agreement
3. Email sign-up from targeted ICP (not friends)
4. Click-through from paid traffic
5. Verbal agreement (does not count as validation)

---

## The "done elsewhere" path

If Phase 3a validation was done outside the framework (external workshop, investor due diligence, Miro session, etc.):

```
/pureinn "Phase 3a done elsewhere"
```

Provide the verdict (GO / PIVOT / STOP) and key evidence. Pureinn logs it and routes forward without re-running experiments.

---

## Dependencies

**Required before running:**
- `design-thinking` - Validation Hypotheses draft, Value Proposition Canvas, HMW questions are the primary inputs

**Recommended:**
- `pm-personas` - ICP definition and pain intensity
- `jtbd-building` - Forces Diagram informs which assumptions are riskiest
- `pm-problem-validation` - Phase 2 evidence base

**Produces for:**
- `pm-lean-canvas` - validated problem, customer, and solution feed Lean Canvas inputs
- `pm-prd` - validation evidence and Go/No-Go verdict are required PRD sections
- `pm-product-roadmap` (v1) - hypotheses and risks section

**Related skills:** `design-thinking`, `pm-personas`, `jtbd-building`, `pm-problem-validation`, `pm-lean-canvas`
