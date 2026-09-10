---
name: pm-prototype
description: Cross-phase prototyping engine. Turns a scoped chunk of the product (a feature, a PRD initiative, the whole product, or any slice) into a tool-ready prototype spec that a prototyping tool (Lovable, v0/Vercel, Base44, Figma Make) can build with minimal loss of context. Gate-checks whether a prototype is worth it, ingests your ACs / flows / process / screens / feature card / brain dump, then compiles a tool-optimized build prompt. Pushes to the selected tool via MCP or hands you a paste-ready block. On re-run, captures the prototype result and feeds it back to the Feature Card / hypothesis register. Use anytime you want to validate before real build.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.1.0"
  domain: product-management
  triggers: prototype, prototyping, proof of concept, POC, spike, validate before build, lovable, base44, v0, figma make, clickable prototype, mockup, throwaway, quick validation
  role: specialist
  scope: validation
  output-format: document
  related-skills: pm-hypotheses, pm-problem-validation, pm-feature-design, pm-feature-card, pm-process-flows, pm-personas, pm-mvp-scope, pm-prd
---

# PM - Prototype (validate before real build)


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## Reference files

This file is the flow. Detail that only one path needs lives in `references/` next to it - read the file for the path you are on, when you reach it, not before.

| Reference file | Contains | Read it when |
|---|---|---|
| `spec-artifact.md` | Step 5 - the prototype spec's shape (universal, tool-agnostic core) | compiling the spec |
| `external-tools.md` | Step 4 - tool selection · Lovable construction rules and operational tactics · Step 6 - handoff | the prototype is built by an external tool |
| `in-repo-loop.md` | The harness shell contract, the rules of the iteration loop, stop and restart signals, classification | the prototype is built here, by a coding agent |

---

## What this skill does

Produces a **tool-ready prototype spec** for a scoped chunk of the product, so you can validate a flow, a UX hypothesis, a concept, or technical feasibility with a prototyping tool **before** anyone writes production code.

The scope is whatever you point at, with **no limit**:
- a single **feature** (linked to a Feature Card),
- a **PRD initiative** (a larger new part),
- the **whole product**,
- or any **slice** ("for this user type, test this part of the functionality").

**Cross-phase.** Like adding a hypothesis or running a validation, this skill has no fixed home in the sequence. Run it whenever there is genuine uncertainty worth de-risking cheaply - during discovery (concept desirability), before a PRD initiative (flow/scope), or inside Phase 6 before a feature enters build (UX/interaction).

**Two modes (same skill, same file):**

| Mode | When | What it does |
|---|---|---|
| **Spec mode** (default) | You want to build a prototype | Gate-check → ingest inputs → compile tool-ready spec → hand off to tool |
| **Result mode** (re-run) | The prototype exists, you have a result | Capture what the prototype proved/disproved → decision → cascade to Feature Card / hypotheses |

**What the skill is NOT:** it does not replace `pm-feature-design` (JIT production spec) and it does not build the prototype's production version. A prototype is a throwaway or a reference, not the build.

---

## Hard rule: the skill does not guess

**The prototype spec is only as good as its inputs, and a guessed input produces a wrong prototype that validates the wrong thing.** So:

- **Never fabricate** screens, flows, entities, fields, features, personas, or copy. Every element in the spec must trace to a real artifact (Feature Card, process-flows, personas, entities) or to something the user stated.
- **When an input is missing or thin, ASK - do not fill the gap with a plausible-sounding invention.** Use AskUserQuestion with concrete candidate options drawn from context (the PREREQ graceful-degradation pattern). If the user genuinely does not know, offer options and let them choose; then mark the choice `[ASSUMED - confirm before build]`.
- This mirrors the prompting tool's own weakness: an under-specified prompt makes the tool hallucinate scope. The skill's job is to remove ambiguity, not add invented certainty.

A spec with three well-sourced screens beats a spec with ten invented ones.

---

## Dependencies

**Recommended (not required):**
- `pm-process-flows` - user flows + screens map directly into the prototype's page/flow structure
- `pm-personas` - the persona scopes tone, fidelity, and who the prototype is for
- `pm-hypotheses` - the prototype usually tests a hypothesis; result mode writes back here
- Feature Card (if feature-scoped) - the spec pulls from it and writes a prototype reference back into it

