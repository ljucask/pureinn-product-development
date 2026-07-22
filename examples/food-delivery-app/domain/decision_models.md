# Decision Models Matrix
# Live Register 3 of 5 - FDD+SDD Framework

> **Product:** PureHunger
> **Version:** 1.0
> **Last updated:** 2026-07-16
> **Maintained by:** pm-business-rules-library (init) + pm-feature-design (JIT enrichment)

---

> **How to read this register:**
> - Decision tables define outputs for all combinations of input conditions
> - Used by Claude Code to generate unit tests covering all edge cases
> - Referenced in Feature Cards Section 1 (Biznis Mantinely) by TBL-ID
> - Status: Draft = structure defined, values TBD | Final = complete, used in build

---

## TBL-REST-01: Restaurant Onboarding Approval

**Domain:** Restaurant Onboarding
**Used by rule:** [BR-REST-001](/domain/business_rules.md#br-rest-001), [BR-REG-003](/domain/business_rules.md#br-reg-003)
**Affected entity:** [Restaurant](/domain/entities.md#restaurant) - gates the `Pending -> Active` transition
**Status:** Final
**Used in features:** FEAT-REST-001 (Restaurant application review)

| Food-service permit valid | Background check | Min. 5 available MenuItems | Outcome |
|---|---|---|---|
| Yes | Passed | Yes | **Approve** - transition to Active |
| Yes | Passed | No | **Hold** - permit and background check clear, but restaurant cannot go live without a minimum viable menu; Ops sends a menu-completion nudge, restaurant stays Pending |
| Yes | Pending | Yes/No | **Hold** - background check must resolve before Active regardless of menu state |
| No | Any | Any | **Reject** - restaurant stays Pending, cannot resubmit until a valid permit is uploaded (BR-REG-003 is a hard governance gate, not a judgment call) |
| Expired mid-review | Passed | Yes | **Hold** - treated as "No" until a renewed permit is uploaded; does not auto-reject an otherwise-approvable applicant |

**Edge cases:**
- Permit expires *after* Active: does not re-trigger this table - handled by the separate annual re-verification job (BR-REG-003), which can move an already-Active restaurant to Paused, not back through this onboarding table.
- Restaurant re-applies after a Reject: re-enters this table from scratch once a valid permit exists - no "second chance" leniency on the other two conditions.

---

## TBL-PAY-01: Cancellation Refund Amount

**Domain:** Payments
**Used by rule:** [BR-PAY-002](/domain/business_rules.md#br-pay-002), [BR-PAY-004](/domain/business_rules.md#br-pay-004), [BR-ORD-003](/domain/business_rules.md#br-ord-003)
**Affected entity:** [Payment](/domain/entities.md#payment), [Order](/domain/entities.md#order)
**Status:** Final
**Used in features:** FEAT-ORD-001, FEAT-PAY-002 (Ops refund tooling, post-MVP)

| Order state at cancellation | Trigger | Refund amount |
|---|---|---|
| Placed (customer-initiated, per BR-ORD-003) | Customer cancels before Restaurant Accepted | 100% - payment was only Authorized, not Captured; the auth is simply released, nothing to refund |
| Placed → 10 min elapsed, no Restaurant response | Auto-refund (BR-PAY-002) | 100% - system-initiated, no customer action required |
| Accepted or later | Restaurant-initiated cancellation (e.g. out of an ingredient) | 100% - full refund regardless of prep progress; PureHunger absorbs the loss, not the customer |
| Accepted or later | Customer-initiated cancellation | **Not permitted** - BR-ORD-003 blocks this state transition entirely; customer must contact support for a manual Ops override, which falls outside this table (logged exception, not an automated decision) |
| Delivered | Any refund request (quality complaint, missing items) | Partial, capped at `payment.captured_amount` per BR-PAY-004; exact percentage is an Ops judgment call outside this table's automation - this table only enforces the ceiling, not the amount |

**Edge cases:**
- Multiple partial refunds against one Payment: each new refund request must check the *running total* against `captured_amount` (BR-PAY-004), not just the current request in isolation.
- Tip handling: refund amounts in this table apply to the food + delivery fee subtotal only - courier tips are never refunded once a Delivery reaches Completed, since the courier has already been paid out.

---

## TBL-DEL-01: Courier Reinstatement Review Outcome

**Domain:** Trust & Safety
**Used by rule:** [BR-DEL-001](/domain/business_rules.md#br-del-001)
**Affected entity:** [Courier](/domain/entities.md#courier) - governs the manual `Suspended -> Active` review that follows an automatic suspend
**Status:** Final
**Used in features:** FEAT-DEL-004 (Ops courier review console, post-MVP)

| Reason for original low rating | Prior suspensions (lifetime) | Ops review finding | Outcome |
|---|---|---|---|
| Isolated bad-weather week (verified via delivery-time data) | 0 | No pattern of fault | **Reinstate**, no warning - rolling average resets on reinstatement |
| Pattern of late deliveries, courier-attributable | 0 | Confirmed courier behavior | **Reinstate with warning** - documented in Courier record; next suspension skips straight to permanent review |
| Pattern of late deliveries, courier-attributable | 1+ | Confirmed courier behavior | **Permanent deactivation** - second confirmed offense |
| Safety complaint (any severity) | Any | Confirmed | **Permanent deactivation** - safety complaints never get a reinstate-with-warning path, regardless of suspension history |
| Safety complaint (any severity) | Any | Not confirmed / insufficient evidence | **Reinstate**, no warning - but the complaint record is retained for pattern detection across future incidents |

**Edge cases:**
- Courier disputes the suspension before Ops review completes: Courier stays Suspended (BR-DEL-001 has no auto-reinstate path) - dispute status does not change this table's inputs, only the timeline Ops is expected to review within.
- Ops override without completing all three input checks: not permitted - BR-GOV-002 (reason-code requirement) applies to this table's outcome exactly as it does to BR-DEL-003's GPS override.

---

## Changelog

| Version | Date | Change | Triggered by |
|---|---|---|---|
| 1.0 | 2026-07-16 | Initial structure - three decision tables covering restaurant onboarding, cancellation refunds, and courier reinstatement | Phase 5 init, alongside business_rules.md v1.2 |
