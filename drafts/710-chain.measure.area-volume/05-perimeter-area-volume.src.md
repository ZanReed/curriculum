```meta
key: act.measure.perimeter-area-volume
skill: measure.volume.cuboid
supporting_skills: measure.perimeter.polygons, measure.area.rect-triangle, measure.area.composite
chain_role: consolidation
title: Perimeter, Area or Volume? — Choosing the Measure
course: Year 7 Mathematics
tags: perimeter, area, volume, square unit, cubic unit
role: lesson
type: worksheet
submission: free
feedback: on_check
calculator: off
x_review_skills: measure.volume.cuboid
x_dol_skills: measure.volume.cuboid, ext.measure.metric-units
x_dol_rubric_levels: A, M, E
```

# Perimeter, Area or Volume? — Choosing the Measure

```objectives
title: Today's goals
Decide whether a question asks for a perimeter, an area or a volume
Calculate it, and give the unit that matches
Explain your choice, and judge a claim about volume
```

## Review

From memory: one quick volume.

```columns
figure:
@@COL a5-review@@
---
The volume of the cuboid is {{=120 | !15 :: That adds the edges, 6 + 4 + 5. Count one layer, 6 × 4, then multiply by the number of layers. :: mis.volume.adds-dimensions}} cm³.
```

## Lesson {checkpoint}

You now have three measures. Before you calculate, decide which one the question asks for.

- Going round an edge is a [[perimeter]]. Add lengths. The unit is a length: cm or m.
- Covering a flat surface is an [[area]]. Multiply two lengths. The unit is a [[square unit]]: cm² or m².
- Filling a space is a [[volume]]. Multiply three lengths. The unit is a [[cubic unit]]: cm³ or m³.

@@FENCE a5-w1@@

```worked
title: One gift box, three questions
The gift box is a [[cuboid]]. How much ribbon goes once round the edge of the lid? Round an edge, so it's a perimeter. Add the four edges of the lid.
$$20 + 10 + 20 + 10 = 60$$
The ribbon is 60 cm.
How much paper covers the top of the lid? Covering a surface, so it's an area. Multiply two lengths.
$$20 \times 10 = 200$$
The paper is 200 cm².
How much space is inside the box? Filling a space, so it's a volume. Multiply three lengths.
$$20 \times 10 \times 5 = 1000$$
The space inside is 1000 cm³.
Same box, same numbers, three different answers. The question decides the measure, and the measure decides the unit.
```

You can decide before you calculate anything.

```worked
title: Round, cover or fill?
Skirting board along the bottom of a bedroom's walls goes round an edge: a perimeter, in metres.
Carpet for the bedroom floor covers a surface: an area, in square metres, m².
Concrete to fill the hole for a fence post fills a space: a volume, in cubic metres, m³.
Check the unit against the calculation. Adding lengths gives a length. Multiplying two lengths gives square units. Multiplying three gives cubic units.
```

```callout
variant: note
Round, cover or fill? Round an edge: perimeter, add, cm. Cover a surface: area, two lengths multiplied, cm². Fill a space: volume, three lengths multiplied, cm³.
```

Now you finish the last steps.

@@FENCE a5-f1@@

```faded
title: A sandpit, three questions
A timber frame goes round the top edge: a perimeter. 3 + 2 + 3 + 2 = 10 m.
A cover goes over the top: an area. 3 × 2 = {{=6 | !10 :: That is the frame, round the edge. The cover covers a surface: multiply. | !5 :: That adds 3 + 2. An area multiplies the two lengths.}} m².
Sand fills it: a volume. 3 × 2 × 0.5 = {{=3 | !5.5 :: That adds the edges, 3 + 2 + 0.5. A volume multiplies all three. :: mis.volume.adds-dimensions | !6 :: That is the top surface, 3 × 2. The sand is 0.5 m deep, so multiply by 0.5 too.}} m³.
```

A classroom floor is 9 m long and 7 m wide. Now you decide which measure.

