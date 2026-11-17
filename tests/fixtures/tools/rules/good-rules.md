```meta
key: act.fixture.rules
minutes: 25
skill: algebra.factorise.common-factor
title: Fixture — links, hints, case (2026-11-17)
dol_skills: algebra.factorise.common-factor, algebra.expressions.like-terms
```

```seed
s: int 2..5
```

A lesson line uses {s}.

![a bar chart of rainfall](https://example.org/rain.png)

```match
hint: Which unit is smaller?
- 1 m :: 100 cm
- 1 cm :: 10 mm
```

Source: [NIWA rainfall data](https://niwa.co.nz/climate)

## Check for understanding {checkpoint dol}

```seed
g: list 4, 6, 8, 10, 12
a: int 2..7
b: int 1..7
p: = g * a
q: = g * b
h: = g / 2
where dol: gcd(a, b) == 1
c: int 5..9
r: int 2..4
d: int 2..9
k: = c - r
```

Factorise fully: $\seed{p}x - \seed{q}$.

{p}x − {q} = {{=g | !h :: Not the highest common factor. :: mis.factorise.not-highest}} ( {{=a}} x − {{=b}} )

Simplify $\seed{c}m + \seed{d}n - \seed{r}m$: {{=k}} m + {{=d}} n
