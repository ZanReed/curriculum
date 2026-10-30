"""Lint a catalogue draft against the generated authoring prompt and the curriculum registries.

Rebuilt 2026-10-07; carried to chain.measure.area-volume 2026-10-08 with two additions:
- a unit blank ({{=n unit: ...}}) is recognised, and a `!unit-wrong`/`!unit-missing` segment on a
  blank with no unit: clause is reported (it can never fire);
- a blank that carries both `!unit-wrong` and an authored match with its own unit is reported:
  reserved matches are checked first in blanks.ts, so the authored one can never fire.
Checks the activity inside the draft (from its ```meta fence to the end of its
```teacher-guide fence, or to the "---" before the notes):
- no {{blank}} inside $...$ or $$...$$ (the prompt's leak rule);
- only fences the prompt allows (now including teacher-guide);
- every [[term]] resolves to glossary.md (plus any entries in this draft's or a sibling
  glossary draft's ```definitions fence marked with id:), and no [[term :: def]] redefines a
  glossary word;
- skill:, x_* skill ids and mis.* bindings are registered, and none is retired;
- every mis.* binding is attached to a skill this activity names (skill: or x_* skill lists),
  so a binding never reports against a skill it doesn't belong to;
- a ```meta key: is present;
- no unit: key; no ^\\circ inside a figure; no student-facing "sprint".
- D65 grammar (2026-10-24, the platform's DL-4 and DL-17): `dol_skills:` ids are registered; derived seed
  values and `where` appear only in the DoL section's seed fence (the `{checkpoint dol}` heading), and
  `where` is spelled `where dol:`; a DoL item uses no activity-level seed variable; a seed reference
  inside $...$ is written \\seed{name}.
- D65 DoL shape (2026-10-30, mirrors the platform's dolImport.ts so a draft fails here first):
  `dol_skills:` starts with `skill:`; the DoL has one gradable item per `dol_skills:` entry; a
  fill-in primary item has 2–3 blanks (C-163); a seeded DoL's primary item uses a DoL seed variable
  (DE-8) and each variable group it uses has at least 2 valid rows (DE-13); a DoL seed variable
  never reuses an activity-level name (DE-6); with --banks DIR, every mis.* the DoL binds is bound
  by a ratified template of the primary skill's bank, when that bank exists (TP-8, C-167).

Moved into the repo 2026-10-10 (tools/): the allowed fences now come from the pinned platform
capability facts (the union of every capability's reached_by.fence and exempt_fences, which the
platform's CI keeps complete: B-140), not a copied list; a bank file (x_kind: bank in its meta)
is exempt from the act.* key check again (the 6 Oct rule, lost in the 7 Oct rebuild).

Usage: python3 tools/lint_draft.py DRAFT.md CURRICULUM_REPO [--banks CATALOGUE/banks] [EXTRA_GLOSSARY.md ...]
"""
import itertools
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_bank import CAP, ev, names_in, seed_spec  # noqa: E402  the bank's seed reader and evaluator

def allowed_fences(repo):
    """Fence tags the platform importer accepts, from the pinned capability facts (B-140)."""
    facts = json.loads((Path(repo) / "platform-pins" / "capability-facts.json").read_text(encoding="utf-8"))
    tags = set(facts["exempt_fences"])
    for cap in facts["capabilities"].values():
        fence = (cap.get("reached_by") or {}).get("fence")
        tags |= set(fence if isinstance(fence, list) else [fence] if fence else [])
    if not tags:
        raise SystemExit("no fence tags found in platform-pins/capability-facts.json (vacuity guard)")
    return tags


def ids(path):
    out = set()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            out.add(line.split()[0])
    return out


SEED_NAME = r"[a-z][a-z0-9_]*"


