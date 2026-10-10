"""Check a practice bank's seeded templates over EVERY seed combination.

The platform draws each seed variable independently (no constraints between variables), so
every combination a student could be served is checked:
- each {{=expr}} answer and each !expr mistake evaluates;
- answers have at most 2 decimal places and mistakes at most 3 (the prompt's exactness rule
  for bindings, tightened: a long decimal gets rounded, so the binding fires for some students
  and not others);
- a !mistake never equals its answer (it could never fire);
- every {name} used in prose or an expression is declared in the ```seed fence;
- it prints each template's answer range, for a human to judge the context is real (§11).

Moved into the repo 2026-10-10 (tools/): a unit blank ({{=n unit: cm}}) is read for its value
only, and the reserved !unit-missing / !unit-wrong segments are skipped (they are outcomes, not
expressions; the old script crashed on them).

Usage: python3 tools/check_bank.py BANK.md
"""
import itertools
import re
import sys
from fractions import Fraction


def seed_vars(md):
    m = re.search(r"```seed\n(.*?)```", md, re.S)
    out = {}
    if not m:
        return out
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line:
            continue
        name, spec = [s.strip() for s in line.split(":", 1)]
        if spec.startswith("list"):
            out[name] = [Fraction(v.strip()) for v in spec[4:].split(",")]
        elif spec.startswith("int"):
            a, b = spec[3:].split("..")
            out[name] = [Fraction(i) for i in range(int(a), int(b) + 1)]
    return out


def terminates(f, places=4):
    return (f * 10 ** places).denominator == 1


def ev(expr, env):
    return eval(expr, {"__builtins__": {}}, env)  # noqa: S307 — our own authored expressions


def main(path):
    md = open(path, encoding="utf-8").read()
    seeds = seed_vars(md)
    problems = []
    sections = re.split(r"^## ", md, flags=re.M)[1:]
    for sec in sections:
        title = sec.splitlines()[0]
        body = re.sub(r"```(mc|graph)\n.*?```", "", sec, flags=re.S)
        used = set(re.findall(r"(?<!\{)\{([a-z][a-z0-9_]*)\}(?!\})", body))
        blanks = re.findall(r"\{\{=(.*?)\}\}", body)
        names = set()
        for b in blanks:
            names |= set(re.findall(r"\b([a-z][a-z0-9_]*)\b", b.split("|")[0]))
        for n in used:
            if n not in seeds:
                problems.append(f"{title}: {{{n}}} is not declared in the seed fence")
        vs = sorted((used | names) & set(seeds))
        if not vs:
            continue
        lo, hi = None, None
        for combo in itertools.product(*(seeds[v] for v in vs)):
            env = dict(zip(vs, combo))
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
                        if re.fullmatch(r"[\w.+\-*/() ]+", mexpr) and re.search(r"[a-z]", mexpr):
                            mis = Fraction(ev(mexpr, env))
                            if mis == ans:
                                problems.append(f"{title}: mistake {mexpr} equals the answer at {env}")
                            if not terminates(mis, 3):
                                problems.append(f"{title}: mistake {mexpr} = {float(mis):.5f} at {env} has more than 3 decimal places, so a student would round it and the binding would miss")
        n = 1
        for v in vs:
            n *= len(seeds[v])
        if lo is not None:
            print(f"{title}: {n} combinations, answers {float(lo):g} to {float(hi):g}")
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"{path}: {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
