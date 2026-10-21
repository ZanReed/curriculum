"""Check a practice bank's seeded templates over EVERY valid seed combination.

Each drawn seed variable is drawn independently, so every combination a student could be served
is checked, after derived variables and `where` constraints (D43 bank format, PB-6, agreed in
C-123 / B-161, 2026-10-12):
- each {{=expr}} answer and each !expr mistake evaluates;
- answers have at most 2 decimal places and mistakes at most 3 (the prompt's exactness rule
  for bindings, tightened: a long decimal gets rounded, so the binding fires for some students
  and not others);
- a !mistake never equals its answer (it could never fire);
- every {name} used in prose or an expression is declared in the ```seed fence;
- it prints each template's answer range, for a human to judge the context is real (§11).

The seed grammar, all inside the ONE ```seed fence (PB-5, PB-6):
    a: int 2..9                     drawn
    p: list 1.50, 2.25              drawn
    k: = a * p                      derived, over EARLIER names only, evaluated in order
    where t3: mod(a, 2) == 0        template-scoped; only that template's variables
Predicates and derived expressions use the platform's seed-expression language (mathjs syntax;
B-162, BE-1): comparisons, and / or / not, ^ for powers, and mod, gcd, lcm, abs, round, floor,
ceil, min, max. round is the platform's floor(x + 1/2). This tool computes in exact Fractions,
the platform in doubles with a 1e-12 relative epsilon on comparisons; they can differ only at an
exact boundary, and the platform's valid/total count per template is the authority. Derived
variables and where are BANKS-ONLY (B-162, BE-2): lint_draft refuses them in an activity. A template
that references a derived variable also references its sources. Refused, as the importer refuses
them: an unscoped `where:` in a bank; a `where` naming an unknown heading or another template's
variable; a forward reference; a reserved name; a template with no valid combination, or more
than CAP combinations. Also checked: headings match [a-z][a-z0-9-]* and are unique; no variable
is shared by two templates (they would share a draw); the file's name matches its `skill:` (or
`<chain>.discrimination` for `role: discrimination`), and a `kind: bank` file has a status and
(for a discrimination bank) no `skill:`; no declared variable goes unused; with --retired, no item id
(<file stem>#<heading>) is in the bank ledger (PB-3: ids are never reused). Each template's
report says how many combinations its `where` lines rejected.

Moved into the repo 2026-10-10 (tools/): a unit blank ({{=n unit: cm}}) is read for its value
only, and the reserved !unit-missing / !unit-wrong segments are skipped (they are outcomes, not
expressions; the old script crashed on them).
School tier (D66, 2026-10-21; position agreed with the platform in B-197): a template may carry
`tier: D|C|P|E` as the first non-blank line under its heading, one uppercase letter. A `tier:`
line anywhere else outside a fence is refused (it would render as text). With --graph, the tag
is REQUIRED on every template of a bank whose skill (or, for a discrimination bank, any skill in
its one-line `discriminates: a, b`, no brackets: B-199) has `band_nz` Y9 or later: the school-first sequence (D55) starts at Y9,
and chain 1's ratified Y8 bank stays valid untagged.

Usage: python3 tools/check_bank.py BANK.md [--retired bank-item-ids-retired.txt] [--graph curriculum-graph.json]
"""
import itertools
import json
import math
import os
import re
import sys
from fractions import Fraction

CAP = 10000
NAME = r"[a-z][a-z0-9_]*"
HEADING = re.compile(r"[a-z][a-z0-9-]*")
TIERS = {"D", "C", "P", "E"}
TIER_FROM = {"Y9", "Y10", "Y11", "Y12", "Y13"}  # D55: the school's programme starts at Y9
# The platform's RESERVED_SEED_NAMES (packages/schema/src/seed-vars.ts), plus `where` (PB-6).
RESERVED = {
    "e", "pi", "tau", "phi", "i", "x", "y",
    "mean", "median", "mode", "min", "max", "sum", "std", "variance",
    "abs", "sqrt", "cbrt", "log", "log2", "log10", "exp",
    "sin", "cos", "tan", "asin", "acos", "atan",
    "round", "floor", "ceil", "sign", "mod", "gcd", "lcm", "pow", "random",
    "true", "false", "null", "where",
}


def _int(v):
    v = Fraction(v)
    if v.denominator != 1:
        raise ValueError(f"{float(v):g} is not a whole number")
    return int(v)


FUNCS = {
    "mod": lambda a, b: Fraction(a) % Fraction(b),
    "gcd": lambda a, b: math.gcd(_int(a), _int(b)),
    "lcm": lambda a, b: abs(_int(a) * _int(b)) // math.gcd(_int(a), _int(b)),
    "abs": abs, "min": min, "max": max,
    "round": lambda a: math.floor(Fraction(a) + Fraction(1, 2)),  # the platform's: half up, so -2.5 -> -2 (B-162)
    "floor": lambda a: math.floor(Fraction(a)),
    "ceil": lambda a: math.ceil(Fraction(a)),
    "true": True, "false": False,
}


def names_in(expr):
    return set(re.findall(rf"\b({NAME})\b", expr)) - set(FUNCS) - {"and", "or", "not"}


