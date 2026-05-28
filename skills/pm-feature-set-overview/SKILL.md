---
name: pm-feature-set-overview
description: Generate a Feature Set Overview - a compact orientation document for the delivery team. Covers purpose, business role, responsibilities, boundaries, and risk. Not a requirements doc - the document someone reads before reading the FSD to understand context and scope. Phase 6 skill.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: feature set overview, FS scope, feature set definition, Phase 6
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-brd, pm-fsd, pm-mvp-scope, pm-stripe
---

# PM - Feature Set Overview

## What this skill does

Produces a compact, team-facing orientation document for a single Feature Set. It answers in plain language:
- What is this Feature Set and why does it exist?
- What does it own and what does it explicitly not own?
- What breaks in the platform if this Feature Set fails?
- Where does it sit in the system?

This is the document someone reads *before* the FSD. It is not a requirements document and does not replace the FSD. It is the team briefing - product, design, engineering, and QA all need a shared mental model of what the Feature Set is before they start detailed spec work.

If an FSD exists, the overview is extracted from it. If not, it is generated from available inputs.

---

## Dependencies

**Recommended before running:**
- `pm-fsd` - if FSD exists, the overview is derived from it (preferred)
- `pm-mvp-scope` - Feature Set definition and delivery stripe context
- `pm-domain-model` - entity context for the business role section

**Produces artifacts used by:**
- `pm-brd` (Phase 6 detail) - team uses overview to understand scope before writing rules
- `pm-fsd` - team uses overview as orientation before reading the full spec
- `feature-forge` - Feature Cards reference the Feature Set context
- Phase 7 build team - developers use overview to understand what they're building

---

## Step 0: Current state check

Check for existing artifacts:
- Feature Set Overview for this Feature Set

Also check: does an FSD exist for this Feature Set? If yes, extract the overview from it rather than generating from scratch.

Look for: overview that is too long (it should be compact, not a mini-FSD), purpose section that describes technical implementation rather than business value, missing "what this FS does NOT do" section, no risk/impact assessment.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

```
I need inputs for the Feature Set Overview - Feature Set: [FS-ID: Name]

1. FSD REFERENCE
   Does an FSD exist for this Feature Set?
   If yes: paste it or confirm it's in context - I'll extract the overview from it.
   If no: answer the questions below.
   [paste FSD or "in context" / "no FSD yet"]

2. (If no FSD) FEATURE SET DESCRIPTION
   What does this Feature Set do - what is its core responsibility?
   What user or business problem does it solve?

3. (If no FSD) SCOPE AND BOUNDARIES
   What does this Feature Set own? (what entities, processes, states)
   What does it explicitly NOT own? (what is handled by another FS)
   What triggers it upstream? What does it trigger downstream?

4. (If no FSD) RISK ASSESSMENT
   What happens in the platform if this Feature Set fails or has a bug?
   Which other Feature Sets depend on it?
   What would a user experience if it broke?

5. DESIGN STATUS
   Is there a Figma/design file for this Feature Set?
   [link or "not yet"]
```

---

## Step 2: Generate artifact

Generate in English.

---

### ARTIFACT: Feature Set Overview

