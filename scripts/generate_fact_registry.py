#!/usr/bin/env python3
"""
Generate fact-scope-registry.json from the graph's `fact_scope` key and
`activity_defaults.fact_probe` (D43 items 1, 15, 18, 25, 31; note 2026-10-03).

The graph is the only edit surface. This script re-encodes it for the platform's
importer, computes each family's fact count by expanding it (item 31: nobody types
counts by hand), and stamps a revision id that is the sha256 of the canonical JSON
body (header excluded), so the same id always means the same content (items 18, 25).

It is also a gate. It fails, and writes nothing, on any contract violation the
platform's importer would otherwise have to discover: an unknown kind, flag,
operation or placeholder; a listed fact without an id; a reused or retired id; an
answer outside item 19's characters or over 8 characters; a fraction denominator
without a name; markup in strategy text; a family in no year or in two.

Usage:
    python3 scripts/generate_fact_registry.py curriculum-graph.json [--retired fact-ids-retired.txt] [--out fact-scope-registry.json]
"""
import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction

KINDS = {"generated", "listed"}
FLAGS = {"at_least_one_negative", "exclude_plain_whole"}           # D43 note 2026-10-02 (later)
OPERATIONS = {"multiply", "divide", "square", "cube", "square_root", "cube_root",
              "fraction_to_decimal", "fraction_to_percent", "add", "subtract"}
PLACEHOLDERS = {"{a}", "{b}", "{b-fraction-name}"}                   # items 26, 18 (CR-22)
ANSWER_RE = re.compile(r"^-?\d+(\.\d+)?$")                           # item 19
ANSWER_MAX = 8                                                       # platform runner limit (CR-16..21)
MARKUP_RE = re.compile(r"[*_#<>`]")                                  # strategy text is plain (B-23)
FACT_PROBE_KEYS = ["floor_factor_k", "accuracy_threshold", "facts_met_threshold",
                   "response_ceiling_s", "min_items_per_family", "practice_window",
                   "two_part_above", "two_part_items_per_family"]          # two-part probe (D43, 2026-10-05)
GROUP_ID_RE = re.compile(r"^group\.[a-z0-9]+(-[a-z0-9]+)*$")


def fail(errors):
    for e in errors:
        print("FACT-SCOPE  " + e, file=sys.stderr)
    print(f"\n{len(errors)} problem(s). Nothing written.", file=sys.stderr)
    sys.exit(1)


def rng(spec):
    ex = set(spec.get("exclude", []))
    return [v for v in range(spec["min"], spec["max"] + 1) if v not in ex]


def fmt(n):
    """Exact answer string: integers plain, terminating decimals without trailing zeros."""
    n = Fraction(n)
    if n.denominator == 1:
        return str(n.numerator)
    d = n.denominator
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    if d != 1:
        raise ValueError(f"{n} is not a terminating decimal")
    s = format(n.numerator / n.denominator, ".10f").rstrip("0").rstrip(".")
    assert Fraction(s) == n
    return s


def expand(f):
    """Return the family's facts as (a, b, answer) on the displayed operands."""
    op, gen = f["operation"], f["generate"]
    out = []
    if op in ("fraction_to_decimal", "fraction_to_percent"):
        for x, y in gen["pairs"]:
            ans = Fraction(x, y) if op == "fraction_to_decimal" else Fraction(100 * x, y)
            if op == "fraction_to_percent" and ans.denominator != 1:
                raise ValueError(f"{x}/{y} is not a whole percentage")
            out.append((x, y, fmt(ans)))
    elif op in ("square", "cube", "square_root", "cube_root"):
        for x in rng(gen["x"]):
            p = 2 if op in ("square", "square_root") else 3
            out.append((x, None, fmt(x ** p)) if op in ("square", "cube") else (x ** p, None, fmt(x)))
    else:
        for x in rng(gen["x"]):
            for y in rng(gen["y"]):
                if op == "multiply":
                    out.append((x, y, fmt(x * y)))
                elif op == "divide":
                    out.append((x * y, x, fmt(y)))
                elif op == "add":
                    out.append((x, y, fmt(x + y)))
                elif op == "subtract":
                    out.append((x, y, fmt(x - y)))
    flags = f.get("flags", [])
    if "at_least_one_negative" in flags:
        out = [t for t in out if t[0] < 0 or (t[1] is not None and t[1] < 0)]
    if "exclude_plain_whole" in flags:
        out = [t for t in out if not (t[0] > 0 and t[1] > 0 and t[0] >= t[1])]
    seen, facts = set(), []
    for t in out:
        key = (tuple(sorted((t[0], t[1]))) if f["turnaround"] and t[1] is not None else (t[0], t[1]))
        if key not in seen:
            seen.add(key)
            facts.append(t)
    return facts


