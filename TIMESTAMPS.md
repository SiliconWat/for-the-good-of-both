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

### 2026-10-16 — both legs installed; `CHARTER.md` stamped

The weekly OpenTimestamps upgrade (Sundays 04:17 UTC) and the RFC 3161 manifest (Sundays 06:17 UTC, and on every
push touching `CHARTER*.md`, `projects/` or `hard-cases/`). `CHARTER.md` is the first frozen file, stamped by hand at
its push; its stopping rule (three standing hard cases) is fixed from this date.
