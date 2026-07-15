---
name: pm-discovery-interview
description: Prepare a session-specific agenda for a live discovery session with a client, sponsor, or their users. Reads what discovery has already covered (meetings, Track artifacts), finds the biggest remaining gaps, and compiles a targeted agenda from its built-in discovery question bank (two planes - commissioner + real users; three user populations; full technique library - all embedded, no external file needed). Use before every client discovery session in Phase 2. After the session, process notes with pm-meeting.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: discovery interview, client session, interview prep, discovery call, session agenda, client meeting prep, requirements session
  role: specialist
  scope: research
  output-format: document
  related-skills: pm-meeting, pm-discovery-report, pm-scope-brief, pm-personas, jtbd-building
---

# PM - Discovery Interview Prep


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the agenda from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Prepares you for a live discovery session. It does NOT run the interview - the interview happens in the room, guided by the agenda this skill produces. This skill:

1. Reads what discovery has already covered (prior `meetings/` notes, Track A-D artifacts, the Discovery Report if one exists)
2. Builds a **coverage map** - which discovery areas are done, thin, or untouched
3. Compiles a **session agenda** targeting the biggest gaps, with the actual questions, follow-ups, and techniques written out in full
4. Saves the agenda to `meetings/prep/` so it pairs with the meeting note that `pm-meeting` produces afterward

**Self-contained (no external file needed):** the complete question bank and technique library are embedded in this skill, in the **Question bank** section at the bottom. The skill depends on nothing outside itself - no companion document, no `docs/` file. Run it standalone at any time: to compile a targeted agenda, to walk the full set of questions live with a client, or to proof-check your own idea by being your own toughest client.

**Standalone agenda output:** the agenda it produces is also self-contained - every question, follow-up, red-flag answer, and technique is written out in full, not referenced by module number. Print the agenda and walk into the session with nothing else; no laptop, no file, no Claude running during the session itself.

---

## The coverage areas (module map)

Each area maps to a module in the **Question bank** below. Use this to decide what a session should target; pull the actual questions from the matching module.

| Area | Module | Covered when |
|---|---|---|
| Pre-meeting research | M0 | Client's business, market, competitors researched before first session |
| Trigger, why-now, business fit | M1.1-1.2 | Trigger + the product's job in their business captured |
| Benefit, success, alignment | M1.3 | Client KPIs named + client-vs-user benefit alignment checked |
| Budget + decision process | M1.4-1.5 | Budget signal + approval chain + late-veto risks known |
| Constraints sweep | M1.6 | Integrations, data, content, brand, IT, operations, migration all swept |
| References | M1.7 | Every "like company XY" decompressed + classified directive/hypothesis |
| Client claims about users | M1.8-1.9 | Claims captured `[CLIENT-ASSERTED]` + client maturity known |
| Real users - three populations | M2 | Customers AND staff/operators AND client's own view discovered |
| Process walkthroughs | M2b | Each core process walked + Exception sweep run |
| Scope shaping | M3 | Must/nice/non-goals/acceptance captured (only after M1-M2b) |

---

## Step 0: Coverage check (current state)

Read, in this order (deep source ingestion - full files, not skims):

1. `meetings/` - all prior `client-discovery` notes (and `customer-discovery` if users were interviewed)
2. `meetings/prep/` - prior agendas (what was planned but maybe not covered)
3. `artifacts/phase-2-discovery/` - Track artifacts + `discovery-report.md` if present
4. `state.json` / assessment - project context

Build the coverage map: per area above, mark ✅ covered / ⚠️ thin / ❌ untouched, citing where the evidence lives. Confirm coverage: "Read [N] meeting notes + [N] artifacts."

**First session (nothing exists yet):** normal case, not a blocker. Default agenda = M0 research summary + M1.1-1.3 + M1.8 (trigger, business, success, their user claims) - relationship-building first, constraints sweep second session. Note it as such.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Session parameters

