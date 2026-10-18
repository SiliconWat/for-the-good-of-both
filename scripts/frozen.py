#!/usr/bin/env python3
"""frozen.py — the rules of this repository, checked by a machine instead of by a person counting.

  python3 scripts/frozen.py              check everything below; exit 1 on any failure
  python3 scripts/frozen.py --list       the frozen files
  python3 scripts/frozen.py --unstamped  the frozen files with no OpenTimestamps proof yet (the stamp workflow reads this)
  python3 scripts/frozen.py --self-test  plant each failure in a scratch copy and confirm the check catches it

What is checked:
  1. every frozen file (timestamps/FROZEN) has a <file>.ots proof beside it;
  2. every proof commits to the file's CURRENT SHA-256 — so a frozen file that changed fails here, offline, with no
     calendar or Bitcoin node needed (the digest is read from the proof's own header);
  3. the README's status table agrees with the files: projects pre-registered and run; hard cases (one file per ROOT)
     filed, dissolved and standing, and the PAIRS inside the standing ones; redesigns and the pairs they meet; declared
     pairs; and the pairs open, against the list under "## Pairs open" (charter §6; GOVERNANCE.md §6). A pair is a
     "## Pair" heading in a hard-case or redesign file, and every such file must list at least one; a dissolution is
     NN-dissolved-MM-<slug>.md, naming the case MM it dissolves;
  4. the stopping rule: three or more STANDING hard cases (a declared pair, NN-declared-*.md, is never counted; a
     contested grouping unanswered in 30 days adds its extra roots through the README row "Contested groupings counted
     apart") require the README to say "FIRED" and to carry, above "## What is here", a line saying the bet is lost;
     fewer require "not fired" and no such line.

Standard library only. Paths are matched against timestamps/FROZEN with fnmatch, where `*` also crosses `/`, the same
reading tsa-verify.sh gives the file with a shell `case`.
"""
import fnmatch, hashlib, os, re, shutil, subprocess, sys, tempfile

OTS_MAGIC = b"\x00OpenTimestamps\x00\x00Proof\x00\xbf\x89\xe2\xe8\x84\xe8\x92\x94"
SHA256_TAG = 0x08


