```meta
kind: bank
role: discrimination
chain: chain.algebra.manipulation
discriminates: algebra.expressions.like-terms, algebra.terms.multiply
title: Discrimination fixture — one-line list
status: draft
```

```seed
a: int 2..5
b: int 6..9
```

## collect

tier: C

{a}k + {b}k = {{=a+b | !a*b :: That multiplies; these terms are added. :: mis.like-terms.adds-to-power}}k
