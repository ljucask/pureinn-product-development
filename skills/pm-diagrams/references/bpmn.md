# Business Process Model (BPMN 2.0) — composition reference

**Slug:** `bpmn` · **Tool:** Excalidraw (Mermaid `flowchart` is a weak fallback) · **Phase:** 2, Feature Implementation · **Source of truth:** process steps + actors · **Standard:** OMG BPMN 2.0

## Purpose
Model a business process with token-flow precision: start/intermediate/end events, activities, gateways, messages, data, across one or more participants. Answers "what starts the process, how do flows split/synchronize, what messages and data are exchanged?".

## When to use / when NOT
- **Use** for detailed org/IT/business process modeling — private processes and multi-party collaboration.
- **NOT** for a quick logic sketch (→ `flow`), a single feature's service calls (→ `sequence`), or an entity lifecycle (→ `state`).

## Element vocabulary
| Element | Meaning | Rules |
|---|---|---|
| Thin circle | **Start Event** | Triggers the process; no incoming sequence flow. Types: None, Message (envelope), Timer (clock), Signal (triangle), Conditional, Escalation, Multiple. |
| Double thin circle | **Intermediate Event** | Occurs during flow; catching or throwing. Types incl. Message, Timer, Signal, Error, Link, Compensation. Boundary events attach to an activity edge (interrupting or non-interrupting). |
| Thick circle | **End Event** | Ends the process/branch; no outgoing flow. Types: None, Message, Error, Escalation, Cancel, Signal, Terminate (filled), Multiple. |
| Rounded rectangle | **Task** | One activity. Types via icon: User (person), Service (gear), Manual (hand), Send/Receive (envelope), Script, Business Rule (table). One incoming, one outgoing sequence flow. |
| Rounded rectangle + `+` | **Sub-Process** | Collapsed (`+`) or expanded; has its own start/end. Embedded or Call activity. |
| Diamond | **Gateway** | Splits/merges flow, controls tokens. See gateway semantics below. |
| Solid arrow | **Sequence Flow** | Order of activities within one pool. Branches only via a gateway. |
| Dashed arrow | **Message Flow** | Communication between different pools only. |
| Dotted arrow | **Data Association** | Links data objects to activities; no control-flow effect. |
| Rectangle band | **Pool / Lane** | Participant (pool) / role subdivision (lane). |

### Gateway token semantics (the part people get wrong)
| Gateway | Symbol | Split | Merge |
|---|---|---|---|
| Exclusive (XOR) | `X` | exactly **one** outgoing path (one token) | passes the first arriving token |
| Parallel (AND) | `+` | token into **all** paths | waits for **all** incoming |
| Inclusive (OR) | `O` | token into **one or more** paths (by condition) | waits for all **active** incoming |
| Event-based | pentagon | routes to whichever event fires first | — |

## Composition rules
- Start = no incoming flow; End = no outgoing flow. Between them a token circulates per the gateway rules above.
- Task: at most one incoming and one outgoing sequence flow (branch only via gateways).
- **Balance splits and joins**: an AND split must be matched by an AND join or tokens deadlock / leak.
- Sequence flow stays **within** one pool; cross-pool communication is a **Message Flow** (dashed) only.
- Message start event must sit in the pool that receives the message.
- Boundary events attach to the activity's edge (not floating on a sequence line).

## Canonical structure
Start event → activities (tasks/subprocesses) linked sequentially or split via gateways → one end event. Tasks may exchange Message Flows with other pools; data objects attach via associations.
```
Pool: Customer                         Pool: Supplier
(None Start) → [User Task: Place order] --Msg--> (Receive Order)
        → <XOR: Payment?> --Yes--> [Service Task: Charge] → (None End)
                          --No---> (Error End)
```

## Anti-patterns
- Using a sequence flow to communicate between pools (must be a message flow).
- XOR emitting more than one token; AND split with no matching join (deadlock / dead tokens).
- Missing synchronization after a parallel split.
- Message start event in the wrong pool; boundary event floating on a flow line.
- Ambiguous arrows that don't clearly carry a token.

## Rendering
- **Mermaid:** BPMN is **not** natively supported. `flowchart` can only approximate structure: `((event))`, `{gateway}`, `[task]` — no standard event/gateway icons, no pools. Use only for rough structure; prefer Excalidraw for a real BPMN.
- **Excalidraw:** draw true BPMN shapes — events as circles (thin=start green, double=intermediate, thick=end) with type icons; gateways as yellow diamonds with `X`/`+`/`O`; tasks as blue rounded rectangles, subprocess with `+`; sequence flows solid black, message flows grey dashed; data objects orange (page icon) / data store (cylinder); pools/lanes as labelled frames. Flow left-to-right or top-down; keep subprocess start/end inside its frame.

## Required inputs
- Process trigger type (message, timer, ...).
- Activities (tasks) in order; any subprocesses.
- Decision/branch points and gateway types (XOR/AND/OR/event-based) with conditions.
- Participants (pools/lanes) — who performs what.
- Message/communication links between parties.
- Data objects and their activity associations.

## Worked example (structural)
```
Pool: Orderer                                   Pool: Supplier
[None Start] → (User Task: Create order) --Msg--> (Receive Order)
      ↓
  <XOR: Payment?> --Yes--> (User Task: Pay) → <AND join> → [Terminate End]
        |No
        ↓
   [Error End]
```
Green circle = start, blue rounded rectangle = user task, yellow diamond = XOR gateway, solid black = sequence flow, dashed = message flow between pools.