def dol_grammar(repo):
    """The D65 DoL grammar, read from the pinned capability facts (prose_facts.dol_grammar, B-214)."""
    facts = json.loads((Path(repo) / "platform-pins" / "capability-facts.json").read_text(encoding="utf-8"))
    g = (facts.get("prose_facts") or {}).get("dol_grammar")
    if not g:
        raise SystemExit("no prose_facts.dol_grammar in platform-pins/capability-facts.json (vacuity guard)")
    marker = g["heading_marker"]                       # "{checkpoint dol}"
    scope = g["where_spelling"].split()[1].rstrip(":")  # "where dol:" -> "dol"
    macro = g["math_reference"].split("{", 1)[0]       # "\\seed{name}" -> "\\seed"
    return {
        "heading": re.compile(r"^## .*" + re.escape(marker) + r"\s*$", re.M),
        "scope": scope,
        "where": g["where_spelling"],
        "macro": macro,
        "meta_keys": list(g["meta_keys"]),
    }


def dol_span(act, gram):
    """The DoL section: from its `{checkpoint dol}` heading to the next ## heading or the guide (D65, DL-1)."""
    m = gram["heading"].search(act)
    if not m:
        return None
    end = re.search(r"^## |^```teacher-guide", act[m.end():], re.M)
    return m.start(), m.end() + (end.start() if end else len(act) - m.end())


def seed_problems(act, gram):
    """D65 grammar in an activity's seed fences (DL-4, DL-17; B-162 BE-2 lifted for the DoL only).

    - Outside the DoL, a seed fence takes drawn variables only: derived values and `where` stay
      banks-only.
    - Inside the DoL, derived values are allowed, and `where dol:` is the only `where` spelling.
    - A DoL item may not use an activity-level variable: it would not redraw on a retake.
    - A seed reference inside $...$ is written \\seed{name}; a bare {name} there is not substituted
      (LaTeX reads it as a group), and \\seed{} must name a declared variable.
    """
    out = []
    span = dol_span(act, gram)
    W, M = gram["where"], gram["macro"]
    outer, inner = set(), set()
    for fm in re.finditer(r"```seed\n(.*?)```", act, re.S):
        in_dol = span is not None and span[0] <= fm.start() < span[1]
        for line in fm.group(1).splitlines():
            s = line.strip()
            if not s:
                continue
            w = re.match(r"where\b\s*(\S*?)\s*:", s)
            if w or s.startswith("where"):
                if not in_dol:
                    out.append(f"seed: {s!r}: where is allowed only in the DoL's seed fence, as `{W}` (D65, DL-4)")
                elif not w or w.group(1) != gram["scope"]:
                    out.append(f"seed: {s!r}: in an activity, where is spelled `{W}` (DL-4; C-123's unscoped form is retracted)")
                continue
            d = re.match(rf"({SEED_NAME})\s*:\s*(=?)", s)
            if not d:
                continue
            if d.group(2) and not in_dol:
                out.append(f"seed: {s!r}: derived values are allowed only in the DoL's seed fence (D65; B-162 BE-2)")
            (inner if in_dol else outer).add(d.group(1))
    if span is not None:
        dol = re.sub(r"```seed\n.*?```", "", act[span[0]:span[1]], flags=re.S)
        used = set(re.findall(rf"(?<!\{{)\{{({SEED_NAME})\}}(?!\}})", dol)) | set(re.findall(re.escape(M) + rf"\{{({SEED_NAME})\}}", dol))
        for b in re.findall(r"\{\{=(.*?)\}\}", dol):
            used |= set(re.findall(rf"\b({SEED_NAME})\b", b.split("::")[0]))
        for n in sorted((used & outer) - inner):
            out.append(f"DoL uses {n}, an activity-level seed variable, so it would not redraw on a retake (D65, DL-4)")
    declared = outer | inner
    body = re.sub(r"```(meta|teacher-guide|seed).*?```", "", act, flags=re.S).replace("\\$", "")
    for m in re.finditer(r"\$\$(.+?)\$\$|\$(.+?)\$", body, re.S):
        math = m.group(0)
        for n in re.findall(rf"(?<!{re.escape(M)})\{{({SEED_NAME})\}}", math):
            if n in declared:
                out.append(f"seed reference {{{n}}} inside maths: write {M}{{{n}}} (DL-17)")
        for n in re.findall(re.escape(M) + rf"\{{({SEED_NAME})\}}", math):
            if n not in declared:
                out.append(f"{M}{{{n}}} names no declared seed variable (DL-17)")
    return out


