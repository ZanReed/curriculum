# Alignment sources — what the `alignment` values point at

Every `nzc_phase` and `ncea` value in the graph is a pointer into one of the documents below.
This file holds the quoted statement each pointer resolves to, so the claim can be checked
against the source rather than against anyone's memory. **Read 2026-09-02.** The NZC pages
are live documents; if a statement here no longer matches the page, the page wins and the
graph value is stale.

Value grammar:

- `nzc_phase`: `P<phase>.Y<year>.<Strand>` — phase and year of the New Zealand Curriculum
  (Te Mātaiaho) Mathematics and Statistics teaching sequence, mandatory for Years 0–10 in all
  state and state-integrated schools from Term 1, 2026.
- `ncea`: `AS<number>` — an NCEA achievement standard as registered by NZQA.

Neither value is checkable by CI. The field makes the claim recordable (D24 audit, §2), and
whether a DoL actually assesses at the level the standard asks is a human read.

---

## New Zealand Curriculum — Phases

| phase | years |
|---|---|
| P1 | Years 0–3 |
| P2 | Years 4–6 |
| P3 | Years 7–8 |
| P4 | Years 9–10 |
| P5 | Years 11–13 — **draft only**; mandatory 2028 (Y11), 2029 (Y12), 2030 (Y13) |

Source: NZC Mathematics and Statistics Phases 1–4 overview,
`https://newzealandcurriculum.tahurangi.education.govt.nz/nzc---mathematics-and-statistics-years-0-8/5637238338.p`
and MoE, *Years 0-10 English, Te Reo Rangatira, Maths and Pāngarau* (19 Oct 2025),
`https://tahurangi.education.govt.nz/final_y0to10_english_maths`.

### P3 — Years 7–8

Page: `https://newzealandcurriculum.tahurangi.education.govt.nz/5637238342.p`

**P3.Y7.Number**
> A fraction can describe a proportional relationship between two amounts.