```faded
title: Tape and carpet
Tape goes once round the edge of the floor, so find the {{perimeter | !area :: Tape goes round the edge. Covering the floor would be an area.}}: {{=32 | !63 :: That is the area, 9 × 7. Tape goes round the edge: add the four sides.}} m.
Carpet tiles cover the floor, so find the {{area | !perimeter :: Carpet covers the floor. Going round the edge would be a perimeter.}}: {{=63 | !32 :: That is the perimeter, round the edge. Carpet covers the floor: 9 × 7. | !16 :: That adds 9 + 7. An area multiplies the two lengths.}} m².
```

A water trough on a farm. You do all of it, including the unit.

```faded
title: Water in the trough
The trough is 2 m long, 0.5 m wide and 0.4 m deep. How much water does it hold when full?
It holds {{=0.4 unit: m³, m3, m^3, cubic m, cubic metres, cubic metre | !0.4 m² :: Water fills a space, so it is a volume, in cubic metres: m³. :: mis.units.volume-as-square | !0.4 m2 :: Water fills a space, so it is a volume, in cubic metres: m³, typed m3. :: mis.units.volume-as-square | !0.4 m^2 :: Water fills a space, so it is a volume, in cubic metres: m³, typed m^3. :: mis.units.volume-as-square | !unit-missing :: Say what 0.4 measures: write the unit, m³. | !2.9 :: That adds the edges, 2 + 0.5 + 0.4. Water fills a space: multiply all three. :: mis.volume.adds-dimensions | !1 :: That is the bottom of the trough, 2 × 0.5. Multiply by the depth, 0.4 m, too.}}
```

### Independent practice

Round, cover or fill? Decide first, then answer.

```mc
prompt: A farmer needs wire to go once round the edge of a paddock. What should she work out?
options: keep-order
(x) The paddock's perimeter
( ) The paddock's area :: Area is how much ground the paddock covers. The wire goes round the edge.
( ) The paddock's volume :: A paddock is flat ground, and the wire goes round its edge. Nothing is being filled.
solution: The wire goes round the edge, so she needs the perimeter.
```

2. A poster is 60 cm long and 40 cm wide. How much wall does it cover? {{=2400 unit: cm², cm2, cm^2, sq cm, sqcm, sq. cm, square cm, square centimetres, square centimetre | !2400 cm :: The poster covers a surface, so its area is in square centimetres: cm². Centimetres alone measure a length. :: mis.units.area-as-linear | !unit-missing :: Say what 2400 counts: write the unit, cm². | !200 :: That is the distance round the poster. Covering a wall is an area: 60 × 40.}}

```mc
prompt: Which unit fits the amount of water in a swimming pool?
options: keep-order
( ) m :: Metres measure a length, like the length of the pool. The water fills a space.
( ) m² :: Square metres measure a flat surface, like the pool's floor. The water fills a space. :: mis.units.volume-as-square
(x) m³
solution: Water fills a space, so it is a volume, measured in cubic metres, m³.
```

```columns
figure:
@@COL a5-p4@@
---
4. Skirting board goes round the bottom of the walls of this room. Ignoring the door, how long is it? {{=22 unit: m, metres, metre | !26 :: That is the floor's area. Skirting goes round the edge: add all six sides. | !unit-missing :: Say what 22 measures: write the unit, m. | !22 m² :: Skirting is a length round the edge, so its unit is metres, m, not m².}}
```

