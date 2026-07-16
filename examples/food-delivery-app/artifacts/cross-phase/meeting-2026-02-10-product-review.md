# Meeting Notes - 2026-02-10
**Type:** Product Review
**Topic:** Guest Checkout launch decision (FEAT-ORD-004)
**Date:** 2026-02-10
**Participants:** Sam Okonkwo (CEO/Product), Lena Vogt (CTO), Marcus Field (Head of Growth & Restaurant Partnerships)
**Duration:** 50 min

---

## Context

Three weeks post-Boise launch, first-order conversion data shows a meaningful drop-off at the account-creation step of checkout. This meeting reviews the FEAT-ORD-004 (Guest Checkout) spec draft to decide whether to ship guest checkout before requiring full account creation, and if so, under what fraud/no-show guardrails.

---

## Summary

- Checkout funnel data (first 3 weeks): 38% of customers who add an item to cart abandon at the "Create Account" step. Sam pulled the numbers ahead of this review.
- Lena had already sketched a guest-checkout flow behind the `ordering.guest-checkout` flag as a hypothesis before this meeting, anticipating this exact drop-off.
- Marcus flagged a downstream restaurant-partner concern: Daniel Osei asked directly whether guest orders would be harder to reach for delivery-issue follow-up (no account = no saved contact history).
- Debate centered on fraud/no-show risk of removing the account gate entirely vs. the conversion cost of keeping it.
- Agreement reached: ship guest checkout, but require phone verification (SMS OTP) before order confirmation - no full account, but not fully anonymous either.
- Lena flagged a technical dependency: guest orders still need a Customer record for the Order entity relationship (BR-ORD-001 checks don't care, but Payment and rating flows assume a customer identity) - guest checkout creates a lightweight shadow account, not a fully accountless order.

---

## Decisions

| # | Decision | Owner | Rationale |
|---|---|---|---|
| 1 | Ship Guest Checkout (FEAT-ORD-004) for the ordering flow - customers can complete an order without creating a full account | Sam Okonkwo | 38% drop-off at account creation is large enough to act on now, not wait for a bigger sample |
| 2 | Guest checkout requires SMS OTP phone verification before the order is confirmed and sent to the restaurant | Sam Okonkwo + Lena Vogt | Balances conversion (no account form) against fraud/no-show risk (a verified phone number still exists to hold someone accountable) - an unverified guest order was rejected as too risky given restaurants are already taking on payment-timing risk under BR-PAY-001 |
| 3 | Guest checkout creates a lightweight shadow Customer record behind the scenes (not visible to the guest as an "account") | Lena Vogt | Payment (BR-PAY-001/BR-PAY-002) and post-delivery rating both need a Customer entity to attach to - this is an implementation necessity, not a UX change |
| 4 | Guest orders get a post-delivery prompt to convert to a full account via a magic link (no forced signup mid-flow) | Sam Okonkwo | Keeps the conversion win intact while still building the account base over time |

**Reversal check:** No prior onboarding brief or meeting note in `/meetings/` addresses guest checkout - this is a new decision, not a reversal.

---

## Action Items

| # | Action | Owner | Deadline | Destination |
|---|---|---|---|---|
| 1 | Finalize FEAT-ORD-004 Feature Card Sections 1-3 (guard conditions for shadow-Customer creation, SMS OTP acceptance criteria) | Lena Vogt | 2026-02-14 | `[Feature Card: FEAT-ORD-004]` |
| 2 | Re-run `/pm-feature-design FEAT-ORD-004` to formalize the OTP guard condition and shadow-Customer state before build | Lena Vogt | 2026-02-14 | `[Skill: /pm-feature-design]` |
| 3 | Message Daniel Osei confirming guest orders still carry a verified phone number reachable for delivery-issue follow-up | Marcus Field | 2026-02-11 | `[Notion Task]` |
| 4 | Check SMS OTP provider cost per verification against current unit economics (adds a per-order cost previously unmodeled) | Sam Okonkwo | 2026-02-17 | `[Notion Task]` |
| 5 | Follow up once FEAT-ORD-004 ships to confirm the account-creation drop-off actually closes | Sam Okonkwo | 2026-03-10 | `[Meeting: Sam, guest checkout conversion results, by 2026-03-10]` |

---

## Review Scope

**What was reviewed:** FEAT-ORD-004 (Guest Checkout) spec draft, pre-`2_Spec_Done`

### Findings

| Item | Finding | Severity | Action |
|---|---|---|---|
| Checkout flow (account gate) | 38% abandonment at forced account creation | P0 | Ship guest checkout with phone verification (Decision 1-2) |
| Shadow Customer entity | Payment and rating flows assume a Customer record exists; guest flow as originally sketched didn't create one | P1 | Add shadow-Customer creation to spec before build (Decision 3) |
| Restaurant-partner visibility | Restaurant partners lose customer contact history on guest orders | P2 | Confirm verified phone number remains visible to restaurant/courier for delivery issues; communicate to Daniel Osei (Action 3) |

### Spec changes needed

- [ ] Add SMS OTP verification step to Section 2 Acceptance Criteria - Lena Vogt - by 2026-02-14
- [ ] Add shadow-Customer creation guard condition to Section 1 (Business Rules referenced) - Lena Vogt - by 2026-02-14
- [ ] Add post-delivery account-conversion magic-link prompt to Section 2 - Lena Vogt - by 2026-02-14

### Design Inspection result

- [x] Changes needed - listed above
- [ ] Re-run `/pm-feature-design FEAT-ORD-004` once changes are incorporated, then move to `3_Ready_to_Build`

---

## Open Questions

- Does SMS OTP cost per verification change the effective delivery-fee economics enough to matter at scale? (Sam to check by 2026-02-17, Action 4)
- Should the magic-link account-conversion prompt eventually feed into the Retention metric (2nd order within 21 days) as a distinct tracked cohort (guest-converted vs. account-first)? Open for KPI discussion, not urgent.

---

## Handoff

**Čo si teraz má:** Rozhodnutie o Guest Checkout (FEAT-ORD-004) so schválenými spec zmenami - jasné, čo ide do Feature Card pred buildom.

**Ďalší krok:** Oprav Feature Card FEAT-ORD-004 podľa Spec changes needed, potom re-run `/pm-feature-design FEAT-ORD-004`.