GRADABLE_FENCES = {"mc", "match", "correspond", "order", "numberline", "explain", "graph", "dataplot"}


def dol_items(dol):
    """The DoL's gradable items in order, as (kind, text): a fence the importer grades, or a
    paragraph or list item carrying a {{blank}} (it becomes fill_in_blank). A graph or dataplot
    with `interaction: display` is not gradable (isGradeable)."""
    out, pos = [], 0
    for f in re.finditer(r"^```([\w-]*)\n(.*?)^```", dol, re.M | re.S):
        out += [("blank", c) for c in re.split(r"\n\s*\n|\n(?=[-*] |\d+\. )", dol[pos:f.start()]) if "{{" in c]
        tag, body = f.group(1), f.group(2)
        if tag in GRADABLE_FENCES and not re.search(r"^interaction:\s*display\s*$", body, re.M):
            out.append((tag, body))
        pos = f.end()
    out += [("blank", c) for c in re.split(r"\n\s*\n|\n(?=[-*] |\d+\. )", dol[pos:]) if "{{" in c]
    return out


def seed_rows(fence):
    """{frozenset(group): valid rows} for a DoL seed fence, grouped as dolImport.ts does: a derived
    value links to its sources, a `where dol:` links every name it uses. None for a group over CAP."""
    drawn, derived, wheres, _ = seed_spec("```seed\n" + fence + "```")
    names = set(drawn) | {n for n, _ in derived}
    parent = {n: n for n in names}

    def find(n):
        while parent[n] != n:
            n = parent[n]
        return n
    links = [[d] + sorted(names_in(e) & names) for d, e in derived] + [sorted(names_in(p) & names) for _, p in wheres]
    for ln in links:
        for o in ln[1:]:
            parent[find(o)] = find(ln[0])
    groups = {}
    for n in names:
        groups.setdefault(find(n), set()).add(n)
    out = {}
    for g in groups.values():
        vs = sorted(g & set(drawn))
        total = 1
        for v in vs:
            total *= len(drawn[v])
        if total > CAP:
            out[frozenset(g)] = None
            continue
        preds = [p for _, p in wheres if names_in(p) <= g]
        valid = 0
        for combo in itertools.product(*(drawn[v] for v in vs)):
            env = dict(zip(vs, combo))
            try:
                for d, e in derived:
                    if d in g:
                        env[d] = Fraction(ev(e, env))
                if all(ev(p, env) for p in preds):
                    valid += 1
            except Exception:  # noqa: BLE001  a row the platform would also drop
                continue
        out[frozenset(g)] = valid
    return out


def bank_bindings(banks, skill):
    """mis.* ids bound in the ratified bank for `skill` under a catalogue banks/ folder, or None
    when there is no ratified bank (TP-8 is silent then: banks lag activities)."""
    for f in sorted(Path(banks).glob(f"*/{skill}.md")):
        md = f.read_text(encoding="utf-8")
        m = re.search(r"```meta\n(.*?)```", md, re.S)
        if m and re.search(r"^status:\s*ratified\s*$", m.group(1), re.M):
            return set(re.findall(r"::\s*(mis\.[\w.-]+)", md))
    return None


