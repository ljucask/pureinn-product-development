---
name: pm-discovery-report
description: Generate the client-facing Discovery Report - a narrative "here is what we heard, here is what we recommend" document for whoever commissioned the work. Incremental and re-runnable - update it after each discovery session, finalize it when Phase 2 converges. Companion to pm-problem-validation (which stays the internal Go/No-Go verdict); this is the version you hand to the client. Feeds pm-scope-brief.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: discovery report, client report, discovery summary, what we heard, discovery handoff, client deliverable
  role: specialist
  scope: documentation
  output-format: document
  related-skills: pm-meeting, pm-discovery-interview, pm-problem-validation, pm-scope-brief, pm-personas
---

# PM - Discovery Report (client-facing)


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Produces the document you put in front of the client: what we heard from you, what we learned about your users and processes, where the value is, what we recommend, what's still open. Its job is dual:

1. **Confirmation loop** - "did we understand you correctly?" Errors caught here cost a conversation; errors caught in build cost a sprint.
2. **Credibility** - a structured, insightful read-back of their own business is the strongest expertise signal you can send during discovery.

**Two documents, one truth:** `pm-problem-validation` remains the internal convergence artifact (verdict, track completeness, Go/No-Go framing). This report retells the same findings for the client - narrative, no internal scaffolding. Never let the two diverge on facts; they differ only in audience and tone.

**Incremental by design:** run it after the first session and re-run after each one. The report header states its own maturity ("Discovery in progress - based on N sessions" → "Final"). An interim report sent mid-discovery is a feature, not a compromise - it keeps the client in the confirmation loop.

---

## Dependencies

**Reads (whatever exists - none are hard prerequisites):**
- `meetings/` - all client-discovery and customer-discovery notes (primary source early on)
- Track A-D artifacts in `artifacts/phase-2-discovery/` (as they appear)
- `problem-validation-summary.md` - when it exists, the final report anchors to it

**Produces artifacts used by:**
- `pm-scope-brief` - the Discovery Report is its primary input
- `design-thinking` - client context and value alignment feed the Define stage (if Phase 3a runs)

---

## Step 0: Current state check

1. Read all sources above in full (deep source ingestion - every meeting note, recursively). Confirm coverage: "Read [N] meeting notes + [N] artifacts."
2. Check for an existing `discovery-report.md`:
   - **Exists → delta mode.** Read it first. Update only what new sessions/artifacts support: `[UPDATED - previous: X / new: Y]` markers in the draft you show the user (strip markers from the client-facing final after confirmation). Never silently reverse a previous statement the client already read - flag reversals explicitly.
   - **Doesn't exist →** first version, maturity = interim unless Phase 2 is already converged.
3. Determine maturity: **Interim** (sessions ongoing, tracks incomplete) or **Final** (Problem Validation Summary exists or user says discovery is done).

**Provenance discipline (critical for honesty toward the client):** every claim in the report carries its source class - what THEY told us (their words), what we observed/researched, what their users said, and what remains `[ASSUMED]` or `[CLIENT-ASSERTED]` awaiting validation. The client must be able to see which parts are their own statements played back vs. our findings.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Frame the report

Use AskUserQuestion tool:

What is this version of the report for?

  A) Interim check-in - keep the client in the confirmation loop mid-discovery (Recommended while sessions are ongoing)
  B) Final discovery handoff - discovery is converged, this closes Phase 2 toward scope definition
  C) Decision support - client needs to decide whether to proceed / fund the next stage

Then ask as plain text:

Anything sensitive to handle carefully? (e.g. a finding that contradicts the client's stated belief, a value-alignment tension, a reference we recommend NOT copying) - these go in, but framed constructively; name them now so the framing is deliberate.

---

## Step 2: Generate artifact

Generate in English. Narrative tone - professional, direct, concrete. No internal jargon (no Track A-D, no FEAT-IDs, no framework skill names), no ✅/⚠️/❌ verdict scaffolding, no completeness tables. Depth over breadth: omit sections with nothing real in them rather than padding.

---

### ARTIFACT: Discovery Report

```markdown
# Discovery Report - [Client / Product Name]

> **Status:** [Discovery in progress - based on N sessions (dates) / Final]
> **Prepared by:** [name] · **Date:** [date]
> **Purpose:** What we heard, what we learned, what we recommend - please read with one question in mind: *did we understand you correctly?*

---

## 1. Why this project - your context as we understand it

[Narrative, 1-2 paragraphs: their trigger, why now, what happens if nothing changes.
Their words where possible - quoted or closely paraphrased.]

**What this product must do for your business:**
[The product's job at business level - earn more / spend less / reduce risk / comply - stated concretely with the numbers or outcomes they named.]

## 2. What success looks like

[The success criteria they named, played back concretely. If they defined failure, include it - it sharpens the target.]

## 3. Who will use it

[The three populations, each 1 short block - omit any that genuinely doesn't apply:]

**Your customers:** [who, what they need, key pains - marked by source: "from our sessions with your users" vs. "as you described them - to be confirmed with real users"]

**Your team:** [who operates it daily, what their workday needs from it]

**You / management:** [oversight, reporting, control needs]

> Where our picture of your users rests on your description rather than direct user research, we've marked it - [validated with users / your assessment, recommended to validate / assumption]. [State plainly what validation we recommend, if any.]

## 4. How the work flows today - and where it hurts

[Per core process walked through: short narrative of the as-is flow, the friction points, the exceptions that matter. This section is where the client sees you understood their operation - be specific.]

## 5. What you asked for - and what we heard behind it

[The requests, each translated: what was asked → the need behind it. Include references honestly:]

**References you mentioned:** [per "like company XY": what specifically appeals, what that product does under the hood that you may not need (or do), and our take - adopt / adapt / avoid, with the reason.]

## 6. Where we see the value

[Value hypothesis: the connection between their business goal (section 1-2) and their users' needs (section 3-4).
**If there is a tension between what the business wants and what users need - name it here, constructively:** what the tension is, why it matters, how we suggest resolving it. Hiding it now means designing around it silently later.]

## 7. What we recommend

[Direction, not spec: the shape of what should be built and why, anchored to sections 1-6. 3-6 concrete recommendations. Where relevant: what we recommend NOT doing, and what to defer.]

## 8. Constraints we're designing within

[The real ones that shape the solution: systems to integrate with, data situation, content responsibilities, brand, operations after launch, timeline. Include who owes what - e.g. content delivery on the client side.]

## 9. Open questions

| Question | Why it matters | Suggested way to resolve |
|---|---|---|
| [open item] | [impact on scope/direction] | [next session / user validation / client decision] |

## 10. Next steps

[Concrete: what happens next on our side, what we need from you (access, content, user introductions, decisions), and what document follows this one (the Scope Brief - what exactly will be built).]
```

---

## Step 3: Review before it leaves the building

Show the draft. Walk the user through: (1) any `[UPDATED]` deltas vs. the previous version, (2) the sensitive items from Step 1 and how they're framed, (3) provenance honesty - nothing `[CLIENT-ASSERTED]` presented as validated. Confirm, then strip working markers and finalize.

---

## Internal completeness checklist

<!-- Claude reference only -->

- [ ] Every claim traceable to a meeting note or artifact - nothing invented
- [ ] Provenance visible to the client (their words vs. our findings vs. assumptions)
- [ ] Value-alignment tension surfaced if it exists - never silently omitted
- [ ] References addressed with a recommendation (adopt/adapt/avoid), not just listed
- [ ] No internal framework jargon or verdict scaffolding
- [ ] Open questions have a resolution path, not just a list
- [ ] Interim vs. Final status honest in the header
- [ ] Facts consistent with pm-problem-validation (if it exists) - same truth, different audience

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-2-discovery/discovery-report.md
```

---

## Handoff

**Čo si teraz má:** Klientský Discovery Report - potvrdenie porozumenia + odporúčaný smer, ktorý môžeš poslať klientovi (aj priebežne počas discovery).

**Ďalší krok:** Interim → pošli klientovi na potvrdenie a `/pm-discovery-interview` na ďalšie sedenie. Final → `/pm-scope-brief` (definícia čo presne postaviť). Ak beží plná validácia, `/pm-problem-validation` zostáva interným uzáverom Phase 2.

**Môžeš preskočiť ak:** Nemáš externého zadávateľa (vlastný produkt, solo) - interná Problem Validation Summary stačí, klientská verzia nemá komu ísť.
