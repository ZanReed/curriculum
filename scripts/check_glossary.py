#!/usr/bin/env python3
"""Glossary check (D40): gates glossary.md, the course glossary file.

    python3 scripts/check_glossary.py glossary.md --retired glossary-retired.txt [--base <git-ref>]

What it checks, and nothing more (the platform's importer is the separate gate
that every [[term]] in an activity resolves; activity files are not in this repo):

  well-formed   every entry sits in a ```definitions fence and opens with
                `id:`, then `term:`, then at most one `us:`, in that order and
                lower case. No other header key (v1's variant set is closed: {us}).
                An id is `gloss.` plus lower-case letters, digits and hyphens.
                Every entry has a definition body.
  unique        ids are unique. Terms and `us:` variants are unique across
                the whole file, compared the way the platform compares them:
                case-, accent- and whitespace-folded.
  bodies        NZ-only: no body contains any entry's `us:` word. No `[[`
                (cross-links are the platform's), no `{{` and no `\\gap`
                (no answer gaps). Terms use plain hyphens, so an activity's
                `[[point-gradient form]]` matches.
  caps          at most 2,000 entries. Each body's source is at most 8 KB and
                all bodies together at most 512 KB: half the platform's
                16 KB / 1 MB, which it measures on the parsed JSON, a larger
                number than the source.
  retirement    no current id is listed in the retired ledger. With --base,
                every id at the base that is gone now must be in the ledger
                (retire, never rename), and the ledger only grows. An id
                whose term changed is printed as a note: a spelling fix is
                allowed, but a change of meaning needs a new id.

Exit 0 when clean, 1 on any failure. A --base that git cannot resolve is a
failure, not a skip: a skipped check reads as a passed one.
"""

import argparse
import re
import subprocess
import sys
import unicodedata

ID_RE = re.compile(r"^gloss\.[a-z0-9][a-z0-9-]*$")
ID_MAX = 120
# The platform's header grammar (markdownToTiptap.ts GLOSSARY_HEADER), verbatim:
# a body line that matches this would be read as a header.
HEADER_RE = re.compile(r"^\s*(id|term|[a-z]{2})\s*:\s*(.*)$", re.IGNORECASE)
SEP_RE = re.compile(r"^\s*---\s*$")
LOCALES = ("us",)
MAX_ENTRIES = 2000
MAX_BODY_BYTES = 8 * 1024
MAX_TOTAL_BYTES = 512 * 1024
DASHES = "‐‑‒–—―−"


def fold(text):
    """The platform's termKey: lower case, NFKD, marks stripped, whitespace collapsed."""
    out = []
    for ch in text:
        f = unicodedata.normalize("NFKD", ch.lower())
        out.append("".join(c for c in f if not unicodedata.category(c).startswith("M")))
    return re.sub(r"\s+", " ", "".join(out).strip())


def parse(text):
    """Return (entries, problems). Each entry: dict(line, id, term, us, headers, body)."""
    entries, problems = [], []
    lines = text.split("\n")
    i, fences = 0, 0
    while i < len(lines):
        if lines[i].strip() != "```definitions":
            if lines[i].lstrip().startswith("```definitions"):
                problems.append(f"{i + 1}: fence opener must be exactly ```definitions")
            i += 1
            continue
        fences += 1
        start = i + 1
        j = start
        while j < len(lines) and lines[j].strip() != "```":
            j += 1
        if j == len(lines):
            problems.append(f"{i + 1}: ```definitions fence never closes")
        chunk, chunk_start = [], start
        for k in range(start, j):
            if SEP_RE.match(lines[k]):
                entries.append(read_entry(chunk, chunk_start, problems))
                chunk, chunk_start = [], k + 1
            else:
                chunk.append(lines[k])
        entries.append(read_entry(chunk, chunk_start, problems))
        i = j + 1
    if fences == 0:
        problems.append("1: no ```definitions fence, so no entries")
    return [e for e in entries if e is not None], problems


def read_entry(chunk, start, problems):
    lead = next((n for n, l in enumerate(chunk) if l.strip()), None)
    if lead is None:
        problems.append(f"{start + 1}: empty entry (two --- in a row, or a --- at a fence edge)")
        return None
    headers, n = [], lead
    while n < len(chunk):
        m = HEADER_RE.match(chunk[n])
        if not m:
            break
        headers.append((m.group(1), m.group(2).strip(), start + n + 1, chunk[n]))
        n += 1
    body = "\n".join(chunk[n:]).strip()
    return {"line": start + lead + 1, "headers": headers, "body": body}