def dol_shape_problems(act, gram, meta, banks):
    """The D65 DoL shape rules (see the module docstring)."""
    span = dol_span(act, gram)
    if span is None:
        return []
    out = []
    dol = act[span[0]:span[1]]
    sk = re.search(r"^skill:\s*(\S+)", meta, re.M)
    ds = re.search(r"^dol_skills:\s*(.+)$", meta, re.M)
    skills = [v.strip() for v in ds.group(1).split(",")] if ds else []
    if not skills:
        out.append("DoL: the {checkpoint dol} section needs a dol_skills: line, primary skill first (DL-2)")
    elif sk and skills[0] != sk.group(1):
        out.append(f"DoL: dol_skills: starts with {skills[0]}, but skill: is {sk.group(1)} (DL-2)")
    fences = re.findall(r"```seed\n(.*?)```", dol, re.S)
    items = dol_items(re.sub(r"```seed\n.*?```", "", dol, flags=re.S))
    if skills and len(items) != len(skills):
        out.append(f"DoL: {len(items)} gradable item(s), but dol_skills: names {len(skills)}: one item per skill, in order (DL-2)")
    if not items:
        return out
    kind, primary = items[0]
    if kind == "blank" and not 2 <= primary.count("{{") <= 3:
        out.append(f"DoL: the primary item has {primary.count('{{')} blank(s); a DoL primary item has 2–3 (C-163)")
    if fences:
        dvars = {d.group(1) for f in fences for d in re.finditer(rf"^\s*({SEED_NAME})\s*:", f, re.M)} - {"where"}
        outer_fences = re.findall(r"```seed\n(.*?)```", act[:span[0]] + act[span[1]:], re.S)
        outer = {d.group(1) for f in outer_fences for d in re.finditer(rf"^\s*({SEED_NAME})\s*:", f, re.M)} - {"where"}
        for n in sorted(dvars & outer):
            out.append(f"DoL seed: {n} is also an activity-level seed variable; a DoL variable may not reuse its name (DE-6)")
        refs = set(re.findall(rf"\{{({SEED_NAME})\}}", primary))
        for b in re.findall(r"\{\{=(.*?)\}\}", primary):
            refs |= names_in(b.split("::")[0])
        rows = seed_rows(fences[0])
        used = [(g, r) for g, r in rows.items() if g & refs & dvars]
        if not used:
            out.append("DoL: the primary item uses no DoL seed variable, so a retake would re-ask the same numbers (DE-8)")
        for g, r in used:
            if r is None:
                out.append(f"DoL seed: group {sorted(g)} has over {CAP} combinations")
            elif r < 2:
                out.append(f"DoL seed: group {sorted(g)} has {r} valid row(s); a retake needs at least 2 (DE-13)")
    if banks and skills:
        bound = bank_bindings(banks, skills[0])
        if bound is not None:
            for mid in sorted(set(re.findall(r"::\s*(mis\.[\w.-]+)", dol)) - bound):
                out.append(f"DoL binds {mid}, which no ratified template of {skills[0]}'s bank binds (TP-8; --strict fails at import)")
    return out


def activity_text(md):
    start = md.find("```meta")
    if start < 0:
        return md
    g = re.search(r"^```teacher-guide\n.*?^```$", md[start:], re.M | re.S)
    if g:
        return md[start:start + g.end()]
    end = md.find("\n---\n\n## Notes", start)
    return md[start:end if end > 0 else len(md)]


def blanks(text):
    """Yield the inside of every {{...}} blank (no nesting in this grammar)."""
    for m in re.finditer(r"\{\{(.*?)\}\}", text, re.S):
        yield m.group(1)


