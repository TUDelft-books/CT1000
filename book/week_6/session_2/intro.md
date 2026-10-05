```{index} Force method; Class exercise for beam structures
```

````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_balk/lesoefeningen_2.html.

```
````

(lesson6.2)=
# Lesson October

During today's lesson you'll work on a complex exercise on the topic of force method for beam structures. Please ask your questions regarding the [homework](homework6.2) as well!

Consider the following structure:

```{figure} ./lesoefeningen_data/structure.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
```

Determine the force distribution and displacements.

We consider the following alternatives for transforming the structure into a statically determinate system:

- Replace the fixed support at $\rm{A}$ with a pin support and add a hinge at $\rm{C}$
- Remove the vertical support at $\rm{A}$
- Replace the fixed support at $\rm{A}$ with a pin support
- Add a hinge at $\rm{C}$
- Remove the vertical support at $\rm{B}$

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option in which the fixed support at $\rm{A}$ is replaced by a pin support and a hinge is added at $\rm{C}$
---
=

```{figure} ./lesoefeningen_data/optie_5.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option in which the vertical support at $\rm{A}$ is removed
---
=

```{figure} ./lesoefeningen_data/optie_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option in which the fixed support at $\rm{A}$ is replaced by a pin support
---
=

```{figure} ./lesoefeningen_data/optie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option in which a hinge is added at $\rm{C}$
---
=

```{figure} ./lesoefeningen_data/optie_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:name: optie3_balk
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option in which the vertical support at $\rm{B}$ is removed
---
=

```{figure} ./lesoefeningen_data/optie_4.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:number:
```

---

:::::

::::{question} Exercise
:variant: multiple-select
:admonition:
:class: exercise
:nocaption:

Which of the following is not a suitable option for making the structure statically determinate for analysis? Also exclude cases for which no standard beam formulas are available or the displacements are relatively complex
---
[x] Replace the fixed support at $\rm{A}$ with a pin support and add a hinge at $\rm{C}$
> Correct: this creates a mechanism, so it is not a valid statically determinate system.
[x] Remove the vertical support at $\rm{A}$
> Correct: no forget-me-not gives the displacements for this statically determinate system.
[x] Replace the fixed support at $\rm{A}$ with a pin support
> Correct: no forget-me-not gives the displacements for this statically determinate system.
[ ] Add a hinge at $\rm{C}$
> forget-me-nots are available for this case, but the right-hand segment will also rotate about $\rm{B}$, making it somewhat more complex than the other options.
[ ] Remove the vertical support at $\rm{B}$
---

::::


## Statically determinate system 1

Consider the following statically determinate system:

```{figure} ./lesoefeningen_data/SB-1.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2

```

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:

---
M[15]
^^^
? Apply the deformation condition to find $B_{\rm{v}}$.

$B_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)

---

::::

## Statically determinate system 2

Now consider the following statically determinate system:

```{figure} ./lesoefeningen_data/SB-2.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2

```

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:

---
M[45]
^^^
? Apply the deformation condition to find $M_{\rm{C}}$.

$M_{\rm{C}}= $ {gap} $\rm{kNm}$

---

::::

## Force distribution and displacements of the statically indeterminate structure

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:

---
M[-39]
M[72]
M[-15]
M[-72]
M[45]
M[39]
M[-15]
M[82.5]
M[-0.0225]

^^^
? Now determine the complete force distribution and displacements using the results from one or both of your statically determinate systems.

- $A_{\rm{v}}= $ {gap} $\rm{kN}$
- $A_{\rm{m}}= $ {gap} $\rm{kNm}$
- $B_{\rm{v}}= $ {gap} $\rm{kN}$
- $M_{\rm{A}}= $ {gap} $\rm{kNm}$
- $M_{\rm{C}}= $ {gap} $\rm{kNm}$
- $V_{\rm{AC}}= $ {gap} $\rm{kN}$
- $V_{\rm{CB}}= $ {gap} $\rm{kN}$
- $w_{\rm{C}}= $ {gap} $\rm{mm}$
- $\varphi_{\rm{C}}= $ {gap} $\rm{rad}$

---

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:

---
MAPE[24/13;0.01;3]

^^^
? Where is the point of contraflexure (where the curvature changes sign)?

$x_{\rm{buigpunt}}= $ {gap} $\rm{m}$

---

::::

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Draw the deformed statically **indeterminate** structure to scale
---
=

```{figure} ./lesoefeningen_data/disp.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
```

---

::::
