# Pureinn - Intake reference

> Reference for `commands/pureinn/COMMAND.md`. The 3-round intake. The document scan lives in `entry.md` (STEP 0a) because it runs on every path.

## STEP 2 - Documents recap

The document scan already ran in **STEP 0** (`references/entry.md` § STEP 0a) - it runs on every path, not just this one. Do **not** scan again here.

Carry its result into the intake:

- **Documents were found and read** → say in one line what they cover and what phase they map to, so the intake questions below can skip what the documents already answer. Do not re-ask what a document states plainly.
- **No documents** → continue to STEP 3 with none. This is a normal starting point, not a gap to apologize for.

If the user adds files at any point during the intake, read them and fold them in - the scan is not a one-shot gate.

---

## STEP 3 - Intake Questions

Ask these questions regardless of whether documents were found. Documents give Claude the written record; these questions capture current thinking, intent, and product shape that documents often don't contain.

Questions are grouped into 3 rounds. Each round: ask questions, then show a summary and wait for confirmation before moving to the next round.

**How to ask questions within a round:**
- Questions with predefined answer options (A/B/C/D) - ask all of them together in one interactive call
- Questions that require free-text input - ask as plain text, one at a time
- Within a single round: ask free-text questions first, then ask the option-based questions together

---

### Group 1 of 3 - What you're building

**Free text (ask first):**

What are you building? Describe it in 2-3 sentences.

Wait for the user's answer, then use the AskUserQuestion tool with both questions together:

- Question 1: "What type of product is it?"
  - A: "SaaS web application"
  - B: "Mobile application (iOS / Android / both)"
  - C: "Marketplace or platform"
  - D: "Something else (internal tool, API)"

- Question 2: "Who is it for?"
  - A: "External customers (product for sale)"
  - B: "Internal team only"
  - C: "Both"

After receiving all answers for Group 1, output a summary block:

```
Here's what I understand so far:
- [1-sentence summary of what they're building]
- Product type: [type]
- Target: [users]

Is this correct, or do you want to change anything before we continue?
```

Wait for confirmation. If corrections needed, update and re-confirm.

**Then build the workspace, before Group 2.** This is the earliest moment a
folder can be named, and it is where the tree gets created - not at STEP 6 at
the end of the run.

1. Derive `project-slug` from what they are building: lowercase, kebab-case, max 30 chars.
2. Read `references/workspace.md` and create the **full** tree for the playbook
   (default Greenfield until the playbook is chosen; STEP 6 reconciles it later
   and adds anything a different playbook needs).
3. Say one line - `Workspace: pureinn-workspace/[slug]/` - and continue to Group 2.

Do not ask permission and do not offer to skip it. An empty tree costs nothing
and is thrown away by deleting one folder; a missing tree costs the session.

`state.json`, `pureinn-variables.md` and `assessment.md` are still written at
STEP 6, once intake and assessment have produced what goes in them. The folders
exist from here on, so every step in between has somewhere to write.

**In `explore` mode this does not run** - explore writes no files at all, by
design. The workspace is created when the user picks a route out of it.

Then proceed to Group 2.

---

### Group 2 of 3 - Product shape

No free-text questions in this group. Use the AskUserQuestion tool with both questions together:

- Question 1: "What is the primary experience?"
  - A: "Mobile first" — description: "Main value delivered on mobile"
  - B: "Desktop first" — description: "Web/desktop: CRM, dashboard, admin tool"
  - C: "Both equally" — description: "Full parity across mobile and web"
  - D: "Not sure yet"

- Question 2: "Will the product be paid?"
  - A: "Yes - paid from day one" — description: "Subscription, one-time, or usage-based"
  - B: "Freemium" — description: "Free tier + paid upgrade"
  - C: "Free / internal" — description: "No revenue target"
  - D: "Not decided yet"

After receiving answers, output a summary block:

```
Adding to the picture:
- Platform: [platform]
- Business model: [model]

Does this match your intent, or anything to adjust?
```

Wait for confirmation. If corrections needed, update and re-confirm. Then proceed to Group 3.

---

### Group 3 of 3 - Context and starting point

Use the AskUserQuestion tool with both questions together first, then ask free-text questions:

- Question 1: "Where are you now?"
  - A: "Idea only" — description: "Nothing validated yet, starting from scratch"
  - B: "Have some research" — description: "Early customer insights or market knowledge"
  - C: "Validated problem" — description: "Ready to define strategy, problem is confirmed"
  - D: "Have strategy or specs" — description: "Moving to execution, know what to build"

- Question 2: "Who is building this?"
  - A: "Solo" — description: "Just me, no team"
  - B: "Small founding team" — description: "2-3 people, wearing multiple hats"
  - C: "Team with defined roles" — description: "PM, developers, designer"
  - D: "Corporate / enterprise team" — description: "Multiple stakeholders"

Wait for answers, then ask the following two free-text questions:

**Free text (ask after options):**

What matters most right now? What is the single most important thing you need to produce or figure out? (e.g., "validate whether the problem is real", "define MVP scope", "get to a spec I can build from")

Any constraints that shape how we approach this? (e.g., 3-month runway, regulated industry, must integrate with existing system, specific tech stack). Say "none" if not applicable.

After receiving all answers for Group 3, output a final summary block:

```
Complete picture:
- [1-sentence product description]
- Type: [type] | Platform: [platform] | Business model: [model]
- Target users: [users]
- Current stage: [stage]
- Priority: [what matters most]
- Team: [team type]
- Constraints: [constraints or none]

Ready to continue with this? Or anything to correct first?
```

Wait for final confirmation before proceeding to Step 3B.

---

**Why these questions matter downstream:**
- Product type and platform strategy affect tech stack recommendations, Phase 6 approach, and which skills apply
- Internal vs. external changes compliance scope, pricing model, and go-to-market
- Business model (paid/free) drives KPI selection and exit gate criteria
- Team structure determines which Phase 1 skills are relevant (see Phase 1 adaptation rules below)
- Current stage determines starting phase directly

---

### Phase 1 Adaptation by Team Structure

Phase 1 skills are not all relevant for every team type. Apply these rules:

**Solo builder:**
- Skip: `/pm-stakeholder-map` (no stakeholders), `/pm-team-roster` (no team), `/pm-comms-charter` (no team communication)
- Keep: `/pm-project-charter` - simplified: assumptions, risks, personal constraints, success definition
- Phase 1 for solo = one skill

**Small founding team (2-3 people):**
- Skip: `/pm-stakeholder-map` (unless external investors or advisors are involved)
- Simplify: `/pm-team-roster` (decision rights matter, skill gaps matter - RACI overkill)
- Keep: `/pm-project-charter`, `/pm-comms-charter` (even 2 people need alignment on how they work)
- Phase 1 for small team = 2-3 skills

**Team with defined roles:**
- Run all 4 Phase 1 skills
- Full RACI and stakeholder map are worth the time

**Corporate / enterprise team:**
- Run all 4 Phase 1 skills
- Stakeholder map and escalation tree are critical - political complexity is real

---

Then read `references/assessment.md` and run **STEP 3B (Assessment)**.