Use AskUserQuestion tool for these two questions:

Who is this session with?

  A) The commissioner - client / sponsor / exec (Recommended if Plane 1 gaps remain - their context anchors everything else)
  B) Their staff - the people who will operate the product daily
  C) Their end users / customers
  D) Mixed - commissioner plus users or staff in one room

What format and length?

  A) Video call 30-45 min - focused, 1-2 areas max
  B) Video call 60-90 min (Recommended for discovery depth - fits 2-3 areas plus close)
  C) On-site workshop half-day - process walkthroughs possible (M2b works best live)
  D) Async / written - questionnaire, use only for constraint sweeps, never for trigger/JTBD

Then ask as plain text:

Date of the session, and is there anything specific you already know you need from it? (e.g. "they keep mentioning a competitor's app", "I need budget clarity before quoting")

If the user is unsure what the session should target, recommend from the coverage map: the highest-leverage gap given where the engagement stands (early → trigger/business; before quoting → budget/constraints/scope; before spec → processes/exceptions).

After answers, confirm the session focus, then generate.

---

## Step 2: Generate the agenda

Generate in English. Select 2-3 areas maximum (per hour of session) from the coverage gaps - depth beats coverage. Pull the matching questions from the **Question bank** section below and **write them out in full** in the agenda - question text, follow-up, red-flag answer, and (where relevant) the complete technique steps, not a "see module X" pointer. Adapt every question to this client's context (their industry, their words from prior notes, their named references). Generic questions are a waste of the session - personalize every one.

**Self-containment rule:** the agenda must be usable by someone who has never seen this skill and will not have anything open during the session. If a technique applies (e.g. Reference decompression), copy its steps into the agenda block in full, condensed to what fits the moment - not a name-drop.

---

### ARTIFACT: Session Agenda

```markdown
# Discovery Session Agenda - [date] - [audience]

> **Session [N]** · **With:** [names/roles] · **Format:** [call/workshop, length]
> Self-contained - everything needed for this session is below. No other document required.

---

## Coverage status going in

| Area | Status | Source |
|---|---|---|
| [area] | ✅ / ⚠️ / ❌ | [meeting note / artifact] |

**This session targets:** [the 2-3 gap areas chosen and why they're the highest-leverage now]

---

## Opening (1 min)

[Suggested framing in one or two sentences - why we're here, what we'll walk out with. Personalized, not generic.]

## Block 1 - [Area name] ([X] min)

Goal: [what must be known by the end of this block]

- [Question 1 - adapted to this client's context]
  - follow-up: [the peel-the-onion follow-up]
  - red-flag answer: [what answer signals a problem, and what to do next]
- [Question 2...]

[If a technique applies this block, write its steps out here in full - e.g.:]
**Technique - Reference decompression** (they mentioned [XY] in session 1, likely to come up again):
1. Split the layers: "What exactly about [XY] - how it looks, how it flows, or what it lets people do?"
2. Force a scenario: "Walk me through how you'd actually use that here."
3. Find the job: "What would that solve for you that you don't have today?"
4. Check fidelity: "Have you used it yourself, or seen it somewhere?"
5. Iceberg move: "Under the hood, [XY] also does A/B/C to make that work - which of those do you need?"
6. Outcome test: "If we got you the same result a different way, would that work?"
7. Classify before moving on: **directive** or **hypothesis** - write it down on the spot.

## Block 2 - [Area name] ([X] min)

[same structure]

## Close ([~10] min)

- Recap: "Here's what I heard: ..." - confirm or correct
- Next steps: ours + THEIRS (content, access, user intros - name what they owe)
- Next session target: [what the following session should cover]

---

## Bring / prepare

- [prior notes to re-read, materials from client to review - this agenda is everything else you need]

## After the session

Run `/pm-meeting` on the notes same day (Client Discovery type) → then `/pm-discovery-report` to update the running report.
```

---

## Internal completeness checklist

<!-- Claude reference only -->

