```meta
kind: bank
skill: algebra.terms.multiply
title: Tier fixture — D66
status: draft
```

```seed
a: int 3..6
b: int 3..6
m: int 2..4
n: int 3..5
```

## coeff

{a}p × {b}q = {{=a*b | !a+b :: Adding the coefficients. :: mis.terms.coefficients-added}}pq

## index

tier: C

c^{m} × c^{n} = c^{{=m+n | !m*n :: Multiplying the indices. :: mis.exponent.indices-multiplied}}
