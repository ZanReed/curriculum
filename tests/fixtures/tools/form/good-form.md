```meta
key: act.fixture.form
minutes: 25
skill: algebra.factorise.common-factor
title: Fixture — form blanks (D60)
dol_skills: algebra.factorise.common-factor, algebra.expressions.like-terms
```

```seed
s: int 2..5
```

A lesson line uses {s}.

Factorise $18x - 12$ fully, as a number times a bracket: {{===6(3x-2) | !2(9x-6) :: Take out the highest common factor. :: mis.factorise.not-highest | !form-wrong :: Equal, but write it as one number times a bracket.}}

Write the product as a single fraction: $\frac{2}{3} \times x = \gap[form]{\frac{2x}{3}}$

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
