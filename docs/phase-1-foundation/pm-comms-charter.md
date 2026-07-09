# pm-comms-charter

> Communication Charter and Meeting Rhythm for a product team

**Phase:** 1 - Foundation  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** communication charter, meeting rhythm, team communication, collaboration protocols, Phase 1

---

## When to use

After `pm-team-roster`. Establishes how the team communicates, which channels carry which types of information, and what the recurring meeting structure looks like.

**Skip if:** solo builder with no team to communicate with.

---

## What it produces

Two artifacts (`artifacts/phase-1-foundation/comms-charter.md`):

1. **Communication Charter** - Channels (Slack/email/docs), async principles, response time expectations, escalation paths, what goes where
2. **Meeting Rhythm** - Recurring meetings with defined purpose, cadence, required attendees, and expected output (e.g. weekly product review, biweekly stakeholder update, daily standup if relevant)

---

## How to invoke

```bash
/pm-comms-charter           # standard interactive run
/pm-comms-charter --agent   # autonomous draft from available context
```

---

## Dependencies

**Recommended before running:**
- `pm-team-roster` - team size, timezones, and tools directly shape the communication setup

**Related skills:** `pm-project-charter`, `pm-team-roster`, `pm-stakeholder-map`
