```meta
key: act.geom.translate
skill: geom.transform.translate
title: Translations — Sliding a Shape
course: Year 7 Mathematics
tags: translation, vector, image, coordinates, transformation
role: lesson
type: worksheet
submission: free
feedback: on_check
calculator: off
x_review_skills: coord.four-quadrant, number.integers.number-line
x_dol_skills: geom.transform.translate, number.integers.number-line
```

# Translations — Sliding a Shape

```objectives
title: Today's goals
Translate a shape by moving every corner the same amount
Write the vector for a translation: how far across, and how far up or down
Describe a translation by following one corner to its own image
```

## Review

Answer these from memory.

```graph
axes: -6..6, -6..6
prompt: Plot the point (−5, 3).
answer: (-5, 3)
mistake: (3, -5) :: That is the point (3, −5). The first number is how far across, so go 5 left first, then 3 up. :: mis.coord.axes-swapped
mistake: (5, 3) :: −5 is 5 to the left of the origin, not 5 to the right.
```

@@FENCE a1-r2@@

1. Point P is at ({{=4 | !-2 :: The first coordinate is how far across. P is 4 to the right of the origin, so x = 4. :: mis.coord.axes-swapped}}, {{=-2}}).

2. On a number line, how many steps is it from −3 to 2? {{=5 | !1 :: That counts from 3 to 2. −3 is 3 below zero: count 3 steps up to 0, then 2 more to 2. | ?Count up to 0 first, then on to 2.}} steps

## Lesson {checkpoint}

A [[translation]] is a [[transformation]] that slides a shape. Every point moves the same distance in the same direction, so the shape doesn't turn or flip. The shape you get is the [[image]], and each corner of the image gets a small mark: A moves to A′.

@@FENCE a1-w1@@

```worked
title: Translate triangle ABC 5 squares right
Every point moves the same amount, so move each corner on its own: 5 squares right, and no squares up or down.
A is at (1, 1). Moving right adds to the x-coordinate, so A′ is at (1 + 5, 1), which is (6, 1).
In the same way, B at (3, 2) moves to B′ at (8, 2), and C at (1, 4) moves to C′ at (6, 4).
Join A′, B′ and C′. The image is the same size and shape as ABC, and it faces the same way.
Now look at the gap between the two triangles. There are only 3 empty squares between B and A′, but the triangle moved 5. The arrows show it: A moved 5 to reach A′, and C moved 5 to reach C′.
So measure a translation from a point to its own image, never across the gap.
```

Now the same triangle moves up as well as across.

@@FENCE a1-w2@@

```worked
title: Translate triangle ABC 5 right and 3 up
Moving right adds to the x-coordinate. Moving up adds to the y-coordinate.
A is at (1, 1), so A′ is at (1 + 5, 1 + 3), which is (6, 4).
B at (3, 2) moves to B′ at (8, 5), and C at (1, 4) moves to C′ at (6, 7).
The arrow from A to A′ is the [[vector]] for this translation: 5 right, 3 up. Every point moves by the same vector, so the arrow from B to B′ would be the same length and point the same way.
```

The last example turns the question round. You see the shape and its image, and you work out the translation.

@@FENCE a1-w3@@

```worked
title: Describe the translation from ABC to A′B′C′
Follow one corner to its own image. A is at (1, 1), and A′ is at (−3, −1).
Across: from x = 1 to x = −3. The x-coordinate got smaller, so the move is to the left. From 1 down to 0 is 1 step, and from 0 down to −3 is 3 more: 4 squares left.
Up or down: from y = 1 to y = −1. The y-coordinate got smaller, so the move is down: 2 squares down.
Check with another corner. C is at (1, 4), and C′ is at (−3, 2): 4 left and 2 down again.
So the translation is 4 left, 2 down. As a vector, the arrow from A to A′ goes 4 left and 2 down.
```

```callout
variant: note
To translate, move every corner by the same amount: right or left changes x, and up or down changes y. To describe a translation, follow one corner to its own image: across first, then up or down.
```

