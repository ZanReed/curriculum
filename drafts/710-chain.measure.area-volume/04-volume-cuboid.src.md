```meta
key: act.measure.volume-cuboid
skill: measure.volume.cuboid
title: Volume — Layers of Cubes
course: Year 7 Mathematics
tags: volume, cuboid, cube, cubic unit
role: lesson
type: worksheet
submission: free
feedback: on_check
calculator: off
x_review_skills: measure.area.composite
x_dol_skills: measure.volume.cuboid, measure.perimeter.polygons
```

# Volume — Layers of Cubes

```objectives
title: Today's goals
Find the volume of a cuboid by counting layers of cubes
Use length × width × height, and give the answer in cubic units
Spot the error when the lengths are added instead of multiplied
```

## Review

From memory: one quick composite shape.

```columns
figure:
@@COL a4-review@@
---
The area of the L-shape is {{=33 | !42 :: Your rectangles overlap: 8 × 3 and 3 × 6 both include the 3 cm by 3 cm corner. :: mis.area.composite-overlap}} cm².
```

## Lesson {checkpoint}

The [[volume]] of a solid is the amount of space it takes up. We measure it by counting [[cubic unit]]s. A cube 1 cm long, 1 cm wide and 1 cm high is one cubic centimetre, written 1 cm³.

@@FENCE a4-w1@@

```worked
title: Find the volume of the cuboid
This [[cuboid]] is built from 1 cm cubes. Count them in layers, starting at the bottom.
The bottom layer is 4 cubes long and 3 cubes wide.
$$4 \times 3 = 12 \text{ cubes}$$
The cuboid is 2 layers high, and every layer is the same.
$$12 \times 2 = 24 \text{ cubes}$$
Each cube is 1 cm³, so the volume is 24 cm³.
```

Same method, a different cuboid.

@@FENCE a4-w2@@

```worked
title: Find the volume of the cuboid
This one is a tall tower. The bottom layer is 2 cubes long and 2 cubes wide: 2 × 2 = 4 cubes.
The tower is 5 layers high: 4 × 5 = 20 cubes. The volume is 20 cm³.
Adding the edges, 2 + 2 + 5 = 9, doesn't count the cubes. A volume comes from multiplying.
One layer is length × width, and the number of layers is the height. So:
$$\text{volume of a cuboid} = \text{length} \times \text{width} \times \text{height}$$
```

Here are two boxes: Box 1 is a cube, and Box 2 is long and thin.

```columns
figure: Box 1
@@COL a4-w3-1@@
---
figure: Box 2
@@COL a4-w3-2@@
```

```worked
title: Which box holds more?
Box 1: the bottom layer is 40 × 40 = 1600 cubes, and there are 40 layers.
$$1600 \times 40 = 64\,000$$
Box 2: the bottom layer is 80 × 20 = 1600 cubes, and there are 40 layers.
$$1600 \times 40 = 64\,000$$
Both boxes hold 64 000 cm³. Their bottom layers are the same size, and they are the same height.
Adding the edges gives 120 for Box 1 and 140 for Box 2, which makes Box 2 look bigger. It isn't.
1000 cm³ holds exactly 1 litre, so each box holds 64 litres.
Box 1 is a [[cube]]: 40 × 40 × 40 = 64 000. That works backwards too: a cube that holds 64 000 cm³ has edges 40 cm long.
```

```callout
variant: note
Volume counts cubes, so its unit is cubed: cm³ or m³. Count one layer (length × width), then multiply by the number of layers (the height). Never add the edges.
```

Now you finish the last steps.

@@FENCE a4-f1@@

```faded
title: Find the volume of the cuboid
The bottom layer is 6 cubes long and 2 cubes wide: 6 × 2 = 12 cubes.
There are 3 layers.
So the volume is {{=36 | !11 :: That adds the edges, 6 + 2 + 3. Volume counts cubes: one layer of 12, three times. :: mis.volume.adds-dimensions}} cm³.
```

No cubes drawn this time. The method is the same.

@@FENCE a4-f2@@

```faded
title: Find the volume of the cuboid
One layer is 5 × 4 = {{=20}} cubes.
The cuboid is 3 cm high, so there are 3 layers. The volume is {{=60 | !12 :: That adds the edges, 5 + 4 + 3. Multiply: one layer of 20, three times. :: mis.volume.adds-dimensions}} cm³.
```

A cube. You do all of it, and write the unit.

@@FENCE a4-f3@@

```faded
title: Find the volume of the cube
Length × width × height.
The volume is {{=125 unit: cm³, cm3, cm^3, cubic cm, cubic centimetres, cubic centimetre | !125 cm² :: A volume counts cubes, so its unit is cubed: cm³. Square centimetres measure a flat surface. :: mis.units.volume-as-square | !125 cm2 :: A volume counts cubes, so its unit is cubed: cm³, typed cm3. cm2 is for a flat surface. :: mis.units.volume-as-square | !125 cm^2 :: A volume counts cubes, so its unit is cubed: cm³, typed cm^3. cm^2 is for a flat surface. :: mis.units.volume-as-square | !unit-missing :: Say what 125 counts: write the unit, cm³. | !15 :: That adds the edges, 5 + 5 + 5. Multiply them. :: mis.volume.adds-dimensions | !25 :: That is one layer, 5 × 5. The cube is 5 layers high.}}
```