def seed_spec(md):
    """(drawn, derived, wheres, problems): drawn {name: values}; derived [(name, expr)] in order;
    wheres [(scope or None, predicate)]."""
    drawn, derived, wheres, problems = {}, [], [], []
    m = re.search(r"```seed\n(.*?)```", md, re.S)
    if not m:
        return drawn, derived, wheres, problems
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line:
            continue
        w = re.fullmatch(r"where(?:\s+(\S+))?\s*:\s*(.+)", line)
        if w:
            wheres.append((w.group(1), w.group(2).strip()))
            continue
        name, spec = [s.strip() for s in line.split(":", 1)]
        if name in RESERVED or not re.fullmatch(NAME, name):
            problems.append(f"seed: {name!r} is a reserved or malformed name")
            continue
        if name in drawn or any(n == name for n, _ in derived):
            problems.append(f"seed: {name} is declared twice")
        if spec.startswith("="):
            expr = spec[1:].strip()
            known = set(drawn) | {n for n, _ in derived}
            later = names_in(expr) - known
            if later:
                problems.append(f"seed: {name} = {expr} uses {', '.join(sorted(later))}, not declared above it")
            derived.append((name, expr))
        elif spec.startswith("list"):
            drawn[name] = [Fraction(v.strip()) for v in spec[4:].split(",")]
        elif spec.startswith("sample"):
            problems.append(f"seed: {name}: sample variables are refused in banks (B-162, BE-5)")
        elif spec.startswith("int"):
            a, b = spec[3:].split("..")
            drawn[name] = [Fraction(i) for i in range(int(a), int(b) + 1)]
    return drawn, derived, wheres, problems


def terminates(f, places=4):
    return (f * 10 ** places).denominator == 1


def ev(expr, env):
    expr = expr.replace("^", "**")
    return eval(expr, {"__builtins__": {}}, {**FUNCS, **env})  # noqa: S307 — our own authored expressions


