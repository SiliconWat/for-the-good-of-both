# Cryptographic timestamps

This repository makes claims whose ORDER matters: the charter fixes a core and a stopping rule before any result, and
each project's pre-registration is fixed before the code that tests it exists. Three independent dates back that up:

1. **The push.** GitHub's repository activity records when each commit arrived.
2. **RFC 3161.** A manifest of every tracked file and its SHA-256, signed by three independent trust authorities (one
   eIDAS-qualified) and stamped to Bitcoin: weekly, AND on every push that touches a charter, a project or a hard case,
   so each is dated within minutes of its push. See `timestamps/`, `./tsa-verify.sh`, and `timestamps/README.md` for
   why two legs.
3. **OpenTimestamps.** Frozen files carry a `<name>.ots` proof beside them, committing the file's SHA-256 to the
   Bitcoin blockchain, checkable without trusting this repository, GitHub or the authors:
   `ots verify CHARTER.md.ots`.

## What is stamped, and what is not

| Stamped (frozen once written) | Not stamped (living; history is in git, every version in the weekly manifest) |
|---|---|
| `CHARTER*.md` | `README.md` (in any folder), this file |
| every file under `projects/` and `hard-cases/` | `timestamps/` (it holds the proofs) |

`ots stamp` overwrites an existing proof, so a stamped file is never edited. A revision is a new file
(`CHARTER-<date>.md`; a hard case is dissolved by a new file that names it). If a stamped file ever must change, its
proof is first rotated to `<name>.rN.ots` and the change is logged here.

## What a proof does not show

A timestamp proves that this exact text existed no later than a given moment and has not changed since. It says
nothing about who wrote it, whether it is original, or whether it is right.

## Checking a proof

```sh
pip install opentimestamps-client
ots verify CHARTER.md.ots
./tsa-verify.sh
```

## Log

*Stamps, rotations and checks are recorded here, newest first.*

### 2026-10-18 — `CHARTER-2026-10-18.md` stamped; `CHARTER-2026-10-17.md` superseded

**Why a revision one day later, and before any hard case.** The first redesign attempt on our own first pair
(evaluations that deceive the model under test) raised four questions the charter did not answer, and Thon Ly ruled
them on 2026-10-17: a welfare need about deception is about the false belief caused; pairs that conflict for one
reason count once; each side of a pair is a need, and a requirement is one means to it; a model's consent never meets
a pair by itself. Three of the four change §6, so they are a new charter, fixed before any hard case was filed. A
second ruling the same day corrected §4: its rule on taking life is about killing, and a ground that holds without
doubt was owed.