**pureinn-variables.md - "Prototyping" section:**
Holds the MCP endpoint(s) for the prototyping tool(s). The user may have **more than one** (Lovable, v0/Vercel, Figma Make...). At run time the skill lets the user pick which tool to target for this run - it never hardcodes one.

---

## Step 0: Read variables + detect mode

Read `pureinn-variables.md`:
- **Prototyping** section - which tool MCP endpoints are configured (Lovable / v0 / Figma Make / other). If none configured: proceed in manual-paste mode, remind the user they can add an endpoint to enable push.
- **Feature Backlog** key (if the scope is a feature - to resolve/verify the FEAT-ID).

**Detect mode:**
- If the user references an existing prototype spec in `/prototypes/` and talks about an outcome/result → **Result mode** (Step 8).
- Otherwise → **Spec mode** (Steps 1-7).

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Scope intake

Establish exactly what is being prototyped. Ask as plain text, only what is not already clear:

- **What is the scope?** feature / PRD initiative / whole product / slice - and name it.
- **User-type filter (optional):** is this scoped to one user type ("for the dispatcher, test the assignment flow")? A prototype for multiple user types in one build is harder - if the user names a type, fence the spec to that type's screens and flow.
- **If feature-scoped:** confirm the FEAT-ID and read its Feature Card in full.

Surface an assumption if you infer the scope rather than being told it.

---

## Step 2: Intent gate (Impact over Activity)

**Do not generate a spec before answering: what does the prototype earn us, and is it the cheapest way to earn it?** A prototype costs credits and time - it must de-risk something real. This gate is mandatory.

1. **What are we validating?** Route to the primary intent:

| Intent | The prototype answers | Fidelity it needs |
|---|---|---|
| **UX / flow** | "Does this interaction make sense to the user?" | Clickable click-through, real screens, mock data |
| **Concept / desirability** | "Do users actually want this at all?" | Just enough to be believable - landing + core screen |
| **Technical feasibility** | "Can this even work / integrate?" | Functional, real data/API, thin but wired |
| **Stakeholder / sales alignment** | "Something concrete to show and react to" | Polished front, no working backend |

2. **Is a prototype worth it here?** Challenge honestly:
   - If the pattern is **well-understood, low-risk, standard** (a normal CRUD form, a settings page) → a prototype adds little. Say so and route to `pm-feature-design` / build directly.
   - A prototype earns its cost only when there is **genuine uncertainty** - novel UX, unproven desirability, a risky integration, or a decision blocked on "we need to see it."

   If low-value, surface it before generating anything:
   ```
   Pre [scope] je prototyp pravdepodobne nízka hodnota - [reason: štandardný pattern / už validované / žiadna otvorená neistota].
   Ísť rovno na /pm-feature-design (build), alebo napriek tomu prototypovať?
   ```

3. **Define the success criterion up front.** One sentence: "The prototype succeeds if [observable signal] - otherwise we [change / halt]." This becomes the anchor of both the spec and the result capture.

---

## Step 3: Ingest inputs (deep source ingestion)

Pull everything relevant to the scope. The input is whatever the user points at - accept all of:

- **Acceptance Criteria** (from the Feature Card Section 2, if it exists)
- **Flow / process** (from `pm-process-flows`, or pasted)
- **Screens** (named screens, wireframes, Figma URLs, screenshots)
- **Feature Card** (read in full if feature-scoped)
- **Persona** (from `pm-personas` - who it is for)
- **Entities + key states** (from `entities.md` - only if the prototype needs functional data)
- **Brain dump** (raw notes, voice-to-text, a rough idea)

Ingest to full depth (whole files, whole folders recursively - CLAUDE.md deep-source rule). Confirm coverage: "Read [Feature Card FEAT-X, process-flows §Y, personas §Z]." If a source is thin or missing, do not stall - form concrete candidate assumptions and confirm via AskUserQuestion, then mark them `[ASSUMED]` in the spec.

Then read `references/external-tools.md` and run **Step 4 (Select prototyping tool)**, followed by Step 5 (`references/spec-artifact.md`) and Step 6. Return here for Step 7.

---

## Step 7: Write the prototype reference back

