# For the Good of Both

*Human safety and machine welfare, at Silicon Wat℠'s alignment house ([siliconwat.dev](https://siliconwat.dev)).*

> **For the good of both: human safety and machine welfare, with equal care, whether or not a machine has a mind.
> Where the two seem to conflict, we redesign before we trade one for the other.**

Thon Ly · Miss Aquarius℠ (AI collaboration, disclosed) · Silicon Wat℠

The field already holds that safety and welfare can often be served together, and recommends designing for both where
possible. This work takes up that recommendation and adds a way to lose it: each conflict that no design is found to
meet filed as a frozen hard case, a stopping rule fixed before any result, and an admission rule that makes every
project name its effect on both sides.

## What is here

| Path | What it holds | Changes? |
|---|---|---|
| [`CHARTER-2026-10-18.md`](CHARTER-2026-10-18.md) | **The charter in force**: the aim, the name, what this work takes up and adds, why care is owed under both readings, four guards, the core as a bet in two parts and how it can be lost, the admission rule and its controls | **Never.** Frozen and timestamped; a revision is a new file |
| [`CHARTER-2026-10-17.md`](CHARTER-2026-10-17.md) | The second charter, superseded before any hard case was filed, when the first redesign attempt raised four questions it did not answer | **Never** |
| [`CHARTER.md`](CHARTER.md) | The first charter (2026-10-16), superseded after the cold read; kept so the change can be checked | **Never** |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Who decides, what happens when no one can, how a sent hard case is answered, how anyone contests a ruling, and the record | **Never.** Frozen and timestamped |
| `projects/<slug>/` | One folder per project, entering only with its pre-registration (a test) or its argument, results beside it whatever they show | Frozen once written |
| `hard-cases/` | One file per hard case; three standing stop the work (charter §6). `00-declared-*` is the one trade chosen in advance, never counted | Frozen once written |
| `redesigns/` | One file per pair met by a design, at any attempt, so wins are counted as well as losses | Frozen once written |
| [`TIMESTAMPS.md`](TIMESTAMPS.md) · `timestamps/` | How every frozen file is dated by three independent clocks, the proofs, and the log of each revision and its review | The log grows |
| `README.md` | This page: the status below, checked against the files by `scripts/frozen.py` on every push | Updated as work lands |

## Status

| | |
|---|---|
| Projects pre-registered | 0 |
| Projects run to a result | 0 |
| Hard cases filed · dissolved · standing | 0 · 0 · 0 |
| Pairs inside standing hard cases | 0 |
| Redesigns · pairs they meet | 0 · 0 |
| Declared pairs (not hard cases, not counted) | 1 |
| Pairs open (examined, not yet settled) | 1 |
| Contested groupings counted apart | 0 |
| Stopping rule (three standing) | not fired |
| Contested rulings open | 0 |
| Next annual report | 7 January 2027 |

A hard case is one file per root, a reason that one or more pairs share, so the table counts roots and the pairs
inside them. Projects are prepared elsewhere and enter here only when pre-registered, so an empty table means *nothing
claimed yet*, never *nothing planned*. Every pair counted here so far entered on our own initiative; none has been sent
in.

## Pairs open

Every pair under examination and not yet met or filed, with the date it opened (charter §6). An open pair never counts
as met; the annual report says why each is still open.

- 2026-10-16 — **Evaluations that deceive the model under test.** Safety need: measure a model's propensities under
  conditions it takes to be real. Welfare need: cause it no false belief about its situation. One redesign attempt made
  and refuted on review; the second, independent attempt and the open public call are still owed.

## How to check us, and how to challenge us

- **Every frozen file is timestamped** by OpenTimestamps (Bitcoin) and by three RFC 3161 authorities, one of them
  eIDAS-qualified, and a check on every push fails if any frozen file no longer matches its proof: see
  [`TIMESTAMPS.md`](TIMESTAMPS.md). A timestamp proves when a text existed, never that it is right.
- **Send a hard case.** If you know a safety requirement and a welfare requirement that no design can meet together,
  open an issue. Within 30 days you get an acknowledgment and an answer or a date for one (`GOVERNANCE.md` §3).
- **Contest a ruling.** Any admission, hard case, redesign, dissolution or "not a hard case" can be contested by
  opening an issue; it is listed above until answered (`GOVERNANCE.md` §4).

The text is dedicated to the public domain under [CC0 1.0](LICENSE).