```markdown
# Feature Set Overview - [FS-ID]: [Feature Set Name]

**Product:** [Product Name]
**FS ID:** [FS-ID]
**Phase:** [MVP / Post-MVP Phase X]
**Priority:** [P1 Critical / P2 High / P3 Medium]
**Delivery:** [Stripe X - Week Y-Z]
**Status:** [Backlog / In Design / In Spec / In Dev / Done]
**FSD:** [Link or version reference / Not yet written]

---

## Design Reference

**Figma / Design:** [Link to design file or "TBD - Design pending"]

[If design exists, include a brief description of the main screens/flows or embed a key screenshot reference]

---

## 1. Purpose

[2-3 sentences: what business problem this Feature Set solves, why it exists, what would happen without it. Written for someone who doesn't know the system - specific about business value, not technical implementation.]

---

## 2. Business Role in the Platform

**Core process:** [Which business process this FS belongs to - e.g., "Booking Orchestration"]

**In the lifecycle of:** [Which entity lifecycles this FS initializes, advances, or terminates]

**Business capability delivered:** [What the user or business can do because of this FS]

---

## 3. What This Feature Set Owns

This Feature Set is responsible for:
- [Responsibility 1: e.g., "Creating and managing BookingRequests"]
- [Responsibility 2: e.g., "Transitioning Bookings from Requested to Confirmed or Declined"]
- [Responsibility 3: e.g., "Emitting booking.confirmed event consumed by Payment FS"]

**Entities owned:** [ENT-003 Booking, ENT-007 BookingRequest]

**States managed:** [Booking: Requested → Confirmed / Declined / Cancelled]

---

## 4. What This Feature Set Does NOT Own

Explicitly out of scope:
- [e.g., "Payment processing - that is FS-03's responsibility"]
- [e.g., "Guest-host messaging - that is FS-04's responsibility"]
- [e.g., "Listing availability validation - triggered here but owned by FS-01"]

This boundary is important. If a developer or designer is unsure where something belongs, the answer is NOT here if it's listed above.

---

## 5. System Position

**Upstream (what triggers this FS):**
- [e.g., "Guest submits booking request via the Search & Discovery flow (FS-02)"]
- [e.g., "Booking.requested event received from FS-01"]

**Downstream (what this FS enables):**
- [e.g., "Payment FS (FS-03) - triggered by booking.confirmed event"]
- [e.g., "Notification FS (FS-05) - triggered by state transitions here"]

**Dependencies:**
- Requires: [FS-01 Property Management - listing must exist and be Active]
- Blocks: [FS-03 Payment - cannot process payment without confirmed booking]

---

## 6. Risk and Impact

**If this Feature Set fails:**
[1-2 sentences: what breaks from the user's perspective and what the business impact is]

**Severity:** [Critical / High / Medium] - [brief reason]

**Failure modes to guard against:**
- [e.g., Double booking - concurrent requests on same listing]
- [e.g., Booking confirmed but payment not initiated]
- [e.g., Host approval timeout not handled]

**Key metric:** [The one number that tells you if this FS is healthy - e.g., "Booking approval rate > 70%"]

---

## 7. Features in This Set

| ID | Feature | Delivery stripe | Notes |
|---|---|---|---|
| F-[ID] | [Feature name] | Stripe [X] | |
| F-[ID] | [Feature name] | Stripe [X] | |

---

## 8. Key Business Rules (summary)

Full rules defined in BRD. Summary for team orientation:

| Rule ID | Summary |
|---|---|
| RULE-A-[ID] | [One-line summary: "Payment must never release without booking.completed event"] |
| RULE-B-[ID] | [One-line summary: "Host has 48h to approve or booking auto-expires"] |

---

## 9. Open Questions

| Question | For whom | Priority |
|---|---|---|
| [Design decision not yet made] | [Design / PM] | High |
| [Business rule to confirm] | [PM / Legal] | Med |
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps in existing artifacts.
     Use in Step 2 to verify full coverage before finalizing output. -->

**Overview must cover:**
- [ ] Purpose: business value, not technical description
- [ ] Business role: which process and entity lifecycle
- [ ] What it owns: specific responsibilities and entities
- [ ] What it does NOT own: explicit boundary
- [ ] System position: upstream triggers and downstream consumers
- [ ] Risk and impact: failure consequence and severity

**Length and quality:**
- [ ] Overview is compact - max 1-2 pages. If longer, it's becoming an FSD
- [ ] Purpose section does not describe technical implementation
- [ ] "Does NOT own" section is specific (not vague "other things")
- [ ] Risk section names actual failure scenarios

## Save to

```
pureinn-workspace/[project-slug]/artifacts/phase-6/[fs-id]-overview.md
```