def placeholders(s):
    return set(re.findall(r"\{[^}]*\}", s))


def check_strategy(fid, st, errors):
    if st is None:
        return
    if set(st) != {"intro", "lines", "example"}:
        errors.append(f"{fid}: strategy must have exactly intro, lines, example")
        return
    texts = [st["intro"], st["example"]] + [x for l in st["lines"] for x in (l.get("label"), l.get("text"))]
    for t in texts:
        if t is not None and MARKUP_RE.search(t):
            errors.append(f"{fid}: markup character in strategy text: {t!r}")
    if not st["lines"]:
        errors.append(f"{fid}: strategy has no lines")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graph")
    ap.add_argument("--retired", default="fact-ids-retired.txt")
    ap.add_argument("--out", default="fact-scope-registry.json")
    args = ap.parse_args()

    g = json.load(open(args.graph, encoding="utf-8"))
    fs, probe = g.get("fact_scope"), g.get("activity_defaults", {}).get("fact_probe")
    errors = []
    if fs is None or probe is None:
        fail(["graph has no fact_scope or no activity_defaults.fact_probe"])
    missing = [k for k in FACT_PROBE_KEYS if k not in probe]
    if missing:
        errors.append(f"activity_defaults.fact_probe missing {missing}")

    retired = set()
    try:
        for line in open(args.retired, encoding="utf-8"):
            line = line.split("#", 1)[0].strip()
            if line:
                retired.add(line)
    except FileNotFoundError:
        fail([f"retired-ids ledger {args.retired} not found (it must exist, even if empty)"])

    names = fs.get("fraction_names", {})
    ids, families_out = set(), []
    for f in fs.get("families", []):
        fid = f.get("id", "?")
        if fid in ids:
            errors.append(f"{fid}: duplicate family id")
        ids.add(fid)
        kind = f.get("kind")
        if kind not in KINDS:
            errors.append(f"{fid}: kind must be generated or listed, got {kind!r}")
            continue
        has_gen, has_list = "generate" in f, "facts" in f
        if has_gen == has_list:
            errors.append(f"{fid}: a family needs exactly one of generate (generated) or facts (listed)")
            continue
        if (kind == "generated") != has_gen:
            errors.append(f"{fid}: kind {kind} does not match its fields")
            continue
        check_strategy(fid, f.get("strategy"), errors)
        if kind == "generated":
            if f.get("operation") not in OPERATIONS:
                errors.append(f"{fid}: unknown operation {f.get('operation')!r}")
                continue
            bad = set(f.get("flags", [])) - FLAGS
            if bad:
                errors.append(f"{fid}: unknown flag(s) {sorted(bad)} (a new flag goes to the platform first)")
            for field in ("display", "spoken"):
                ph = placeholders(f[field])
                if ph - PLACEHOLDERS:
                    errors.append(f"{fid}: {field} uses unknown placeholder(s) {sorted(ph - PLACEHOLDERS)}")
            if "__" not in f["display"]:
                errors.append(f"{fid}: display has no answer blank __")
            try:
                facts = expand(f)
            except ValueError as e:
                errors.append(f"{fid}: {e}")
                continue
            for a, b, ans in facts:
                if not ANSWER_RE.match(ans) or len(ans) > ANSWER_MAX:
                    errors.append(f"{fid}: answer {ans!r} breaks item 19 or the {ANSWER_MAX}-character limit")
                if "{b-fraction-name}" in f["spoken"] and str(b) not in names:
                    errors.append(f"{fid}: denominator {b} has no entry in fraction_names")
            count = len(facts)
        else:
            count = len(f["facts"])
            for fact in f["facts"]:
                lid = fact.get("id")
                if not lid or not lid.startswith(fid + "."):
                    errors.append(f"{fid}: listed fact {lid!r} needs an id under {fid}.")
                if lid in ids:
                    errors.append(f"{lid}: duplicate id")
                ids.add(lid)
                if "__" not in fact.get("display", ""):
                    errors.append(f"{lid}: display has no answer blank __")
                if placeholders(fact.get("display", "")) or placeholders(fact.get("spoken", "")):
                    errors.append(f"{lid}: listed facts take no placeholders")
                ans = str(fact.get("answer", ""))
                if not ANSWER_RE.match(ans) or len(ans) > ANSWER_MAX:
                    errors.append(f"{lid}: answer {ans!r} breaks item 19 or the {ANSWER_MAX}-character limit")
        out = dict(f)
        out["fact_count"] = count
        families_out.append(out)

    for rid in sorted(ids & retired):
        errors.append(f"{rid}: id is in {args.retired} and may not be reused")

    fam_ids = [f["id"] for f in fs.get("families", [])]
    placed = {}
    years = fs.get("year_scope", {})
    cumulative, cum, probe_len = {}, [], {}
    for y in sorted(years, key=int):
        for fid in years[y]["adds"]:
            if fid not in fam_ids:
                errors.append(f"year {y}: unknown family {fid}")
            if fid in placed:
                errors.append(f"{fid}: in year {placed[fid]} and year {y}")
            placed[fid] = y
            cum.append(fid)
        cumulative[y] = list(cum)
        probe_len[y] = max(30, int(probe.get("min_items_per_family", 5)) * len(cum))
    for fid in fam_ids:
        if fid not in placed:
            errors.append(f"{fid}: in no year")

    # Family groups and probe parts (D43 amendment 2026-10-05, two-part probe).
    groups = fs.get("family_groups", [])
    parts = fs.get("probe_parts", [])
    group_of, gids = {}, []
    if not groups:
        errors.append("fact_scope.family_groups is missing or empty")
    for gr in groups:
        gid = gr.get("id", "?")
        if set(gr) != {"id", "label", "families"}:
            errors.append(f"{gid}: a group has exactly id, label and families, got {sorted(gr)}")
        if not GROUP_ID_RE.match(gid):
            errors.append(f"{gid}: group id must look like group.<kebab-name>")
        if gid in gids:
            errors.append(f"{gid}: duplicate group id")
        if gid in retired:
            errors.append(f"{gid}: id is in {args.retired} and may not be reused")
        if not str(gr.get("label", "")).strip() or MARKUP_RE.search(str(gr.get("label", ""))):
            errors.append(f"{gid}: label must be plain, non-empty text")
        gids.append(gid)
        for fid in gr.get("families", []):
            if fid not in fam_ids:
                errors.append(f"{gid}: unknown family {fid}")
            elif fid in group_of:
                errors.append(f"{fid}: in {group_of[fid]} and {gid}")
            group_of[fid] = gid
    for fid in fam_ids:
        if fid not in group_of:
            errors.append(f"{fid}: in no family group")
    if not (isinstance(parts, list) and len(parts) == 2 and all(isinstance(p, list) and p for p in parts)):
        errors.append("fact_scope.probe_parts must be a list of exactly two non-empty lists of group ids")
        parts = []
    seen_g = {}
    for i, part in enumerate(parts, 1):
        for gid in part:
            if gid not in gids:
                errors.append(f"part {i}: unknown group {gid}")
            elif gid in seen_g:
                errors.append(f"{gid}: in part {seen_g[gid]} and part {i}")
            seen_g[gid] = i
    for gid in gids:
        if gid not in seen_g:
            errors.append(f"{gid}: in no probe part")

    if errors:
        fail(errors)

    # Probe sizes (items 20, 22; two-part rule): reported, not written to the body.
    count_of = {f["id"]: f["fact_count"] for f in families_out}
    part_of = {fid: seen_g[group_of[fid]] for fid in fam_ids}
    above, per = int(probe["two_part_above"]), int(probe["two_part_items_per_family"])
    for y, cum_y in cumulative.items():
        if probe_len[y] > above:
            sizes = [sum(min(per, count_of[f]) for f in cum_y if part_of[f] == k) for k in (1, 2)]
            if all(sizes):
                probe_len[y] = f"{sum(sizes)} ({sizes[0]} + {sizes[1]})"

    body = {
        "fact_probe": {k: probe[k] for k in FACT_PROBE_KEYS},
        "families": families_out,
        "year_scope": {y: {"adds": years[y]["adds"], "cumulative": cumulative[y],
                           "description": years[y].get("description")} for y in sorted(years, key=int)},
        "fraction_names": names,
        "family_groups": groups,
        "probe_parts": parts,
    }
    canonical = json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    revision = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    doc = {
        "header": {
            "generated_from": f"{args.graph} v{g.get('version')}",
            "revision": revision,
            "revision_rule": "sha256 of the canonical JSON body (sort_keys, no whitespace, UTF-8), header excluded",
            "note": "GENERATED by scripts/generate_fact_registry.py. Do not hand-edit: edit the graph's fact_scope and regenerate.",
        },
        "body": body,
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    total = sum(f["fact_count"] for f in families_out)
    print(f"{args.out}: {len(families_out)} families, {total} facts, revision {revision[:12]}")
    print("fact counts: " + ", ".join(f"{f['id']}={f['fact_count']}" for f in families_out))
    print("probe items by year: " + ", ".join(f"Y{y}={n}" for y, n in probe_len.items()))


if __name__ == "__main__":
    main()
