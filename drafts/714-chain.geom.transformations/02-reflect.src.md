```meta
key: act.geom.reflect
skill: geom.transform.reflect
title: Reflections — Flipping a Shape in a Mirror Line
course: Year 7 Mathematics
tags: reflection, mirror line, image, transformation, coordinates
role: lesson
type: worksheet
submission: free
feedback: on_check
calculator: off
x_review_skills: geom.transform.translate
x_dol_skills: geom.transform.reflect, number.integers.number-line
```

# Reflections — Flipping a Shape in a Mirror Line

```objectives
title: Today's goals
Reflect a shape in a vertical or horizontal mirror line, using its [[coordinates]]
Reflect a shape in a diagonal mirror line by counting straight across it
Tell a reflection from a slide by which way the image faces
```

## Review

From memory: one quick translation.

The point (2, −3) is translated 4 left and 5 up. It ends up at ({{=-2 | !2 :: That is the answer with its coordinates swapped. Across first: 2 − 4 = −2. :: mis.coord.axes-swapped | !6 :: Left takes away from x: 2 − 4 = −2.}}, {{=2 | !-8 :: Up adds to y: −3 + 5 = 2.}}).

## Lesson {checkpoint}

A [[reflection]] is a [[transformation]] that flips a shape over a [[mirror line]]. Each point of the [[image]] is on the other side of the line, the same distance from it, measured straight across. So the image faces the opposite way. That is why AMBULANCE is printed back to front: a mirror flips it the right way round again.

@@FENCE a2-w1@@

```worked
title: Reflect triangle ABC in the mirror line x = 0
Reflect one corner at a time. Count straight across from the corner to the mirror line, then the same number of squares on the other side.
A is at (−3, 1). The line x = 0 is 3 squares to the right of A, so A′ is 3 squares to the right of the line: A′ is at (3, 1).
B is at (−1, 1), 1 square from the line, so B′ is 1 square past it: (1, 1). C is at (−3, 5), 3 squares from the line, so C′ is at (3, 5).
Join A′, B′ and C′. In ABC, the right angle at A is on the left. In the image, A′ is on the right. The image faces the opposite way, which is what makes it a reflection and not a slide.
```

Now the same triangle, with a horizontal mirror line: the x-axis instead of the y-axis.

@@FENCE a2-w2@@

```worked
title: Reflect triangle ABC in the mirror line y = 0
The line is horizontal, so straight across means straight down.
A is at (−3, 1). The line y = 0 is 1 square below A, so A′ is 1 square below the line: (−3, −1).
B is at (−1, 1), also 1 square above the line, so B′ is at (−1, −1). C is at (−3, 5), 5 squares above the line, so C′ is 5 squares below it: (−3, −5).
The image is upside down: C was at the top, and C′ is at the bottom. A reflection in a horizontal line flips a shape top to bottom.
```

The last example uses a diagonal mirror line. Straight across a diagonal line is diagonal too.

@@FENCE a2-w3@@

```worked
title: Reflect triangle ABC in the mirror line y = x
The line y = x goes through (0, 0), (1, 1), (2, 2) and so on. Straight across it, at right angles, means moving diagonally: each step is 1 right and 1 down, through the corner of a square.
A is at (−3, 1). Step diagonally: (−2, 0), then (−1, −1), which is on the line. That's 2 steps. Take 2 more steps past the line: (0, −2), then (1, −3). So A′ is at (1, −3).
B is at (−1, 1). 1 step reaches (0, 0) on the line, and 1 more reaches (1, −1). So B′ is at (1, −1).
C is at (−3, 5). 4 steps reach (1, 1) on the line, and 4 more reach (5, −3). So C′ is at (5, −3).
Don't count straight right or straight down to a diagonal line. That reflects the shape in a vertical or horizontal line instead.
```

```callout
variant: note
Count straight across from each corner to the mirror line, then the same distance on the other side. For a diagonal line, count diagonal steps. The image faces the opposite way: if it faces the same way, it has been slid, not reflected.
```

Now you finish the last steps.

@@FENCE a2-f1@@

