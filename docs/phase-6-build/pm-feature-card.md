# pm-feature-card

> Create and manage Feature Cards - the atomic delivery unit in the FDD+SDD framework

**Phase:** 6 - JIT Delivery (and Phase 5 stub creation)  
**Agent mode:** `synthesis` - runs fully autonomously  
**Version:** 2.1.0  
**Triggers:** feature card, FEAT-ID, feature spec, feature lifecycle, cards

---

## When to use

- Creating a Feature Card stub manually (when not auto-created by `pm-features-list`)
- Reviewing a Feature Card's completeness at any status
- Advancing card status after human confirmation
- Getting the canonical card template

Normal flow: cards are created automatically by `pm-features-list` (status: `1_Backlog`) and populated by `pm-feature-design` (Sections 1-3). Use this skill when you need to create or inspect a card outside that flow.

---

## What it produces

Feature Card at `features/cards/[FEAT-ID].md`

A Feature Card has four sections with defined ownership:

| Section | Content | Written by | When |
|---|---|---|---|
| Frontmatter | ID, title, status, stripe, KANO, V×C, feature flag, PRD ref | `pm-features-list` + `pm-mvp-scope` | Phase 5 |
| Section 1 - Business Constraints | Entity IDs, BR-IDs, TBL-IDs, scope exclusions | `pm-feature-design` | JIT before build |
| Section 2 - Acceptance Criteria | Given/When/Then ACs (happy path, guard failures, flag OFF) | `pm-feature-design` | JIT before build |
| Section 3 - JIT Technical Design | Sequence diagram + files to modify | `pm-feature-design` | JIT before build |
| Section 4 - Build Record | Commits, test files, flag verification, code inspection result | Build team + `pm-stripe` | After build |

**Section 4 and `6_Shipped` status make the card immutable.**

---

## How to invoke

```bash
/pm-feature-card FEAT-ORD-012        # review or create card for a specific feature
/pm-feature-card --template          # show the canonical card template
```

---

## Feature Card lifecycle

```
1_Backlog → 2_Spec_Done → [2b_In_Design] → 3_Ready_to_Build → 4_In_Build → 5_In_Review → 6_Shipped
```

| Status | Meaning | Who sets it |
|---|---|---|
| `1_Backlog` | Stub created, feature defined | `pm-features-list` (auto) |
| `2_Spec_Done` | JIT spec complete (Sections 1-3 populated) | `pm-feature-design` |
| `2b_In_Design` | **(frontend only)** Figma/UI design being produced | `pm-feature-design` / designer |
| `3_Ready_to_Build` | Design inspection approved | Human / `pm-stripe` |
| `4_In_Build` | Build in progress | `pm-stripe` |
| `5_In_Review` | Code review in progress | Human / AI guardrail |
| `6_Shipped` | Complete - immutable | `pm-stripe` after CI pass |

`2b_In_Design` is layer-gated: only features whose `layer` includes `frontend` pass through it. Backend/system features go straight `2_Spec_Done → 3_Ready_to_Build`.

---

## Stub completeness requirements

**Stub (`1_Backlog`) must have:**
- All frontmatter fields: `id`, `title`, `status`, `stripe`, `layer`, `phase`, `actor`, `priority`, `kano`, `vxc`, `feature_flag`, `flag_default`, `prd_ref`
- Sections 1-4 present as stubs (placeholder text, not filled)
- Description block (2-3 sentences: what the feature does, who uses it, value delivered)

**After `pm-feature-design` (`2_Spec_Done`) must have:**
- Section 1: entity state transitions + BR-IDs linked
- Section 2: at minimum AC-01 (happy path), AC-02 (one guard failure), AC-03 (flag OFF)
- Section 3: Mermaid sequence diagram (not empty) + files to modify listed

**After build (`6_Shipped`) must have:**
- Section 4: at least one commit link, at least one test file path
- Section 4: feature flag OFF verification
- Section 4: Code Inspection result with date

---

## Dependencies

**Required before creating a stub:**
- Feature must exist in `features/feature_list.md`

**Related skills:** `pm-feature-design`, `pm-features-list`, `pm-stripe`, `pm-entity-registry`
