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
