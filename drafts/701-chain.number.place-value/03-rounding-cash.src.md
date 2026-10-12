```meta
key: act.number.round-cash
skill: number.round.cash
title: Rounding — to a Place, and Cash to the Nearest 10c
course: Year 7 Mathematics
tags: round, decimal, place value, tenth, hundredth, digit
role: lesson
type: worksheet
submission: free
feedback: on_check
calculator: off
x_review_skills: number.place-value.powers-of-ten
x_dol_skills: number.round.cash, ext.arith.whole-ops
x_dol_rubric_levels: A, M, E
```

# Rounding — to a Place, and Cash to the Nearest 10c

```objectives
title: Today's goals
Round a number to the nearest whole number, tenth, hundredth, ten, hundred or thousand
Round a cash total to the nearest 10 cents
Round the total once, not each price
```

## Review

From memory.

```mc
prompt: What is $0.8 \times 10$?
(x) 8
( ) 0.80 :: 0.80 is the same number as 0.8. Times 10 moves the 8 one place left: 8 tenths become 8 ones. :: mis.place-value.append-zero
( ) 80 :: That moves the 8 two places, which is times 100.
solution: Times 10, every digit moves one place left. 8 tenths become 8 ones: 0.8 × 10 = 8.
```

## Lesson {checkpoint}

To [[round]] a number to a place, find the two numbers at that place that it sits between, and pick the nearer one. To see which is nearer, look at the next [[digit]] to the right. 0, 1, 2, 3 or 4: round down, to the smaller one. 5, 6, 7, 8 or 9: round up, to the bigger one. Everything after the place you round to is dropped.

```worked
title: Round 3.47 to the nearest tenth
The tenths place is the first place after the point. 3.47 is between 3.4 and 3.5.
The next digit to the right is the hundredths digit: 7.
7 is 5 or more, so round up. 3.47 is 3.5 to the nearest [[tenth]].
```

The same number, rounded to a different place.

```worked
title: Round 3.47 to the nearest whole number
The ones place. 3.47 is between 3 and 4.
The next digit to the right is now the tenths digit: 4.
4 is less than 5, so round down. 3.47 is 3 to the nearest whole number.
The 7 hundredths don't matter here. Only the digit straight after the place you round to decides.
```

The same steps work for any place. To round to the nearest [[hundredth]], the next digit is the third one after the point.

```worked
title: Round 3.476 to the nearest hundredth
The hundredths place is the second place after the point. 3.476 is between 3.47 and 3.48.
The next digit to the right is the third digit after the point: 6.
6 is 5 or more, so round up. 3.476 is 3.48 to the nearest hundredth.
```

Now money. New Zealand has no 1c, 2c or 5c coins, so when you pay in cash, the shop rounds your total to the nearest 10 cents. 10 cents is a tenth of a dollar, so this is rounding to the nearest tenth. Add up first, then round the total once. Paying by card, nothing is rounded. A total ending in exactly 5c is up to the shop: most round it down.

```worked
title: You pay cash for milk at \$3.36 and bread at \$2.27. What do you pay?
Add first: \$3.36 + \$2.27 = \$5.63.
Round the total to the nearest 10c. \$5.63 is between \$5.60 and \$5.70.
The next digit is 3 cents. 3 is less than 5, so round down.
You pay \$5.60.
Rounding each price first gives \$3.40 + \$2.30 = \$5.70, which is 10c too much. The shop rounds the total, not each price.
```

```callout
variant: warning
Round once, at the end: add the prices, then round the total. And round, don't just cut: \$4.97 is \$5.00, not \$4.90.
```

First, see where 5.82 sits.

```numberline
prompt: The number line goes from 5.8 to 5.9, with a tick for every hundredth. Plot 5.82.
axis: 5.8..5.9 step 0.01
answer: 5.82
solution: 5.82 is 2 hundredths past 5.8, so it is on the second tick after 5.8, and 8 ticks before 5.9.
```

Now you finish the last step.

```faded
title: Round 5.82 to the nearest tenth
5.82 is between 5.8 and 5.9. On the number line, it is 2 ticks from 5.8 and 8 ticks from 5.9.
The next digit to the right is the hundredths digit: 2.
2 is less than 5, so round down. 5.82 is {{=5.8 | !5.9 :: The hundredths digit is 2, which is less than 5, so round down to 5.8.}} to the nearest tenth.
```

You do more of this one.

```faded
title: Round 2.96 to the nearest tenth
2.96 is between 2.9 and {{=3 | !2.1 :: One tenth more than 2.9 is 3.0: 9 tenths and 1 more tenth make a whole one.}}.
The next digit to the right is {{=6}}.
So round {{up | !down :: 6 is 5 or more, so round up.}}. 2.96 is {{=3 | !2.9 :: Cutting off the 6 isn't rounding. 6 is 5 or more, so round up to 3.0. :: mis.round.truncates}} to the nearest tenth. Write it as 3.0, to show it is rounded to tenths.
```

You do almost all of this one.

```faded
title: You pay cash for a muffin at \$1.46 and a juice at \$2.36. What do you pay?
Add first. The total is \$ {{=3.82}}.
Round the total to the nearest 10c. You pay \$ {{=3.8 | !3.9 :: Rounding each price gives \$1.50 + \$2.40 = \$3.90. The shop rounds the total, \$3.82, which ends in 2c, so it rounds down. :: mis.round.cash-per-item}}.
```

### Independent practice

Round each number to the nearest tenth.

1. 7.34: {{=7.3}}

