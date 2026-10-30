```meta
skill: algebra.factorise.common-factor
title: Fixture bank — binds cancelled-to-zero only, so the DoL's not-highest binding is uncovered (TP-8)
kind: bank
status: ratified
```

```seed
a: int 2..5
```

## t1

Factorise $\seed{a}x + \seed{a}$: {a}({{=1 | !0 :: Taking out a whole term leaves 1, not 0. :: mis.algebra.cancelled-to-zero}} + x)