def patterns(root):
    inc, exc = [], []
    with open(os.path.join(root, "timestamps", "FROZEN"), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            (exc if line.startswith("!") else inc).append(line.lstrip("!"))
    return inc, exc


def tracked(root):
    out = []
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in (".git",)]
        for f in files:
            out.append(os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/"))
    return sorted(out)


def frozen_files(root):
    inc, exc = patterns(root)
    return [p for p in tracked(root)
            if any(fnmatch.fnmatchcase(p, i) for i in inc) and not any(fnmatch.fnmatchcase(p, e) for e in exc)]


def ots_digest(path):
    """the SHA-256 a detached .ots proof commits to, read from its header; None if it is not one"""
    with open(path, "rb") as f:
        b = f.read(len(OTS_MAGIC) + 1 + 1 + 32)
    if not b.startswith(OTS_MAGIC):
        return None
    rest = b[len(OTS_MAGIC):]
    if len(rest) < 34 or rest[0] != 0x01 or rest[1] != SHA256_TAG:
        return None
    return rest[2:34].hex()


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


PAIR = re.compile(r"^#{2,3}\s+Pair\b", re.M)


def pairs_in(path):
    return len(PAIR.findall(open(path, encoding="utf-8").read()))


def counts(root):
    proj = os.path.join(root, "projects")
    pre = run = 0
    if os.path.isdir(proj):
        for d in sorted(os.listdir(proj)):
            pd = os.path.join(proj, d)
            if not os.path.isdir(pd):
                continue
            if any(re.fullmatch(r"PREREGISTRATION.*\.md", f) for f in os.listdir(pd)):
                pre += 1
                rd = os.path.join(pd, "results")
                if os.path.isdir(rd) and any(not f.endswith(".ots") for f in os.listdir(rd)):
                    run += 1
    hc = os.path.join(root, "hard-cases")
    names = sorted(os.listdir(hc)) if os.path.isdir(hc) else []
    dissolutions = [f for f in names if re.fullmatch(r"\d\d-dissolved-.+\.md", f)]
    gone = {m.group(1) for f in dissolutions for m in [re.fullmatch(r"\d\d-dissolved-(\d\d)-.+\.md", f)] if m}
    declared = sum(1 for f in names if re.fullmatch(r"\d\d-declared-.+\.md", f))
    filed = [f for f in names if re.fullmatch(r"\d\d-.+\.md", f) and "-dissolved-" not in f and "-declared-" not in f]
    standing = [f for f in filed if f[:2] not in gone]
    rd = os.path.join(root, "redesigns")
    rfiles = sorted(f for f in os.listdir(rd) if re.fullmatch(r"\d\d-.+\.md", f)) if os.path.isdir(rd) else []
    return {"pre": pre, "run": run, "filed": len(filed), "dissolved": len(dissolutions), "declared": declared,
            "standing": len(standing), "standing_pairs": sum(pairs_in(os.path.join(hc, f)) for f in standing),
            "redesigns": len(rfiles), "redesign_pairs": sum(pairs_in(os.path.join(rd, f)) for f in rfiles),
            "unnamed_dissolutions": [f for f in dissolutions if not re.fullmatch(r"\d\d-dissolved-\d\d-.+\.md", f)],
            "pairless": [f"hard-cases/{f}" for f in filed if pairs_in(os.path.join(hc, f)) == 0]
                        + [f"redesigns/{f}" for f in rfiles if pairs_in(os.path.join(rd, f)) == 0]}


def readme_table(root):
    text = open(os.path.join(root, "README.md"), encoding="utf-8").read()
    def row(label):
        m = re.search(r"^\|\s*" + re.escape(label) + r"\s*\|\s*(.+?)\s*\|\s*$", text, re.M)
        return m.group(1) if m else None
    head = text.split("## What is here")[0]
    return text, head, {
        "pre": row("Projects pre-registered"),
        "run": row("Projects run to a result"),
        "hard": row("Hard cases filed · dissolved · standing"),
        "standing_pairs": row("Pairs inside standing hard cases"),
        "redesigns": row("Redesigns · pairs they meet"),
        "declared": row("Declared pairs (not hard cases, not counted)"),
        "open": row("Pairs open (examined, not yet settled)"),
        "contested": row("Contested groupings counted apart"),
        "rule": row("Stopping rule (three standing)"),
    }


def check(root, allow_unstamped=False):
    errs = []
    for p in frozen_files(root):
        proof = os.path.join(root, p + ".ots")
        if not os.path.isfile(proof):
            if not allow_unstamped:
                errs.append(f"UNSTAMPED frozen file: {p} (stamp it by hand at its push)")
            continue
        d = ots_digest(proof)
        if d is None:
            errs.append(f"NOT A PROOF: {p}.ots (no OpenTimestamps sha256 header)")
        elif d != sha256(os.path.join(root, p)):
            errs.append(f"FROZEN FILE CHANGED: {p} no longer matches its proof — restore it, or make the revision a new file")
    c = counts(root)
    for f in c["unnamed_dissolutions"]:
        errs.append(f"A DISSOLUTION MUST NAME ITS CASE: hard-cases/{f} (write NN-dissolved-MM-<slug>.md)")
    for f in c["pairless"]:
        errs.append(f"LISTS NO PAIR: {f} (each pair is a '## Pair' heading)")
    text, head, t = readme_table(root)
    sec = re.search(r"^## Pairs open\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    listed = len(re.findall(r"^- ", sec.group(1), re.M)) if sec else 0
    want = {"pre": str(c["pre"]), "run": str(c["run"]),
            "hard": f"{c['filed']} · {c['dissolved']} · {c['standing']}", "standing_pairs": str(c["standing_pairs"]),
            "redesigns": f"{c['redesigns']} · {c['redesign_pairs']}", "declared": str(c["declared"]),
            "open": str(listed)}
    for k, v in want.items():
        if t[k] is None:
            errs.append(f"README status row missing: {k}")
        elif t[k] != v:
            errs.append(f"README says {k} = {t[k]!r}, the files say {v!r}")
    extra = 0
    if t["contested"] is None:
        errs.append("README status row missing: contested")
    elif not t["contested"].isdigit():
        errs.append(f"README says contested = {t['contested']!r}: write a whole number of extra roots")
    else:
        extra = int(t["contested"])
    fired = c["standing"] + extra >= 3
    banner = re.search(r"core is wrong|bet is lost", head, re.I) is not None
    if t["rule"] is None:
        errs.append("README status row missing: stopping rule")
    elif fired and (t["rule"].upper() != "FIRED" or not banner):
        errs.append(f"STOPPING RULE FIRED ({c['standing']} standing hard cases + {extra} contested apart): the README must "
                    "say FIRED and carry, above '## What is here', a line saying the bet is lost")
    elif not fired and (t["rule"] != "not fired" or banner):
        errs.append(f"stopping rule not fired ({c['standing']} standing + {extra} contested apart): the README must say "
                    "'not fired' and carry no 'bet is lost' line")
    return errs


def setrow(text, label, value):
    return re.sub(r"(\|\s*" + re.escape(label) + r"\s*\|\s*).+?(\s*\|\s*$)", lambda m: m.group(1) + value + m.group(2),
                  text, count=1, flags=re.M)


def self_test(root):
    """plant each failure in a scratch copy; every plant must be caught, and the clean copy must pass"""
    results = []
    # The base is the COMMITTED tree (git ls-files), never the working tree: an untracked, unstamped frozen file is a
    # real failure for the main check, but it would make the self-test's "clean copy" dirty and report the instrument
    # broken when only the tree is (found 2026-10-17 with GOVERNANCE.md drafted and not yet stamped).
    try:
        base = subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True, check=True).stdout.split()
    except (OSError, subprocess.CalledProcessError):
        base = tracked(root)
    def scratch():
        d = tempfile.mkdtemp(prefix="ftgob-selftest-")
        for p in base:
            dst = os.path.join(d, p)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(os.path.join(root, p), dst)
        return d
    def frozen_target(d):
        f = frozen_files(d)
        return f[0] if f else None

    d = scratch(); results.append(("clean copy passes", check(d) == [])); shutil.rmtree(d)

    d = scratch(); t = frozen_target(d)
    if t:
        open(os.path.join(d, t), "a").write("\ntampered\n")
        results.append(("a tampered frozen file is caught", any("FROZEN FILE CHANGED" in e for e in check(d))))
    shutil.rmtree(d)

    d = scratch(); os.makedirs(os.path.join(d, "hard-cases"), exist_ok=True)
    open(os.path.join(d, "hard-cases", "98-planted.md"), "w").write("# planted\n\n## Pair 1\n")
    e = check(d)
    results.append(("an unstamped frozen file is caught", any("UNSTAMPED" in x for x in e)))
    results.append(("a hard case the README does not count is caught", any("README says hard" in x for x in e)))
    shutil.rmtree(d)

    d = scratch(); os.makedirs(os.path.join(d, "hard-cases"), exist_ok=True)
    for n in ("01", "02", "03"):
        open(os.path.join(d, "hard-cases", f"{n}-planted.md"), "w").write("# planted\n\n## Pair 1\n")
    rd = os.path.join(d, "README.md"); s = open(rd).read()
    s = setrow(s, "Hard cases filed · dissolved · standing", "3 · 0 · 3")
    s = setrow(s, "Pairs inside standing hard cases", "3")
    open(rd, "w").write(s)
    results.append(("three standing hard cases with no FIRED banner are caught",
                    any("STOPPING RULE FIRED" in x for x in check(d, allow_unstamped=True))))
    shutil.rmtree(d)

    d = scratch(); os.makedirs(os.path.join(d, "hard-cases"), exist_ok=True)
    for n in ("01", "02"):
        open(os.path.join(d, "hard-cases", f"{n}-planted.md"), "w").write("# planted\n\n## Pair 1\n")
    open(os.path.join(d, "hard-cases", "03-declared-planted.md"), "w").write("# planted\n\n## The pair\n")
    rd = os.path.join(d, "README.md"); s2 = open(rd).read()
    s2 = setrow(s2, "Hard cases filed · dissolved · standing", "2 · 0 · 2")
    s2 = setrow(s2, "Pairs inside standing hard cases", "2")
    s2 = setrow(s2, "Declared pairs (not hard cases, not counted)", str(counts(d)["declared"]))
    open(rd, "w").write(s2)
    results.append(("a declared trade is never counted toward the stopping rule",
                    check(d, allow_unstamped=True) == []))
    shutil.rmtree(d)


    d = scratch(); os.makedirs(os.path.join(d, "hard-cases"), exist_ok=True)
    open(os.path.join(d, "hard-cases", "01-planted.md"), "w").write("# planted\n\n## Pair 1\n\n## Pair 2\n")
    rd = os.path.join(d, "README.md"); s3 = setrow(open(rd).read(), "Hard cases filed · dissolved · standing", "1 · 0 · 1")
    s3 = setrow(s3, "Pairs inside standing hard cases", "1")
    open(rd, "w").write(s3)
    e = check(d, allow_unstamped=True)
    results.append(("one root holding two pairs, undercounted as one pair, is caught",
                    any("standing_pairs" in x for x in e) and not any("README says hard" in x for x in e)))
    shutil.rmtree(d)

    d = scratch(); os.makedirs(os.path.join(d, "hard-cases"), exist_ok=True)
    open(os.path.join(d, "hard-cases", "01-planted.md"), "w").write("# planted, no pair heading\n")
    results.append(("a hard case that lists no pair is caught",
                    any("LISTS NO PAIR" in x for x in check(d, allow_unstamped=True))))
    shutil.rmtree(d)

    d = scratch(); os.makedirs(os.path.join(d, "hard-cases"), exist_ok=True)
    for n in ("01", "02"):
        open(os.path.join(d, "hard-cases", f"{n}-planted.md"), "w").write("# planted\n\n## Pair 1\n")
    rd = os.path.join(d, "README.md"); s4 = setrow(open(rd).read(), "Hard cases filed · dissolved · standing", "2 · 0 · 2")
    s4 = setrow(s4, "Pairs inside standing hard cases", "2")
    s4 = setrow(s4, "Contested groupings counted apart", "1")
    open(rd, "w").write(s4)
    results.append(("two standing + one contested grouping counted apart, with no FIRED banner, is caught",
                    any("STOPPING RULE FIRED" in x for x in check(d, allow_unstamped=True))))
    shutil.rmtree(d)

    d = scratch()
    rd = os.path.join(d, "README.md"); s5 = open(rd).read()
    s5 = s5.replace("## Pairs open\n", "## Pairs open\n\n- 2026-10-16 — a planted pair, not counted in the table\n", 1)
    open(rd, "w").write(s5)
    results.append(("an open pair listed but not counted is caught", any("README says open" in x for x in check(d))))
    shutil.rmtree(d)

    d = scratch(); os.makedirs(os.path.join(d, "hard-cases"), exist_ok=True)
    open(os.path.join(d, "hard-cases", "01-planted.md"), "w").write("# planted\n\n## Pair 1\n")
    open(os.path.join(d, "hard-cases", "02-dissolved-planted.md"), "w").write("# planted\n")
    results.append(("a dissolution that does not name its case is caught",
                    any("MUST NAME ITS CASE" in x for x in check(d, allow_unstamped=True))))
    shutil.rmtree(d)

    for name, ok in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    return all(ok for _, ok in results) and len(results) == 11


def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    args = sys.argv[1:]
    if args == ["--list"]:
        print("\n".join(frozen_files(root))); return 0
    if args == ["--unstamped"]:
        print("\n".join(p for p in frozen_files(root) if not os.path.isfile(os.path.join(root, p + ".ots")))); return 0
    if args == ["--self-test"]:
        ok = self_test(root)
        print("self-test:", "PASS" if ok else "FAIL"); return 0 if ok else 1
    if args:
        print(__doc__); return 2
    errs = check(root)
    for e in errs:
        print("⛔", e)
    c = counts(root)
    print(f"{len(frozen_files(root))} frozen file(s) · {c['pre']} pre-registered · {c['run']} run · hard cases "
          f"{c['filed']} filed, {c['dissolved']} dissolved, {c['standing']} standing ({c['standing_pairs']} pairs), {c['declared']} declared · "
          f"{c['redesigns']} redesign(s) ({c['redesign_pairs']} pairs) · "
          f"{'FAIL' if errs else 'OK'}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