Now you finish the last steps.

@@FENCE a1-f1@@

```faded
title: Translate triangle PQR 2 left and 4 up
Moving left takes away from the x-coordinate. Moving up adds to the y-coordinate.
P is at (1, −3), so P′ is at (1 − 2, −3 + 4), which is (−1, 1).
Q is at (4, −3), so Q′ is at ({{=2 | !1 :: Write the x-coordinate first. Q′ is 2 left of Q, so x = 4 − 2 = 2. :: mis.coord.axes-swapped | !6 :: Left takes away from x: 4 − 2 = 2.}}, {{=1}}).
R is at (4, −1), so R′ is at ({{=2}}, {{=3}}).
```

This time you do every corner.

@@FENCE a1-f2@@

```faded
title: Translate triangle KLM 3 right and 5 down
Right adds 3 to the x-coordinate. Down takes 5 away from the y-coordinate.
K is at (−4, 3), so K′ is at ({{=-1 | !-7 :: Right adds to x: −4 + 3 = −1.}}, {{=-2 | !8 :: Down takes away from y: 3 − 5 = −2.}}).
L is at (−2, 3), so L′ is at ({{=1}}, {{=-2}}).
M is at (−4, 6), so M′ is at ({{=-1}}, {{=1}}).
```

Now describe a translation.

@@FENCE a1-f3@@

```faded
title: Describe the translation from WXYZ to W′X′Y′Z′
Follow W to its own image. W is at (−5, 1), and W′ is at (0, −2).
Across: the move is {{=5 | !3 :: 3 is the number of empty squares between the rectangles. Follow W to its own image: from −5 to 0 is 5 squares. :: mis.translate.counts-gaps}} squares {{right | ?Did the x-coordinate get bigger or smaller?}}.
Up or down: the move is {{=3 | !2 :: That counts the empty rows between the rectangles. Follow W to W′: from 1 down to −2 is 3 squares. :: mis.translate.counts-gaps}} squares {{down}}.
```

### Independent practice

```graph
axes: -6..8, -2..6
prompt: Translate rectangle ABCD 6 squares right. Plot A′, B′, C′ and D′.
alt: Rectangle ABCD on a grid, 3 squares wide and 2 squares tall
show: point (-5,2) "A"
show: point (-2,2) "B"
show: point (-2,4) "C"
show: point (-5,4) "D"
show: polygon A B C D
answer: (1,2), (4,2), (4,4), (1,4)
mistake: (4,2), (7,2), (7,4), (4,4) :: That leaves 6 empty squares between the rectangles, so each corner moved 9. Move each corner 6: A goes from −5 to 1. :: mis.translate.counts-gaps
mistake: (2,1), (2,4), (4,4), (4,1) :: Those points have their coordinates swapped. A′ is at (1, 2): 1 across, then 2 up. :: mis.coord.axes-swapped
```

```graph
axes: -4..9, -4..5
prompt: Translate triangle STU 3 left and 4 up. Plot S′, T′ and U′.
alt: Triangle STU on a grid, below the x-axis on the right
show: point (2,-1) "S"
show: point (5,-1) "T"
show: point (2,-3) "U"
show: polygon S T U
answer: (-1,3), (2,3), (-1,1)
mistake: (5,3), (8,3), (5,1) :: That moved 3 right. Left takes away from the x-coordinate: S goes from 2 to −1.
mistake: (3,-1), (3,2), (1,-1) :: Those points have their coordinates swapped. S′ is at (−1, 3): 1 left, then 3 up. :: mis.coord.axes-swapped
```

