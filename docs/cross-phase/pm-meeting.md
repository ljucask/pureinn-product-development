# pm-meeting

> Structured meeting notes, decisions log, and action items from raw notes or a transcript

**Phase:** Cross-phase  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.1.0  
**Triggers:** meeting, notes, transcript, summary, action items, action points, standup, retro, retrospective, planning, grooming, customer interview, discovery call, strategic review

---

## When to use

After any meeting where notes or a transcript exist. Detects meeting type from content and applies the correct summary template automatically.

---

## What it produces

1. **Structured meeting summary** - template varies by meeting type
2. **Decisions log** - what was settled in this session (should not be re-opened without new evidence)
3. **Action items** - each tagged with destination and owner
4. **Notion push** - new record in Meetings DB + linked tasks (if Notion URL configured in `pureinn-variables.md`)

---

## How to invoke

```bash
/pm-meeting           # interactive - paste notes/transcript or reference a file
/pm-meeting --agent   # autonomous synthesis from notes file
```

Input can be:
- **Pasted notes or transcript** - used directly
- **File or folder reference** - read in full (deep ingestion, all files recursively)
- **No notes** - guided recall: 3-4 targeted questions (what was the meeting about, who attended, what was decided, what needs to happen next); output marked as reconstructed from recall

---

## Six meeting types

The skill detects type from the content. Each type has its own summary template and routing:

| Type | Detection keywords | Primary routing |
|---|---|---|
| **Customer Discovery** | customer, user, prospect, "they said", pain, interview | Insights → personas / jtbd / pm-problem-validation |
| **Product Review** | FEAT-, AC-, spec, design review, Section, Figma | Feature Card update / pm-feature-design re-run |
| **Planning / Grooming** | sprint, stripe, priority, backlog, phase, who takes what | feature_list update / pm-stripe / pm-mvp-scope |
| **Strategic Review** | roadmap, investor, revenue, phase gate, business model, PRD | pm-prd / pm-product-roadmap delta |
| **Standup / Retro** | yesterday, today, blocker, retrospective, what went well | pm-stripe (blockers) / Notion tasks (retro actions) |
| **Partner / Vendor** | partner, vendor, contract, integration, API, SLA | Notion tasks + follow-up calendar |

---

## Action item tags

Every action item gets a destination tag regardless of meeting type:

| Tag | Meaning |
|---|---|
| `[Notion Task]` | Standalone task in Notion, assigned with deadline |
| `[Feature Card: FEAT-ID]` | Update or create a Feature Card |
| `[Meeting: person, topic, by when]` | Schedule a follow-up meeting |
| `[Skill: /pm-xxx]` | Run a framework skill to process this item |

---

## Dependencies

**Recommended:**
- `pm-team-roster` - to resolve names to real team members when assigning action items
- `pm-comms-charter` - defines the meeting rhythm; `pm-meeting` captures each individual instance
- `pureinn-variables.md` - `Meetings` key must contain the Notion DB URL for push

**Produces for:**
- Notion Meetings DB (if configured)
- Feature Cards (for Product Review and Planning types)
- Downstream skills depending on meeting type (see routing table above)

**Related skills:** `pm-personas`, `jtbd-building`, `pm-problem-validation`, `pm-stripe`, `pm-feature-card`, `pm-product-roadmap`, `pm-team-roster`
