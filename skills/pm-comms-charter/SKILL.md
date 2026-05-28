---
name: pm-comms-charter
description: Generate a Communication Charter and Meeting Rhythm for a product team. Use in Phase 1 to establish collaboration rules.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: communication charter, meeting rhythm, team communication, collaboration protocols, Phase 1
  role: specialist
  scope: planning
  output-format: document
  related-skills: pm-project-charter, pm-team-roster, pm-stakeholder-map
---

# PM - Communication Charter

## What this skill does

Generates two artifacts:
1. **Communication Charter** - Channels, rules, async principles
2. **Meeting Rhythm** - Meeting cadence with clear purpose and outputs

---

## Dependencies

**Recommended before running:**
- `pm-team-roster` - team size, timezones, and tools directly shape communication setup

**Produces artifacts used by:**
- All subsequent phases - communication charter is the operational backbone of the project

---

## Step 0: Current state check

Check for existing artifacts:
- Communication Charter
- Meeting Rhythm

Also check: does a Team Roster exist? Cross-reference team size and timezones vs. proposed meeting cadence.

Look for: tools no longer in use, meeting cadence that doesn't match current project phase, missing async alternatives, escalation path not defined.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Ask the user all questions at once:

```
I need team context for the Communication Charter.

1. TEAM
   Team size: how many people?
   Timezones: is everyone in the same timezone, or distributed?
   Fully remote / hybrid / office?

2. AVAILABLE TOOLS
   Async: Slack / Teams / Email / Notion / other
   Documentation: Notion / Confluence / Google Drive / other
   Project management: Linear / Jira / Asana / other
   Video calls: Zoom / Meet / other

3. WORKING PREFERENCES
   What is the team style - prefers async or meetings?
   Are there any past problems you want to avoid repeating?

4. KEY COMMUNICATION MOMENTS
   What are the critical communication moments in this project?
```

---

## Step 2: Generate artifacts

Generate all documents in English.

---

### ARTIFACT 1: Communication Charter

```markdown
# Communication Charter - [Product Name]

> **Version:** 1.0 · **Date:** [date]
> The team commits to following these rules. Update at retrospective if something is not working.

---

## Async by default

**Rule #1:** Sync meeting = last resort, not first instinct.
Every sync meeting must justify why it could not be resolved async.

**Async alternatives:**
| Instead of | Do this |
|---|---|
| Daily standup meeting | Slack thread - daily async update (5 min to write, read anytime) |
| Weekly review meeting | Written memo (PM writes, team comments async, sync only for decisions) |
| Design review meeting | Loom video walkthrough + async comments in Figma |
| "Quick question" call | Slack message + 4h response window |

---

## Communication channels

| Channel | Tool | Purpose | Response SLA |
|---|---|---|---|
| Team communication | [Slack/Teams] | Daily questions, updates, sharing | 4 hours (business hours) |
| Documentation | [Notion/Confluence] | All decisions, artifacts, SSoT | N/A - source of truth |
| Project tracking | [Linear/Jira] | Tasks, bugs, feature requests | Same day when assigned |
| Urgent | [Phone/Slack DM] | Production incident, critical blocker | 30 minutes |
| Email | Email | External communication (investors, partners) | 24 hours |

---

## Communication rules

**Response time:**
- Slack: within 4 hours during business hours
- Urgent (@here / @channel): within 30 minutes
- Email: within 24 hours
- Outside business hours: next business day (unless marked urgent)

**Decision documentation:**
- Every significant decision = written in [Notion/Confluence]
- Format: What was decided + Why + Who decided + Date
- "If it's not written down, it didn't happen"

**Stakeholder communication:**
- Internal stakeholders: weekly written memo (PM owns)
- Investors / External: [frequency] update (PM owns)

---

## What we reserve for sync

These communication types require a real-time call:
- Go/No-Go decisions (phase gates)
- Retrospectives (team dynamics, psychological safety)
- Complex design discussions (real-time whiteboarding)
- Conflict resolution (nuance hard to capture in text)
- New team member onboarding
```

---

### ARTIFACT 2: Meeting Rhythm

```markdown
# Meeting Rhythm - [Product Name]

> Only meetings with a clear purpose and output. If a meeting has no output, cancel it.

---

## Regular meetings

| Meeting | Frequency | Duration | Participants | Purpose | Output |
|---|---|---|---|---|---|
| Daily Standup | Daily async (Slack) | 5 min to write | Core team | Blockers, progress, today's plan | Slack thread |
| Weekly Review | Weekly async | PM writes 30 min | Core team + key stakeholders | Progress vs OKRs, decisions, risks | Written memo in Notion |
| Sprint / Stripe Planning | Every 2 weeks | 60 min sync | PM + Tech Lead + UX | What we build in the next stripe | Feature Cards assigned, sprint goal clear |
| Design Review | Per Feature Set | 45 min sync | PM + Tech Lead + Architect + UX | Catch problems before build | Design Review Summary |
| Phase Gate | Per phase | 60 min sync | Core team + Accountable stakeholders | Go/No-Go decision | Go/No-Go recorded + rationale |
| Retrospective | Every stripe (2 weeks) | 60 min sync | Core team | What worked, what didn't, action items | Retro summary + action items |
| Steering Committee | Monthly | 60 min sync | PM + Leadership + Investors (if relevant) | Strategic decisions, pivots | Meeting notes |

---

## Meeting format requirements

**Required for every sync:**
1. Agenda shared in advance (at least 2 hours before)
2. Pre-read materials available (if relevant)
3. One facilitator (owns time and outputs)
4. Notes / output written to [Notion] within 1 hour after the meeting

**Anti-pattern:** Meeting without an agenda = cancel or postpone.

---

## Async Daily Standup - Format

```
📅 [Date]

✅ Yesterday:
- [What I completed]

🔜 Today:
- [What I'm working on]

🚧 Blockers:
- [What is blocking me - if nothing, write "none"]
```

Channel: [#standup in Slack]
Time: by [9:00] every business day
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Communication Charter must cover:**
- [ ] Async-first principle stated explicitly with rationale
- [ ] Async alternatives defined for each common sync meeting type
- [ ] All communication channels listed with purpose and response SLA
- [ ] Document storage location defined - single source of truth
- [ ] Document access rights defined (who can read/write/approve)
- [ ] Decision documentation protocol ("if it's not written, it didn't happen")
- [ ] Conflict resolution process defined (async first, then sync, then escalate)
- [ ] Escalation path for blockers defined (to whom, in what timeframe)
- [ ] For SaaS products with uptime SLA: production incident communication protocol defined (on-call, war room, status page)

**Meeting Rhythm must cover:**
- [ ] Daily standup format defined (async preferred)
- [ ] Weekly review format defined (written memo preferred)
- [ ] Sprint / Stripe planning cadence defined (2-week recommended)
- [ ] Design Review cadence defined (per stripe)
- [ ] Retrospective cadence defined (per stripe)
- [ ] Phase gate meeting defined (Go/No-Go, per phase)
- [ ] Steering committee defined (monthly, strategic decisions)
- [ ] Each meeting has: owner, output, what happens if output is missing

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-1/communication-charter.md
pureinn-workspace/[project-slug]/artifacts/phase-1/meeting-rhythm.md
```
