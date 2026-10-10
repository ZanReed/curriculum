```meta
key: act.geom.which-transformation
skill: geom.transform.rotate
supporting_skills: geom.transform.translate, geom.transform.reflect
chain_role: consolidation
title: Slide, Flip or Turn? — Naming the Transformation
course: Year 7 Mathematics
tags: transformation, translation, reflection, rotation, image, centre of rotation
role: lesson
type: worksheet
submission: free
feedback: on_check
calculator: off
x_review_skills: geom.transform.rotate
x_dol_skills: geom.transform.rotate, ext.arith.whole-ops
x_dol_rubric_levels: A, M, E
```

# Slide, Flip or Turn? — Naming the Transformation

```objectives
title: Today's goals
Decide whether a shape was slid, flipped or turned onto its image
Tell a reflection from a half turn, even when both images are upside down
Describe the transformation fully: the vector, the mirror line, or the turn and its centre
```

## Review

From memory: one quick rotation.

The point (2, 3) is rotated a quarter turn clockwise about the origin. Its image is at ({{=3 | !-2 :: That is the answer with its coordinates swapped. From the origin to (2, 3) is 2 right and 3 up; turned clockwise, that is 2 down and 3 right. :: mis.coord.axes-swapped | !-3 :: That turns anticlockwise. Clockwise turns up into right and right into down.}}, {{=-2}}).

## Lesson {checkpoint}

You know three kinds of [[transformation]]. To decide which one maps a shape onto its [[image]], ask one question first: was the shape flipped over? Picture the shape cut out of paper. A [[translation]] slides it and a [[rotation]] turns it, both without lifting it off the desk. A [[reflection]] flips it over.

Here is how to check. Go round the corners in order, A to B to C. Picture walking from A to B, then turning to head for C. If you turn left, you are going round [[anticlockwise]]; if you turn right, you are going round [[clockwise]]. Then go round A′, B′ and C′ the same way. If the direction has changed, the shape was flipped: it is a reflection. If it is the same, the shape was slid or turned.

@@FENCE a4-w1@@

```worked
title: Which transformation maps ABC onto A′B′C′?
Go round ABC: A to B goes right, then you turn left to head up to C. That is anticlockwise.
Go round A′B′C′: A′ to B′ goes right, then you turn right to head down to C′. That is clockwise.
The direction has changed, so the triangle was flipped over. It is a reflection.
The [[mirror line]] is halfway between each corner and its image. A is at (1, 1) and A′ is at (1, −1), so halfway is y = 0.
So the transformation is a reflection in the x-axis, the line y = 0.
```

The same triangle again. This image is also below it and upside down.

@@FENCE a4-w2@@

```worked
title: Which transformation maps ABC onto A′B′C′?
Go round ABC: anticlockwise, as before.
Go round A′B′C′: A′ to B′ goes left, then B′ to C′ goes down and to the right. That is anticlockwise too.
The direction is the same, so the triangle was not flipped. It is upside down, so it was turned: a half turn.
P is at (2, 0). It is halfway between A at (1, 1) and A′ at (3, −1), and halfway between C and C′ too, so P is the [[centre of rotation]].
So the transformation is a rotation of 180° about P.
Both images are upside down, but only the first one was flipped.
```

The last example: the direction is the same, and the image isn't turned.

@@FENCE a4-w3@@

```worked
title: Which transformation maps ABC onto A′B′C′?
Go round A′B′C′: A′ to B′ goes right, then B′ to C′ goes up and to the left. That is anticlockwise, the same as ABC, so the triangle was not flipped.
It isn't turned either: the right angle is still at the bottom left, and A′B′ still runs along the bottom, like AB. So it was slid: a translation.
Follow A to its own image. A is at (1, 1) and A′ is at (5, 0): 4 right and 1 down.
So the transformation is a translation by the [[vector]] 4 right, 1 down.
```

```callout
variant: note
First, go round the corners. Direction changed: a reflection, with the mirror line halfway between each corner and its image. Same direction and turned: a rotation, with its angle, direction and centre. Same direction and not turned: a translation, with its vector.
```

Now you finish the last steps.

@@FENCE a4-f1@@

```faded
title: Which transformation maps ABC onto A′B′C′?
Go round ABC: A to B goes right, then B to C goes up and to the left. That is anticlockwise.
Go round A′B′C′: A′ to B′ goes left, then B′ to C′ goes up and to the right. That is {{clockwise | !anticlockwise :: Follow it: A′ to B′ goes left, then up to the right. That is the way a clock's hands go: clockwise.}}.
The direction has changed, so the transformation is a {{reflection | !rotation :: The direction of the corners changed, so the triangle was flipped, not turned. :: mis.reflect.half-turn-confused | !translation :: The direction of the corners changed, so it was flipped, not slid.}}.
A is at (−4, 1) and A′ is at (4, 1), so the mirror line is x = {{=0}}.
```

You do more of this one.

@@FENCE a4-f2@@