- [ ] Coverage map built from actual files, not assumed
- [ ] 2-3 areas max per hour - agenda is not a checklist dump of the whole question bank
- [ ] Every question personalized to this client (their industry, their words, their references)
- [ ] Each block has a goal, follow-ups, and at least one red-flag answer
- [ ] Techniques matched to expected session content (references expected → decompression ready)
- [ ] Close block present with recap + mutual next steps
- [ ] If mixed audience: commissioner questions and user questions separated (never probe budget in front of staff)

## Save to

```
pureinn-workspace/[project-slug]/meetings/prep/[YYYY-MM-DD]-[audience-slug]-agenda.md
```

---

## Question bank (complete - the skill's source, embedded)

Everything needed to compile an agenda or walk a session live. Two planes (the commissioner above, the real users below), three user populations (the client's customers, the client's staff, the client's own oversight). Provenance rule throughout: real user research > `[CLIENT-ASSERTED]` (client's claim about their users) > `[ASSUMED]`. Never let a client's claim silently become a validated persona.

### Module 0 - Pre-meeting research (before the first session)

- The client's company: what they sell, to whom, how they position themselves
- Their market and **their competitors** (in commissioned work, the market lens is the client's market, not yours) → `/pm-market-analysis`, `/pm-domain-analysis`
- Their current digital footprint: existing site/app/system, visible workflows, reviews of their service
- The people attending: roles, likely priorities, likely objections
- Any prior materials they sent (brief, RFP, deck) - read fully first
- **Output:** 3-5 hypotheses about their likely problems and priorities, to test in Module 1

### Module 1 - The commissioner (Plane 1)

**1.1 Trigger and why-now** → Discovery Report (context), `/pm-project-charter`
- What brought you to this? What made you take this meeting? *(the real trigger - get them talking early)*
- Why now - why not a year ago, why not next year? *(urgency, external pressure)*
- What happens if you do nothing for the next 6-12 months? *(is the problem fund-worthy; consequence framing)*
- Have you tried to solve this before? What happened? *(prior attempts, why past solutions failed)*

**1.2 Their business and the product's job in it** → Discovery Report, `/jtbd-building` (commissioner's job)
- Walk me through your business - how do you make money, who pays you? *(the business model the product serves)*
- Where does this product fit? What does it have to do **for the business**? *(job at business level: earn more / spend less / reduce risk / comply / status)*
- Which part of your operation does this touch or replace? *(integration surface → Module 2b)*

**1.3 Benefit, success, alignment check** → Discovery Report (value hypothesis), Scope Brief (acceptance)
- How will you measure whether this was worth it? What number moves? *(success in their terms)*
- What KPIs are you responsible for? *(personal stake)*
- When would you call it a failure? *(the inverse test - a criterion that cannot fail is not one)*
- **Alignment check (explicit):** compare the client's benefit with the users' benefit (Module 2). Client wants control/reporting/upsell, users want simplicity/speed → surface the tension as a finding, don't design around it silently.

**1.4 Budget and decision process** (never open with "what's your budget?") → Meeting notes, Discovery Report
- How are you determining the value of solving this? What's it costing you today? *(value-first: the number surfaces through impact)*
- Have you solved something like this before - what did that cost? *(anchors from their history)*
- When you think about solving this, is there a range in mind, or are we still shaping that? *(direct but calm; an out that still gives signal)*
- Besides cost, how will you choose between options? *(decision criteria; where you differentiate)*
- Who else needs to sign off, and what does that process look like? *(approval chain, procurement, timeline reality)*

**1.5 Stakeholders and the late-veto check** → Meeting notes; `/pm-stakeholder-map` if corporate-sized
- Who on your side works with us day to day? Who decides? *(contact vs. decision-maker - usually two people)*
- Who can block or kill this at the END, close to launch? (IT, legal, co-owner, key franchisee) *(the late vetoer - get them an early touchpoint)*
- Whose work does this change? Who might resist it? *(internal adoption risk)*

