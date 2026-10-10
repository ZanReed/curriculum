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

Moved into the repo 2026-10-10 (tools/): the allowed fences now come from the pinned platform
capability facts (the union of every capability's reached_by.fence and exempt_fences, which the
platform's CI keeps complete: B-140), not a copied list; a bank file (x_kind: bank in its meta)
is exempt from the act.* key check again (the 6 Oct rule, lost in the 7 Oct rebuild).

Usage: python3 tools/lint_draft.py DRAFT.md CURRICULUM_REPO [EXTRA_GLOSSARY.md ...]
"""
import json
import re
import sys
from pathlib import Path

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
    md = Path(draft).read_text(encoding="utf-8")
    act = activity_text(md)
    problems = []

    allowed = allowed_fences(repo)
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
    if "x_kind: bank" not in meta and not re.search(r"^key:\s*act\.", meta, re.M):
        problems.append("no key: act.* in the meta fence")
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
    for key, val in re.findall(r"^(x_\w*skills|supporting_skills):\s*(.+)$", meta, re.M):
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
