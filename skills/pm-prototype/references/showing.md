# pm-prototype - Showing it, and collecting what comes back

> Reference for `skills/pm-prototype/SKILL.md`. Read it before the prototype is put in front of anyone - which is usually between the build and Step 8.

A prototype is a **social artifact**. Its value is realised when it is shown, and that is also where good ones die: the wrong screen order, fumbling at *"can it also do X?"*, an unadmitted fake spotted by the audience, which then discredits everything else in the room.

---

## 1. Show alternatives, or mark what is unresolved

The strongest documented distortion is not polish - it is **single-option framing**. In a controlled study the same design was rated significantly higher and criticised less when shown alone: **none of 36 participants rejected the single design**, while 3 of 12 explicitly rejected an alternative when three were shown.

So:

- If the prototype exists to **choose a direction**, show more than one. The harness variant switcher is for exactly this.
- If it is an **answer to a decided direction**, show one - and then explicitly mark the dimensions that are still open, so there is something legitimate to push back on.
- Ask **problem-specific critique**, never *"what do you think?"*. "Where would this break for you?" gets an answer; the open question gets politeness.

Related, and worth knowing before an investor meeting: three crowdfunding studies found an **inverted-U** between prototype fidelity and funding performance. Moderate outperformed both very low and very high, the authors arguing that extreme fidelity reads as a fait accompli and reduces perceived co-creation.

---

## 2. The order of the showing

1. **What question this exists to answer**, in one sentence, before anything is on screen. Without it every reaction is aimed at whatever the viewer happened to notice.
2. **The path that carries the claim**, end to end, in the state that makes it real - not the empty state unless emptiness is the point.
3. **The state that is least flattering** - the error, the unauthorised view, the first-run empty. Volunteering it early buys more credibility than any amount of polish, and it stops the audience discovering it as a gotcha.
4. **What is simulated** - the disclosure screen, once, rather than a running apology.
5. **What you want from them**, specifically.

**Say the faked part before someone notices it.** An admission that arrives after the audience spotted the thing is not an admission any more; it is a correction, and it costs the credibility of everything you said before it.

**Answering "can it also do X?"** - the honest form is *"not in this prototype, and here is what it would take"* or *"deliberately out of scope, because it does not affect the question we are answering."* Never a promise. The capability register on the disclosure screen exists so this answer is already written down.

---

## 3. Before it leaves the room

A checklist, because every item on it has bitten someone:

- [ ] Customer records, credentials, private URLs and internal comments removed
- [ ] Production connections and unapproved telemetry disabled
- [ ] **The built app and its network requests inspected** - not just the visible screens
- [ ] Sensitive fixtures replaced with fictional ones
- [ ] Sessions reset
- [ ] Access restricted to the intended testers

**Prototype events never go into production analytics.** Use a separate store or the harness's local log. An event-name prefix alone does not prevent contamination - the events still land in production funnels and can still trigger automations.

---

## 4. Three intents, with conflicting requirements

These are not levels of the same thing, and mixing them quietly invalidates one of them:

| Intent | What it needs | What breaks it |
|---|---|---|
| **Async test with real users** | behaviour capture, minimal prompting, and commenters who **cannot see each other** | shared comments - the sample is contaminated the moment the second person reads the first |
| **Internal review** | comments visible and threaded; that is the entire point | treating the resulting opinions as user evidence |
| **Cumulative requirement gathering** | persistence across sessions, and **a way out** | requests that die in a thread |

**The way out matters most.** A request raised in a comment should end up as an `OQ-` in the Open Questions Register or an item in a feature plan. Comments that flow nowhere are just another channel, and the person who raised one learns not to bother again.

Route what comes back:

| What came back | Where it goes |
|---|---|
| A question the prototype cannot answer | `OQ-` in the Open Questions Register, with the prototype as its source |
| A missing capability that would change the decision | a `PRT-` item if it is still a prototype question; a feature-plan item if the direction survived |
| A defect in the prototype itself | fix it, or record it as a known limitation on the disclosure screen |
| Evidence about the hypothesis | `findings.md`, in the right one of the four records |

---

## 5. Repeat participants

Record prior exposure and **separate first-use from learned performance**. Sequential revisions cannot undo exposure: once someone has seen a flow, they are no longer a first-use participant for it, and faster repeat performance alone does not prove the redesign helped.

When first-use clarity is the question, recruit fresh people. When both versions are available, vary and balance the order across participants.

---

## 6. Who moderates

**In a solo build the maker is the moderator**, and that makes demand effects the single most likely contamination - participants were ~2.5x more likely to prefer the artifact they believed the interviewer had built, and labelling a keyboard "research-based" measurably changed *objective typing speed*.

Controls that cost nothing:

- Neutral provenance - do not say you built it
- Hide the intended direction, and do not signal which option you prefer
- Include an equivalent or negative control where one is available
- Ask afterwards what they thought was being tested
- Privilege unprompted behaviour over praise

And when none of that was possible, **name it in `findings.md`** rather than presenting the result as clean. A stated distortion can be discounted by the reader; an unstated one just makes the finding wrong.