**1.6 Constraints sweep** (each one skipped is a surprise later) → Scope Brief, `/pm-tech-feasibility`, `/pm-domain-analysis`
- **Integrations:** what systems today - ERP, CRM, accounting, payments, inventory, booking? Which must connect? Who owns them?
- **Data:** what exists, where does it live, quality, migration needed, who owns it legally?
- **Content:** who supplies texts, photos, product data, translations, by when? *(the classic web-project killer - never assume they'll "just deliver content")*
- **Brand / design:** existing brand book, design system, non-negotiable visual identity?
- **IT / security:** hosting, IT policy, security review, data residency?
- **Operations after launch:** who maintains and administers this, what's their technical skill, support model?
- **Replacement / migration:** does this replace something? What happens to current data, users, SEO, integrations? Parallel run or hard switch?
- **Time / budget:** hard deadline (event, contract, season)? What flexes first - scope, time, or budget?

**1.7 References - "I want it like [company XY]"** → run Reference decompression (Techniques below); classify directive/hypothesis before moving on

**1.8 Claims about their target group** → `/pm-personas` tagged `[CLIENT-ASSERTED]`
- Who will actually use this? Describe a real, specific person. *(their model of their users)*
- How do you know? Have you talked to them about this? *(evidence vs. assumption)*
- Who is your best customer today - and your most painful one? *(segment texture)*

**1.9 Client maturity** (decides whether Plane 2 is an import or your job)
- Have you done research with your users - interviews, surveys, analytics? → yes: import (Path A of Track skills) / no: run Plane 2 yourself or proceed `[CLIENT-ASSERTED]` with eyes open
- Do you have analytics on the current solution? → yes: baseline for Scope Brief / no: note the blind spot
- Previous attempts, agencies, prototypes? → read the postmortem, cheapest lesson available

### Module 2 - The real users (Plane 2)

**2.1 Three populations - always sweep all three** (staff personas are legitimate personas → `/pm-personas`)
- a) **Customers:** who are they, what job are they hiring this for? *(nobody skips this one)*
- b) **Staff:** who operates this day to day on your side? What's their workday? *(skip it → staff can't operate the launch)*
- c) **Client's own view:** what do YOU need to see - reports, oversight, control? *(skip it → the person who paid never sees value)*

**2.2 Segments, jobs, pains** → `/pm-personas`, `/jtbd-building`, `/pm-problem-validation`
- Which type of user/customer matters most? Which hurts most today? *(segment priority by pain intensity)*
- Walk me through the last time [user] had to deal with [the problem]. *(concrete episode - Mom Test; stories over opinions)*
- How often does that happen? In what situation - where, when, under what pressure? *(job frequency and context)*
- What do they do about it today? Tools, workarounds, spreadsheets? *(the real competition)*
- What's the most frustrating part? What have they given up on? *(pain intensity, resignation)*
- What would change for them if this worked perfectly? *(expected gains, outcome language)*

