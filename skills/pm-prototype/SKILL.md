---
name: pm-prototype
description: Cross-phase prototyping engine. Takes a scoped chunk of the product (a feature, a PRD initiative, the whole product, or any slice) and gets a prototype of it built by one of two paths - compiled as a tool-ready spec for an external tool (Lovable, v0/Vercel, Base44, Figma Make), or built in-repo by a coding agent against a harness carrying states, fixtures, time, variants, device presets and an event log. Gate-checks whether a prototype is worth it at all, then decides depth and path from who it is for and which uncertainty it resolves. On re-run, captures the result against a precommitted threshold and feeds it back to the Feature Card / hypothesis register. Use anytime you want to validate before real build.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.2.0"
  domain: product-management
  triggers: prototype, prototyping, proof of concept, POC, spike, validate before build, lovable, base44, v0, figma make, clickable prototype, mockup, throwaway, quick validation, in-repo prototype, coding agent prototype, prototype harness
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
| `way-in.md` | Step 1 - getting from a raw idea to something buildable, and deciding whether code is the right test at all | the scope is a thought rather than a named chunk |
| `hypotheses.md` | Steps 2 and 8 - what makes a hypothesis testable, what thresholds are defensible, and the four verdict states | writing the success criterion, and recording the result |
| `audience-depth.md` | Step 3b - who it is for, how deep that makes it, and which path builds it | **every run**, right after ingestion |
| `in-repo-loop.md` | The harness shell contract, the rules of the iteration loop, stop and restart signals | the prototype is built here, by a coding agent |
| `prototype-folder.md` | Step 7 - the folder an in-repo prototype lives in, `targets:`, the decision state | writing an in-repo prototype back |
| `promotion.md` | Classification before the first line of code; kill and promotion once there is a decision | Step 3b, then Step 8 |
| `scaffold/` | The harness itself - copy it into the prototype's build folder | on the in-repo path |

---

## What this skill does

Takes a scoped chunk of the product and gets a prototype of it built, so you can validate a flow, a UX hypothesis, a concept, or technical feasibility **before** anyone writes production code.

**Two paths, chosen at Step 3b, not assumed:**

| | |
|---|---|
| **External tool** | compiles a tool-ready spec and hands it to Lovable / v0 / Figma Make. One shot out, iteration goes back through the tool |
| **In-repo** | builds here, with a coding agent, against a harness that carries states, fixtures, time, variants, device presets, annotations and an event log. A continuous loop with no moment of handoff |

The path is an **output of the flow, not an input**: it follows from who the prototype is for and which uncertainty it resolves. Do not ask the user to pick it up front.

The scope is whatever you point at, with **no limit**:
- a single **feature** (linked to a Feature Card),
- a **PRD initiative** (a larger new part),
- the **whole product**,
- or any **slice** ("for this user type, test this part of the functionality").

**Cross-phase.** Like adding a hypothesis or running a validation, this skill has no fixed home in the sequence. Run it whenever there is genuine uncertainty worth de-risking cheaply - during discovery (concept desirability), before a PRD initiative (flow/scope), or inside Phase 6 before a feature enters build (UX/interaction).

**Two modes (same skill, same file):**

| Mode | When | What it does |
|---|---|---|
| **Spec mode** (default) | You want to build a prototype | Gate-check → ingest inputs → audience, depth and path → build it, by whichever path fits |
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

**If what arrived is a raw idea rather than a scoped chunk** - a sentence, a situation, a hunch, or a `/pureinn` run in `explore` mode - **read `references/way-in.md` and run it first.** Everything downstream assumes a concept that already has an actor, a mechanism and a killer assumption; without those the intent gate has nothing to weigh and the prototype gets built for a problem nobody stated.

That sequence can legitimately end with *"the cheapest test of your riskiest belief is not a prototype"*. If it does, say so and stop - that is the skill working, not failing.

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

3. **Define the success criterion up front, as a hypothesis that can fail.** Read `references/hypotheses.md` § 1 and write it in the formulation there - because, we believe, this prototype represents / does not represent, we will measure, kill-iterate-persevere criteria including the ambiguous zone, and the rival explanation.

   The short form - *"the prototype succeeds if [observable signal], otherwise we [change / halt]"* - is the minimum, and it is only usable when the signal is **behaviour rather than opinion** and the threshold is written down before anyone sees a result. A threshold agreed after seeing the data is a rationalisation, not a threshold.

   If `references/way-in.md` ran, its **test contract already is this criterion** - carry it forward rather than writing a second one. Two success criteria for one prototype means the result can always be narrated against whichever one it happened to clear.

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

---

## Step 3b: Audience, depth and path

**Read `references/audience-depth.md` and run it.** This is where the run stops being one-size-fits-all: it decides how deep the prototype has to be, and by which of two structurally different paths it gets built.

