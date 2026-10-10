```meta
key: act.geom.rotate
skill: geom.transform.rotate
title: Rotations — Turning a Shape About a Point
course: Year 7 Mathematics
tags: rotation, centre of rotation, clockwise, anticlockwise, image, transformation
role: lesson
type: worksheet
submission: free
feedback: on_check
calculator: off
x_review_skills: geom.transform.reflect
x_dol_skills: geom.transform.rotate, ext.arith.whole-ops
```

# Rotations — Turning a Shape About a Point

```objectives
title: Today's goals
Rotate a shape by a half turn about a given centre
Rotate a shape by a quarter turn, clockwise or anticlockwise
Use the centre you are given, wherever it is
```

## Review

From memory: one quick reflection.

The point (−1, 4) is reflected in the mirror line x = 2. Its image is at ({{=5 | !1 :: That reflects the point in the y-axis, x = 0. The mirror line is x = 2: (−1, 4) is 3 squares to the left of it, so the image is 3 squares to the right, at x = 5.}}, {{=4}}).

## Lesson {checkpoint}

A [[rotation]] is a [[transformation]] that turns a shape about a fixed point, the [[centre of rotation]]. Every point turns through the same angle in the same direction: [[clockwise]], the way a clock's hands go, or [[anticlockwise]]. Where the centre is decides where the [[image]] lands.

Here is the method. From the centre, describe the path to a corner: so many squares right or left, then so many up or down. Turn that path, then follow the turned path from the centre.

@@FENCE a3-w1@@

```worked
title: Rotate triangle ABC a half turn (180°) about P
P is at (1, 0). From P to A is 1 right and 1 up.
A half turn points every path the opposite way: right becomes left, and up becomes down. So the turned path is 1 left and 1 down.
Follow it from P: A′ is at (1 − 1, 0 − 1), which is (0, −1).
From P to B is 3 right and 1 up. Turned: 3 left and 1 down, so B′ is at (−2, −1).
From P to C is 1 right and 2 up. Turned: 1 left and 2 down, so C′ is at (0, −2).
The dashed lines show it: P to A and P to A′ are the same length, pointing opposite ways.
The shaded triangle is the same half turn about corner B instead of P. B stays where it is, and the triangle lands to the right of B, nowhere near A′B′C′. A different centre puts the image in a different place.
```

Now the same triangle and centre, with a quarter turn.

@@FENCE a3-w2@@

```worked
title: Rotate triangle ABC a quarter turn (90°) clockwise about P
A quarter turn clockwise turns each direction one step round the clock: right becomes down, down becomes left, left becomes up, and up becomes right.
From P to A is 1 right and 1 up. Turned: 1 down and 1 right. From P at (1, 0), that is A′ at (2, −1).
From P to B is 3 right and 1 up. Turned: 3 down and 1 right, so B′ is at (2, −3).
From P to C is 1 right and 2 up. Turned: 1 down and 2 right, so C′ is at (3, −1).
The dashed lines from P to A and from P to A′ make a right angle: the path has turned a quarter turn.
```

The last example keeps the triangle and the centre, and turns the other way.

@@FENCE a3-w3@@

```worked
title: Rotate triangle ABC a quarter turn (90°) anticlockwise about P
Anticlockwise turns each direction the other way round: right becomes up, up becomes left, left becomes down, and down becomes right.
From P to A is 1 right and 1 up. Turned: 1 up and 1 left. From P at (1, 0), that is A′ at (0, 1).
From P to B is 3 right and 1 up. Turned: 3 up and 1 left, so B′ is at (0, 3).
From P to C is 1 right and 2 up. Turned: 1 up and 2 left, so C′ is at (−1, 1).
A quarter turn anticlockwise ends in the same place as three quarter turns clockwise. So a rotation of 270° clockwise is done this way too.
```

```callout
variant: note
Always start from the centre you are given. Half turn: every direction reverses. Quarter turn clockwise: right → down → left → up → right. Quarter turn anticlockwise, or 270° clockwise: right → up → left → down → right.
```

Now you finish the last steps.

@@FENCE a3-f1@@

