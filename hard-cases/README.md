# Hard cases

One file per hard case (charter §6): one or more pairs, each a safety need and a welfare need, that are in conflict
for one stated reason, their **root**, and that no design met after two independent redesign attempts (one not
drafted by Miss Aquarius) and an open public call (GOVERNANCE.md §3). **None filed.** The folder also holds the one
declared pair, `00-declared-oversight-floor.md`, which is not a hard case and is never counted.

Each file is `<NN>-<slug>.md`, numbered in the order filed, frozen once written (an OpenTimestamps proof beside it, and
the RFC 3161 manifest on its push), never edited. It states:

1. **The root**: the one fact that is why each of its pairs conflicts, specific enough that a single design defeating
   it would meet them all.
2. **Each pair, under its own `## Pair <n>` heading**: the safety need and the welfare need (each the purpose a
   requirement is offered for, never wider), under which reading of the machine-mind question the welfare side binds
   (charter §4), and who sent it, if it came from outside, with the date.
3. **The redesign attempts**: at least two, independent; every design tried, and why each failed one side.

A hard case is **dissolved** only by a later file, `<NN>-dissolved-<MM>-<slug>.md`, where `MM` is the case it
dissolves, naming the design that meets both. **Standing** = filed and not dissolved; it stands while any of its pairs
stands. Three standing hard cases stop the work (charter §6). The README counts the roots and the pairs inside them,
and `scripts/frozen.py` checks both against these files on every push.