```faded
title: Reflect triangle PQR in the mirror line x = −1
P is at (1, 2). The line x = −1 is 2 squares to the left of P, so P′ is 2 squares to the left of the line: (−3, 2).
Q is at (4, 2). The line is 5 squares to the left of Q, so Q′ is at ({{=-6 | !-3 :: Q is 5 squares from the line, not 2. Count from Q: 5 squares left to the line, then 5 more. | !-1 :: That is 5 squares left of Q itself, which only reaches the line. Go 5 more past it: x = −6.}}, {{=2}}).
R is at (1, 4), so R′ is at ({{=-3}}, {{=4}}).
```

A horizontal mirror line. You do every corner.

@@FENCE a2-f2@@

```faded
title: Reflect triangle KLM in the mirror line y = 1
The line is horizontal, so count straight up from each corner to the line, then the same number past it.
K is at (−2, −1), so K′ is at ({{=-2}}, {{=3 | !1 :: (−2, 1) is on the mirror line. K is 2 squares below the line, so K′ is 2 squares above it: y = 3.}}).
L is at (1, −1), so L′ is at ({{=1}}, {{=3}}).
M is at (−2, −3), so M′ is at ({{=-2}}, {{=5}}).
```

A diagonal mirror line. The first corner is started for you.

@@FENCE a2-f3@@

```faded
title: Reflect triangle DEF in the mirror line y = x
Count diagonal steps: 1 left and 1 up each time.
D is at (3, 1). 1 step reaches (2, 2) on the line, and 1 more reaches D′. D′ is at ({{=1 | !-3 :: That reflects D in the vertical line x = 0. The mirror line is diagonal, so count diagonal steps: (2, 2), then (1, 3). :: mis.reflect.diagonal-as-vertical}}, {{=3 | !-1 :: That reflects D in the horizontal line y = 0. Count diagonal steps across y = x: (2, 2), then (1, 3). :: mis.reflect.diagonal-as-vertical}}).
E is at (5, 1), so E′ is at ({{=1}}, {{=5}}).
F is at (3, −3), so F′ is at ({{=-3}}, {{=3}}).
```

### Independent practice

```graph
axes: -7..5, -7..5
prompt: Reflect triangle ABC in the mirror line x = −1. Plot A′, B′ and C′.
alt: Triangle ABC on a grid and a vertical dashed mirror line x = −1
show: point (1,1) "A"
show: point (4,1) "B"
show: point (1,3) "C"
show: polygon A B C
show: line x = -1 dashed
answer: (-3,1), (-6,1), (-3,3)
mistake: (-6,1), (-3,1), (-6,3) :: That slides the triangle across without flipping it. In a reflection the image faces the opposite way: A is 2 squares from the line, so A′ is 2 squares past it, at (−3, 1). :: mis.reflect.translates
mistake: (1,-3), (1,-6), (3,-3) :: Those points have their coordinates swapped. A′ is at (−3, 1): 3 left, then 1 up. :: mis.coord.axes-swapped
```

```graph
axes: -6..7, -4..8
prompt: Reflect triangle DEF in the mirror line y = 2. Plot D′, E′ and F′.
alt: Triangle DEF on a grid and a horizontal dashed mirror line y = 2
show: point (-4,0) "D"
show: point (-1,0) "E"
show: point (-4,-2) "F"
show: polygon D E F
show: line y = 2 dashed
answer: (-4,4), (-1,4), (-4,6)
mistake: (-4,6), (-1,6), (-4,4) :: That slides the triangle up without flipping it. The image should be upside down: F is the lowest corner, so F′ is the highest. :: mis.reflect.translates
mistake: (4,-4), (4,-1), (6,-4) :: Those points have their coordinates swapped. D′ is at (−4, 4): 4 left, then 4 up. :: mis.coord.axes-swapped
```

```graph
axes: -6..6, -6..6
prompt: Reflect triangle PQR in the mirror line y = x. Plot P′, Q′ and R′.
alt: Triangle PQR on a grid and a diagonal dashed mirror line y = x
show: point (-5,-1) "P"
show: point (-3,-1) "Q"
show: point (-5,3) "R"
show: polygon P Q R
show: line y = x dashed
answer: (-1,-5), (-1,-3), (3,-5)
mistake: (5,-1), (3,-1), (5,3) :: That reflects the triangle in the vertical line x = 0. The mirror line is diagonal, so count diagonal steps across it: P goes to (−3, −3) on the line, then on to (−1, −5). :: mis.reflect.diagonal-as-vertical
mistake: (-5,1), (-3,1), (-5,-3) :: That reflects the triangle in the horizontal line y = 0. The mirror line is diagonal, so count diagonal steps across it: P goes to (−3, −3) on the line, then on to (−1, −5). :: mis.reflect.diagonal-as-vertical
```

