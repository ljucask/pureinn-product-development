---
name: pm-meeting
description: Structured meeting notes, summary, and action items from raw notes or a transcript. Detects meeting type (Customer Discovery, Product Review, Planning/Grooming, Strategic Review, Standup/Retro, Partner/Vendor) and applies the correct summary template. Tags each action item with its destination (Notion Task, Feature Card, follow-up meeting, framework skill). Pushes to Notion Meetings DB with linked tasks. Run after any meeting where notes or a transcript exist.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: meeting, notes, transcript, summary, action items, action points, standup, retro, retrospective, planning, grooming, customer interview, discovery call, strategic review
  role: specialist
  scope: documentation
  output-format: document
  related-skills: pm-personas, jtbd-building, pm-problem-validation, pm-stripe, pm-feature-card, pm-product-roadmap, pm-prd, pm-team-roster
---

# PM - Meeting Notes & Action Items

## What this skill does

Takes raw meeting notes or a transcript and produces:
1. Structured meeting summary (template depends on meeting type)
2. Decisions log (what was settled)
3. Action items - each tagged with its destination and owner
4. Notion push - new record in Meeting DB + linked tasks

**Six meeting types, six routing paths:**

| Type | Signal keywords | Primary output destination |
|---|---|---|
| **Customer Discovery** | customer, user, prospect, "they said", pain, interview | Insights → personas / jtbd / problem-validation |
| **Product Review** | FEAT-, AC-, spec, design review, Section, Figma | Feature Card update / pm-feature-design re-run |
| **Planning / Grooming** | sprint, stripe, priority, backlog, phase, who takes what | feature_list update / pm-stripe / pm-mvp-scope |
| **Strategic Review** | roadmap, investor, revenue, phase gate, business model, PRD | pm-prd / pm-product-roadmap delta |
| **Standup / Retro** | yesterday, today, blocker, retrospective, what went well | pm-stripe (blockers) / Notion tasks (retro actions) |
| **Partner / Vendor** | partner, vendor, contract, integration, API, SLA | Notion tasks + Google Calendar follow-up |

**Action item tags (applied to every action item regardless of type):**

| Tag | Meaning |
|---|---|
| `[Notion Task]` | Standalone task in Notion, assigned to a person with deadline |
| `[Feature Card: FEAT-ID]` | Update or create a Feature Card for this item |
| `[Meeting: person, topic, by when]` | Schedule a follow-up meeting |
| `[Skill: /pm-xxx]` | Run a framework skill to process this item |

---

## Dependencies

**Recommended:**
- `pm-team-roster` - to resolve names to real team members when assigning action items
- `pureinn-variables.md` - key "Meetings" must contain the Notion DB URL for push

---

## Step 0: Read pureinn-variables + current state

Read `pureinn-variables.md`:
- Check "Meetings" key for Notion DB URL
- Check "Feature Backlog" key (for Feature Card action items)
- Check "Team Roster" for member list (to validate assignees)

If "Meetings" URL is blank: proceed, save locally, remind user to push manually.

---

## Step 1: Intake

Ask as plain text:

Paste your meeting notes or transcript below. Include participants if you have them.

Then ask:

```
[Use AskUserQuestion - meeting type]

What type of meeting was this?

A) Customer Discovery - call or interview with a user, prospect, or customer
B) Product Review - team reviewing a feature, spec, design, or PRD
C) Planning / Grooming - sprint planning, backlog grooming, stripe assignment
D) Strategic Review - roadmap, investor update, stakeholder alignment, business model
```

If Standup or Retro, or Partner / Vendor - offer as "Other" option / user describes.

Then ask as plain text:

Date and time of the meeting? (YYYY-MM-DD)

Who attended? (names + roles if known - or paste from calendar invite)

---

## Step 2: Auto-detect + confirm type

If the notes contain strong type signals (see signal keywords in the routing table), state the detected type before asking:

```
Detected meeting type: [Type] (based on: [signal found])
Is this correct?
```

Confirm with a simple yes/no before proceeding.

---

## Step 3: Generate artifact

---

### ARTIFACT: Meeting Notes - [Date] - [Topic]

