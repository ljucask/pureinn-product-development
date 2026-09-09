# Pureinn - Intake reference

> Reference for `commands/pureinn/COMMAND.md`. Document scan and the 3-round intake.

## STEP 2 - Document Scan and Intake

First, scan the entire working directory recursively for any existing documents (.md, .txt, .pdf, .docx, .csv, notes, research files - anything that could be product or research material). Exclude code files, system files, dependency/build directories (`node_modules/`, `.git/`, `dist/`, `build/`), and this framework's own operational files (`.claude/`, `pureinn-workspace/`).

**If documents are found outside the framework:**

Read them. Then inform the user:

```
I found the following files that may be relevant:

  [list of files with paths]

I'll include these in the analysis. If you have additional documents
not yet in the directory, add them now and let me know - otherwise
we'll proceed with what's here.
```

**If no documents found:**

```
I don't see any existing documents in the directory.

If you have research notes, specs, interview transcripts, or anything
else relevant - add them anywhere in this directory and let me know.

If you're starting from scratch, say "nothing" and we'll go from there.
```

Wait for confirmation. If user adds files, read them. If "nothing", proceed to Step 3 with no documents.

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

Wait for confirmation. If corrections needed, update and re-confirm. Then proceed to Group 2.

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
