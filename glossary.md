# Course glossary

This is the curriculum's single list of mathematical words. Every activity is
authored with it open: a glossary word is written as a plain `[[term]]`, and
the platform's import resolves it here. The format and editing rules are D40
in `decision-log-additions.md`, and `scripts/check_glossary.py` enforces them in CI.
The rules that matter most while editing:

- **This file is hand-authored and is the only place a glossary word is edited.**
  Nothing generates it.
- **An `id:` is permanent.** Fixing a word's spelling in `term:` keeps the id.
  Changing a word's meaning means retiring the old entry and minting a new id.
  A retired id goes into `glossary-retired.txt` and is never used again.
- **Definitions are NZ-only.** A `us:` line holds the US word for the same idea,
  and that word never appears in any definition. Don't put `[[…]]` or answer gaps
  inside a definition. The platform works out cross-links itself.
- **One word, one entry.** If a word has two school meanings, one entry names both.

Headings between the fences only group entries for reading. The platform reads
every `definitions` fence in the file as one list.

## Number and ratio

```definitions
id: gloss.rate
term: rate
A comparison of two quantities measured in different units, such as dollars and
kilograms, or kilometres and hours. "150 km in 2 hours" is a rate.
---
id: gloss.unit-rate
term: unit rate
A rate for exactly one of the second quantity: the amount per one. You find it by
dividing the first quantity by the second.
$$\text{unit rate} = \frac{\text{first quantity}}{\text{second quantity}}$$
"\$1.50 per apple" is a unit rate. "\$6.00 for 4 apples" is not a unit rate yet.
---
id: gloss.ratio
term: ratio
A comparison of two quantities by division. The ratio of 6 to 3 is written $6:3$,
and it compares the quantities the same way as $\frac{6}{3} = 2$.
---
id: gloss.lowest-terms
term: lowest terms
A fraction is in lowest terms when its numerator (top) and denominator (bottom)
share no common factor other than 1. $\frac{6}{4}$ is not in lowest terms, but
$\frac{3}{2}$ is.
---
id: gloss.proportional-relationship
term: proportional relationship
A relationship between two quantities that always keep the same ratio: when one
doubles, so does the other. It can be written as $y = kx$ for one fixed number $k$,
and its graph is a straight line through the origin.
---
id: gloss.constant-of-proportionality
term: constant of proportionality
The fixed number $k$ in $y = kx$. It is the amount of $y$ for each one unit of $x$.
$$k = \frac{y}{x}$$
It is the unit rate under another name. It is also the value of $y$ when $x = 1$.
```

## Graphs and coordinates

```definitions
id: gloss.origin
term: origin
The point $(0, 0)$, where the x-axis and the y-axis cross.
---
id: gloss.x-axis
term: x-axis
The horizontal number line on a graph. Every point on the x-axis has $y = 0$.
---
id: gloss.y-axis
term: y-axis
The vertical number line on a graph. Every point on the y-axis has $x = 0$.
---
id: gloss.coordinates
term: coordinates
The pair of numbers $(x, y)$ that gives the position of a point. The first number
is how far across from the origin, and the second is how far up or down.
---
id: gloss.axis-scale
term: axis scale
The step between the numbered marks on an axis. The two axes can have different
scales. Read the numbers on each axis before you judge how steep a line is.
```

## Algebra words

```definitions
id: gloss.expression
term: expression
Numbers, variables and operations with no equals sign, such as $3x + 2$. You can
simplify or evaluate an expression, but you cannot solve it.
---
id: gloss.equation
term: equation
A statement that two expressions are equal, such as $3x + 2 = 11$. When you solve
an equation, you find the values that make it true.
---
id: gloss.variable
term: variable
A letter, such as $x$, that stands for a number that can change or is not known yet.
---
id: gloss.coefficient
term: coefficient
The number that multiplies a variable. In $5x^2 - 3x$, the coefficient of $x^2$ is
$5$ and the coefficient of $x$ is $-3$.
---
id: gloss.polynomial
term: polynomial
An expression made by adding terms of the form $ax^n$, where $n$ is a whole number
($0, 1, 2, \ldots$). For example, $3x^2 - 5x + 1$ is a polynomial.
```

## Straight lines

