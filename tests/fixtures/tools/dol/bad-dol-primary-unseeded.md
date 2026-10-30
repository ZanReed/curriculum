```meta
key: act.fixture.dol-seeded
skill: algebra.factorise.common-factor
title: Fixture — seeded DoL whose primary item uses no DoL variable (DE-8)
dol_skills: algebra.factorise.common-factor, algebra.expressions.like-terms
```

```seed
s: int 2..5
```

A lesson line uses {s}.

## Check for understanding {checkpoint dol}

```seed
c: int 5..9
r: int 2..4
d: int 2..9
k: = c - r
```

Factorise fully: $12x - 18$.

12x − 18 = {{6 | !3 :: Not the highest common factor. :: mis.factorise.not-highest}} ( {{2}} x − {{3}} )

Simplify $\seed{c}m + \seed{d}n - \seed{r}m$: {{=k}} m + {{=d}} n
