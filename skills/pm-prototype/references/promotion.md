# pm-prototype - Classification, kill and promotion

> Reference for `skills/pm-prototype/SKILL.md`. Classification is read at **Step 3b**, before any code exists. Kill and promotion are read at **Step 8**, once there is a decision.

---

## Classification - decided before the first line of code

It sets the quality bar, so deciding it afterwards means the bar was never applied.

| Classification | Meaning | Where the code lives |
|---|---|---|
| **Disposable** | proof only, never merged | `build/` in the prototype folder |
| **Reference** | binding for flow, states and measurement - **not** architecture. Engineering reimplements, but must not have to guess what should happen | `build/` in the prototype folder |
| **Evolutionary** | deliberately may reach production | **the real repo, on a branch** - repo rules, security, tests and review from the first commit. The prototype folder holds the spec and a pointer to the branch |

**The dangerous middle is *throwaway quality with evolutionary expectations*.** Evolutionary code sitting inside a prototype folder is outside repo rules, which defeats the point of the classification entirely.

Say the classification out loud when it is chosen, and write it into `meta.md`. If nobody can say which one it is, that is itself a finding - it usually means the prototype is being built to be impressive rather than to answer something.

**Reference is the useful default** for most product prototypes: it binds the thing that matters (what should happen) without pretending the implementation is production-shaped.

---

## Kill

Killing your own work is unpleasant and organisations systematically defer it. The whole economics of this structure rests on kills actually happening, so the ritual has to be cheap and dignified rather than an admission of failure.

**First, check the kill is defensible** - all five conditions in `references/hypotheses.md` § 4. A *Prototype or study failure* is **not** a kill: it means the instrument did not expose the hypothesis, so the instrument gets fixed and the test re-run.

**What is kept:** the findings. Not the code.

`findings.md` is the thing that survives, and it is worth writing properly - what was observed, what was not tested, which distortions were present, and what would have to be true for this to be worth revisiting. A killed prototype with good findings is a cheap answer. A killed prototype with no findings was pure cost.

**What happens to the artifacts:**

| | |
|---|---|
| The prototype folder | deleted, or archived with the reason - a one-line decision note in `meta.md` and `findings.md` kept |
| Production registers | **untouched.** Nothing was ever written there, which is the entire point of the separate folder |
| Evolutionary code on a branch | the branch is closed. Say so explicitly - an abandoned branch that nobody deleted becomes someone's surprise later |
| `targets:` entries | if it targeted an `OQ-`, update that entry: the question was explored and this is what came back |

**How it is said.** A well-run test that rejects a weak idea is a *successful experiment*. The experiment and the idea succeed or fail separately, and the write-up should make that distinction visible rather than reading as a post-mortem.

---

## Promotion

A surviving prototype is, in the end, **a proposal to ship functionality into the real codebase**. Promotion is the moment that proposal is accepted, and it happens layer by layer rather than as one move.

| Layer | What happens |
|---|---|
| **Thin card** | becomes a production Feature Card, gets a real `FEAT-ID`, and records `promoted_from: PRT-[NAME]-00N` |
| **Local rules**, if any | into the global register as proper `BR-` IDs |
| **Local entities**, if any | into `entities.md` |
| **Local context** (personas, JTBD) | merged into the global artifacts, or discarded with a reason. Never left in both places |
| **Code** | Evolutionary is already in the repo - merge it. Reference is reimplemented against the card. Disposable is dropped |
| **The prototype folder** | freezes as history. It is never edited again |

That last row is what keeps two truths out. Once promoted, the prototype folder is a record of how the decision was reached, not a live document. If something needs changing afterwards, it changes in the production artifact.

**Same field names, thinner content** is what makes this a move rather than a rewrite. A thin card that used its own vocabulary would have to be translated; one that used the production field names only needs filling in.

**Use production components inside the prototype wherever they exist.** It is the single thing that makes promotion cheap, and it costs nothing at build time.

### After promotion

The card enters the normal JIT cycle through `pm-feature-design`, which should record two things the prototype earned:

- **what the prototype resolved** - so the JIT design does not re-open a settled question
- **what changed against it** - because the production spec will diverge, and an undocumented divergence is how a "reference" prototype quietly stops being binding

### Partial

Neither kill nor promotion: some of it survives. Promote the cards that earned it, kill the rest **explicitly** rather than leaving them in the folder, and record which was which. A partial decision that does not say what was dropped is an open decision wearing a decided label.
