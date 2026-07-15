---
name: pm-scope-brief
description: Generate the Scope Brief - the definition document for a commissioned build. States what exactly will be built, for whom, within which constraints, and how done is judged. Phase 3b alternative to pm-prd when the mandate is already given (client engagement, exec directive) and full market validation + business model work is not needed. Carries a Business Capabilities section so Phase 4-5 skills (pm-entity-registry, pm-features-list) can consume it exactly as they consume a PRD.
license: MIT
metadata:
  agent-mode: decision
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: scope brief, scope definition, client scope, what we will build, definition document, engagement scope, build definition
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-discovery-report, pm-prd, pm-entity-registry, pm-features-list, pm-process-flows, pm-business-rules-library
---

# PM - Scope Brief


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.
- **Review required:** the artifact contains commitments - the IN/OUT/DEFERRED scope cut is decided here for the first time. After drafting, require the user's review before finalizing; never close scope decisions autonomously.

---

## What this skill does

Turns converged discovery into a definition: what exactly gets built. Written for whoever executes - you, your dev team, your employer - and precise enough to run a dev kickoff call from. It is the document a developer reads instead of "make it like company XY".

**When Scope Brief, when PRD:** both fill the same Phase 3b exit slot - pick one.

| Situation | Document |
|---|---|
| Mandate already given: a client commissioned it, an exec directed it, the decision to build is made | **Scope Brief** (this skill). Phase 3a validation and business-model work would re-answer a question that's already answered. |
| Speculative product: you're deciding whether/what to build, market risk is yours | **PRD** via full Phase 3a + 3b (`/pm-prd`). Skipping validation there is skipping your own risk management. |

**Context fit check (surface before generating):** if no committed mandate exists - nobody has decided this gets built - say so: "Scope Brief presumes a given mandate. For a speculative product, `/pm-hypotheses` → `/pm-prd` is the honest path. Proceed anyway?"

**Downstream contract:** the **Business Capabilities** section of this document is a named interface - `/pm-entity-registry` extracts entities from it and `/pm-features-list` derives the feature inventory from it, exactly as they do from PRD Section 7. Everything else in the brief supports that core.

---

## Dependencies

**Reads (Discovery Report is the primary input):**
- `artifacts/phase-2-discovery/discovery-report.md` - primary; if absent, fall back to `meetings/` client-discovery notes + Track artifacts directly
- `problem-validation-summary.md` - if it exists
- `artifacts/phase-3-define/design-thinking-synthesis.md` - if Phase 3a ran (POV/HMW enrich the problem framing)

**Produces artifacts used by:**
- `/pm-entity-registry`, `/pm-features-list` - via the Business Capabilities section
- `/pm-process-flows` - roles and process context
- `/pm-business-rules-library` - the `[CANDIDATE-BR]` edge cases seed the rules register

---

## Step 0: Current state check

1. Run the context fit check above.
2. Read all inputs in full (deep source ingestion). Confirm coverage: "Read [list]."
3. Check for an existing `scope_brief.md`:
   - **Exists, status Draft → delta mode.** Update against new inputs, show the delta, never silently reverse a scope decision.
   - **Exists, status Baselined →** changes go through the **Change Log** (see artifact) - each with what/why/impact/who approved. In client work a scope change after baseline is a commercial event; the log is what keeps it honest.
4. **Gap check** - discovery thin in an area the brief needs (no process walkthroughs, users never validated, constraints unswept)? Say so: which sections will carry `[ASSUMED]` or `[CLIENT-ASSERTED]` markers, and whether one more discovery session would be cheaper than a wrong brief. Recommend, don't block.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: The scope cut (the decision of this skill)

From the discovery inputs, draft the three-way cut and put it in front of the user - propose, don't impose:

1. **Extract candidate capabilities** from the Discovery Report: must-haves, nice-to-haves, references classified directive, process needs, the three populations' needs.
2. **Propose the cut:** IN (v1) / DEFERRED (real, later) / OUT (non-goals - explicitly not doing). For each proposal: one-line reason anchored to discovery evidence (client's must-have, process necessity, staff-operability, dependency).
3. **Confirm with the user** - group the contentious calls (where discovery signals conflict, where client wishes exceed budget/time signals) via AskUserQuestion with a recommended option reasoned from the engagement goal. Uncontested calls: present in the summary, confirm as a block.
4. **Guard the classic traps:** a reference classified *hypothesis* must not appear in IN as settled; staff/admin capability (population b) missing from IN is the launch-failure pattern - flag it if absent; every IN capability without an acceptance signal gets one before the brief is done.

---

## Step 2: Generate artifact

Generate in English. Concrete over abstract; every section traceable to discovery sources. Omit sections with nothing real rather than padding - but Business Capabilities, Scope, Acceptance are mandatory.

---

### ARTIFACT: Scope Brief

```markdown
# Scope Brief - [Product / Project Name]

> **Version:** 1.0 · **Status:** Draft / Baselined · **Date:** [date]
> **Commissioned by:** [client / sponsor] · **Prepared by:** [name]
> **Sources:** Discovery Report ([date]), [N] discovery sessions, [other artifacts]
> Fills the Phase 3b definition slot (alternative to PRD) - Phase 4-5 skills consume the Business Capabilities section below.

---

## 1. Context

[3-5 sentences: who commissioned this, the trigger, the product's job in their business, the success measure. Compressed from the Discovery Report - reference it, don't duplicate it.]

## 2. Problem framing

**Point of view:** [WHO - the user/role] needs [NEED - the outcome] because [INSIGHT - the discovery finding that explains it].

**The problem this build solves:** [2-3 sentences. Even on a directive path, state the problem behind the mandate - a spec without a problem statement can be built correctly and still fail.]

[If design-thinking ran: carry its Problem Statement / POV here instead of drafting fresh.]

## 3. Users and roles

| Population | Role(s) | What they need from the product | Provenance |
|---|---|---|---|
| Client's customers | [roles] | [needs] | [validated / CLIENT-ASSERTED / assumed] |
| Client's staff | [admin, operator, support roles] | [daily operation needs] | |
| Client / management | [oversight roles] | [reporting, control] | |

[Every role here must appear in at least one capability below. A population with no capability = discovered but not served - deliberate or a gap?]

## 4. Business Capabilities

<!-- Downstream interface: pm-entity-registry extracts entities from this section;
     pm-features-list derives the feature inventory from it. Same contract as PRD Section 7. -->

| # | Capability | Serves (role) | Description (what the system enables, not UI) | Core process it supports |
|---|---|---|---|---|
| C1 | [e.g. Order intake and tracking] | [customer + staff] | [1-2 sentences, outcome language] | [process from discovery M2b] |
| C2 | | | | |

## 5. Scope

### In scope (v1)
| Capability / item | Why in | Acceptance signal |
|---|---|---|
| [item] | [discovery evidence] | [how we'll know it works - observable] |

### Deferred (real, not now)
| Item | Why deferred | Revisit when |
|---|---|---|

### Out of scope - non-goals
| We will NOT | Why - stated to the client |
|---|---|
| [explicit non-goal] | [reason; the cheapest scope protection available] |

## 6. References - translated

[Only references classified **directive** in discovery. Each becomes a bounded requirement:]

| Reference | What we take from it | Translated requirement | What we explicitly do NOT copy |
|---|---|---|---|
| [company XY] | [the flow / the function - the layer identified in decompression] | [concrete, buildable statement] | [visual identity / features they need and we don't / ...] |

[References classified *hypothesis* do not appear here - they live in section 9 until resolved.]

## 7. Edge cases and exceptions

[From the Exception sweeps - the register that saves the build:]

| # | Edge case | Expected behavior | Source | Tag |
|---|---|---|---|---|
| E1 | [e.g. customer cancels mid-order] | [what the system must do] | [session/process] | `[CANDIDATE-BR]` if product-enforced |

[`[CANDIDATE-BR]` items seed `/pm-business-rules-library` in Phase 4 - same convention as pm-domain-analysis.]

## 8. Integrations, data, environment

| Area | Requirement | Owner / dependency |
|---|---|---|
| Integrations | [systems to connect, direction, owner] | |
| Data | [existing data, migration, quality, ownership] | |
| Content | [who supplies what, by when - a client-side dependency, name it] | |
| Operations post-launch | [who administers, their skill level - shapes admin UX] | |
| Replacement / migration | [what this replaces, switchover approach] | |

## 9. Constraints, assumptions, open questions

**Hard constraints:** [budget/time/tech/brand/regulatory - the non-negotiables]

**Assumptions we are building on:**
| Assumption | Provenance | If wrong, it affects |
|---|---|---|
| [item] | [ASSUMED / CLIENT-ASSERTED] | [which capability/scope item] |

**Open questions:** [each with: why it matters + who resolves + by when. An open question blocking an IN item is a red flag - say so.]

## 10. Acceptance

**Done means:** [engagement-level criteria - observable, agreed with the commissioner]
**Sign-off:** [who approves, on what cadence - demo rhythm, review points]
**Success measure after launch:** [the number from discovery section 2 - how and when it gets checked]

## 11. Delivery sketch

[Rough phasing only - v1 cut, what follows. The real plan comes from Phase 5 (/pm-features-list → /pm-mvp-scope). Do not pre-plan stripes here.]

## 12. Input map

| Section | Built from |
|---|---|
| [each section] | [Discovery Report §, meeting note, artifact] |

## Change Log

| Date | Change | Why | Impact (scope/time/budget) | Approved by |
|---|---|---|---|---|
| - | - | - | - | - |

[After Baselined status, every scope change lands here first.]
```

---

## Step 3: Review and baseline

Decision skill - the user reviews before anything is final:

1. Walk the scope cut: IN/DEFERRED/OUT with reasons; contested calls first.
2. Verify the traps from Step 1 (hypothesis-references not in IN; staff capabilities present; acceptance signals everywhere).
3. On confirmation → **Status: Baselined**. From here, changes go through the Change Log.
4. Offer: keep as Draft if the client still needs to see it first - baselining before commissioner sign-off inverts the engagement.

---

## Internal completeness checklist

<!-- Claude reference only -->

- [ ] Context fit check ran (mandate exists, or user chose to proceed)
- [ ] Problem framing present - directive path did not skip the POV
- [ ] All three populations addressed in roles AND capabilities (or absence deliberate)
- [ ] Business Capabilities section present, outcome-language, downstream-consumable
- [ ] Every IN item has evidence + acceptance signal
- [ ] Non-goals explicit - never an empty section
- [ ] Directive references translated with NOT-copying bounds; hypothesis references NOT in scope
- [ ] Edge cases registered, product-enforced ones tagged `[CANDIDATE-BR]`
- [ ] Client-side dependencies named with owners (content!)
- [ ] Assumptions carry provenance and blast radius
- [ ] Acceptance: done-criteria + sign-off + post-launch measure
- [ ] Input map traceable

## Save to

```
pureinn-workspace/[project-slug]/product/scope_brief.md
```

---

## Handoff

**Čo si teraz má:** Baselinovaný Scope Brief - definícia čo presne sa stavia, s akceptačnými kritériami a hranicami. Developer z neho vie viesť kickoff; klientovi je jasné, čo dostane a čo nie.

**Ďalší krok:** `/pm-entity-registry` (Phase 4) - entity a stavy z Business Capabilities sekcie. Alebo `/pureinn` pre phase gate check.

**Môžeš preskočiť ak:** Robíš špekulatívny vlastný produkt bez daného mandátu - tam patrí plná Phase 3a validácia a `/pm-prd`, nie tento brief.
