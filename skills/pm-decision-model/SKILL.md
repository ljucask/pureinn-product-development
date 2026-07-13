---
name: pm-decision-model
description: JIT helper - add a single decision table (TBL-[DOMAIN]-NN) to domain/decision_models.md. For multi-condition logic where several inputs combine to produce different outputs (pricing matrices, eligibility rules, risk scoring, discount tiers). The decision-models counterpart to the single-rule helpers (pm-business-rule-core/critical/governance). Use during pm-feature-design when a multi-condition decision surfaces, or standalone - without re-running the full pm-business-rules-library.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: decision table, decision model, decision matrix, multi-condition logic, lookup table, pricing matrix, eligibility matrix, risk scoring
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-business-rules-library, pm-business-rule-core, pm-feature-design, pm-entity-registry
---

# PM - Decision Model (JIT Helper)


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments - after drafting, require the user's review before finalizing; do not close decisions autonomously.

---

## What this skill does

Adds a single **decision table** (`TBL-[DOMAIN]-NN`) to `domain/decision_models.md` (Live Register 3) - without re-running the full `pm-business-rules-library`. This is the decision-models counterpart to the single-rule helpers: where `pm-business-rule-core/critical/governance` add one business rule to Register 2, this adds one decision table to Register 3.

A decision table belongs here when:
- **Several input conditions combine** to produce different outputs (not a single if/then)
- The logic is best read as a matrix - rows = condition combinations, columns = inputs + output
- Examples: discount tiers by customer level + order value + promo, eligibility by age + region + status, risk score by multiple signals, pricing matrix

If the logic is a single condition → one output, it is a **business rule**, not a table → use `pm-business-rule-core` / `-critical` / `-governance` instead.

**When to run:** During `pm-feature-design` when the JIT design reveals multi-condition logic that should be centralized. Or standalone when a decision matrix needs to be formalized before a feature enters build. (`pm-business-rule-core` routes here when a rule it is adding turns out to have multiple condition combinations.)

---

## Dependencies

**Required before running:**
- `pm-business-rules-library` - `domain/decision_models.md` must exist (initialized in Phase 4)
- `pm-entity-registry` - entity context for scoping the table

**Recommended:**
- A related business rule (`BR-[DOMAIN]-NNN`) the table elaborates - link it via "Used by rule".

**Produces artifacts used by:**
- `pm-feature-design` - JIT design references the TBL-ID in Feature Card Section 1 (Biznis Mantinely)
- Build phase - the table drives unit tests covering every condition combination

---

## Step 0: Current state check

If `domain/decision_models.md` does not exist yet, do not attempt to create it here - tell the user to run `/pm-business-rules-library` first (it initializes the register), then return to this skill.

Read `domain/decision_models.md`.

List existing tables in the relevant domain. Identify the next available `TBL-[DOMAIN]-NN`.

Check that this is genuinely multi-condition: if a single condition produces a single outcome, redirect to `pm-business-rule-core` (it is a rule, not a table). Check whether a similar table already exists (avoid duplicates).

Use AskUserQuestion to confirm scope before proceeding.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Gather inputs

Gather via text prompt:

```
I need inputs to define a Decision Table for decision_models.md.

1. WHAT DECISION DOES IT MAKE?
   In plain language, what does this table decide?
   (e.g., "what discount % a customer gets", "whether a loan application is eligible",
    "what risk tier a transaction falls into")

2. WHICH DOMAIN?
   (PAY / ORD / USR / BKG / DISC / RISK / Other: [specify])

3. INPUT CONDITIONS (the columns)
   List the inputs that drive the decision.
   (e.g., Customer Tier, Order Value, Promo Code)

4. OUTPUT
   What does the table produce? (e.g., Discount %, Eligibility, Risk Tier)

5. THE ROWS (condition combinations → output)
   Give the combinations you know. I'll surface gaps and ask about missing
   combinations so the table is exhaustive. If some values are not yet final, mark TBD.

6. RELATED RULE
   Is there a business rule this table elaborates? (BR-[DOMAIN]-NNN, or "none")
```

After answers, surface any **uncovered condition combinations** ("what happens when Tier=Basic AND Promo=EXTRA10?") so the table is exhaustive - a partial decision table is the most common defect.

---

## Step 2: Generate the table

Generate the `TBL-[DOMAIN]-NN` ID as the next available number in that domain. Generate in English.

- Every realistic combination of input conditions has a row (or an explicit catch-all).
- Mark unfinalized output values as `TBD` (finalized JIT by `pm-feature-design`).
- Document edge cases below the table.

---

### OUTPUT: decision_models.md entry

```markdown
## TBL-[DOMAIN]-[NN]: [Decision Table Name]
**Domain:** [Domain / category]
**Used by rule:** [BR-[DOMAIN]-NNN, or "none"]
**Affected entity:** [Entity name] (entities.md#[entity])
**Status:** Draft / Final
**Used in features:** [FEAT-IDs - filled JIT by pm-feature-design]

| [Input 1] | [Input 2] | [Input 3] | [Output] | Notes |
|---|---|---|---|---|
| [value] | [value] | [value] | [result] | |
| [value] | [value] | [value] | [result] | |

**Edge cases:**
- [Conflicting / missing / boundary inputs and how they resolve]
- [What happens for any combination not covered above - catch-all behaviour]
```

---

## Save to

Append the new table under the correct domain section in:
```
pureinn-workspace/[project-slug]/domain/decision_models.md
```

If a related rule exists in `business_rules.md`, add a back-reference on that rule (`Decision model: TBL-[DOMAIN]-NN`).

Update the Changelog in `decision_models.md`.

---

## Handoff

**Čo si teraz má:** Jeden decision table (nový `TBL-[DOMAIN]-NN`) pridaný do `decision_models.md` (Register 3) - multi-condition logika zachytená ako matica, pripravená na generovanie testov.

**Ďalší krok:** Späť do JIT cyklu - `/pm-feature-design [FEAT-ID]` (ak tabuľka vznikla pri dizajne feature - tam sa doplnia TBD bunky a status Draft → Final) alebo `/pm-stripe`.

**Môžeš preskočiť ak:** Logika je jedna podmienka → jeden výsledok - to nie je tabuľka, ale pravidlo: použi `/pm-business-rule-core` (alebo `-critical` / `-governance`).