### Independent practice

Find each volume.

```columns
figure:
@@COL a4-p1@@
---
1. The volume is {{=56 | !13 :: That adds the edges, 7 + 2 + 4. Count one layer, then multiply by the number of layers. :: mis.volume.adds-dimensions}} cm³.
```

```columns
figure:
@@COL a4-p2@@
---
2. The volume is {{=80 | !15 :: That adds the edges, 8 + 5 + 2. Multiply them. :: mis.volume.adds-dimensions}} cm³.
```

3. A raised garden bed is a cuboid 2 m long, 1 m wide and 0.5 m deep. How much soil fills it? {{=1 unit: m³, m3, m^3, cubic m, cubic metres, cubic metre | !1 m² :: Soil fills a space, so its volume is in cubic metres: m³. :: mis.units.volume-as-square | !1 m2 :: Soil fills a space, so its volume is in cubic metres: m³, typed m3. :: mis.units.volume-as-square | !1 m^2 :: Soil fills a space, so its volume is in cubic metres: m³, typed m^3. :: mis.units.volume-as-square | !unit-missing :: Say what 1 measures: write the unit, m³. | !3.5 :: That adds the edges, 2 + 1 + 0.5. Multiply them. :: mis.volume.adds-dimensions}}

4. A cube has a volume of 1000 cm³. Each edge is {{=10 | !100 :: 100 × 100 × 100 = 1 000 000, far more than 1000. Which number, times itself, times itself again, makes 1000? | ?Which number, multiplied by itself three times, gives 1000?}} cm long.

@@FENCE a4-p5@@

```mc
prompt: Ben says this box holds 13 cm³, because 6 + 5 + 2 = 13. What is Ben's error?
(x) He added the edges. Volume counts cubes: one layer is 6 × 5 = 30 cubes, and there are 2 layers, so the volume is 60 cm³.
( ) There is no error. 6 + 5 + 2 = 13. :: The sum is right, but adding the edges doesn't count cubes. Multiply: 6 × 5 × 2. :: mis.volume.adds-dimensions
( ) His unit is wrong. It should be 13 cm². :: A volume counts cubes, so its unit is cm³. And 13 comes from adding, which doesn't count cubes. :: mis.units.volume-as-square
solution: One layer is 6 × 5 = 30 cubes, and the box is 2 layers high: 30 × 2 = 60 cm³.
```

```mc
prompt: Hana works out the volume of a box. Her answer is 30. Which unit should she write after it?
options: keep-order
( ) cm :: Centimetres measure a length. A volume counts cubes.
( ) cm² :: Square centimetres measure a flat surface. A volume counts cubes, so it is cubed. :: mis.units.volume-as-square
(x) cm³
solution: Volume counts 1 cm cubes, so the unit is cubic centimetres, cm³.
```

## Check for understanding {checkpoint}

@@FENCE a4-d1@@

```mc
prompt: Tama finds the volume of this box. He writes 4 × 4 × 3 = 48 cm². What is Tama's error?
( ) There is no error. 4 × 4 × 3 = 48. :: The multiplication is right, but cm² is for a flat surface. A volume counts cubes: cm³. :: mis.units.volume-as-square
(x) His unit is wrong. A volume counts cubes, so it is 48 cm³.
( ) He should have added: 4 + 4 + 3 = 11 cm³. :: Adding the edges doesn't count cubes. Multiplying does. :: mis.volume.adds-dimensions
solution: One layer is 4 × 4 = 16 cubes, and there are 3 layers: 48 cubes. Each is 1 cm³, so the volume is 48 cm³.
```

A rectangular field is 120 m long and 80 m wide. How far is it once round the edge? {{=400 unit: m, metres, metre | !unit-missing :: Say what 400 measures: write the unit, m. | !200 :: That is one length and one width: halfway round. Add all four sides.}}

```teacher-guide
## The sequence

One idea, the one the skill names: volume counts cubes, so count one layer, then multiply by the number of layers. The first two examples show the cubes before any formula; length × width × height arrives at the end of the second, as a name for what the layers did. Say aloud why adding the edges counts nothing. The third answers the two-boxes hook: same layer, same height, same volume, 64 litres each.

## Watch for

- Adding the three edges (`mis.volume.adds-dimensions`). Ask, "How many cubes are in the bottom layer?"
- Volumes in cm² (`mis.units.volume-as-square`). Ask, "Does it count squares or cubes?" Accepted spellings include cm³, cm3, cm^3 and cubic centimetres. Say so before practice.
- Stopping after one layer.

## If time runs short

Cut practice item 2, then item 6. Keep every faded example and both check-for-understanding items.
```