```graph
axes: -6..6, -6..6
prompt: Rectangle JKLM is translated onto J′K′L′M′. Draw the vector for this translation. You can draw it anywhere on the grid.
alt: Rectangle JKLM and its image J′K′L′M′ on a grid
show: point (1,-2) "J"
show: point (3,-2) "K"
show: point (3,0) "L"
show: point (1,0) "M"
show: polygon J K L M
show: point (-4,0) "J′"
show: point (-2,0) "K′"
show: point (-2,2) "L′"
show: point (-4,2) "M′"
show: polygon J′ K′ L′ M′
answer: vector -5, 2
mistake: vector 5, -2 :: That arrow goes from the image back to the shape. Start at J and finish at J′: 5 left, 2 up.
mistake: vector 2, -5 :: That goes 2 across and 5 up or down. Swap them: J to J′ is 5 left, then 2 up. :: mis.coord.axes-swapped
mistake: vector -3, 2 :: 3 is the number of empty squares between the rectangles. Follow J to J′: from 1 to −4 is 5 squares left. :: mis.translate.counts-gaps
```

4. The point (−2, 3) is translated 5 right and 4 down. It ends up at ({{=3 | !-1 :: That is the answer with its coordinates swapped. Across first: −2 + 5 = 3. :: mis.coord.axes-swapped | !-7 :: Right adds to x: −2 + 5 = 3.}}, {{=-1 | !7 :: Down takes away from y: 3 − 4 = −1.}}).

@@FENCE a1-p5@@

```mc
prompt: Aroha says rectangle DEFG has moved 4 squares to the right to reach D′E′F′G′. What is her error?
(x) She counted the empty squares between the rectangles. Each corner moved 7 squares: D goes from −6 to 1.
( ) There is no error. There are 4 squares between the rectangles, so it moved 4. :: The gap isn't how far it moved. Follow D to its own image D′: from −6 to 1 is 7 squares. :: mis.translate.counts-gaps
( ) She should have counted 10 squares, from D to E′. :: E′ isn't D's image. Follow D to D′: from −6 to 1 is 7 squares.
solution: Follow one corner to its own image. D is at (−6, 1) and D′ is at (1, 1), so the rectangle moved 7 squares right. The 4 empty squares are only the gap between the rectangles.
```

## Check for understanding {checkpoint}

@@FENCE a1-d1@@

```mc
prompt: Hana describes the translation from RST to R′S′T′ as 3 right, 4 down. What is her error?
(x) She swapped the two numbers. R goes from x = −4 to 0 (4 right) and from y = 2 to −1 (3 down), so it is 4 right, 3 down.
( ) There is no error. :: Follow R to R′: x goes from −4 to 0, which is 4 right, and y goes from 2 to −1, which is 3 down. Across comes first. :: mis.coord.axes-swapped
( ) She should count the gap between the triangles: 2 right. :: The gap isn't how far the triangle moved. Follow R to its own image R′: 4 right and 3 down. :: mis.translate.counts-gaps
solution: Follow R to R′. Across: from −4 to 0 is 4 right. Down: from 2 to −1 is 3 down. So the translation is 4 right, 3 down. Hana wrote the two numbers the wrong way round.
```

```mc
prompt: Which of these numbers is the smallest: −7, −3 or 2?
(x) −7
( ) −3 :: 3 is smaller than 7, but −3 is to the right of −7 on a number line, so −3 is bigger. :: mis.integers.larger-digit-larger
( ) 2 :: 2 is a positive number, so it is bigger than both negative numbers.
solution: On a number line, −7 is furthest to the left, so it is the smallest. Then −3, then 2.
```

```teacher-guide
## The sequence

One idea: every point moves by the same amount, so follow one corner to its own image. The first example moves right only. Point out the gap: 3 empty squares, but the triangle moved 5. That answers the domino hook. The second adds an up move and names the arrow as the vector. The third turns the question round: given both shapes, follow A to A′ and count across, then up or down.

## Watch for

- Counting the empty squares between the shapes (`mis.translate.counts-gaps`). Ask, "Where did A end up? Count from A to there."
- Coordinates or vector parts written the wrong way round (`mis.coord.axes-swapped`). Ask, "Across first: which way did it go?"
- Moving the wrong way on a "left" or "down". Ask whether x or y should get bigger or smaller.

## If time runs short

Cut practice item 4, then item 2. Keep every faded example and both check-for-understanding items.
```