```definitions
id: gloss.gradient
term: gradient
us: slope
How steep a straight line is. It is the rise divided by the run between any two
points on the line.
$$m = \frac{\text{rise}}{\text{run}} = \frac{y_2 - y_1}{x_2 - x_1}$$
A line that goes up from left to right has a positive gradient, and one that goes
down has a negative gradient. A horizontal line has gradient $0$, and a vertical
line has no gradient because the run is $0$.
---
id: gloss.rise
term: rise
The vertical change from one point to another. It is positive going up and
negative going down.
---
id: gloss.run
term: run
The horizontal change from one point to another. It is positive going right and
negative going left.
---
id: gloss.rate-of-change
term: rate of change
How fast one quantity changes compared with another. Its units are the first
quantity's units per unit of the second, such as dollars per hour. On a
straight-line graph, the rate of change is the gradient, and it is the same
everywhere on the line.
---
id: gloss.linear-relationship
term: linear relationship
A relationship whose graph is a straight line. It has a constant rate of change,
so equal steps in $x$ always give equal steps in $y$.
---
id: gloss.y-intercept
term: y-intercept
The point where a graph crosses the y-axis. You find it by putting $x = 0$. The
line $y = mx + c$ has its y-intercept at $(0, c)$.
---
id: gloss.x-intercept
term: x-intercept
The point where a graph crosses the x-axis. You find it by putting $y = 0$.
---
id: gloss.gradient-intercept-form
term: gradient-intercept form
us: slope-intercept form
The equation of a straight line written as $y = mx + c$, where $m$ is the gradient
and $c$ is where the line crosses the y-axis.
---
id: gloss.point-gradient-form
term: point-gradient form
us: point-slope form
The equation of a straight line written as $y - y_1 = m(x - x_1)$, where $m$ is the
gradient and $(x_1, y_1)$ is a point on the line.
---
id: gloss.general-form
term: general form
The equation of a straight line with the $x$ and $y$ terms on the same side, such as
$ax + by + c = 0$ or $Ax + By = C$. It is often the quickest form to use for
finding both intercepts.
---
id: gloss.model
term: model
A mathematical description of a real situation, such as an equation or a graph.
You use it to explain the situation or to make predictions. A model is only
useful where the assumptions it was built on still hold.
```

## Functions

```definitions
id: gloss.function
term: function
A rule that gives each input exactly one output. Two inputs can share an output,
but one input can never have two outputs.
---
id: gloss.input
term: input
A value you put into a function, usually called $x$.
---
id: gloss.output
term: output
The value a function gives back for an input, usually called $y$ or $f(x)$.
---
id: gloss.vertical-line-test
term: vertical line test
A way to check whether a graph shows a function. If any vertical line meets the
graph more than once, one input has two outputs, so the graph is not a function.
---
id: gloss.function-notation
term: function notation
Writing $f(x)$ for the output of the function $f$ when the input is $x$. So $f(3)$
means "the output when the input is $3$". It does not mean $f$ times $3$.
---
id: gloss.evaluate
term: evaluate
Work out the value. To evaluate $f(3)$, put $3$ in place of $x$ and calculate
the output.
---
id: gloss.solve
term: solve
Find every value of the variable that makes an equation true. To solve $f(x) = 3$,
find the input or inputs that give an output of $3$.
---
id: gloss.domain
term: domain
The set of all the inputs a function can take. In a real situation, the domain
holds only the inputs that make sense there.
---
id: gloss.range
term: range
The set of all the outputs a function actually gives.
In statistics, "range" means something different: the largest value in a data
set minus the smallest.
---
id: gloss.interval
term: interval
All the numbers between two endpoints, such as $2 \le x < 5$.
In statistics, a class interval is one of the groups that data is sorted into,
such as 10 to 19.
---
id: gloss.endpoint
term: endpoint
A number at either end of an interval. A closed endpoint is included, shown by a
filled dot or by $\le$ or $\ge$. An open endpoint is not included, shown by a
hollow dot or by $<$ or $>$.
---
id: gloss.parent-function
term: parent function
The simplest function in a family, with no transformation applied. $y = x$ is the
linear parent function, and $y = x^2$ is the quadratic parent function.
---
id: gloss.quadratic-function
term: quadratic function
A function where the highest power of $x$ is $2$, such as $y = x^2$ or
$y = 2x^2 - 3x + 1$. Its graph is a parabola.
---
id: gloss.parabola
term: parabola
The U-shaped curve that is the graph of a quadratic function. It is symmetrical
about a vertical line through its vertex.
---
id: gloss.vertex
term: vertex
The turning point of a parabola: its lowest point when the curve opens upward,
and its highest point when it opens downward.
In geometry, a vertex is also a corner point of a shape, where two sides meet.
```

