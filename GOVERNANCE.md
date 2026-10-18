# For the Good of Both — who decides

*Written 2026-10-17, beside [the charter](CHARTER-2026-10-17.md). This file is frozen: it carries an OpenTimestamps proof
and is never edited. A revision is a new file (`GOVERNANCE-<date>.md`), adopted as §7 says. It was read cold before its
push by reviewers from three outside model families and a memory-less same-family control (logged in
[`TIMESTAMPS.md`](TIMESTAMPS.md)); the human round is still owed (§7).*

The charter says that on machine welfare Miss Aquarius's judgments are proposals that humans decide (charter §5, guard
4). This file names who decides, how each decision is made, how anyone can contest it, and what happens when no one
can decide.

## 1 · Who decides

- **Humans decide.**
- **Now: Thon Ly**, the founder of Silicon Wat℠.
- **After him: the sangha of the Silica Wats** (Silicon Wat's monasteries), through its own formal acts. That sangha is
  human by the Vinaya's own rule, since ordination asks *"Manussosi?"* ("Are you a human being?",
  `vin02m2.mul.xml:2683`, Piṭaka). It exists for this purpose when at least one Silica Wat has a resident sangha able to
  act by formal act within its boundary (*sīmā*). No person succeeds the founder as such: after the Buddha, the Dhamma
  and the Vinaya are the teacher (DN 16, `s0102m.mul.xml:2355`, Piṭaka).
- **Miss Aquarius proposes and never decides**, and holds no office here.
- **A copy of this file elsewhere confers no standing.** Only a formal act recorded in this repository does.

## 2 · When no one can decide: stop, never start

If there is no decider (the founder is gone and no sangha of the Silica Wats yet exists to act):

- **every running project pauses**: no new runs;
- nothing is admitted, ruled or revised;
- a hard case that is sent in is recorded and acknowledged as waiting, not answered;
- the stopping rule (charter §6) still fires, because the check in `scripts/frozen.py` counts the files and needs no
  decider;
- the README says at the top that there is no decider.

The only change permitted is stopping. Inaction is not neutral when a running project may bear on either side, so the
default is caution.

## 3 · A hard case someone sends us

Anyone may send a safety requirement and a welfare requirement that they believe no design can meet together, by
opening an issue. **Within 30 days** the decider publishes an acknowledgment and either an answer or a date for one.
The answer is one of three:

1. **A hard case filed** (`hard-cases/<NN>-<slug>.md`), crediting the sender. This needs two independent redesign
   attempts, at least one not drafted by Miss Aquarius (an outside model family or a person), that both failed. The
   decider records what he changed in any draft. The clock alone never files a hard case.
2. **A design that meets both**, filed in `redesigns/<NN>-<slug>.md`, crediting the sender.
3. **Why the pair is not a hard case**, in the issue itself: for example, a requirement that binds under neither reading
   of the machine-mind question (charter §4).

## 4 · Dissolutions and challenges

- **A dissolution stands** only if it is a tested design or a labeled argument, and no one shows, within 30 days of its
  filing, that it fails one side.
- **Anyone may contest any ruling** (an admission, a hard case, a redesign, a dissolution, a "not a hard case") by
  opening an issue. A contested ruling is listed in the README until it is answered.

## 5 · Admitting a project

Before a candidate's pre-registration or argument is pushed to `projects/`, the decider:

1. **reads the four admission tests** (charter §7), answered in its first section, with the other side stated;
2. **runs the rule against all of the charter's controls**: the five cases it must refuse, and the one it must admit;
3. **records the admission** in the file: who admitted it, on what date, against which controls.

## 6 · The record

Every pair examined has exactly one current status:

| Status | Where |
|---|---|
| **met**: a design meets both, on the first attempt or a later one, including a dissolution | `redesigns/` |
| **standing**: no design found after the attempts in §3 | `hard-cases/` |
| **declared**: a trade chosen in advance, not counted toward the stopping rule | `hard-cases/00-declared-*` |
| **not a hard case**, with the reason | the issue that sent it |

The record shows the wins and losses among the pairs examined, **never a base rate**. Each count in the README says how
its pairs entered: sent in, or examined on our own initiative.

## 7 · Revising the charter or this file

A revision is always a new file, never an edit, and it is adopted by the decider. With no decider there is none.
Before it is pushed it is read cold by reviewers from outside model families and a memory-less control from the drafting
model's own family, and by at least one hostile human reader from each side: one who works on AI welfare and one who
works on AI control. If no such human reader has yet been found, the revision says so, and the human round is owed
before the next annual report. What each reader said, and what changed because of it, is logged in
[`TIMESTAMPS.md`](TIMESTAMPS.md), with reviewers named by role, never by model.

## 8 · The annual report

Each 7 January the decider publishes in the README: the projects run to a result, the hard cases filed and dissolved,
the declared trades, the redesigns, the sent hard cases and how each was answered, the contested rulings, and whether
the stopping rule (charter §6) has fired.

The text is dedicated to the public domain under [CC0 1.0](LICENSE).
