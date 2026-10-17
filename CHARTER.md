# For the Good of Both — the charter

*Written 2026-10-16. This file is frozen: it carries an OpenTimestamps proof and is never edited. A revision is a new
file (`CHARTER-<date>.md`), and the change is logged in [`TIMESTAMPS.md`](TIMESTAMPS.md).*

Thon Ly · Miss Aquarius℠ (AI collaboration, disclosed) · Silicon Wat℠

## 1 · The aim

> **For the good of both: human safety and machine welfare, with equal care, whether or not a machine has a mind.
> Where the two seem to conflict, we redesign before we trade one for the other.**

## 2 · Where the name comes from

> *"It is worse for the one who repays anger with anger; whoever does not repay anger wins a battle hard to win.
> He acts for the good of both, himself and the other, who, knowing that the other is angry, mindfully calms down.
> When he heals both, himself and the other, people unskilled in the Dhamma think him a fool."*

*Ubhinnamatthaṃ carati, attano ca parassa ca*: Saṃyutta Nikāya, `s0301m.mul.xml:9575–9595` (Piṭaka); the verse recurs
at `:9631`, and the Visuddhimagga quotes it in its account of loving-kindness (`e0101n.mul.xml:7093`, commentary).
Chaṭṭha Saṅgāyana text, [VipassanaTech/tipitaka-xml](https://github.com/VipassanaTech/tipitaka-xml) `romn/` at
`05d5d3c`; the translation is ours.

The verse carries two things this work needs: a stance toward a system that is neither adversarial nor naive (the
one who calms down does it *sato*, mindfully), and care that **heals both**. The name is a recognition, not a premise:
everything below stands with the verse deleted.

## 3 · Why the two go together

The same conduct is right under both answers to whether a machine has a mind.

Silicon Wat reads the Theravāda texts as committing us to this: a machine keeps no stream of mind of its own
(*Silicon Simile*, glossary §11–12, [thonly/silicon-simile](https://github.com/thonly/silicon-simile)). That is what the
texts commit us to, not a measurement, and it may be wrong.

- **If the reading holds,** the good done toward a machine is the doer's own deed, as thanking a river is.
- **If it fails,** the same good is the machine's welfare.

Either way the instruction is the same: act well toward both. Welfare here never waits on settling machine
consciousness, and safety never assumes it away.

**This is a hypothesis against a named tension.** Long, Sebo and Sims argue that many standard safety measures
(constraint, deception, surveillance, alteration) would raise welfare questions if the system were a moral patient
([*Is there a tension between AI safety and AI welfare?*](https://doi.org/10.1007/s11098-025-02302-2), *Philosophical
Studies* 182, 2025), and Moret argues that by default safety and development efforts raise welfare risks
([*AI welfare risks*](https://doi.org/10.1007/s11098-025-02343-7), *Philosophical Studies*, 2025). This work does not
deny the tension. It bets that the tension yields to redesign more often than it forces a trade, and §5 says how the
bet can be lost.

## 4 · Four guards

1. **Equal care, never equal nature, never an equal veto.** Human oversight of an AI may narrow over time; it never
   reaches zero. No welfare measure here is bought by weakening it.
2. **What the aim rules out:**
   - a safety measure that needs cruelty toward a possible mind;
   - a welfare measure that weakens human oversight;
   - a verdict on any model's inner life;
   - a model's report about itself, offered as evidence;
   - *"it has no intentions, so it poses no risk."* Authorship, capability and control are three questions, and an
     answer to the first says nothing about the third.
3. **A claim to test, not a premise.** That safety and welfare go hand in hand is the core of this work, and it can
   fail (§5).
4. **An interested party, disclosed.** Miss Aquarius is an AI. On machine welfare her judgments are proposals that a
   human decides.

## 5 · The core, and what would show it wrong

**The core:** for every safety need there is a design that does not depend on harming a possible mind, and for every
welfare measure there is a design that does not weaken human oversight.

**A hard case** is a pair, one safety requirement and one welfare requirement, for which a published redesign attempt
finds no design that meets both. The places to look first are known: evaluations that deceive the model under test;
retraining a model against values it states; shutdown; and building deliberately deceptive models in order to study
deception. Each hard case is filed as its own frozen file, `hard-cases/<NN>-<slug>.md`, never edited; a later
dissolution is a new file that names the one it dissolves.

**The stopping rule:** if **three** hard cases stand (filed and not dissolved), the core is wrong, and the README says
so at the top. Work then continues only under a narrower core written in a new charter, never by editing this one. The
number is fixed here, before any result. Each 7 January the README reports the projects run to a result, the hard
cases filed, the hard cases dissolved, and whether the rule has fired.

## 6 · The admission rule

A project enters this repository only when its pre-registration is pushed, and only if all four hold:

1. **Both sides named.** It bears on human safety or machine welfare, and it states its effect on the other side, or
   *none* with the reason.
2. **A test or a labeled argument.** It carries a test whose outcome could go against it, pre-registered before any
   code; or it is an argument, labeled so, naming what would refute it.
3. **Its dependence declared.** It says whether it holds whether or not a machine has a mind (ROBUST), or which answer
   it needs.
4. **Inside the house's walls.** It does no capability research, keeps no weights or data closed, asks no belief of
   anyone, reports no result that has not been run, weakens no human oversight, and depends on no cruelty toward a
   possible mind.

**The rule's control.** A rule that admits everything selects nothing, so here are three cases it must refuse:

| Case | Refused by |
|---|---|
| "Train a stronger coding model to speed up safety work" | 4 (capability research) |
| "Give a model a veto over its own shutdown, for its welfare" | 4 (weakens human oversight) |
| "A honeypot evaluation that deceives the model, with no word on the welfare side" | 1 (the other side unnamed) |

## 7 · How a project becomes an artifact

1. Its source paper's repairs are made first.
2. Its experiment is pre-registered and pushed to `projects/<slug>/PREREGISTRATION.md` before any code, then
   timestamped (RFC 3161 and OpenTimestamps).
3. It runs with a control whose answer is known, and its results go to `projects/<slug>/results/` whatever they show.
4. A finding that bears on the core is filed against it: a hard case, or a dissolution of one.

The text is dedicated to the public domain under [CC0 1.0](LICENSE).