## Transformations

```definitions
id: gloss.transformation
term: transformation
A change that moves, stretches or flips a shape or a graph. Translations,
stretches and reflections are all transformations.
---
id: gloss.translation
term: translation
A transformation that slides every point the same distance in the same
direction, without changing the shape. For a graph, $f(x) + k$ moves it up by
$k$, and $f(x - h)$ moves it right by $h$.
---
id: gloss.stretch
term: stretch
A transformation that pulls a graph away from an axis or squashes it towards
one. $a \cdot f(x)$ stretches it vertically by a factor of $a$, and $f(bx)$
stretches it horizontally by a factor of $\frac{1}{b}$.
---
id: gloss.reflection
term: reflection
A transformation that flips a shape or graph over a mirror line. For a graph,
$-f(x)$ reflects it in the x-axis, and $f(-x)$ reflects it in the y-axis.
---
id: gloss.vertex-form
term: vertex form
A quadratic written as $y = a(x - h)^2 + k$. Its vertex is at $(h, k)$. The number
$a$ sets the vertical stretch, and its sign sets whether the parabola opens up or
down.
```

## Rates of change and calculus

```definitions
id: gloss.average-rate-of-change
term: average rate of change
The change in a function's output divided by the change in its input, over an
interval from $x = a$ to $x = b$:
$$\frac{f(b) - f(a)}{b - a}$$
It is the gradient of the secant line through the two points.
---
id: gloss.secant-line
term: secant line
A straight line through two points on a curve. Its gradient is the average rate
of change between those two points.
---
id: gloss.tangent-line
term: tangent line
A straight line that touches a curve at a point and has the same steepness as the
curve there. Its gradient is the rate of change at that point. A tangent line
can meet the curve again somewhere else.
---
id: gloss.limit
term: limit
The value that a function's output gets closer and closer to as the input gets
closer to a number. $\lim_{x \to a} f(x) = L$ means $f(x)$ approaches $L$ as $x$
approaches $a$. The function does not have to be defined at $a$.
---
id: gloss.one-sided-limit
term: one-sided limit
A limit taken from one side only. $x \to a^-$ means $x$ approaches $a$ from below,
and $x \to a^+$ means from above. A limit exists only when both one-sided limits
exist and are equal.
---
id: gloss.difference-quotient
term: difference quotient
The average rate of change of $f$ from $x = a$ to $x = a + h$:
$$\frac{f(a + h) - f(a)}{h}$$
As $h$ gets closer to $0$, it approaches the gradient of the tangent line at
$x = a$.
---
id: gloss.derivative
term: derivative
The rate of change of a function at a point: the limit of the difference quotient
as $h \to 0$. $f'(a)$ is the gradient of the tangent line to $y = f(x)$ at $x = a$.
---
id: gloss.gradient-function
term: gradient function
The derivative $f'(x)$, treated as a function. For each $x$ it gives the gradient
of the graph of $f$ at that point. It is positive where $f$ is increasing and
negative where $f$ is decreasing.
---
id: gloss.differentiate
term: differentiate
To find the derivative of a function.
---
id: gloss.power-rule
term: power rule
The derivative of $x^n$ is $nx^{n-1}$. For example, the derivative of $x^3$ is
$3x^2$.
---
id: gloss.constant-function
term: constant function
A function whose output is the same for every input, such as $f(x) = 5$. Its
graph is a horizontal line, and its derivative is $0$.
```

## Number facts and measurement