```faded
title: Which transformation maps ABC onto A′B′C′?
Go round ABC: anticlockwise.
Go round A′B′C′: A′ to B′ goes left, then B′ to C′ goes down and to the right. That is {{anticlockwise}}.
The direction is the same, and the triangle is upside down. So it is a {{rotation | !reflection :: The corners go round the same way, so it wasn't flipped. Upside down and not flipped means a half turn. :: mis.reflect.half-turn-confused}} of {{=180}}° about P.
```

You do almost all of this one.

@@FENCE a4-f3@@

```faded
title: Which transformation maps ABC onto A′B′C′?
Go round ABC: anticlockwise. Go round A′B′C′: {{anticlockwise | !clockwise :: A′ to B′ goes right, then you turn left to head up to C′: anticlockwise.}}.
The right angle is still at the bottom left, so the triangle hasn't been turned either. It is a {{translation | !rotation :: The right angle is still at the bottom left, so the triangle hasn't been turned. It was slid.}}.
Follow A to A′: it moves {{=5 | !3 :: 3 is the number of empty squares between the triangles. Follow A at (−3, −1) to A′ at (2, 1): 5 squares across. :: mis.translate.counts-gaps}} right and {{=2}} up.
```

### Independent practice

In the two "which diagram" questions, each diagram shows an outlined triangle moved onto a shaded one. There are no letters, so look at the right angle: is the shaded triangle upside down, and is its right angle on the same side or the other side?

```columns
figure: A
@@COL a4-p1-A@@
---
figure: B
@@COL a4-p1-B@@
---
figure: C
@@COL a4-p1-C@@
```

```mc
prompt: Which diagram shows a half turn?
options: keep-order
( ) A :: The shaded triangle is upside down, but the right angle is still on the left. It was flipped over a horizontal line, so it is a reflection. :: mis.reflect.half-turn-confused
(x) B
( ) C :: The shaded triangle faces the same way: the right angle is still at the bottom left. It was slid down, so it is a translation.
solution: In B the shaded triangle is upside down and the right angle has moved from the left to the right, so the triangle was turned, not flipped: a half turn. In A it is upside down but the right angle stays on the left: a reflection. In C it faces the same way: a translation.
```

@@FENCE a4-p2@@

```mc
prompt: What single transformation maps ABC onto A′B′C′?
(x) A rotation of 90° clockwise about P
( ) A rotation of 90° anticlockwise about P :: From P to A is 1 right and 1 up, and from P to A′ is 1 right and 1 down. Up turning into right is clockwise.
( ) A reflection :: Go round the corners: ABC and A′B′C′ both go round anticlockwise, so the triangle wasn't flipped.
( ) A translation :: A′B′C′ doesn't face the same way as ABC: AB runs along, but A′B′ runs up and down. It has been turned.
solution: Both triangles go round anticlockwise, so it isn't a reflection. AB runs along but A′B′ runs up and down, so it has been turned: a rotation. From P to A is 1 right and 1 up; from P to A′ is 1 right and 1 down. That is a quarter turn clockwise about P.
```

```graph
axes: -6..4, -4..6
prompt: Reflect triangle KLM in the mirror line y = 1. Plot K′, L′ and M′.
alt: Triangle KLM on a grid and a horizontal dashed mirror line y = 1
show: point (-3,2) "K"
show: point (-1,2) "L"
show: point (-3,4) "M"
show: polygon K L M
show: line y = 1 dashed
answer: (-3,0), (-1,0), (-3,-2)
mistake: (-1,0), (-3,0), (-1,-2) :: That is a half turn, not a reflection: the right angle has moved to the right. In a reflection in a horizontal line, K stays on the left: K′ is at (−3, 0). :: mis.reflect.half-turn-confused
mistake: (-3,-2), (-1,-2), (-3,0) :: That slides the triangle down without flipping it. The image should be upside down: M is the highest corner, so M′ is the lowest. :: mis.reflect.translates
```

```graph
axes: -4..6, -4..4
prompt: Rotate triangle UVW a half turn (180°) about P. Plot U′, V′ and W′.
alt: Triangle UVW and the centre of rotation P on a grid
show: point (-2,1) "U"
show: point (0,1) "V"
show: point (-2,3) "W"
show: polygon U V W
show: point (1,0) "P"
answer: (4,-1), (2,-1), (4,-3)
mistake: (-2,-1), (0,-1), (-2,-3) :: That reflects the triangle in the horizontal line through P. A half turn also swaps left and right: from P to U is 3 left and 1 up, so U′ is 3 right and 1 down from P. :: mis.reflect.half-turn-confused
mistake: (4,1), (2,1), (4,3) :: That reflects the triangle in the vertical line through P. A half turn also turns it upside down: from P to U is 3 left and 1 up, so U′ is 3 right and 1 down from P. :: mis.reflect.half-turn-confused
mistake: (2,-1), (0,-1), (2,-3) :: That turns the triangle about the origin, (0, 0). Start from P at (1, 0). :: mis.rotate.centre-ignored
```

@@FENCE a4-p5@@