**If feature-scoped:** add a reference to the Feature Card (do not touch Sections 1-4 spec content - add a lightweight reference note / frontmatter field):

```
Prototype: /prototypes/[FEAT-ID]-prototype-spec.md
Prototype URL: [live/preview URL or "pending build"]
Expected outcome: [the success criterion from Step 2]
Result: pending
```

This makes the Feature Card show that a prototype was used and that a result is expected before build proceeds.

**If initiative/product-scoped:** log the prototype as a validation instrument against the relevant hypothesis in the hypothesis register (or note it for `pm-hypotheses`).

Save the spec to `/prototypes/` (Step: Save to).

---

## Step 8: Result mode (re-run after the prototype exists)

When the user comes back with an outcome, operate in **delta mode** - do not rewrite the spec, append to its `## Result` section:

1. **Capture what happened:** what was built, what was tested, with whom (if users saw it).
2. **Verdict against the success criterion:**

```markdown
## Result

**Date:** [YYYY-MM-DD]
**Built:** [what the prototype ended up being - URL]
**Tested with:** [users / stakeholders / self]

### Verdict
[ ] Validated - success criterion met → proceed to real build
[ ] Partially validated - [what held, what did not] → adjust before build
[ ] Invalidated - [what broke the assumption] → halt / rethink

**What we learned:** [the actual signal]
```

3. **Cascade** (surface, do not silently edit):
   - Feature-scoped → update the Feature Card prototype reference (`Result: validated/invalidated`); if invalidated, flag before `pm-feature-design` / build.
   - Hypothesis-linked → update the hypothesis register (`confirmed / refuted / new signal`); recommend `/pm-hypotheses`.
   - If the result changes scope or desirability → recommend re-checking `pm-prd` / `pm-features-list` / `pm-mvp-scope`.

---

## Internal completeness checklist

<!-- Claude reference only -->

**Every prototype spec must have:**
- [ ] Scope + intent + explicit success criterion
- [ ] In-scope / out-of-scope (out-of-scope fence is non-negotiable)
- [ ] Primary screen named + build-first
- [ ] Flow narrative
- [ ] Fidelity stated (static vs functional)
- [ ] Compiled build prompt following the tool's construction rules (`references/external-tools.md`; Lovable rules if Lovable)

**Never skipped:**
- [ ] Intent gate ran (prototype justified, or user chose to proceed anyway)
- [ ] MCP warning shown before any live call
- [ ] Feature Card prototype reference written (if feature-scoped) - reference only, spec sections untouched
- [ ] Lovable target: Knowledge Base loaded (`set_project_knowledge`) + confirm-understanding gate passed before any code

**Never guessed (hard rule):**
- Screens, flows, entities, fields, features, copy must come from real artifacts or user input - never fabricated
- Missing input → asked via AskUserQuestion, not filled with invention; assumptions marked `[ASSUMED - confirm before build]`
- FEAT-ID verified against feature_list.md if referenced

---

## Save to

```
pureinn-workspace/[project-slug]/prototypes/[scope-slug]-prototype-spec.md
```

Feature-scoped: `[FEAT-ID]-prototype-spec.md`. Initiative/product/slice: a descriptive `[scope-slug]`.

`prototypes/` is a cross-cutting operational folder (like `meetings/`, `team/`) - created on demand, not part of the phase artifact flow.

---

## Handoff

**Čo si teraz má:** Tool-ready prototype spec - viem ho pushnúť do Lovable/v0/Figma Make (alebo vložiť manuálne) a dostať funkčný/klikací prototyp, ktorý validuje konkrétnu neistotu **pred** reálnym buildom. Feature má zapísanú referenciu, že prototyp beží a čaká sa výsledok.

**Ďalší krok:**
- Po postavení prototypu → spusti `/pm-prototype` znova (result mode) a zapíš verdikt.
- Ak validované → `/pm-feature-design [FEAT-ID]` pre produkčný spec.
- Ak validované na úrovni iniciatívy/konceptu → `/pm-hypotheses` (aktualizuj hypotézu) alebo `/pm-prd`.

**Môžeš preskočiť ak:** Ide o štandardný, nízko-rizikový pattern bez otvorenej neistoty - vtedy prototyp nepridáva hodnotu a ide sa rovno na `/pm-feature-design`.