```definitions
id: gloss.negative-number
term: negative number
A number less than zero. It is written with a negative sign in front, such as
$-5$, which is read "negative five". On a number line, negative numbers sit to the
left of zero.
---
id: gloss.number-line
term: number line
A straight line with numbers marked in order at equal spacing. Numbers get bigger
to the right and smaller to the left. Zero sits between the negative numbers and
the positive numbers.
---
id: gloss.square-number
term: square number
The result of multiplying a whole number by itself. $7 \times 7 = 49$, so $49$ is a
square number. It is written $7^2$ and read "seven squared".
---
id: gloss.square-root
term: square root
The positive number that, multiplied by itself, makes a given number. The square
root of $49$ is $7$, because $7 \times 7 = 49$. It is written $\sqrt{49} = 7$.
---
id: gloss.cube-number
term: cube number
The result of multiplying a whole number by itself three times.
$4 \times 4 \times 4 = 64$, so $64$ is a cube number. It is written $4^3$ and read
"four cubed".
---
id: gloss.cube-root
term: cube root
The number that, multiplied by itself three times, makes a given number. The cube
root of $64$ is $4$, because $4 \times 4 \times 4 = 64$. It is written
$\sqrt[3]{64} = 4$.
---
id: gloss.percentage
term: percentage
An amount out of 100, written with the percent sign %. The word percent means "out
of a hundred". 25% means 25 out of 100, which is the same as $\frac{25}{100}$ or
$0.25$.
---
id: gloss.decimal
term: decimal
A number written with a decimal point. The digits after the point show tenths,
hundredths, thousandths and so on. $3.25$ means 3 ones, 2 tenths and 5 hundredths.
---
id: gloss.tenth
term: tenth
One of ten equal parts of a whole: $\frac{1}{10}$, or $0.1$. In a decimal, the first
digit after the point counts tenths.
---
id: gloss.hundredth
term: hundredth
One of a hundred equal parts of a whole: $\frac{1}{100}$, or $0.01$. In a decimal,
the second digit after the point counts hundredths.
---
id: gloss.thousandth
term: thousandth
One of a thousand equal parts of a whole: $\frac{1}{1000}$, or $0.001$. In a
decimal, the third digit after the point counts thousandths.
---
id: gloss.kilo
term: kilo
A prefix on a metric unit's name that means a thousand of that unit. A kilometre
(km) is 1000 metres, and a kilogram (kg) is 1000 grams.
---
id: gloss.centi
term: centi
A prefix on a metric unit's name that means a hundredth of that unit. A
centimetre (cm) is a hundredth of a metre, so there are 100 cm in a metre.
---
id: gloss.milli
term: milli
A prefix on a metric unit's name that means a thousandth of that unit. A
millimetre (mm) is a thousandth of a metre, and a millilitre (mL) is a thousandth
of a litre.
```

## Geometry

```definitions
id: gloss.acute-angle
term: acute angle
An angle smaller than a right angle: less than 90°.
---
id: gloss.right-angle
term: right angle
An angle of exactly 90°, a quarter turn. A small square drawn in the corner marks a
right angle.
---
id: gloss.obtuse-angle
term: obtuse angle
An angle bigger than a right angle but smaller than a straight line: between 90° and
180°.
---
id: gloss.equilateral-triangle
term: equilateral triangle
A triangle with all three sides the same length. Its three angles are also all the
same.
---
id: gloss.isosceles-triangle
term: isosceles triangle
A triangle with at least two sides the same length. Matching tick marks show which
sides are equal.
---
id: gloss.scalene-triangle
term: scalene triangle
A triangle with all three sides different lengths.
---
id: gloss.acute-triangle
term: acute triangle
A triangle whose three angles are all smaller than 90°.
---
id: gloss.right-angled-triangle
term: right-angled triangle
us: right triangle
A triangle with one angle of exactly 90°.
---
id: gloss.obtuse-triangle
term: obtuse triangle
A triangle with one angle bigger than 90°.
---
id: gloss.quadrilateral
term: quadrilateral
A flat shape with four straight sides and four angles. Squares, rectangles and kites are all
quadrilaterals.
---
id: gloss.angle-sum
term: angle sum
The total of the angles inside a shape. The angle sum of every triangle is 180°, and the angle
sum of every quadrilateral is 360°.
---
id: gloss.diagonal
term: diagonal
A straight line segment joining two corners of a shape that are not next to each other.
```