def main(draft, repo, extra):
    repo = Path(repo)
    banks = None
    if "--banks" in extra:
        i = extra.index("--banks")
        banks, extra = extra[i + 1], extra[:i] + extra[i + 2:]
    md = Path(draft).read_text(encoding="utf-8")
    act = activity_text(md)
    problems = []

    allowed = allowed_fences(repo)
    gram = dol_grammar(repo)
    for tag in re.findall(r"^```([\w-]*)", act, re.M):
        if tag and tag not in allowed:
            problems.append(f"fence not allowed: {tag}")

    body = re.sub(r"```(meta|teacher-guide).*?```", "", act, flags=re.S).replace("\\$", "")
    for m in re.finditer(r"\$\$(.+?)\$\$|\$(.+?)\$", body, re.S):
        if "{{" in m.group(0):
            problems.append(f"blank inside maths: {m.group(0)[:60]!r}")

    for b in blanks(body):
        segs = [s.strip() for s in b.split("|")]
        head = segs[0]
        has_unit = head.startswith("=") and " unit:" in head
        reserved = [s for s in segs[1:] if s.startswith("!unit-")]
        if reserved and not has_unit:
            problems.append(f"!unit-* on a blank with no unit: clause: {b[:50]!r}")
        if any(s.startswith("!unit-wrong") for s in segs[1:]):
            for s in segs[1:]:
                if s.startswith("!") and not s.startswith("!unit-"):
                    match = s[1:].split("::")[0].strip()
                    if re.match(r"^-?[\d.,/]*\d\s*[^\d\s.,/]", match):
                        problems.append(f"authored unit match {match!r} can never fire beside !unit-wrong")
        if has_unit:
            units = head.split(" unit:", 1)[1]
            if "|" in units:
                problems.append(f"unit list runs into a segment: {b[:50]!r}")

    for fig in re.findall(r"^```figure\n(.*?)^```", act, re.M | re.S) + \
            re.findall(r"^figure:.*?\n(.*?)(?=^---$|^```)", act, re.M | re.S):
        if "\\circ" in fig:
            problems.append("^\\circ inside a figure")

    gtext = (repo / "glossary.md").read_text(encoding="utf-8")
    for e in extra:
        gtext += "\n" + Path(e).read_text(encoding="utf-8")
    gtext += "\n" + md
    terms = {t.strip().lower() for t in re.findall(r"^term:\s*(.+)$", gtext, re.M)}
    terms |= {t.strip().lower() for t in re.findall(r"^us:\s*(.+)$", gtext, re.M)}
    guide = re.search(r"```teacher-guide.*?```", act, re.S)
    student = act.replace(guide.group(0), "") if guide else act
    for ref in re.findall(r"\[\[([^\]]+)\]\]", student):
        if "::" in ref:
            if ref.split("::")[0].strip().lower() in terms:
                problems.append(f"local definition shadows a glossary word: {ref[:40]!r}")
            continue
        if ref.strip().lower() not in terms:
            problems.append(f"[[{ref}]] is not in the glossary")

    meta = re.search(r"```meta\n(.*?)```", act, re.S)
    meta = meta.group(1) if meta else ""
    is_bank = bool(re.search(r"^(x_)?kind:\s*bank\s*$", meta, re.M))
    if not is_bank and not re.search(r"^key:\s*act\.", meta, re.M):
        problems.append("no key: act.* in the meta fence")
    if not is_bank:
        problems += seed_problems(act, gram)
        problems += dol_shape_problems(act, gram, meta, banks)
    if re.search(r"^unit:", meta, re.M):
        problems.append("unit: key present (the chain registry sets it)")

    skills = ids(repo / "skill-registry.txt")
    exts = ids(repo / "external-prereq-registry.txt")
    retired = ids(repo / "skill-ids-retired.txt") | ids(repo / "external-prereq-retired.txt")
    miscs = ids(repo / "misconception-registry.txt")
    attach = {}
    for line in (repo / "misconception-attachments.txt").read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].split()
        if len(line) == 2:
            attach.setdefault(line[1], set()).add(line[0])

    named = set()
    m = re.search(r"^skill:\s*(\S+)", meta, re.M)
    if not m or m.group(1) not in skills:
        problems.append(f"skill: {m.group(1) if m else None} is not registered")
    else:
        named.add(m.group(1))
    skill_keys = "|".join(re.escape(k) for k in gram["meta_keys"] if k.endswith("skills"))
    for key, val in re.findall(rf"^(x_\w*skills|supporting_skills|{skill_keys}):\s*(.+)$", meta, re.M):
        for sid in [v.strip() for v in val.split(",")]:
            if sid in retired:
                problems.append(f"{key}: {sid} is retired")
            elif sid not in skills and sid not in exts:
                problems.append(f"{key}: {sid} is not registered")
            named.add(sid)

    for mid in sorted(set(re.findall(r"::\s*(mis\.[\w.-]+)\s*(?:\}\}|\||$)", act, re.M))):
        if mid not in miscs:
            problems.append(f"binding {mid} is not in the misconception registry")
        elif not attach.get(mid, set()) & named:
            problems.append(f"binding {mid} attaches to none of this activity's skills {sorted(named)}")

    for line in student.splitlines():
        if re.search(r"\bsprint", line, re.I) and not line.startswith("x_"):
            problems.append(f"student-facing 'sprint': {line[:60]!r}")

    for p in problems:
        print(f"{draft}: {p}")
    print(f"{draft}: {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3:]))