> Using proportional reasoning to explore multiplicative relationships between quantities
> (e.g. "If there are 3 red for every 7 blue balls, how many balls are there altogether when
> there are 18 red balls?")

**P3.Y8.Number**
> Ratios can be used to describe proportional relationships and unequal division of a whole.

> Ratios, fractions, and percentages can all represent proportional relationships between two
> quantities.

> Dividing a quantity into two parts, given the part:part or part:whole ratio

> Expressing the division of quantity into two parts as a ratio

**P3.Y7.Algebra**
> A variable can be used to represent: an unknown number, often in formulae (e.g. s in s²); a
> quantity that can vary or change (e.g. y = 3x + 4; A = bh); a specific unknown value to be
> solved (e.g. 3a = 18).

> A coordinate plane extends to 4 quadrants that meet at the origin (0, 0).

> Linear patterns have a constant increase or decrease, can be described by the rule
> t = a × n + d, and can be graphed as a straight line on a coordinate plane.

> Identifying and plotting points in the four quadrants of the coordinate plane, using ordered
> pairs and values from a table

> Using tables, graphs in the coordinate plane, and diagrams to recognise the relationship
> between the ordinal position and its corresponding element in a linear pattern, develop a
> rule for the pattern in words, and make conjectures about further elements in the pattern

**P3.Y8.Algebra**
> Using substitution to find the value of an expression or formula (e.g. calculating w + 12
> given w = 4)

> Forming and solving linear equations with rational solutions (e.g. t + 7 = 6.5,
> 5s + 9 = −18)

> Investigating the patterns of triangular numbers, square numbers, and cube numbers,
> extending the patterns, creating tables of values, and plotting the values on the
> coordinate plane

*Note the absence:* there is no Year 8 statement about rates, "per", unit rates, or a line
through the origin. Year 8 is ratio and part:whole; **rates arrive at Year 9.** The
`rate.*` chain's `band_nz: Y8` is therefore the proportional-reasoning reading of Phase 3,
not a literal placement — see D32 and the open question on the middle of the spine.

### P4 — Years 9–10

Page: `https://newzealandcurriculum.tahurangi.education.govt.nz/5637291579.p`

**P4.Y9.Number**
> A rate proportionally compares two quantities that have different units of measure; when
> working with rates, 'per' means 'for every' in day-to-day contexts.

> Comparing and using ratios and rate (e.g. finding speed, given distance and time)

**P4.Y10.Number**
> Representing proportional relationships using whole-number ratios, including reducing the
> ratios to their simplest form

**P4.Y9.Algebra**
> For a specific straight line, the gradient, m, and y-intercept, c, are fixed, and x varies
> with y according to the rule y = mx + c. The y-intercept touches the y-axis and has
> coordinates (0, c).

> The constant rate of change of a linear graph is the vertical change (how far it goes up or
> down) divided by the horizontal change (how far it moves sideways).

> Interpreting rules of the form y = mx + c and using a combination of substitution and
> tables to plot points from the linear graph

> Identifying the constant increase or decrease in a linear pattern

> … tables and graphs in the coordinate plane (showing all four quadrants)

**P4.Y10.Algebra**
> The gradient m of a straight line can be determined with the formula m = rise/run = Δy/Δx.

> Interpreting and graphing linear equations in the form y = mx + c, using the gradient and
> y-intercept

> Calculating the gradient and y-intercept of a line, using a graph

> Solving quadratic equations that are factorised or of the form x² + c = 0 (where c is an
> integer), and connecting the solutions to the x-intercepts

> Determining the effect on graphs in the coordinate plane of changing the coefficient of x²
> and the fixed value c, for a range of quadratic equations

*Note the absences:* no function notation, no domain/range, no exponential graphs, no
point–gradient or general form of a line anywhere in Years 9–10. Those enter at Phase 5 and
are assessed by Level 1–2 standards below.

### P5 — Years 11–13

Draft content was due for feedback in Term 1 2026. Subject descriptors are published
(`https://newzealandcurriculum.tahurangi.education.govt.nz/new-zealand-curriculum-years-11-13-subject-descriptors/5637350826.p`):
Year 11 *Mathematics & Statistics*; Years 12–13 *Mathematics | Pāngarau*, *Mathematical and
Statistical Modelling*, *Statistics and Data Science*, *Further Mathematics* (Y13, additional).
This thread's spine maps to Y11 Mathematics & Statistics → Y12–13 *Mathematics*. No
year-by-year P5 statements were reachable on 2026-09-02, so **no `P5.*` values are used**;
the NCEA standards carry the Y11–13 alignment instead.

---

## NCEA achievement standards

All read from NZQA on 2026-09-02. Grades N / A / M / E; Merit is *relational thinking*,
Excellence is *extended abstract thinking* (SOLO wording, identical across L1–L3).

| id | level | title | credits | mode |
|---|---|---|---|---|
| AS91944 | 1 | Explore data using a statistical enquiry process | 5 | internal |
| AS91945 | 1 | Use mathematical methods to explore problems that relate to life in Aotearoa New Zealand or the Pacific | 5 | internal |
| AS91946 | 1 | Interpret and apply mathematical and statistical information in context | 5 | external |
| AS91947 | 1 | Demonstrate mathematical reasoning | 5 | external |
| AS91256 | 2 | Apply co-ordinate geometry methods in solving problems | 2 | internal |
| AS91257 | 2 | Apply graphical methods in solving problems | 4 | internal |
| AS91261 | 2 | Apply algebraic methods in solving problems | 4 | external |
| AS91262 | 2 | Apply calculus methods in solving problems | 5 | external |
| AS91578 | 3 | Apply differentiation methods in solving problems | 6 | external |

AS91256's title and credits are from the standard NZQA listing and were **not** re-read on
2026-09-02; the three `linear.form.*` pointers to it are the weakest in the graph (see D32).

### AS91945 — achievement criteria (verbatim)

| Achievement | Merit | Excellence |
|---|---|---|
| Use mathematical methods to explore problems that relate to life in Aotearoa New Zealand or the Pacific | … by applying relational thinking | … by applying extended abstract thinking |

Explanatory notes: Achieved — uses appropriate mathematical methods and communicates accurate
mathematical information related to the context. Merit (relational thinking) — applies
methods using logical connections and communicates through appropriate mathematical
statements. Excellence (extended abstract thinking) — extends methods using logical
connections to explore or solve a problem by considering limitations, assumptions,
generalisations, or predictions.
Source: `https://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2024/as91945.pdf`

### Level 1 subject learning outcomes (MoE, 2024) — the lines the pointers use

Source: *Mathematics and Statistics NCEA Level 1 Subject Learning Outcomes*,
ncea.education.govt.nz (April 2024).

Under 1.2 / AS91945:
> operate with more complex rates and ratios involving metric unit conversions to solve
> problems

> graph linear, quadratic, and exponential functions from patterns, tables, and equations

> interpret features of linear, quadratic, and exponential graphs in relation to the equation
> or the situation including x and y intercepts, gradient, vertices, asymptotes, symmetry

> find the equations for linear and quadratic functions, including horizontal and vertical
> lines, from patterns, tables or graphs

> make links between different representations for the same model for example, connects an
> equation, table and graph for distance-time graphs

Under 1.4 / AS91947:
> relate graphs, tables, equations, and patterns, which includes: graphing linear, quadratic,
> and exponential functions from patterns, tables, and equations

> interpreting features of linear, quadratic, and exponential graphs in relation to the
> equation or the situation including x and y intercepts, gradient, vertex, asymptote,
> symmetry

> finding the equations for linear and quadratic functions, including horizontal and
> vertical lines, from patterns, tables or graphs

> relate rate of change to the gradient of a graph, which includes interpreting rates of
> change from contextual graphs

AS91946 (external, 2026 specification): resource booklet of data representations; three
multi-part questions; *"Candidates must bring a ruler and an approved calculator."*
Source: `https://www.nzqa.govt.nz/nqfdocs/ncea-resource/specifications/2026/91946-spc-2026.pdf`

### AS91257 — explanatory notes (methods)

> graphs at curriculum Level 7, their features and their equations; transformations of
> graphs; connecting different representations of relations; properties of functions (may
> include domain and range)

Source: `https://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2019/as91257.pdf`

### AS91262 — explanatory notes (methods)

Derivatives and anti-derivatives of polynomials in expanded form; gradient functions and the
gradient at a point; equations of tangents; turning points where f′(x) = 0 and their nature;
reconstructing a function from its derived function; *rate of change problems (such as
kinematics)*. 2026 specification adds: draw gradient-function graphs from function graphs or
vice versa; justify maxima/minima. **Limits are not listed.**
Sources: `https://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2019/as91262.pdf`,
`https://www.nzqa.govt.nz/nqfdocs/ncea-resource/specifications/2026/91262-spc-2026.pdf`

### AS91578 — explanatory notes (methods)

Derivatives of power, exponential and logarithmic (base e) functions; trigonometric and
reciprocal trigonometric functions; chain, product and quotient rules; optimisation;
equations of normals; maxima, minima and points of inflection; related rates of change;
parametric functions; **graph properties including limits, differentiability, continuity and
concavity.**
Source: `https://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2019/as91578.pdf`

---

## The qualification timeline the locales encode

- 4 Aug 2025 — Government announces NCEA will be replaced (subject-based; A–E letter grades;
  no fully internally assessed subjects).
- 19 Oct 2025 — Years 0–10 curriculum finalised; mandatory Term 1 2026.
- 26 Mar 2026 — Beehive confirms next steps; grading methodology and internal/external
  balance deferred to "Tranche 2".
  `https://www.beehive.govt.nz/release/government-confirms-next-steps-new-senior-secondary-qualification`
- 16 May 2026 — MoE: Foundational Award (Y11, literacy and numeracy, Maths compulsory) 2028;
  NZCE (Y12) 2029; NZACE (Y13) 2030. "The current Year 9 cohort will be the first full cohort
  through the system." Y12–13: at least five subjects, pass at least three.
  `https://ncea.education.govt.nz/whats-new/further-details-new-senior-secondary-qualifications`
  `https://www.education.govt.nz/news/ncea-update-structure-new-qualification-system-agreed`

Cohort consequence, stated once here and cited by the locales:

| in 2026 | Y11 | Y12 | Y13 | sits |
|---|---|---|---|---|
| Year 8 | 2029 | 2030 | 2031 | new system only |
| Year 9 | 2028 | 2029 | 2030 | new system only |
| Year 10 | 2027 | 2028 | 2029 | NCEA L1, L2, L3 |
| Year 11 | 2026 | 2027 | 2028 | NCEA L1, L2, L3 |