```mc
prompt: Rangi says A′B′C′ is a reflection of ABC, because it is upside down. What is his error?
(x) The corners of both triangles go round anticlockwise, so ABC wasn't flipped. It was given a half turn about P.
( ) There is no error. It is upside down, so it is a reflection. :: Upside down can be a reflection or a half turn. Go round the corners: both go anticlockwise, so it wasn't flipped. It is a half turn about P. :: mis.reflect.half-turn-confused
( ) It is a translation, because it is the same size and shape. :: Every one of the three transformations keeps the size and shape. This triangle is upside down, so it hasn't just been slid.
solution: Go round the corners. A to B to C is anticlockwise, and A′ to B′ to C′ is anticlockwise too, so the triangle wasn't flipped. It is upside down, so it was turned: a half turn about P, which is halfway between A and A′.
```

```graph
axes: -6..4, -5..3
prompt: Translate triangle GHJ 3 right and 2 down. Plot G′, H′ and J′.
alt: Triangle GHJ on a grid, to the left of the y-axis
show: point (-4,-1) "G"
show: point (-2,-1) "H"
show: point (-4,1) "J"
show: polygon G H J
answer: (-1,-3), (1,-3), (-1,-1)
mistake: (-3,-1), (-3,1), (-1,-1) :: Those points have their coordinates swapped. G′ is at (−1, −3): 1 left, then 3 down. :: mis.coord.axes-swapped
```

```columns
figure: A
@@COL a4-p7-A@@
---
figure: B
@@COL a4-p7-B@@
---
figure: C
@@COL a4-p7-C@@
```

```mc
prompt: Which diagram shows a reflection?
options: keep-order
(x) A
( ) B :: The shaded triangle has turned upside down as well as swapping sides, so it was turned, not flipped: a half turn. :: mis.reflect.half-turn-confused
( ) C :: The shaded triangle faces the same way: the right angle is still at the bottom left. It was slid, so it is a translation.
solution: In A the right angle swaps from the left of the triangle to its right, but the triangle is not upside down: it was flipped over a vertical line, a reflection. In B it is upside down too: a half turn. In C it faces the same way: a translation.
```

## Check for understanding {checkpoint}

@@FENCE a4-d1@@

```shortanswer
prompt: (1) Describe fully the single transformation that maps triangle ABC onto A′B′C′, and explain how you know it is a rotation, not a reflection. (2) Ana says, "You can always tell a reflection from a half turn just by looking at the image." Is she right? Explain, using an example.
starter: (1) It is a …
rubric: Describes the transformation | 2 | A rotation of 90° anticlockwise (or 270° clockwise) about P: 2 marks for all three parts, 1 mark for "rotation" with one part missing
rubric: Explains why it is not a reflection | 2 | Explains from this figure why the triangle was turned, not flipped: A to B to C and A′ to B′ to C′ both go round anticlockwise (or an equivalent argument about turning the triangle without lifting it); and links the turn to its size, such as AB running along while A′B′ runs up and down
rubric: Judges Ana's claim | 2 | Ana is wrong, shown by a shape with a line of symmetry, such as a rectangle, whose reflection in a horizontal line and half turn give exactly the same image; only labelled corners show which one happened
answer: (1) A rotation of 90° anticlockwise about P (the same as 270° clockwise). Going round A to B to C is anticlockwise, and going round A′ to B′ to C′ is anticlockwise too. A reflection would change the direction, so the triangle was turned, not flipped. AB runs along and A′B′ runs up and down, so it turned a quarter turn: from P to A is 2 left and 1 up, and from P to A′ is 1 left and 2 down.
(2) Ana is wrong. Take a rectangle with corners (1, 1), (3, 1), (3, 2) and (1, 2). Reflecting it in the x-axis and giving it a half turn about (2, 0) both put it at (1, −1), (3, −1), (3, −2) and (1, −2): the same image. Without labels on the corners you can't tell which one happened. This happens when a shape has a line of symmetry at right angles to the mirror line, and the half turn is about the point where that line of symmetry meets the mirror line.
solution: The corners go round the same way in both triangles, so it was turned, not flipped: a quarter turn anticlockwise about P. Ana is wrong: a shape with a line of symmetry, such as a rectangle, can give the same image either way.
```

7 × 36 = {{=252 | !217 :: 7 × 30 is 210, and 7 × 6 is 42, not 7. 210 + 42 = 252.}}

```teacher-guide
## The sequence

One idea: go round the corners to decide whether the shape was flipped, then describe the transformation. The first two examples are the minimal pair: both images are upside down below the triangle, but only the first was flipped, which answers the playing-card hook. The third keeps the corner direction and removes the turn, leaving a translation. Paper triangles help.

## Watch for

- Calling any upside-down image a reflection (`mis.reflect.half-turn-confused`). Ask, "Which way do the corners go round?"
- Counting the gap for a translation (`mis.translate.counts-gaps`).

## If time runs short

Cut practice item 6, then item 3. Keep every faded example and the whole check for understanding.

## Marking

- **Describes the transformation (A):** rotation, 90° anticlockwise (or 270° clockwise), about P. One mark if a part is missing.
- **Explains why it is not a reflection (M):** corner direction or turning without lifting, plus why it is a quarter turn.
- **Judges Ana's claim (E):** 2 for "no" with a worked symmetric shape; 1 for a reason without an example. Mark the reasoning, not the writing.
```