def meta(md):
    m = re.search(r"```meta\n(.*?)```", md, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def tier_problems(title, sec, required):
    """D66: `tier: X` is the first non-blank line under the heading, and nowhere else outside a fence."""
    out = []
    lines = sec.splitlines()[1:]
    first = next((i for i, ln in enumerate(lines) if ln.strip()), None)
    fenced, tagged = False, False
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced or not re.match(r"\s*tier\s*:", ln):
            continue
        if i != first:
            out.append(f"{title}: a tier: line must be the first line under the heading (B-197); elsewhere it renders as text")
            continue
        value = ln.split(":", 1)[1].strip()
        if value not in TIERS:
            out.append(f"{title}: tier: {value!r} is not one of D, C, P, E (one uppercase letter, D66)")
        tagged = True
    if required and not tagged:
        out.append(f"{title}: no tier: line; a bank for a Y9-or-later skill tags every template (D66)")
    return out


def main(path, retired_path=None, graph_path=None):
    md = open(path, encoding="utf-8").read()
    drawn, derived, wheres, problems = seed_spec(md)
    dsrc = {}  # derived name -> every drawn and derived name it rests on
    for n, expr in derived:
        dsrc[n] = set()
        for s in names_in(expr):
            dsrc[n] |= {s} | dsrc.get(s, set())
    declared = set(drawn) | set(dsrc)

    info = meta(md)
    stem = os.path.basename(path)[:-3] if path.endswith(".md") else os.path.basename(path)
    if info.get("role", info.get("x_role")) == "discrimination":
        item_stem = f"{info.get('chain', info.get('x_chain', ''))}.discrimination"
    else:
        item_stem = info.get("skill", "")
    if info.get("kind") == "bank":
        if stem != item_stem:
            problems.append(f"file name {stem}.md: a bank file is named {item_stem}.md (PB-1)")
        if info.get("status") not in ("draft", "ratified"):
            problems.append("status: draft or status: ratified is required in a bank (PB-10, B-163)")
        if info.get("role") == "discrimination" and "skill" in info:
            problems.append("a discrimination bank has no skill: line (PB-7)")
    retired = set()
    if retired_path:
        for line in open(retired_path, encoding="utf-8"):
            # Ids hold a '#', so a comment is a whole line starting with '#', or text after the id.
            if line.strip() and not line.lstrip().startswith("#"):
                retired.add(line.split()[0])

    sections = re.split(r"^## ", md, flags=re.M)[1:]
    headings = [sec.splitlines()[0].strip() for sec in sections]
    for h in headings:
        if not HEADING.fullmatch(h):
            problems.append(f"heading {h!r} does not match [a-z][a-z0-9-]* (PB-3)")
        if f"{item_stem}#{h}" in retired:
            problems.append(f"{item_stem}#{h} is retired in {retired_path}; bank item ids are never reused")
    for h in {h for h in headings if headings.count(h) > 1}:
        problems.append(f"heading {h} is used twice (PB-3)")
    if re.search(r"[\[\]]", info.get("discriminates", "")):
        problems.append("discriminates: is written `a, b` on one line, without brackets (B-199: the importer splits on commas)")
    tier_required = False
    if graph_path:
        bands = {s["id"]: s.get("band_nz") for s in json.load(open(graph_path, encoding="utf-8"))["skills"]}
        covered = [info.get("skill", "")] if info.get("skill") else \
            [s.strip() for s in info.get("discriminates", "").split(",") if s.strip()]
        tier_required = any(bands.get(s) in TIER_FROM for s in covered)
    for sec, h in zip(sections, headings):
        problems += tier_problems(h, sec, tier_required)
    for scope, pred in wheres:
        if scope is None:
            problems.append(f"where: {pred}: an unscoped where is refused in a bank; write `where <heading>:` (PB-6)")
        elif scope not in headings:
            problems.append(f"where {scope}: no template has the heading {scope}")

    owner = {}
    for sec in sections:
        title = sec.splitlines()[0].strip()
        body = re.sub(r"```(mc|graph)\n.*?```", "", sec, flags=re.S)
        used = set(re.findall(r"(?<!\{)\{([a-z][a-z0-9_]*)\}(?!\})", body))
        blanks = re.findall(r"\{\{=(.*?)\}\}", body)
        # Blank bodies are literal on the platform since 694584ec (B-170), so any number of bare *
        # is fine; an escaped \* still imports as a plain *.
        blanks = [b.replace("\\*", "*") for b in blanks]
        names = set()
        for b in blanks:
            names |= names_in(b.split("|")[0].split(" unit:")[0].split("+-")[0])
            for p in b.split("|")[1:]:
                if p.strip().startswith("!") and not p.strip().startswith("!unit-"):
                    names |= names_in(p.strip()[1:].split("::")[0])
        for n in used:
            if n not in declared:
                problems.append(f"{title}: {{{n}}} is not declared in the seed fence")
        refs = (used | names) & declared
        for n in list(refs):
            refs |= dsrc.get(n, set())
        for n in refs:
            if n in owner and owner[n] != title:
                problems.append(f"{n} is used by both {owner[n]} and {title}, so they would share a draw (PB-5)")
            owner.setdefault(n, title)
        preds = [p for s, p in wheres if s == title]
        for p in list(preds):
            stray = names_in(p) - refs
            if stray:
                problems.append(f"where {title}: {p} uses {', '.join(sorted(stray))}, which {title} does not reference (PB-6)")
                preds.remove(p)
        vs = sorted(refs & set(drawn))
        if not vs:
            continue
        n = 1
        for v in vs:
            n *= len(drawn[v])
        if n > CAP:
            problems.append(f"{title}: {n} combinations, over the cap of {CAP}")
            continue
        lo, hi, valid = None, None, 0
        for combo in itertools.product(*(drawn[v] for v in vs)):
            env = dict(zip(vs, combo))
            try:
                for d, expr in derived:
                    if d in refs:
                        env[d] = Fraction(ev(expr, env))
                if not all(ev(p, env) for p in preds):
                    continue
            except Exception as e:  # noqa: BLE001
                problems.append(f"{title}: at {env}: {e}")
                break
            valid += 1
            for b in blanks:
                parts = [p.strip() for p in b.split("|")]
                ans_expr = parts[0].split(" unit:")[0].split("+-")[0].strip()
                tol = "+-" in parts[0]
                try:
                    ans = Fraction(ev(ans_expr, env))
                except Exception as e:  # noqa: BLE001
                    problems.append(f"{title}: {ans_expr}: {e}")
                    continue
                if not tol and not terminates(ans, 2):
                    problems.append(f"{title}: answer {ans_expr} = {float(ans):.5f} at {env} has more than 2 decimal places")
                if ans_expr != "0":
                    lo = ans if lo is None else min(lo, ans)
                    hi = ans if hi is None else max(hi, ans)
                for p in parts[1:]:
                    if p.startswith("!") and not p.startswith("!unit-"):
                        mexpr = p[1:].split("::")[0].strip()
                        if re.fullmatch(r"[\w.+\-*/^() ]+", mexpr) and re.search(r"[a-z]", mexpr):
                            mis = Fraction(ev(mexpr, env))
                            if mis == ans:
                                problems.append(f"{title}: mistake {mexpr} equals the answer at {env}")
                            if not terminates(mis, 3):
                                problems.append(f"{title}: mistake {mexpr} = {float(mis):.5f} at {env} has more than 3 decimal places, so a student would round it and the binding would miss")
        if valid == 0:
            problems.append(f"{title}: no valid combination ({n} drawn, all rejected by where)")
        elif lo is not None:
            kept = f", {n - valid} rejected by where ({(n - valid) / n:.0%})" if preds else ""
            print(f"{title}: {valid} of {n} combinations{kept}, answers {float(lo):g} to {float(hi):g}")
    for name in sorted(declared - set(owner)):
        problems.append(f"seed: {name} is declared and no template uses it")
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"{path}: {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    retired = graph = None
    if "--retired" in args:
        i = args.index("--retired")
        retired = args[i + 1]
        del args[i:i + 2]
    if "--graph" in args:
        i = args.index("--graph")
        graph = args[i + 1]
        del args[i:i + 2]
    sys.exit(main(args[0], retired, graph))
