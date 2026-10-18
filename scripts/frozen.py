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
  3. the README's status table agrees with the files: projects pre-registered and run, hard cases filed, dissolved and
     standing (charter §5), and pairs met by a redesign (GOVERNANCE.md);
  4. the stopping rule: three or more STANDING hard cases require the README to say "FIRED" and to carry, above
     "## What is here", a line saying the core is wrong; fewer require "not fired" and no such line.

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
    names = [f for f in os.listdir(hc)] if os.path.isdir(hc) else []
    dissolved = sum(1 for f in names if re.fullmatch(r"\d\d-dissolved-.+\.md", f))
    filed = sum(1 for f in names if re.fullmatch(r"\d\d-.+\.md", f) and "-dissolved-" not in f)
    rd = os.path.join(root, "redesigns")
    redesigns = sum(1 for f in os.listdir(rd) if re.fullmatch(r"\d\d-.+\.md", f)) if os.path.isdir(rd) else 0
    return {"pre": pre, "run": run, "filed": filed, "dissolved": dissolved,
            "standing": max(filed - dissolved, 0), "redesigns": redesigns}


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
        "redesigns": row("Pairs met by a redesign on the first attempt"),
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
    _, head, t = readme_table(root)
    want = {"pre": str(c["pre"]), "run": str(c["run"]),
            "hard": f"{c['filed']} · {c['dissolved']} · {c['standing']}", "redesigns": str(c["redesigns"])}
    for k, v in want.items():
        if t[k] is None:
            errs.append(f"README status row missing: {k}")
        elif t[k] != v:
            errs.append(f"README says {k} = {t[k]!r}, the files say {v!r}")
    fired = c["standing"] >= 3
    banner = re.search(r"core is wrong", head, re.I) is not None
    if t["rule"] is None:
        errs.append("README status row missing: stopping rule")
    elif fired and (t["rule"].upper() != "FIRED" or not banner):
        errs.append(f"STOPPING RULE FIRED ({c['standing']} standing hard cases): the README must say FIRED and carry, "
                    "above '## What is here', a line saying the core is wrong")
    elif not fired and (t["rule"] != "not fired" or banner):
        errs.append(f"stopping rule not fired ({c['standing']} standing): the README must say 'not fired' and carry no "
                    "'core is wrong' line")
    return errs


def self_test(root):
    """plant each failure in a scratch copy; every plant must be caught, and the clean copy must pass"""
    results = []
    def scratch():
        d = tempfile.mkdtemp(prefix="ftgob-selftest-")
        for p in tracked(root):
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
    open(os.path.join(d, "hard-cases", "98-planted.md"), "w").write("# planted\n")
    e = check(d)
    results.append(("an unstamped frozen file is caught", any("UNSTAMPED" in x for x in e)))
    results.append(("a hard case the README does not count is caught", any("README says hard" in x for x in e)))
    shutil.rmtree(d)

    d = scratch(); os.makedirs(os.path.join(d, "hard-cases"), exist_ok=True)
    for n in ("01", "02", "03"):
        open(os.path.join(d, "hard-cases", f"{n}-planted.md"), "w").write("# planted\n")
    rd = os.path.join(d, "README.md"); s = open(rd).read()
    s = re.sub(r"(\|\s*Hard cases filed · dissolved · standing\s*\|\s*).+?(\s*\|)", r"\g<1>3 · 0 · 3\2", s)
    open(rd, "w").write(s)
    results.append(("three standing hard cases with no FIRED banner are caught",
                    any("STOPPING RULE FIRED" in x for x in check(d, allow_unstamped=True))))
    shutil.rmtree(d)

    for name, ok in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    return all(ok for _, ok in results) and len(results) == 5


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
          f"{c['filed']} filed, {c['dissolved']} dissolved, {c['standing']} standing · {c['redesigns']} redesign(s) · "
          f"{'FAIL' if errs else 'OK'}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