```faded
title: Rotate triangle KLM a half turn about P
P is at (1, 1). From P to K at (2, 3) is 1 right and 2 up. Reversed, that is 1 left and 2 down, so K′ is at (0, −1).
From P to L at (4, 3) is 3 right and 2 up. Reversed: 3 left and 2 down, so L′ is at ({{=-2 | !-4 :: That turns L about the origin, (0, 0). Start from P at (1, 1): 3 left of P is x = −2. :: mis.rotate.centre-ignored}}, {{=-1}}).
From P to M at (2, 5) is 1 right and 4 up. So M′ is at ({{=0}}, {{=-3}}).
```

A quarter turn clockwise. You do more of it.

@@FENCE a3-f2@@

```faded
title: Rotate triangle TUV a quarter turn clockwise about P
P is at (−1, 0). From P to T at (0, 1) is 1 right and 1 up. Turned clockwise: 1 down and 1 right, so T′ is at (0, −1).
From P to U at (2, 1) is 3 right and 1 up. Turned clockwise: 3 {{down}} and 1 {{right}}.
So U′ is at ({{=0 | !1 :: That turns U about the origin, (0, 0). Start from P at (−1, 0): 1 right of P is x = 0. :: mis.rotate.centre-ignored}}, {{=-3}}).
V is at (0, 3), so V′ is at ({{=2}}, {{=-1}}).
```

A rotation of 270° clockwise. You do almost all of it.

@@FENCE a3-f3@@

```faded
title: Rotate triangle GHJ 270° clockwise about P
270° clockwise ends in the same place as a quarter turn anticlockwise.
G is at (−3, 1), so G′ is at ({{=-3 | !-1 :: That turns G about the origin, (0, 0). Start from P at (−1, −1): from P to G is 2 left and 2 up, which turns to 2 down and 2 left. :: mis.rotate.centre-ignored | !1 :: That is a quarter turn clockwise. 270° clockwise is a quarter turn anticlockwise: left becomes down, up becomes left.}}, {{=-3}}).
H is at (−3, 3), so H′ is at ({{=-5}}, {{=-3}}).
J is at (−2, 1), so J′ is at ({{=-3}}, {{=-2}}).
```

### Independent practice

```graph
axes: -6..4, -5..5
prompt: Rotate triangle DEF a half turn (180°) about P. Plot D′, E′ and F′.
alt: Triangle DEF and the centre of rotation P on a grid
show: point (1,2) "D"
show: point (3,2) "E"
show: point (1,4) "F"
show: polygon D E F
show: point (-1,1) "P"
answer: (-3,0), (-5,0), (-3,-2)
mistake: (-1,-2), (-3,-2), (-1,-4) :: That turns the triangle about the origin, (0, 0). Start from P: from P to D is 2 right and 1 up, so D′ is 2 left and 1 down from P. :: mis.rotate.centre-ignored
mistake: (1,2), (-1,2), (1,0) :: That turns the triangle about its own corner D. The centre is P: from P to D is 2 right and 1 up, so D′ is 2 left and 1 down from P. :: mis.rotate.centre-ignored
mistake: (0,-3), (0,-5), (-2,-3) :: Those points have their coordinates swapped. D′ is at (−3, 0): 3 left, then 0 up. :: mis.coord.axes-swapped
```

```graph
axes: -5..5, -5..4
prompt: Rotate triangle KLM a quarter turn (90°) clockwise about P. Plot K′, L′ and M′.
alt: Triangle KLM and the centre of rotation P on a grid
show: point (1,1) "K"
show: point (3,1) "L"
show: point (1,2) "M"
show: polygon K L M
show: point (0,-1) "P"
answer: (2,-2), (2,-4), (3,-2)
mistake: (-2,0), (-2,2), (-3,0) :: That turns anticlockwise. Clockwise turns right into down and up into right: from P to K is 1 right and 2 up, so K′ is 1 down and 2 right from P.
mistake: (1,-1), (1,-3), (2,-1) :: That turns the triangle about the origin, (0, 0). Start from P at (0, −1): from P to K is 1 right and 2 up. :: mis.rotate.centre-ignored
mistake: (-2,2), (-4,2), (-2,3) :: Those points have their coordinates swapped. K′ is at (2, −2): 2 right, then 2 down. :: mis.coord.axes-swapped
```

