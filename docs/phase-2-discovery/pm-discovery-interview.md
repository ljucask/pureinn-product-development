# pm-discovery-interview

> Session agenda for a live discovery session - targets the biggest remaining gaps, questions personalized to this client

**Phase:** 2 - Discovery (client discovery layer)  
**Agent mode:** `synthesis` - runs fully, review the agenda after  
**Version:** 1.0.0  
**Triggers:** discovery interview, client session, interview prep, discovery call, session agenda, client meeting prep, requirements session

---

## When to use

Before every live discovery session with a client, sponsor, their staff, or their users. The skill does NOT run the interview - it prepares you for it: reads what discovery has already covered, finds the gaps, and compiles a targeted agenda from its built-in discovery question bank (embedded in the skill - two planes, three user populations, full technique library). After the session, process the notes with `/pm-meeting` (Client Discovery type).

---

## What it produces

One artifact (`meetings/prep/[YYYY-MM-DD]-[audience]-agenda.md`):

- **Coverage map** - which discovery areas are done, thin, untouched (from prior meeting notes + Track artifacts)
- **Session agenda** - 2-3 gap areas per hour, each block with a goal, personalized questions, follow-ups, and red-flag answers
- **Techniques to have ready** - e.g. reference decompression when the client keeps mentioning a competitor product
- **Close block** - recap, mutual next steps (including what the client owes)

---

## How to invoke

```bash
/pm-discovery-interview           # interactive - asks audience, format, session goal
/pm-discovery-interview --agent   # autonomous draft from workspace state
```

**First session (nothing exists yet):** normal case - defaults to trigger/business/success + the client's claims about their users; constraints sweep comes second session.

---

## Dependencies

**Reads (whatever exists):**
- `meetings/` - prior client-discovery and customer-discovery notes
- `artifacts/phase-2-discovery/` - Track artifacts + Discovery Report

**Produces for:**
- the live session itself (field agenda)
- `pm-meeting` - the agenda pairs with the meeting note produced afterward

**Related skills:** `pm-meeting`, `pm-discovery-report`, `pm-scope-brief`, `pm-personas`, `jtbd-building`
