---
name: pm-business-rule-critical
description: JIT helper - add a single Critical priority rule (hard invariant) to domain/business_rules.md. For rules where violation causes financial loss, legal exposure, or irreversible system damage. No exceptions allowed. Use during pm-feature-design when a missing invariant is identified, or anytime a new hard constraint needs to be formalized.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "2.0.0"
  domain: product-management
  triggers: critical invariants, hard constraints, financial integrity rules, legal constraints, non-negotiable rules
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-business-rules-library, pm-entity-registry, pm-feature-design
---

# PM - Business Rule: Critical Invariant (JIT Helper)


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments - after drafting, require the user's review before finalizing; do not close decisions autonomously.

---

## What this skill does

Adds a single **Critical priority rule** to `domain/business_rules.md`.

A rule belongs here when:
- Violation causes financial loss, legal exposure, or irreversible system damage
- It must hold in ALL circumstances - no exceptions, no admin overrides
- Breaching it is a system failure, not a policy deviation

If the rule has exceptions or context-dependent variations → use `pm-business-rule-core` (High priority).
If it is a compliance or policy rule → use `pm-business-rule-governance`.

**When to run:** During `pm-feature-design` when the JIT design reveals a missing invariant that must be captured before build. Or standalone when a business decision introduces a new hard constraint.

---

## Dependencies

**Required before running:**
- `pm-business-rules-library` - `domain/business_rules.md` must exist (initialized in Phase 4)
- `pm-entity-registry` - entity and lifecycle context needed to scope the rule correctly

**Produces artifacts used by:**
- `pm-feature-design` - JIT design reads BR-IDs when defining Feature Card Section 1 (Biznis Mantinely)
- Build phase - developers implement invariant enforcement as guard conditions

---

## Step 0: Current state check

Read `domain/business_rules.md`.

List existing Critical rules and their IDs. Identify the next available BR-[DOMAIN]-NNN for the relevant domain.

Check if a similar invariant already exists - prevent duplicates or conflicting definitions.
Check: is the rule truly critical (no exceptions) or does it have edge cases? If edge cases exist, this is a High priority rule, not Critical.

Use AskUserQuestion tool to confirm scope and mode before proceeding.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Gather inputs

Use AskUserQuestion for structured choices. Gather via text prompt:

```
I need inputs to define a Critical Invariant rule for business_rules.md.

1. WHAT IS THE RULE?
   Describe the constraint in plain language.
   (e.g., "Payment must never be released to the provider without delivery confirmation",
    "A booking cannot be confirmed if the listing is not in Active state",
    "User personal data must be fully deleted within 30 days of an erasure request")

2. WHAT DOES IT PROTECT?
   What would happen if this rule was violated?
   (financial loss / legal exposure / data corruption / safety risk / regulatory penalty)

3. DOMAIN AND ENTITY
   Which domain does this rule belong to?
   (PAY / ORD / USR / REG / BKG / LST / Other: [specify])
   Which entity from entities.md does it apply to?

4. WHEN IS IT ENFORCED?
   At what point in the flow must it be checked?
   (before state transition / on API call / at payment capture / on data deletion / other)

5. EXCEPTIONS
   Are there ANY exceptions or admin overrides?
   If yes → this is a High priority rule, not Critical. Use pm-business-rule-core.
   If no → confirm this is the right skill.
```

---

## Step 2: Generate rule entry

Generate the BR-[DOMAIN]-NNN ID as the next available number in that domain section of business_rules.md.

Generate in English.

---

### OUTPUT: business_rules.md entry

```markdown
### BR-[DOMAIN]-[NNN]: [Rule Name]
**Category:** [Payment / Order / User / Compliance / Booking / Listing / other]
**Affected entity:** [Entity name] (entities.md#[entity])
**Priority:** Critical
**Status:** Final

**Rule:**
[Description of the invariant in business language. Precise enough to implement. No implementation details.]
Example: "Payment must not be released to the provider until the Order transitions to Confirmed state AND delivery.confirmed == true."

**Formula/Condition:**
[Exact logical condition or guard expression]
Example: `release_payment = true ONLY IF order.status == Confirmed AND delivery.confirmed == true`

**Enforcement point:** [When in the flow this must be checked]
**Exceptions:** None - this is a hard invariant
**Applies to features:** [TBD - filled JIT by pm-feature-design]
**Source:** [Business decision / legal requirement / financial integrity / regulatory]
```

---

## Save to

Append the new rule under the correct domain section in:
```
pureinn-workspace/[project-slug]/domain/business_rules.md
```

If the domain section does not yet exist, create it as:
```
## [Domain] Rules

### BR-[DOMAIN]-[NNN]: [Rule Name]
```

Update the Rule Coverage Map at the bottom of the file.
Update the Changelog with: `| [new version] | [date] | BR-[DOMAIN]-[NNN] added | pm-business-rule-critical |`

State update: no state.json change needed (business_rules_initialized already true).

---

## Handoff

**Čo si teraz má:** Jeden Critical invariant (hard rule) pridaný do `business_rules.md` - porušenie znamená finančnú stratu, právne riziko alebo nezvratnú škodu.

**Ďalší krok:** Späť do JIT cyklu - `/pm-feature-design [FEAT-ID]` alebo `/pm-stripe`. Ak má pravidlo viac vetiev, zváž TBL v `decision_models.md` cez `/pm-business-rules-library`.

**Môžeš preskočiť ak:** Invariant už v registri existuje.