1. **Who is it for?** AskUserQuestion, multi-select. The audience decides what must be real and what may be admitted-fake - those differ per audience, which is why depth is not a single dial. More than two audiences: warn and ask for the primary one.
2. **Which uncertainty does it resolve?** Step 2 already established the intent; carry it here rather than asking again. Propose the row the audience implies and confirm.
3. **Route** - and say which path you are taking and why, in one line, before continuing:

| Path | Nature | Continue with |
|---|---|---|
| **External tool** | one-shot handoff - compile the brief, send it, iterate through the tool | `references/external-tools.md` (Step 4), `references/spec-artifact.md` (Step 5), then Step 6 |
| **In-repo** | a continuous loop - no brief to compile, no moment of handoff | `references/in-repo-loop.md`, plus `references/scaffold/` for the harness |

Both paths return here for **Step 7**.

Two conditional requirements fall out of the audience answer, so settle them now rather than discovering them later:

- **Variants** are mandatory when the prototype exists to *choose* a direction, and wrong when it is an answer to a decided one.
- **Behaviour capture** earns its place the moment real users touch it, and is overhead when a reader reviews it alone.

**Then classify it, before any code exists** - `references/promotion.md` § Classification. Disposable, Reference or Evolutionary decides the quality bar and where the code lives, so deciding it afterwards means the bar was never applied. Evolutionary code belongs on a branch in the real repo, under repo rules, not in the prototype folder. If nobody can say which one it is, that is itself a finding: it usually means the prototype is being built to impress rather than to answer something.

---

## Step 7: Write the prototype reference back

**If feature-scoped:** add a reference to the Feature Card (do not touch Sections 1-4 spec content - add a lightweight reference note / frontmatter field):

```
Prototype: [see path below]
Prototype URL: [live/preview URL, local harness URL, or "pending build"]
Audience: [primary audience from Step 3b]
Expected outcome: [the success criterion from Step 2]
Result: pending
```

The `Prototype:` value depends on which path Step 3b took:

| Path | What it points at |
|---|---|
| External tool | the spec file - `/prototypes/[FEAT-ID]-prototype-spec.md` |
| In-repo | the prototype's folder - `/prototypes/[name]/`. **Read `references/prototype-folder.md` and create it there**; `meta.md` carries the uncertainty, audience, classification, `targets:`, the declared stop condition and the decision state |

This makes the Feature Card show that a prototype was used and that a result is expected before build proceeds.

**If initiative/product-scoped:** log the prototype as a validation instrument against the relevant hypothesis in the hypothesis register (or note it for `pm-hypotheses`).

External path: save the spec to `/prototypes/` (Step: Save to). In-repo path: the folder is already the artifact - do not also write a spec file for it, or the same prototype exists twice and the two will drift.

---

## Step 8: Result mode (re-run after the prototype exists)

When the user comes back with an outcome, operate in **delta mode** - do not rewrite the spec, append to its `## Result` section:

1. **Capture what happened:** what was built, what was tested, with whom (if users saw it).
2. **Verdict against the success criterion:**

**Read `references/hypotheses.md` § 4 before writing the verdict.** The four states are not a relabelling of pass/fail - the third one exists to stop a broken test being recorded as a verdict on the idea.

```markdown
## Result

**Date:** [YYYY-MM-DD]
**Built:** [what the prototype ended up being - URL or folder]
**Audience:** [who it was actually shown to]
**Tested with:** [n, and who they were - "self" is a valid and important answer]

### Verdict - one of four, never "validated"
[ ] Supported within scope - cleared the precommitted bar, for [population / context / represented dimension], with [stated uncertainty]
[ ] Refuted within scope - crossed the negative threshold, rival explanations checked by [control]
[ ] Prototype or study failure - the instrument did not expose the hypothesis. **Belief in the product is unchanged**
[ ] Inconclusive - fell in the ambiguous zone, or too weak for this decision

**Where it failed, if it did:** [study instrument / representation / interaction design / value proposition / feasibility-viability - the failure tree in references/hypotheses.md § 4]

**What we observed:** [behaviour, not opinion]
**What we did not test:** [the excluded dimensions named in the hypothesis]
**Known distortions:** [demand effects if the maker moderated; staged behaviour; small n and the bound it actually supports]
```

3. **Cascade** (surface, do not silently edit) - and only on the two states that carry evidence:
   - Feature-scoped → update the Feature Card prototype reference with the state; if refuted, flag before `pm-feature-design` / build.
   - Hypothesis-linked → update the hypothesis register; recommend `/pm-hypotheses`.
   - If the result changes scope or desirability → recommend re-checking `pm-prd` / `pm-features-list` / `pm-mvp-scope`.

   **A prototype-or-study failure cascades nowhere.** It updates nothing downstream, because nothing was learned about the product - it says the instrument needs fixing and the test re-running. **Inconclusive** cascades nothing either; it schedules another round or a different method.