```markdown
# Meeting Notes - [Date]
**Type:** [Meeting type]
**Topic:** [Inferred from notes - 3-5 words]
**Date:** [YYYY-MM-DD]
**Participants:** [list]
**Duration:** [if known]

---

## Context

[1-2 sentences: what prompted this meeting, what was the goal]

---

## Summary

[3-6 bullets: the most important things that happened or were discussed.
Not a transcript replay - only what matters for decisions and next steps.]

---

## Decisions

Things that were settled in this meeting. Do not re-open without new evidence.

| # | Decision | Owner | Rationale |
|---|---|---|---|
| 1 | [what was decided] | [person] | [why - brief] |

[If no decisions were made: "No decisions made - discussion only."]

---

## Action Items

| # | Action | Owner | Deadline | Destination |
|---|---|---|---|---|
| 1 | [clear, specific action] | [person] | [date or "ASAP"] | [tag - see below] |
| 2 | | | | |

**Destination tags:**
- `[Notion Task]` - goes to Notion as a task linked to this meeting record
- `[Feature Card: FEAT-ID]` - update or input to a specific Feature Card
- `[Meeting: person, topic, by when]` - schedule a follow-up
- `[Skill: /pm-xxx]` - run a framework skill to process this

---

## [TYPE-SPECIFIC SECTION]

[See below - insert the relevant block for the detected meeting type]

---

## Open Questions

Things raised but not resolved. Not action items yet - but need a decision.

- [Question 1 - who needs to resolve it]
- [Question 2]

[If none: omit this section.]
```

---

### Type block A: Customer Discovery

```markdown
## Customer Insights

**Participant:** [Name, role/context, company if relevant]

### Pains surfaced

| Pain | Intensity (H/M/L) | Current workaround | Direct quote |
|---|---|---|---|
| [pain description] | [H/M/L] | [what they do today] | "[their words]" |

### Goals and jobs-to-be-done

- [What they're trying to achieve in their own words]

### Reactions to our product / solution

| Aspect shown | Reaction | Quote |
|---|---|---|
| [feature or concept] | [positive / negative / confused / interested] | "[quote]" |

### Hypotheses affected

[List any existing hypotheses (from hypothesis register) that this call confirms, refutes, or opens]

- [HYP-ID]: [confirmed / refuted / new signal] - [brief reason]

### Recommended next skills

[Based on insights - which framework skills should process this:]
- `/pm-personas` - if new segment signal or persona update
- `/jtbd-building` - if new job or force identified
- `/pm-problem-validation` - if this call validates or refutes core problem hypothesis
```

---

### Type block B: Product Review

```markdown
## Review Scope

**What was reviewed:** [Feature Card FEAT-ID / PRD section / design file / other]

### Findings

| Item | Finding | Severity | Action |
|---|---|---|---|
| [Section 1 / AC / diagram / other] | [what was found] | [P0/P1/P2/cosmetic] | [what to do] |

### Spec changes needed

[List any changes to Feature Card Sections 1-3, business rules, or acceptance criteria]

- [ ] [Specific change - who makes it - by when]

### Design Inspection result (if design was reviewed)

[ ] Approved - ready for `3_Ready_to_Build`
[ ] Changes needed - listed above
[ ] Re-run `/pm-feature-design [FEAT-ID]`
```

---

### Type block C: Planning / Grooming

```markdown
## Decisions Made

**Features committed to next stripe:** [FEAT-IDs]
**Features de-prioritized or moved:** [FEAT-IDs + where they moved]
**Phase changes:** [if any feature's phase changed]

### Stripe state after this meeting

| Stripe | Active feature | Queue (in order) |
|---|---|---|
| [stripe-name] | [FEAT-ID] | [FEAT-ID, FEAT-ID] |

### Framework updates needed

- [ ] Update `feature_list.md` - [what changed]
- [ ] Run `/pm-stripe` at next dev session
- [ ] Update Feature Card frontmatter for phase/priority changes
```

---

### Type block D: Strategic Review

```markdown
## Strategic Decisions

| Decision | Changed from | Changed to | Rationale |
|---|---|---|---|
| [e.g., Target segment] | [previous] | [new] | [reason] |

### Artifacts to update (delta mode)

[List which strategic artifacts need re-running based on what changed]

- [ ] `/pm-prd` - sections: [list]
- [ ] `/pm-product-roadmap` - sections: [list]
- [ ] `/pm-business-model` - [what changed]
- [ ] Run `/pm-audit strategy` after updates to verify cross-artifact consistency

### Stakeholder commitments

| Person | Commitment | Deadline |
|---|---|---|
| [name] | [what they committed to] | [by when] |
```

---

### Type block E: Standup / Retro