@@FENCE a2-p4@@

```mc
prompt: Mere says triangle T′U′V′ is the reflection of TUV in the dashed line x = 0. Is she right?
(x) No. T′U′V′ faces the same way as TUV, so it has been slid across. A reflection would face the opposite way.
( ) Yes. T′U′V′ is on the other side of the line, so it is a reflection. :: Being on the other side isn't enough. In TUV the right angle at T is on the left; in T′U′V′ it is still on the left, so the triangle was slid, not flipped. :: mis.reflect.translates
( ) Yes, because T′U′V′ is the same size and shape as TUV. :: A slide also keeps the size and shape. Check which way it faces: T′ is still on the left, so it hasn't been flipped. :: mis.reflect.translates
solution: In a reflection the image faces the opposite way. The right angle is at T, on the left of TUV, and at T′, still on the left of T′U′V′. So T′U′V′ is a slide of TUV, not a reflection. The reflection of T in x = 0 would be at (4, 1).
```

5. The point (3, −2) is reflected in the mirror line y = 1. Its image is at ({{=3}}, {{=4 | !2 :: That reflects the point in the x-axis, y = 0. The mirror line is y = 1: (3, −2) is 3 below it, so the image is 3 above it, at y = 4.}}).

```graph
axes: -8..8, -8..8
prompt: Reflect triangle STU in the mirror line y = x. Plot S′, T′ and U′.
alt: Triangle STU on a grid and a diagonal dashed mirror line y = x
show: point (1,-3) "S"
show: point (3,-3) "T"
show: point (1,-7) "U"
show: polygon S T U
show: line y = x dashed
answer: (-3,1), (-3,3), (-7,1)
mistake: (-1,-3), (-3,-3), (-1,-7) :: That reflects the triangle in the vertical line x = 0. The mirror line is diagonal, so count diagonal steps across it: 1 left and 1 up each time. :: mis.reflect.diagonal-as-vertical
mistake: (1,3), (3,3), (1,7) :: That reflects the triangle in the horizontal line y = 0. The mirror line is diagonal, so count diagonal steps across it: 1 left and 1 up each time. :: mis.reflect.diagonal-as-vertical
```

## Check for understanding {checkpoint}

@@FENCE a2-d1@@

```mc
prompt: Tom reflected triangle ABC in the dashed mirror line y = x and drew A′B′C′. What is his error?
(x) He reflected ABC in a vertical line, x = 0. Counting diagonal steps across y = x, A′ should be at (0, −4).
( ) There is no error. A′B′C′ is the same distance from the line on the other side. :: Check A: (−4, 0) is 2 diagonal steps from y = x, at (−2, −2). 2 more steps give (0, −4), not (4, 0). :: mis.reflect.diagonal-as-vertical
( ) He should have slid ABC across the line without flipping it. :: A slide never makes a reflection. The image of a reflection faces the opposite way. :: mis.reflect.translates
solution: To reflect in y = x, count diagonal steps. A at (−4, 0) takes 2 steps to reach (−2, −2) on the line, and 2 more to reach A′ at (0, −4). Tom's A′ is at (4, 0), which is the reflection in the vertical line x = 0.
```

On a number line, the number exactly halfway between −3 and 5 is {{=1 | !4 :: 4 is halfway between 3 and 5 counted from 0. From −3 to 5 is 8 steps, so halfway is 4 steps from −3: at 1. | ?How many steps is it from −3 to 5? Go half of them from −3.}}.

```teacher-guide
## The sequence

One idea: count straight across from each corner to the mirror line, then the same distance past it. The first two examples use the same triangle and change only the mirror line, from the y-axis to the x-axis. Point out that the image faces the opposite way: that answers the ambulance hook. The third keeps the triangle and makes the line diagonal, so straight across becomes diagonal steps.

## Watch for

- An image that faces the same way as the shape (`mis.reflect.translates`). Ask, "Which side is the right angle on now?"
- A diagonal line treated as vertical or horizontal (`mis.reflect.diagonal-as-vertical`). Have students trace the diagonal steps with a finger, corner to corner.
- Distances counted from the shape's edge rather than each corner. Ask, "How far is this corner from the line?"

## If time runs short

Cut practice item 6, then item 5. Keep every faded example and both check-for-understanding items.
```
