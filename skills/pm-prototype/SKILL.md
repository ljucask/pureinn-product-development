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

Podporuje `--agent`: beží autonómne v subagentovi, nadraftuje artefakt z existujúcich vstupov, vráti krátky súhrn + coverage note.

- **Bez flagu** → interaktívne (default); pri ťažkých vstupoch ponúkni agent režim.
- **`--agent`** → poslúchni. Najprv over úplnosť vstupov. Čo chýba: NEVYMÝŠĽAJ - označ `[ASSUMED - čo/prečo]` vo výstupe aj v súhrne. Nikdy nehalucinuj medzeru.

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

Apply the standard skill interaction pattern (CLAUDE.md).

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

---

## Step 4: Select prototyping tool

From the "Prototyping" section of pureinn-variables, present the configured tools. Let the user pick which to target for this run (they may have several). If more than one is configured, use **AskUserQuestion**; recommend the tool that best fits the intent from Step 2:

- **Lovable** - functional full-stack (React + Tailwind + shadcn + Supabase). Best for clickable flows and functional/feasibility prototypes. Deepest prompt-optimization support (see the Lovable rules below).
- **v0 / Vercel** - fast UI generation, deploy to a live URL. Good for front-heavy UX/concept prototypes.
- **Figma Make** - design-native, best when the flow already lives in Figma.
- **Base44 / other** - manual paste (no MCP push here) - the compiled spec is copy-paste ready.

If no tool is configured, default to producing the spec paste-ready and note push is unavailable until an endpoint is added.

---

## Step 5: Compile the prototype spec

Generate `[scope]-prototype-spec.md`. It has two layers:

1. **Universal core** - tool-agnostic, human-readable, the source of truth for the prototype.
2. **Compiled build prompt** - the core rewritten in the selected tool's optimal format. This is what goes into the tool. For Lovable it follows the Lovable construction rules below; for other tools it follows the same universal principles adapted to that tool.

---

### ARTIFACT: [scope]-prototype-spec.md

```markdown
# Prototype Spec - [Scope name]

**Scope:** [feature FEAT-ID / initiative / product / slice]
**User type (if scoped):** [type or "all"]
**Intent:** [UX-flow / concept / feasibility / stakeholder]
**Target tool:** [Lovable / v0 / Figma Make / manual]
**Success criterion:** [The prototype succeeds if [observable signal], otherwise we [action].]
**Status:** Spec ready → awaiting build

---

## 1. Goal (what we are learning)

[2-3 sentences. What decision is blocked on this prototype. What signal we are hunting.]

## 2. In scope / Out of scope

**In scope (build this):**
- [screen / flow / interaction]

**Out of scope (do NOT build - fence hard):**
- [everything the tool must not wander into - auth if not needed, admin, other user types, real payments, etc.]

## 3. Screens + flow

**Primary screen (build first):** [name] - [detailed contents]

| Screen | Purpose | Key elements | Reached from |
|---|---|---|---|
| [screen] | [why] | [components] | [prev screen / entry] |

**User flow (narrative):**
[User lands on X → does Y → sees Z. Map from pm-process-flows.]

## 4. Data + key interactions

[Only if functional. Entities + key states the prototype needs, and what each core interaction does.]

- [Entity]: [fields the prototype shows], states: [state → state]
- Interaction: [action] → [result]

## 5. Design guidance

- **Fidelity:** [static click-through / functional]
- **For whom:** [persona - tone, polish level]
- **Look:** [design principles, color, typography, layout, nav - or "tool default taste"]
- **Responsive:** mobile-first, shadcn + Tailwind breakpoints.

## 6. Acceptance signals (maps to success criterion)

[The concrete things a user/tester must be able to do or feel for the prototype to have answered the question.]

- [ ] [signal]

---

## Compiled build prompt ([tool])

> Paste this into [tool], or push via MCP (Step 6).

[The compiled, tool-optimized prompt - see construction rules below.]

---

## Result

[Empty until Result mode (Step 8). Do not fill at spec time.]
```

---

## Lovable build-prompt construction rules

**These are baked in - when the target is Lovable, the compiled build prompt MUST follow them.** They come from the Lovable Prompting Bible and are what separates a usable first prompt from a credit-burning mess. For other tools, apply the same underlying principles (front-load, fence scope, explicit stack, flow narrative, plan-first) adapted to the tool.

1. **The first prompt is everything.** `create_project(initial_message)` sets the tone for the entire build. It must be complete and precise upfront - not "we'll clarify later."

2. **Front-load and book-end.** The tool weights the **start and end** of the prompt most. Put app type + primary goal in the first two sentences. Restate the single hardest constraint (usually the out-of-scope fence) at the very end.

3. **Opening pattern:** start with `I need a [type] application with:` then the tech stack.

4. **State the stack explicitly, even if default.** Lovable default: Frontend React, styling Tailwind + shadcn/ui, Auth + DB Supabase (native). State it. Only override if the spec requires it.

5. **Split features: main vs secondary.** Do not present a flat list of equal features.

6. **In-scope / out-of-scope is mandatory.** This is the single most important block for a prototype - it stops the tool building the whole product. Explicitly fence what NOT to build ("Do not build auth / admin / other user types / real payments").

7. **Screen-by-screen, section-by-section.** Do not pile 5 things into one instruction. Name the pages, then direct: `Start with the [primary page] containing: [detailed requirements]`. Build order: front design first (page by page) → then backend/Supabase → then UX refinement.

8. **Flow as narrative.** "User lands on X → clicks Y → sees Z." Maps from pm-process-flows.

