# Communication Charter - PureHunger

> **Version:** 1.0 · **Date:** 2025-10-14
> The team commits to following these rules. Update at retrospective if something is not working.

---

## Async by default

**Rule #1:** Sync meeting = last resort, not first instinct.
Every sync meeting must justify why it could not be resolved async.

**Async alternatives:**
| Instead of | Do this |
|---|---|
| Daily standup meeting | Slack thread - daily async update (5 min to write, read anytime) |
| Weekly review meeting | Written memo in Notion (Sam writes, Lena/Marcus comment async, sync only for decisions) |
| Design review meeting | Loom video walkthrough + async comments in Figma once a contract designer is engaged |
| "Quick question" call | Slack message + 4h response window |

---

## Communication channels

| Channel | Tool | Purpose | Response SLA |
|---|---|---|---|
| Team communication | Slack | Daily questions, restaurant/courier issue escalation, updates | 4 hours (business hours) |
| Documentation | Notion | All decisions, artifacts, single source of truth | N/A - source of truth |
| Project tracking | Notion (Feature Backlog + Meetings DB) | Tasks, features, meeting records | Same day when assigned |
| Urgent | Phone / Slack DM | Production incident, payment/payout failure, critical restaurant or courier blocker | 30 minutes |
| Email | Email | External communication - Grace Lindqvist (investor), legal counsel, payment processor | 24 hours |

---

## Communication rules

**Response time:**
- Slack: within 4 hours during business hours
- Urgent (@here / @channel): within 30 minutes
- Email: within 24 hours
- Outside business hours: next business day (unless marked urgent - e.g. a live payout failure)

**Decision documentation:**
- Every significant decision is written in Notion
- Format: What was decided + Why + Who decided + Date
- "If it's not written down, it didn't happen" - this exists specifically because Sam and Marcus are frequently out meeting restaurants together and have a habit of deciding things in the field; those decisions are worthless to Lena until they're written down

**Stakeholder communication:**
- Internal (the 3 founders): weekly written memo (Sam owns) plus the founder sync
- Grace Lindqvist (investor): monthly written update (Sam owns) - problem, progress vs. the 6/12-month targets in the Project Charter, runway, asks
- Restaurant and courier partners: Marcus owns all direct communication; anything that changes commission, payout structure, or the Partner Agreement is written and confirmed, never verbal-only

---

## What we reserve for sync

These communication types require a real-time call:
- Go/No-Go decisions (phase gates)
- Retrospectives (team dynamics, psychological safety)
- Complex design or dispatch-logic discussions (real-time whiteboarding)
- Conflict resolution (nuance hard to capture in text) - e.g. Marcus wanting to discount commission for a restaurant vs. Sam protecting the 12% differentiator
- New team member onboarding (starting with the backend engineer hire)

---

# Meeting Rhythm - PureHunger

> Only meetings with a clear purpose and output. If a meeting has no output, cancel it.
> **Right-sized for a 2-3 person founder team:** Steering Committee and Weekly Review are merged into one weekly founder sync - a 3-person team with 5 recurring meetings is an anti-pattern.

---

## Regular meetings

| Meeting | Frequency | Duration | Participants | Purpose | Output |
|---|---|---|---|---|---|
| Daily Standup | Daily async (Slack #standup) | 5 min to write | Sam, Lena, Marcus | Blockers, progress, today's plan - restaurant/courier field updates from Marcus, engineering progress from Lena | Slack thread |
| Founder Weekly Sync (merged Review + Steering) | Weekly | 45 min sync | Sam, Lena, Marcus | Progress vs. Project Charter metrics, decisions needing real-time discussion, risk register review | Written memo in Notion within 1 hour |
| Stripe Planning | Every 2 weeks (Phase 6+) | 45 min sync | Sam, Lena | What ships in the next Delivery Stripe | Feature Cards assigned, stripe queue set |
| Design Review | Per Feature Set (ad hoc, once contract designer engaged) | 30 min sync | Sam, Lena, contract UX designer | Catch problems before build | Design Review Summary |
| Phase Gate | Per phase | 45 min sync | Sam, Lena, Marcus | Go/No-Go decision | Go/No-Go recorded + rationale in Notion |
| Retrospective | Every 2 weeks (Phase 6+, aligned to stripe cadence) | 30 min sync | Sam, Lena, Marcus | What worked, what didn't, action items | Retro summary + action items |
| Investor Update | Monthly, async | N/A (written memo) | Sam → Grace Lindqvist | Keep the angel investor satisfied without a standing meeting slot | Written memo via email |

---

## Meeting format requirements

**Required for every sync:**
1. Agenda shared in advance (at least 2 hours before)
2. Pre-read materials available (if relevant - e.g. the current risk register before Phase Gate)
3. One facilitator (owns time and outputs) - Sam by default, Lena for Design Review and Stripe Planning
4. Notes / output written to Notion within 1 hour after the meeting

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

Channel: `#standup` in Slack
Time: by 9:00 every business day

---

## Handoff

**Čo si teraz má:** Dohodnutú komunikačnú kadenciu a meeting rhythm - Phase 1 Foundation je kompletná.

**Ďalší krok:** `/pureinn` pre Phase 1 gate check, potom Phase 2 Discovery - štyri tracky paralelne (`/pm-tech-feasibility`, `/pm-domain-analysis`, `/pm-market-analysis`, `/pm-personas`).