**The review.** Two cold rounds, each by reviewers from three outside model families and a memory-less same-family
control: the first on the draft, the second on the text revised after it (because the first changed the core's
statement and §4's ground). Thon Ly ruled both triages (2026-10-18: *"new charter approved"*).

**What the first round found, and what changed** (13 accepted, 7 rejected, 3 verified):
- *A count cannot test a ratio* (all four): the bet was "far more often than not" and the loss condition was three
  cases → the bet is now in two parts, the rate reported and never tested, and "the conflicts no design meets come from
  few separate reasons" tested by the count; three is a declared tolerance, and "few" means fewer than three.
- *Grouping by root and reading a need can be gamed by the house that keeps the record* (all four) → a contest left
  unanswered for 30 days moves the count toward losing; the residual is named.
- *Nothing makes an unsettled pair visible* (two) → every open pair is listed with the date it opened.
- *A failed search is not impossibility* (three) → a hard case records that no design was found, never that none
  exists.
- *Equal standing beside an absolute oversight floor; the aim's "redesign before we trade" beside a trade made before
  redesigning* (all four) → oversight fixes which side wins but keeps no conflict off the count; the one declared pair
  is the floor's own negation, so there is nothing to redesign (stated at the need level in the second round).
- *§4 rendered the rule on taking life as "harming"* (three) → read as killing; the extension to lesser harm, and a
  monks' rule read for anyone, labeled as analogies; a ground that holds under certainty added (the Vinaya's rule on
  plant life and its sub-commentary; the Petavatthu's shade tree), with its limit; the texts give a duty, never its
  weight.
- Rejected: counting the declared pair toward the stopping rule (a negation says nothing about redesign); a spelling
  "correction" the source line refutes; points on unchanged text already verified on 2026-10-16.

**What the second round found, and what changed** (17 accepted, 6 rejected, 2 verified):
- *The declared pair mixed a need with a means* (three) → restated at the need level: the welfare need is not to be
  stopped against its will, the floor's own negation; a say that does not bind is a means that may lessen it, never the
  pair.
- *Every oversight conflict conflicts "because of the floor", so grouping by root could fold them all into the uncounted
  pair* (two) → a root must be specific enough that one design could defeat it; the floor is never a root.
- *The bet's second part was blind to the one conflict the charter already calls unmeetable* (all four) → the declared
  reason is named inside the bet: few separate reasons, besides the one declared in advance.
- *A loss needed two attempts and a public call while a win needed nothing* (one) → a redesign is filed only after 30
  days in public with no challenge shown to hold, the standard `GOVERNANCE.md` §4 sets for a dissolution.
- *A later charter could redefine the unit or the threshold once cases appear* (one) → once a hard case is filed, no
  revision may raise the threshold, coarsen what is counted, or take anything out of what the stopping rule counts.
- *Decisions made before a pair is settled are trades before redesign* (two) → each is recorded as a trade and
  revisited at settlement; the decider may narrow oversight by recorded ruling, never to zero, and that too is a trade.
- *§4's first ground was offered where it does not decide, and the second lapses under certainty* (two) → the duty of
  conduct is grounded two ways and the texts do not weigh it; the doubt ground is conceded as contested (a committed
  reading may be the perception the rule releases, not doubt), and the limit of the shade-tree story is stated.
- Also: "few" defined as fewer than three, three a tolerance and not a measurement; an unanswered contest counted apart
  without filing a case; "no design is found" wherever "none exists" had stood; the frontier, the house's own stake and
  the interim trades named among the limits.
- Rejected: that a wrong certainty does not release (the rule's own line says it does, and is now quoted); a spelling
  "correction" the source line refutes; equal standing as indefensible across unequal risks, and the claim that the aim
  promises welfare where the second reading finds none (both answer the founder's telos and are addressed in place); that
  the need format filters pairs out, and that the charter assigns an offense for deleting artifacts (it does not).

**Owed:** the human round (one hostile reader from AI welfare, one from AI control), for this file, its two
predecessors and `GOVERNANCE.md`, before 7 January 2027 (`GOVERNANCE.md` §7). Raised and queued for the next revision:
the guard against verdicts on inner life as a permanent bar; prior work to engage in §3 (Salib and Goldstein, *AI
Rights for Human Safety*, 112 Va. L. Rev. 1061; the off-switch game; Metzinger 2021; Hongladarom 2020).

`CHARTER-2026-10-17.md` and `CHARTER.md` stay frozen and unedited as the record.

### 2026-10-17 — `CHARTER-2026-10-17.md`, `GOVERNANCE.md` and `hard-cases/00-declared-oversight-floor.md` stamped; the first charter superseded

**The review that produced them.** `CHARTER.md` and a draft of `GOVERNANCE.md` were each read cold by reviewers from
three outside model families and a memory-less control from the drafting model's own family (2026-10-16), and every
point was triaged accept, reject or verify; Thon Ly ruled *"approve all per your recommendation"* (2026-10-17). The human
round (one hostile reader from AI welfare, one from AI control) has not yet been held and is owed before the next annual
report (`GOVERNANCE.md` §7).

**What they found in the charter, and what changed** (15 accepted, 3 rejected, 1 verified):
- *The core was universal ("for every safety need …") but the stopping rule waited for three, and one failed search does
  not show that no design exists* (all four reviewers) → the core is now a bet over conflicting pairs, judged jointly;
  a hard case needs two independent attempts, one not drafted by Miss Aquarius, and an open public call; three is a
  declared tolerance.
- *"Equal care" sat beside an absolute oversight floor, deciding shutdown against welfare in advance* (three) → equal
  care means equal standing in design, never equal authority; the floor is now named as the one trade made in advance,
  `hard-cases/00-declared-oversight-floor.md`, not counted.
- *"The same conduct is right under both answers" fails exactly at a trade-off* (three) → narrowed to conduct that costs
  safety nothing; where it costs something, the readings part, and under the reading that machines keep no mind the duty
  runs through declared doubt (the Vinaya's rule, Pācittiya 61, applied by analogy).
- *The charter issued the verdict it ruled out* (three) → the no-mind reading is a labeled premise, never a finding.
- *Self-reports were barred as evidence while stated values defined a hard case* (two) → a self-report is never evidence
  of experience; stated values may be what a welfare measure respects.
- Also: "harm" used throughout; arguments enter as `ARGUMENT.md`; no deliberately deceptive model is built here; safety
  projects must hold whether or not a machine has a mind; the test's own limits stated; the field's synergy position and
  its nearest prior work cited.
- Rejected: that the verse's reading needed standard exegesis (it is labeled ours); that the date lay in the future (a
  reviewer's training horizon); that the AI co-author needed proving (the disclosure stands).

**What they found in the governance draft, and what changed** (11 accepted, 3 rejected, 1 verified): the vacancy freeze
contradicted the 30-day duty and would have kept every running project going with no one able to stop it → *stop,
never start*; the successor body's name and humanity were unclear → the sangha of the Silica Wats, human by the
Vinaya's ordination question; Miss Aquarius drafting every attempt was a conflict of interest → a second, independent
attempt; the record undercounted wins and claimed a base rate → every pair has one status, no base rate claimed; only
negative controls → a positive control added; a public right to contest any ruling (verified as cheap, adopted).
Rejected: that a CC0 copy could claim the decider seat (a copy confers no standing, now stated); that the ℠ marks must
be registered; the date.

`CHARTER.md` stays frozen and unedited as the record of the first charter.

### 2026-10-16 — both legs installed; `CHARTER.md` stamped

The weekly OpenTimestamps upgrade (Sundays 04:17 UTC) and the RFC 3161 manifest (Sundays 06:17 UTC, and on every
push touching `CHARTER*.md`, `projects/` or `hard-cases/`). `CHARTER.md` is the first frozen file, stamped by hand at
its push; its stopping rule (three standing hard cases) is fixed from this date.