9. **Design guidance concrete.** Design principles, color palette, typography, layout, nav. Always mobile-first and responsive on shadcn/Tailwind breakpoints - no custom breakpoints unless required.

10. **Data model only if functional.** Entities + key states → Supabase tables. A static click-through skips this ("use mock data, no backend").

11. **Plan-first tail.** End the prompt with: `Before writing any code, create a phased plan, save it as plan.md, and confirm your understanding of the scope and what is out of scope before building.` This pairs with `plan_mode=true` on the first message and prevents hallucinated scope.

12. **Precision over vibes.** Specific element placement + consistent styling. Never "make it nice" - say what, where, and how.

13. **Fidelity calibration.** Match tool effort to the intent (Step 2). State it in the prompt: static clickable click-through vs. functional CRUD with real data.

14. **The spec IS the Knowledge Base.** Lovable's biggest lever is its project Knowledge Base (PRD, app/user flow, tech stack, frontend guidelines, backend structure). Our spec sections 1-5 map onto exactly those. Load the spec into the project Knowledge Base (`set_project_knowledge` via MCP), not only the first message - it grounds every subsequent prompt and cuts hallucination + credits.

15. **Confirm understanding before code.** The first message ends with: `Before writing any code, review the Knowledge Base and tell me your understanding of what to build and what is out of scope. Do not write code yet.` Only after the tool plays scope back correctly do you let it build. This is the anti-hallucination gate, paired with `plan_mode=true`.

**Multi-variant validation (UX hypothesis with competing directions):** when the intent is to compare directions, instruct: `Build N versions of [screen], each with a different [layout/visual approach], deploy all N, and return the live URLs.` (Lovable `create_project` per variant, then `deploy_project`.)

**Iterating a prototype (send_message):** scope-lock every follow-up - `Change only [X]. Do not alter [Y or Z]. Test that nothing else regresses.` Use `plan_mode=true` for delicate changes. For a visual-only tweak: `Make only visual changes. Do not touch logic, state, or APIs.`

---

## Lovable operational tactics (from the Bible)

These govern **how the run behaves** once the prompt is in Lovable - the skill applies them during handoff and iteration, and surfaces the relevant ones to the user.

**Credit economics (do not waste the user's credits):**
- **Free:** "Try to Fix" and publishing/deploy do **not** cost credits. Use "Try to Fix" first on any build error.
- **Costs credits:** each build message, and especially SQL / database scripts. When the prototype needs DB work, ask Lovable to output **all** SQL first (in one go) rather than running it piecemeal.
- One instruction at a time - piling 5 asks into one message burns credits and causes hallucination loops.

**Chat/plan mode vs build mode:**
- Use `plan_mode=true` (discuss, no code changes) for: the initial scope confirmation, weighing approaches, and any delicate change. It does not modify the project.
- Use normal build mode only once scope is confirmed.

**Debugging ladder (when a build breaks - climb in order, stop when fixed):**
1. **"Try to Fix"** up to 3 times (free).
2. Still broken → copy the error into a `plan_mode` message: `Use chain-of-thought reasoning to find the root cause. Do not edit code yet - investigate logs, flow and dependencies first, then propose a fix.`
3. UI bug → attach a **screenshot** (`files` on `send_message`) showing actual vs. intended.
4. Persistent → `Map the full flow (auth, data, integrations, state, redirects), document expected vs actual, and identify the root cause with evidence before changing anything.`
5. Debugging spiral → **revert to the last working version** rather than digging deeper.

**Reduce hallucination with visuals:** pass wireframes / Figma screenshots / reference UIs as `files` attachments on the message. A picture fences the design far better than prose.

**Reverse-meta (feed learnings back):** when a prototype iteration surfaces a fix or a scope correction, capture it in the spec's `## Result` (Step 8) as a reusable note - so the next prototype/spec starts one degree more precise.

**Note on scope:** the Lovable Bible also carries extensive refactoring / codebase-audit / production-maintenance prompts. Those are for mature production codebases and are **out of scope for a throwaway prototype** - do not apply them here. If a prototype graduates to real build, that is `pm-feature-design` + the build skills, not this skill.

---

## Step 6: Hand off to the tool

**If an MCP endpoint is configured for the selected tool:**

Confirm before any live call - MCP calls run on the user's real account and spend real credits.

**Lovable (mcp.lovable.dev):**
1. Warn once: `Lovable MCP = celý účet, live kredity, deploy je verejný na Free/Pro. Pokračovať?`
2. `create_project(initial_message = compiled build prompt, plan_mode = true)` - plan mode first so the tool confirms scope before spending build credits.
3. **Load the Knowledge Base:** push spec sections 1-5 into the project via `set_project_knowledge` so every later prompt is grounded (rule 14). Do this right after project creation.
4. **Confirm-understanding gate (rule 15):** the plan-mode reply must play the scope + out-of-scope back correctly. If it invented anything, correct it in `plan_mode` before allowing any code. Do not proceed on a wrong readback.
5. Return the **preview URL** and the tool's plan for the user to approve.
6. On approval, let the tool build; iterate via `send_message` with scope-locked follow-ups (attach screenshots as `files` for UI direction/bugs). Apply the debugging ladder if a build breaks.
7. When the user is happy: `deploy_project` → capture the **live URL** for the prototype reference.

**v0 / Vercel:** push the compiled prompt, return the deploy URL.

**Figma Make / Base44 / no endpoint:** present the compiled build prompt as a copy-paste block and tell the user to paste it into the tool. Remind them the spec is the source of truth if they iterate.

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
- [ ] Compiled build prompt following the tool's construction rules (Lovable rules if Lovable)

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