```graph
axes: -6..4, -4..5
prompt: Rotate triangle ABC a quarter turn (90°) anticlockwise about its corner A. Plot A′, B′ and C′.
alt: Triangle ABC on a grid
show: point (-2,1) "A"
show: point (1,1) "B"
show: point (-2,3) "C"
show: polygon A B C
answer: (-2,1), (-2,4), (-4,1)
mistake: (-1,-2), (-1,1), (-3,-2) :: That turns the triangle about the origin, (0, 0). The centre is the corner A, so A stays where it is: A′ is at (−2, 1). :: mis.rotate.centre-ignored
mistake: (-2,1), (-2,-2), (0,1) :: That turns clockwise. Anticlockwise turns right into up: from A to B is 3 right, so from A to B′ is 3 up.
```

@@FENCE a3-p5@@

```mc
prompt: Liam was asked to rotate triangle ABC a half turn about P. He drew the unlabelled triangle. What did he do wrong?
(x) He turned it about corner A instead of about P. From P to A is 3 left and 1 up, so A′ should be 3 right and 1 down from P, at (2, −1).
( ) Nothing. His triangle has been given a half turn. :: It has, but about A, not about P. A rotation must turn about the centre it gives you. :: mis.rotate.centre-ignored
( ) He turned it a quarter turn instead of a half turn. :: His triangle still has a corner at A, and from A its sides point the opposite way to ABC's: a half turn. The problem is the centre: he turned it about A, not P.
solution: A half turn about P reverses each path from P. From P at (−1, 0) to A at (−4, 1) is 3 left and 1 up, so A′ is 3 right and 1 down from P: (2, −1). Liam's triangle still has a corner at A, which shows he turned it about A.
```

```graph
axes: -4..6, -4..5
prompt: Rotate triangle STU 270° clockwise about P. Plot S′, T′ and U′.
alt: Triangle STU and the centre of rotation P on a grid
show: point (3,2) "S"
show: point (5,2) "T"
show: point (3,3) "U"
show: polygon S T U
show: point (1,1) "P"
answer: (0,3), (0,5), (-1,3)
mistake: (2,-1), (2,-3), (3,-1) :: That is a quarter turn clockwise. 270° clockwise is three quarter turns, which ends in the same place as one quarter turn anticlockwise.
mistake: (-2,3), (-2,5), (-3,3) :: That turns the triangle about the origin, (0, 0). Start from P at (1, 1): from P to S is 2 right and 1 up. :: mis.rotate.centre-ignored
```

## Check for understanding {checkpoint}

@@FENCE a3-d1@@

```mc
prompt: Kiri was asked to rotate triangle ABC a quarter turn clockwise about P. She drew A′B′C′. What is her error?
(x) She turned the triangle about the origin, (0, 0), not about P. Turning about P, A′ should be at (0, 1).
( ) There is no error. A′B′C′ has been turned a quarter turn clockwise. :: It has been turned the right amount, but about (0, 0). From P to A is 1 left and 2 up; turned clockwise, that is 1 up and 2 right, so A′ is at (0, 1). :: mis.rotate.centre-ignored
( ) She turned the triangle anticlockwise. :: Turning about (0, 0), her triangle is a clockwise quarter turn. The problem is the centre, not the direction.
solution: From P at (−2, 0) to A at (−3, 2) is 1 left and 2 up. A quarter turn clockwise turns left into up and up into right, so the path becomes 1 up and 2 right: A′ is at (0, 1). Kiri's A′ is at (2, 3), which is A turned about (0, 0).
```

8 × 27 = {{=216 | !166 :: 8 × 20 is 160, and 8 × 7 is 56, not 6. 160 + 56 = 216. | !1656 :: 8 × 20 is 160, not 1600. 160 + 56 = 216.}}

```teacher-guide
## The sequence

One idea: describe the path from the centre to each corner, turn the path, and follow it from the centre. All three examples use the same triangle and centre and change only the turn: half, quarter clockwise, quarter anticlockwise. Point out the dashed lines in each: same length from P, turned through the angle. The first also turns the triangle about corner B: a different centre, a different place. That answers the pencil hook.

## Watch for

- Turning about the origin or a corner instead of the given centre (`mis.rotate.centre-ignored`). Ask, "Where is P? Start there."
- Clockwise and anticlockwise mixed up. Have students point to the clock on the wall and say the order aloud: right, down, left, up.
- Coordinates written the wrong way round (`mis.coord.axes-swapped`).

## If time runs short

Cut practice item 5, then item 2. Keep every faded example and both check-for-understanding items.
```