```markdown
## Status (Standup)

| Person | Done since last | Working on now | Blocker |
|---|---|---|---|
| [name] | [done] | [in progress] | [blocker or none] |

### Blockers requiring action

| Blocker | Affects | Owner to unblock | Route |
|---|---|---|---|
| [blocker description] | [FEAT-ID or person] | [who fixes it] | [pm-stripe / Notion task / other] |

## Retrospective items (if retro)

**What went well:**
- [item]

**What to improve:**
- [item] → Action: [what we'll do differently] → Owner: [person]
```

---

### Type block F: Partner / Vendor

```markdown
## Meeting Purpose

[1 sentence: what this meeting was about]

### Our commitments

| Commitment | Owner | Deadline |
|---|---|---|
| [what we agreed to deliver/do] | [person] | [date] |

### Their commitments

| Commitment | From whom | Deadline | Follow-up if missed |
|---|---|---|---|
| [what they agreed to] | [company/person] | [date] | [escalation] |

### Integration / technical items

[If technical topics were discussed - API, data format, SLA, access]

- [item]

### Follow-up meeting

- **Topic:** [what to discuss next]
- **Who:** [participants needed]
- **By:** [target date]
- **Action:** `[Meeting: organizer, topic, by date]`
```

---

## Step 4: Action item triage

After generating the summary, present action items grouped by destination:

```
ACTION ITEM TRIAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Notion Tasks ([N]):
  → [Action] — [Owner] — [Deadline]
  → [Action] — [Owner] — [Deadline]

Feature Card updates ([N]):
  → [FEAT-ID]: [what to update] — [Owner]

Follow-up meetings ([N]):
  → [Topic] — [Who] — [By when]

Framework skills to run ([N]):
  → /pm-[skill] — [reason]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Confirm this triage before Notion push? (yes / adjust)
```

Wait for confirmation before pushing.

---

## Step 5: Notion push

Read `pureinn-variables.md` key "Meetings" → Notion DB URL.

**If URL present:**

Create a new page in the Meetings DB via `notion-create-pages`:

| Notion property | Value |
|---|---|
| `Title` | `[YYYY-MM-DD] [Meeting type] - [Topic]` |
| `Type` | `[Meeting type]` (select) |
| `Date` | `[meeting date]` |
| `Participants` | `[names]` (multi-select or text) |
| `Status` | `Notes captured` |

Push meeting notes content as the page body (full artifact above).

**Tasks:** For each action item tagged `[Notion Task]`:
- Create a linked task in Notion connected to this meeting record
- Set: task name, assignee (from participants), due date

**Feature Card action items:** Do not auto-edit Feature Cards. List them in the push confirmation and remind user to update manually or run the relevant skill.

**If URL is blank:** Save locally only. Remind:
```
Notion Meetings URL not set in pureinn-variables.md.
Saved locally. To push: add the URL and re-run /pm-meeting push.
```

---

## Internal completeness checklist

<!-- Claude reference only -->

**Every meeting note must have:**
- [ ] Date, participants, type
- [ ] Summary: 3-6 bullets, no transcript replay
- [ ] Decisions table (even if empty - write "No decisions made")
- [ ] Action items: every item has owner + deadline + destination tag
- [ ] Type-specific block populated from real notes (not placeholder text)
- [ ] Open questions (if any arose)

**Action item triage:**
- [ ] Every action item tagged with exactly one destination
- [ ] Notion Tasks have assignee + deadline
- [ ] Feature Card items have FEAT-ID (or note "new card needed")
- [ ] Follow-up meetings have topic + who + by when
- [ ] Framework skill items have /skill-name + reason

**Never invented:**
- Direct quotes must come from the notes/transcript
- Participant names must come from the notes or user input
- FEAT-IDs must be verified against feature_list.md if referenced

---

## Save to

```
pureinn-workspace/[project-slug]/meetings/[YYYY-MM-DD]-[type]-[topic-slug].md
```

---

## Handoff

**Čo si teraz má:** Štruktúrovaný záznam meetingu, rozhodnutia a action items s jasnou destináciou - čo ide do Notion, čo do Feature Cards, čo vyžaduje follow-up.

**Ďalší krok (podľa typu meetingu):**
- Customer Discovery → `/pm-personas` alebo `/jtbd-building` ak insights menia persony
- Product Review → oprav Feature Card alebo re-run `/pm-feature-design [FEAT-ID]`
- Planning → `/pm-stripe` na ďalšej dev session
- Strategic Review → authoring skill v delta mode + `/pm-audit strategy`
- Standup/Retro → `/pm-stripe` pre blocker resolution

**Môžeš preskočiť ak:** Meeting bol len informačný, nevznikli žiadne rozhodnutia ani action items.