**2.3 Empathy sweep (depth on a key persona)** → `/pm-personas`
Six quadrants - fill each: **think and feel** (worries, aspirations), **say and do** (public behavior, contradictions), **see** (environment, competitors' offers), **hear** (influencers, colleagues, reviews), plus **pains** and **gains**.

### Module 2b - Process walkthrough (for any "system / workflow / portal" request)

Seeds domain modeling → `/pm-process-flows`, `/pm-entity-registry`; pains → `/pm-problem-validation`. Pick one end-to-end process (an order, a booking, a claim, a publication):
1. **Walk it start to finish:** "take me through what happens from the moment X arrives until it's done." Let them narrate; don't interrupt with solutions.
2. **Capture per step:** who does it (actor), what they touch (system, paper, phone), what they hand off and to whom, how long, how often (volume).
3. **Mark the friction:** where does it break, wait, get retyped, get lost?
4. **Run the Exception sweep** (Techniques below) before leaving the process.
Repeat for each core process (usually 2-4 in a commissioned build).

### Module 3 - Solution and scope shaping (only after M1-M2b) → `/pm-scope-brief`

- Of everything we discussed - what MUST v1 do, or it's not worth launching? *(the real core, their words)*
- What would be great later but doesn't block launch? *(deferred scope - captured, not lost)*
- What should this explicitly NOT do or be? *(non-goals - cheapest scope protection)*
- If we achieved the same outcome a different way than you imagined, is that acceptable? *(outcome vs. output - design freedom or literal directive)*
- How will you evaluate that we delivered what you wanted? Who signs off? Demo cadence? *(acceptance model)*
- Re-run the **Exception sweep** against the proposed scope.

### Module 4 - Close

- "Looking at the clock, ~10 minutes left - let's align on next steps." *(interject professionally; never let it just run out)*
- Recap: "Here's what I heard: [3-5 points]. Did I get that right? What did I miss?"
- Concrete next steps: who, what, by when - including what THEY deliver (content, access, user intros).
- Same day: run `/pm-meeting` (Client Discovery type) on the notes.

### Techniques

**Reference decompression** ("like company XY") - run every time a reference appears:
1. Split the layers: "What exactly about [XY] - how it looks, how it flows, or what it lets people do?" (visual / UX / function / business model)
2. Force a scenario: "Walk me through how you'd actually use that here." (shallow references collapse)
3. Find the job: "What would that solve for you that you don't have today?"
4. Check fidelity: "Have you used it yourself, or seen it somewhere?" (used / seen / heard-of)
5. Iceberg move: "Under the hood, [XY] also runs A, B, C, D to make that work. Which of those do you actually need?" *(best scope protection + strongest credibility signal at once)*
6. Outcome test: "If we got you the same result a different way, would that work?"
7. Classify before moving on: **directive** (→ Scope Brief as a bounded requirement + explicit non-goals) or **hypothesis** (→ assumptions/`/pm-hypotheses`, never into spec as settled).

**Exception sweep** - after any process walkthrough or scope discussion. Tag product-enforced exceptions `[CANDIDATE-BR]` → `/pm-business-rules-library`:
- Failure edges: cancellation, return, refund, no-show, error?
- Role edges: special permissions? Who can override?
- Volume edges: peak season, bulk operations, everything arriving at once?
- Lifecycle edges: first user, offboarding, account/data deletion (GDPR), dormant accounts?
- Migration edges: existing customers/data/contracts on day one?

**Conversation craft:**
- Open-ended, then silent. Ask, then shut up - most people break 5 seconds of silence with the detail they withheld.
- Peel the onion: "You mentioned [X] - tell me more." The first telling is incomplete nine times in ten.
- Consequence chain: "What happens then? Who else does it impact? What does it cost the business?" - impact turns a complaint into a case.
- Say it with questions: not "that will fail because ABC" but "a client of ours hit ABC - how does your plan handle that?"
- No feature tours: later, show ONLY what maps to challenges they named.
- Disqualify honestly: if the problem is too small, the budget unreal, or value below cost - say so and stop. Ending an engagement early is a successful discovery.

---

## Handoff

**Čo si teraz má:** Cielenú agendu na najbližšie discovery sedenie - mierenú na najväčšie medzery, s otázkami prispôsobenými tomuto klientovi, nie generický dotazník.

**Ďalší krok:** Vytlač alebo otvor agendu a odveď sedenie priamo podľa nej - je samostatná, nepotrebuješ pri nej žiadny ďalší dokument ani Claude. V ten istý deň `/pm-meeting` (Client Discovery typ) na spracovanie poznámok → `/pm-discovery-report` na update priebežného reportu.

**Môžeš preskočiť ak:** Discovery už konvergovalo (coverage mapa je zelená) - choď na `/pm-scope-brief` namiesto ďalšieho sedenia.