def check_entry(e, problems):
    keys = [h[0] for h in e["headers"]]
    where = e["line"]
    for key, _, line, raw in e["headers"]:
        if key != key.lower() or raw != raw.strip() or not re.match(r"^[a-z]+: ", raw):
            problems.append(f"{line}: header must be written `{key.lower()}: <value>`, lower case, no indent")
    low = [k.lower() for k in keys]
    if low[:2] != ["id", "term"]:
        problems.append(f"{where}: an entry must open with `id:` then `term:` (found {low[:2]})")
    extra = low[2:]
    for k in extra:
        if k not in LOCALES:
            problems.append(f"{where}: unknown header key `{k}:` — v1 knows only us: (a new locale is a "
                            f"format change, D40); if this is body text, reword its first word")
    if len(extra) != len(set(extra)):
        problems.append(f"{where}: a variant key appears twice")
    vals = {k.lower(): v for k, v, _, _ in reversed(e["headers"])}
    e["id"], e["term"], e["us"] = vals.get("id", ""), vals.get("term", ""), vals.get("us")
    if not ID_RE.match(e["id"]) or len(e["id"]) > ID_MAX:
        problems.append(f"{where}: id `{e['id']}` must be `gloss.` + lower-case letters, digits, hyphens")
    for label, v in (("term", e["term"]), ("us", e["us"])):
        if v is None:
            continue
        if not v:
            problems.append(f"{where}: empty `{label}:`")
        if any(d in v for d in DASHES):
            problems.append(f"{where}: `{label}: {v}` uses a typographic dash; use a plain hyphen")
        if "[[" in v or "]]" in v or "::" in v:
            problems.append(f"{where}: `{label}: {v}` holds [[, ]] or ::")
    if e["us"] is not None and fold(e["us"]) == fold(e["term"]):
        problems.append(f"{where}: `us:` is the same word as the term — drop the line")
    if not e["body"]:
        problems.append(f"{where}: {e['id']} has no definition body")
    for bad, why in (("[[", "no [[…]] in a definition (cross-links are computed platform-side)"),
                     ("{{", "no {{…}} in a definition"),
                     ("\\gap", "no answer gap in a definition")):
        if bad in e["body"]:
            problems.append(f"{where}: {e['id']} — {why}")
    size = len(e["body"].encode("utf-8"))
    if size > MAX_BODY_BYTES:
        problems.append(f"{where}: {e['id']} body is {size} bytes, over {MAX_BODY_BYTES}")
    return size


def git_show(ref, path):
    r = subprocess.run(["git", "cat-file", "-e", f"{ref}^{{commit}}"], capture_output=True)
    if r.returncode != 0:
        return None, False
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    return (r.stdout if r.returncode == 0 else ""), True


def ledger_ids(text):
    ids = []
    for n, raw in enumerate(text.split("\n"), 1):
        s = raw.split("#", 1)[0].strip()
        if s:
            ids.append((s, n))
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("glossary")
    ap.add_argument("--retired", required=True)
    ap.add_argument("--base", help="git ref to compare against (retire-not-rename)")
    a = ap.parse_args()

    text = open(a.glossary, encoding="utf-8").read()
    retired_text = open(a.retired, encoding="utf-8").read()
    entries, problems = parse(text)

    total = sum(check_entry(e, problems) for e in entries)
    if len(entries) > MAX_ENTRIES:
        problems.append(f"{len(entries)} entries, over {MAX_ENTRIES}")
    if total > MAX_TOTAL_BYTES:
        problems.append(f"bodies total {total} bytes, over {MAX_TOTAL_BYTES}")

    ids, names = {}, {}
    for e in entries:
        if e["id"] in ids:
            problems.append(f"{e['line']}: duplicate id {e['id']} (first at line {ids[e['id']]})")
        ids.setdefault(e["id"], e["line"])
        for label in ("term", "us"):
            v = e.get(label)
            if not v:
                continue
            k = fold(v)
            if k in names:
                problems.append(f"{e['line']}: {label} `{v}` is already a name of {names[k]}")
            names.setdefault(k, e["id"])

    us_words = {e["us"]: e["id"] for e in entries if e.get("us")}
    for e in entries:
        for word, owner in us_words.items():
            if re.search(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", e["body"], re.IGNORECASE):
                problems.append(f"{e['line']}: {e['id']} body uses the US word `{word}` "
                                f"({owner}'s us: variant); definitions are NZ-only")

    retired = ledger_ids(retired_text)
    seen = {}
    for rid, n in retired:
        if not ID_RE.match(rid):
            problems.append(f"{a.retired}:{n}: `{rid}` is not a glossary id")
        if rid in seen:
            problems.append(f"{a.retired}:{n}: {rid} listed twice")
        seen.setdefault(rid, n)
        if rid in ids:
            problems.append(f"{a.retired}:{n}: {rid} is retired but back in {a.glossary} — ids are never reused")

    notes = []
    if a.base:
        base_gloss, ok = git_show(a.base, a.glossary)
        if not ok:
            problems.append(f"--base {a.base} is not a commit git can resolve (a force-push, or a "
                            f"shallow checkout?) — retirement cannot be checked, so this fails")
        else:
            base_ret, _ = git_show(a.base, a.retired)
            base_entries, _ = parse(base_gloss) if base_gloss else ([], [])
            for be in base_entries:
                be_vals = {k.lower(): v for k, v, _, _ in reversed(be["headers"])}
                bid, bterm = be_vals.get("id", ""), be_vals.get("term", "")
                if not bid:
                    continue
                if bid not in ids and bid not in seen:
                    problems.append(f"{bid} (term `{bterm}`) was removed without retiring it — add it "
                                    f"to {a.retired}; an id is never renamed or dropped silently")
                cur = next((e for e in entries if e["id"] == bid), None)
                if cur and fold(cur["term"]) != fold(bterm):
                    notes.append(f"note: {bid} term `{bterm}` → `{cur['term']}` — fine for a spelling "
                                 f"fix; a change of meaning must retire {bid} and mint a new id")
            now_ret = {rid for rid, _ in retired}
            for rid, _ in ledger_ids(base_ret or ""):
                if rid not in now_ret:
                    problems.append(f"{a.retired}: {rid} was removed from the ledger — it is append-only")
            if not base_gloss:
                notes.append(f"note: no {a.glossary} at {a.base}; nothing to compare for retirement")

    for n in notes:
        print(n)
    variants = sum(1 for e in entries if e.get("us"))
    if problems:
        for p in problems:
            print(f"FAIL {a.glossary}:{p}" if p[:1].isdigit() else f"FAIL {p}")
        print(f"glossary check: {len(problems)} problem(s)")
        return 1
    print(f"glossary check: OK — {len(entries)} entries, {variants} us: variants, "
          f"{len(retired)} retired, {total} body bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