4. **Before a kill is recorded, check it is defensible** - all five conditions in `references/hypotheses.md` § 4. Before that bar is met, "iterate the representation" is usually the more accurate conclusion than "the idea is wrong".

5. **Act on the decision** - `references/promotion.md`. The verdict is what the evidence says; the decision is what you do about it, and they are not the same field.

   | Decision | What happens |
   |---|---|
   | **Kill** | findings kept, code not. Folder deleted or archived with the reason; production registers untouched; an Evolutionary branch closed explicitly rather than abandoned |
   | **Promote** | layer by layer - thin card becomes a Feature Card with a real `FEAT-ID` and `promoted_from:`; local rules and entities move into the global registers; the folder then **freezes as history and is never edited again** |
   | **Partial** | promote what earned it, kill the rest **explicitly**, and record which was which. A partial decision that does not say what was dropped is an open decision wearing a decided label |

---

## Internal completeness checklist

<!-- Claude reference only -->

**Every prototype spec must have:**
- [ ] Scope + intent + a success criterion written as a hypothesis that can fail, with its ambiguous zone, before anyone sees a result
- [ ] In-scope / out-of-scope (out-of-scope fence is non-negotiable)
- [ ] Primary screen named + build-first
- [ ] Flow narrative
- [ ] Fidelity stated (static vs functional)
- [ ] Raw idea: the way-in ran, and the code-vs-no-code decision was made explicitly rather than assumed
- [ ] Audience named, and depth chosen from it rather than from habit (Step 3b)
- [ ] Path stated out loud with its reason before building
- [ ] External path only: compiled build prompt following the tool's construction rules (`references/external-tools.md`; Lovable rules if Lovable)
- [ ] In-repo path only: harness in place per `references/in-repo-loop.md`, all four states reachable
- [ ] Classification decided **before** the first line of code, and Evolutionary code on a real branch rather than in the prototype folder
- [ ] In-repo path only: the prototype folder exists per `references/prototype-folder.md`, with `targets:` and a declared stop condition
- [ ] Local `domain.md` / `rules.md` / `context/` exist only where the prototype deliberately diverges, and say in what way

**Never skipped:**
- [ ] Intent gate ran (prototype justified, or user chose to proceed anyway)
- [ ] MCP warning shown before any live call
- [ ] Feature Card prototype reference written (if feature-scoped) - reference only, spec sections untouched
- [ ] Lovable target: Knowledge Base loaded (`set_project_knowledge`) + confirm-understanding gate passed before any code

**Result mode:**
- [ ] Verdict is one of the four states - never the word "validated"
- [ ] A prototype-or-study failure cascaded nowhere
- [ ] Small-n results reported as the bound they support, not as a percentage
- [ ] Demand effects named when the maker was also the moderator
- [ ] Synthetic-user output never recorded as user evidence

**Never guessed (hard rule):**
- Screens, flows, entities, fields, features, copy must come from real artifacts or user input - never fabricated
- Missing input → asked via AskUserQuestion, not filled with invention; assumptions marked `[ASSUMED - confirm before build]`
- FEAT-ID verified against feature_list.md if referenced

---

## Save to

Both paths write under `pureinn-workspace/[project-slug]/prototypes/`, in different shapes:

```
prototypes/[scope-slug]-prototype-spec.md     external path - one spec file
prototypes/[prototype-name]/                  in-repo path - a folder
```

External path, feature-scoped: `[FEAT-ID]-prototype-spec.md`. Initiative, product or slice: a descriptive `[scope-slug]`.

In-repo path: a kebab-case folder named for what it explores - `ama-lifecycle`, `pricing-tiers` - never for a date or a version. Shape in `references/prototype-folder.md`.

**Never both for the same prototype.** One prototype, one artifact; two means they drift and nobody knows which one is current.

`prototypes/` is a cross-cutting operational folder (like `meetings/`, `team/`) - created on demand, not part of the phase artifact flow.

---

## Handoff

**Čo si teraz má:** Tool-ready prototype spec - viem ho pushnúť do Lovable/v0/Figma Make (alebo vložiť manuálne) a dostať funkčný/klikací prototyp, ktorý validuje konkrétnu neistotu **pred** reálnym buildom. Feature má zapísanú referenciu, že prototyp beží a čaká sa výsledok.

**Ďalší krok:**
- Po postavení prototypu → spusti `/pm-prototype` znova (result mode) a zapíš verdikt.
- Ak validované → `/pm-feature-design [FEAT-ID]` pre produkčný spec.
- Ak validované na úrovni iniciatívy/konceptu → `/pm-hypotheses` (aktualizuj hypotézu) alebo `/pm-prd`.

**Môžeš preskočiť ak:** Ide o štandardný, nízko-rizikový pattern bez otvorenej neistoty - vtedy prototyp nepridáva hodnotu a ide sa rovno na `/pm-feature-design`.