5. Carpet covers the floor of the same room. How much carpet is needed? {{=26 unit: m², m2, m^2, sq m, sqm, sq. m, square m, square metres, square metre | !26 m :: Carpet covers a surface, so its area is in square metres: m². :: mis.units.area-as-linear | !unit-missing :: Say what 26 counts: write the unit, m². | !38 :: Your two rectangles overlap at the corner. Split so the pieces don't overlap. :: mis.area.composite-overlap | !22 :: That is the skirting, round the edge. Carpet covers the floor.}}

```mc
prompt: Tama finds the area of a deck 6 m long and 4 m wide. He writes "24 m". What is Tama's error?
( ) There is no error. 6 × 4 = 24, and the deck is measured in metres. :: The number is right, but an area counts squares 1 m by 1 m, so its unit is m². :: mis.units.area-as-linear
(x) His unit is wrong. An area counts squares, so it is 24 m².
( ) He found the wrong thing. The answer is 20 m. :: 20 m is the perimeter, the distance round the deck. The question asks for the area, which Tama found.
solution: 6 × 4 = 24 counts squares 1 m by 1 m, so the area is 24 m². Metres alone would be a length.
```

7. A shoebox is 30 cm long, 20 cm wide and 12 cm high. How much space is inside it? {{=7200 unit: cm³, cm3, cm^3, cubic cm, cubic centimetres, cubic centimetre | !7200 cm² :: The space inside is a volume, so its unit is cubed: cm³. :: mis.units.volume-as-square | !7200 cm2 :: The space inside is a volume, so its unit is cubed: cm³, typed cm3. :: mis.units.volume-as-square | !7200 cm^2 :: The space inside is a volume, so its unit is cubed: cm³, typed cm^3. :: mis.units.volume-as-square | !unit-missing :: Say what 7200 counts: write the unit, cm³. | !62 :: That adds the edges, 30 + 20 + 12. Multiply all three. :: mis.volume.adds-dimensions | !600 :: That is one layer, 30 × 20. The box is 12 layers high.}}

## Check for understanding {checkpoint}

@@FENCE a5-d1@@

```shortanswer
prompt: This fish tank is 50 cm long, 30 cm wide and 40 cm high. (1) Find how much water it holds when full, and the length of trim that goes once round its top edge. Give each answer with its unit, and say how you decided which calculation each one needed. (2) Rawiri says, "If two boxes give the same total when you add their length, width and height, they hold the same amount." Is Rawiri right? Explain, using an example.
starter: (1) The water: …
rubric: Finds both measures | 2 | water 60 000 cm³ and trim 160 cm, each with its unit (1 each)
rubric: Explains the choices | 2 | Links each question to its measure, its calculation and its unit: the water fills a space, so it is a volume, three lengths multiplied, in cm³; the trim goes round an edge, so it is a perimeter, the four top edges added, in cm
rubric: Judges Rawiri's claim | 2 | Rawiri is wrong, shown by a pair of boxes whose edges add to the same total but whose volumes differ, both worked out, with the reason: adding the edges doesn't count cubes, multiplying does
answer: (1) The water fills a space, so it is a volume: 50 × 30 × 40 = 60 000 cm³. The trim goes round the top edge, so it is a perimeter: 50 + 30 + 50 + 30 = 160 cm.
(2) Rawiri is wrong. A box 4 cm × 4 cm × 4 cm and a box 10 cm × 1 cm × 1 cm both add to 12 cm, but they hold 64 cm³ and 10 cm³. Adding the edges doesn't count the cubes inside; multiplying does, so the same total can give very different volumes.
solution: Water fills a space: volume, 50 × 30 × 40 = 60 000 cm³. Trim goes round an edge: perimeter, 50 + 30 + 50 + 30 = 160 cm. Rawiri is wrong: 4 × 4 × 4 = 64 and 10 × 1 × 1 = 10, though both add to 12. Volume multiplies; adding doesn't count cubes.
```

1.2 kg = {{=1200 | !120 :: A kilogram is 1000 g, so multiply by 1000, not 100. | !12 :: A kilogram is 1000 g, so multiply by 1000.}} g

```teacher-guide
## The sequence

One idea: decide what is being measured before calculating: round an edge, cover a surface, or fill a space. The gift box asks all three questions of one object: point out that the numbers stay the same and only the question changes. The second example decides without calculating, and checks the unit against the calculation.

## Watch for

- Calculating before deciding. Ask, "Round, cover or fill?"
- A unit that doesn't match the measure (`mis.units.area-as-linear`, `mis.units.volume-as-square`).
- A perimeter given for an area, or an area for a perimeter. No misconception id names this yet, so it shows only in the marks.

## If time runs short

Cut practice item 1, then item 3. Keep every faded example and the whole check for understanding.

## Marking

- **Finds both measures (A):** 60 000 cm³ and 160 cm, with units. One mark each.
- **Explains the choices (M):** each answer linked to what is measured, its calculation and its unit.
- **Judges Rawiri's claim (E):** 2 for "no" with a worked pair of boxes (same edge total, different volumes) and why adding can't count cubes; 1 for either alone. Mark the reasoning, not the writing.
```