2. 0.68: {{=0.7 | !0.6 :: Cutting off the 8 isn't rounding. 8 is 5 or more, so round up. :: mis.round.truncates}}

3. 9.97: {{=10 | !9.9 :: 7 is 5 or more, so round up. One tenth more than 9.9 is 10.0. :: mis.round.truncates | !9.10 :: One tenth more than 9.9 is 10.0, not 9.10: ten tenths make a whole one.}}

Round each number to the place given.

4. 6.72 to the nearest whole number: {{=7}}

5. 437 to the nearest ten: {{=440 | !430 :: The ones digit is 7, so round up to 440.}}

6. 5.428 to the nearest hundredth: {{=5.43 | !5.42 :: Cutting off the 8 isn't rounding. 8 is 5 or more, so round up to 5.43. :: mis.round.truncates}}

7. 0.354 to the nearest hundredth: {{=0.35 | !0.36 :: The third digit after the point is 4, which is less than 5, so round down to 0.35.}}

8. 3649 to the nearest thousand: {{=4000 | !3600 :: That is the nearest hundred. To the nearest thousand, look at the hundreds digit: 6, so round up.}}

Your cash total is \$7.98. You pay \$ {{=8 | !7.9 :: Cutting off the 8 cents isn't rounding. 8 is 5 or more, so round up to \$8.00. :: mis.round.truncates}}

```mc
prompt: At the dairy you buy three things, at \$1.16, \$2.47 and \$0.99, and pay cash. What do you pay?
(x) \$4.60
( ) \$4.70 :: That rounds each price first: \$1.20 + \$2.50 + \$1.00. Add first: the total is \$4.62, which rounds down. :: mis.round.cash-per-item
( ) \$4.62 :: That's the total, but it can't be paid exactly in coins. Round it to the nearest 10c.
( ) \$5.00 :: That rounds to the nearest dollar. Cash is rounded to the nearest 10c.
solution: Add first: \$1.16 + \$2.47 + \$0.99 = \$4.62. The total ends in 2c, so it rounds down to \$4.60.
```

You pay for the same three things by card. You pay \$ {{=4.62 | !4.6 :: Card payments aren't rounded. Only cash totals are.}}

```mc
prompt: Mele's cash total is \$12.96. She says she pays \$12.90, "because you just drop the 6." What is her error?
(x) She cut off the 6 cents instead of rounding. 6 is 5 or more, so the total rounds up to \$13.00.
( ) There is no error. You always drop the cents. :: Dropping digits isn't rounding. \$12.96 is nearer \$13.00 than \$12.90. :: mis.round.truncates
( ) She should round down to \$12.00. :: Cash rounds to the nearest 10c, not the nearest dollar.
solution: \$12.96 is between \$12.90 and \$13.00. The next digit is 6, so round up: she pays \$13.00.
```

## Check for understanding {checkpoint}

```shortanswer
prompt: At the dairy, Sione buys a drink for \$2.34 and a pie for \$4.13. He pays for both together, in cash. (1) How much does he pay? Show your working. (2) His friend says that rounding each price first gives the same answer. Is she right for these prices? Show how you know. (3) Is it ever cheaper to pay for the drink and the pie separately, as two cash payments? Explain, and give an example.
starter: (1) The total is …
rubric: Finds the cash total | 1 | Adds first: \$2.34 + \$4.13 = \$6.47, and rounds to \$6.50
rubric: Judges the friend's claim | 2 | Rounds each price: \$2.30 + \$4.10 = \$6.40, which isn't \$6.50, so she is wrong; and says that in one payment only the total is rounded. 1 mark for the calculation with no conclusion
rubric: Separate payments | 2 | Yes for these prices: two payments of \$2.30 and \$4.10 cost \$6.40, 10c less, because each payment is rounded on its own. Says when this happens (each price rounds down, but the total rounds up) or that it can also cost more or the same (e.g. two prices ending in 6c to 9c). 1 mark for a correct example with no reason or condition
answer: (1) \$2.34 + \$4.13 = \$6.47. 7c rounds up, so he pays \$6.50.
(2) She is wrong. Rounding each price gives \$2.30 + \$4.10 = \$6.40, not \$6.50. In one payment the shop rounds only the total.
(3) Yes, for these prices. Paid separately, each payment is rounded: \$2.34 is \$2.30 and \$4.13 is \$4.10, so he pays \$6.40, 10c less. It is cheaper when each price rounds down but the total rounds up. It isn't always cheaper: two prices ending in 7c, such as \$1.27 and \$2.17, cost \$1.30 + \$2.20 = \$3.50 separately, but \$3.44 rounds to \$3.40 together.
solution: Add first, then round the total once: \$6.47 is \$6.50. Rounding each price gives \$6.40, so the friend is wrong. Two separate payments are each rounded, which here saves 10c, but with prices that round up it costs more.
```

$7 \times 48 =$ {{=336 | !286 :: 7 × 40 = 280 and 7 × 8 = 56. 280 + 56 = 336.}}

```teacher-guide
## The sequence

One idea: to round, find the two numbers either side at that place, and the next digit decides. The first three examples round to a tenth, a whole number, then a hundredth, so students see the deciding digit move with the place. Cash rounding is the same idea at tenths of a dollar, plus one rule: add first, then round the total once.

## Watch for

- Cutting off digits instead of rounding (4.97 to 4.90). Ask, "Which is it nearer?"
- Rounding each price before adding. Ask, "How many times does the shop round?"
- 2.96 rounded to 2.10. Ask what one more tenth after 2.9 is.

## If time runs short

Cut practice items 5 and 8, then the card item. Keep every faded example and the whole check for understanding.

## Marking

- **Finds the cash total (A):** 6.50, with the total 6.47 shown.
- **Judges the friend's claim (M):** 2 for 6.40 and "she's wrong", with the reason; 1 for the calculation alone.
- **Separate payments (E):** 2 for "yes, 6.40", why (each payment is rounded), and when it helps or costs more; 1 for the example alone.
```
