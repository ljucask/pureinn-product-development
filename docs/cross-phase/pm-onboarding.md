# pm-onboarding

> Role-specific Onboarding Brief for a new team member - right context, no noise

**Phase:** Cross-phase  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 1.0.0  
**Triggers:** onboarding, new team member, new developer, new designer, new pm, role brief, team brief, joining

---

## When to use

When a new person joins the team mid-project. Reads the existing workspace and distills the right subset of artifacts for the role. Skip if solo builder with no team to onboard.

---

## What it produces

**Onboarding Brief** (`onboarding/[name]-[role]-brief.md`):

- Product context for the role (filtered to what they need)
- **Settled decisions** - what has been decided and should not be re-opened without new evidence (mandatory section for every role)
- Where things live (workspace artifact map)
- Current delivery state (active stripes, Feature Cards in queue)
- Who to talk to about what

---

## How to invoke

```bash
/pm-onboarding           # interactive - asks role and name
/pm-onboarding --agent   # autonomous synthesis from workspace artifacts
```

---

## Four role tracks

| Role | Gets |
|---|---|
| **Developer** | Domain model, entities + state transitions, business rules, current stripe/Feature Cards in queue, coding conventions, who to ask about what |
| **PM** | Product vision, PRD (problem + value prop + target customer), roadmap + phases, feature_list (KANO/V×C/phase), personas, open hypotheses, settled decisions |
| **Designer** | Personas, user flows, features currently in `2b_In_Design`, Figma links, design system reference, early adopter profile |
| **Stakeholder / Investor** | Executive brief: problem + market, value prop, MVP scope, traction/metrics, team, next milestone |

The skill adapts to what actually exists in the workspace - missing artifacts are reported as gaps, not invented.

---

## Dependencies

**Recommended:**
- `pm-team-roster` - to know the team structure and who owns what
- A workspace with at least some artifacts (`state.json`, PRD, features)

If artifacts are missing, the skill reports what is absent rather than blocking. A brief built on partial artifacts is better than no brief.

**Produces for:**
- The new team member (primary consumer)
- Notion (if workspace Notion integration is configured - brief linked to the team member record)

**Related skills:** `pm-team-roster`, `pm-stakeholder-map`, `pm-comms-charter`, `pm-stripe`
