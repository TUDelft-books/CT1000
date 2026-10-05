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
:showanswer:

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
:showanswer:

---
M[15]
^^^
? Apply the deformation condition to find $B_{\rm{v}}$.

$B_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)

---

::::

::::{admonition} Worked-out solution
:class: solution, dropdown

Using the given free-body diagram, the shear force just to the left of C, the moment at C, and the shear force just to the left of B can be determined as functions of $B_{\rm{v}}$:

$$ V_{\rm{C}}^{\rm{AC}} \left( B_{\rm{v}} \right) = -1 \cdot B_{\rm{v}} + 54 $$
$$ M_{\rm{C}} \left( B_{\rm{v}} \right) = -3 \cdot B_{\rm{v}} $$ 
$$ V_{\rm{B}}^{\rm{BC}} \left( B_{\rm{v}} \right) = -1 \cdot B_{\rm{v}} $$

The deflection $w_{\rm{C}}$ and rotation $\varphi_{\rm{C}}$ at C can be found by moving the force $B_{\rm{v}}$ from B to C and adding a moment, as shown in the free-body diagram below:

```{figure} ./lesoefeningen_data/VrijlichaamsschemaAC_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
```

Using the forget-me-nots for a cantilever beam subjected to a force and a moment gives:

$$ w_{\rm{C}} \left( B_{\rm{v}} \right) = \cfrac{\left(54 - B_{\rm{v}} \right) \cdot 3^3}{3 \cdot 1800} - \cfrac{3 \cdot B_{\rm{v}} \cdot 3^2}{2 \cdot 1800} = -0.0125 \cdot B_{\rm{v}} + 0.27 $$
$$ \varphi_{\rm{C}} \left( B_{\rm{v}} \right) = -\cfrac{\left(54 - B_{\rm{v}} \right) \cdot 3^2}{2 \cdot 1800} + \cfrac{3 \cdot B_{\rm{v}} \cdot 3}{1800} = 0.0075 \cdot B_{\rm{v}} - 0.135 $$

The deflection at B, $w_{\rm{B}}$, is therefore:

$$ w_{\rm{B}} \left( B_{\rm{v}} \right) = w_{\rm{C}} - \varphi_{\rm{C}} \cdot 3 - \cfrac{B_{\rm{v}} \cdot 3^3}{3 \cdot 900} = -0.045 \cdot B_{\rm{v}} + 0.675 $$

The deformation condition is: $w_{\rm{B}} = -0.045 \cdot B_{\rm{v}} + 0.675 = 0$.

This gives $B_{\rm{v}} = 15 \rm{kN}$.

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
:showanswer:

---
M[45]
^^^
? Apply the deformation condition to find $M_{\rm{C}}$.

$M_{\rm{C}}= $ {gap} $\rm{kNm}$

---

::::

::::{admonition} Worked-out solution
:class: solution, dropdown

The expressions for $B_{\rm{v}}$ and $V_{\rm{C}}^{\rm{AC}}$ can be derived from equilibrium of segment BC.

$$ \sum \left. T \right| _ {\rm{C}} ^{\rm{CB}} = - 3 \cdot B_{\rm{v}} - M_{\rm{C}} = 0 \rightarrow B_{\rm{v}} = - \cfrac{1}{3} \cdot M_{\rm{C}} $$
$$ V_{\rm{C}}^{\rm{AC}} = B_{\rm{v}} + 54 = - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 $$

The rotation just to the left of C, $\varphi_{\rm{C}}^{\rm{AC}}$, and the deflection at C, $w_{\rm{C}}$, can be determined using the forget-me-nots for a cantilever beam subjected to a moment and a point load, as shown in the free-body diagram below:

```{figure} ./lesoefeningen_data/VrijlichaamsschemaAC_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
```

$$ \varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}} \right) = \cfrac{M_{\rm{C}} \cdot 3}{1800} - \cfrac{\left( - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 \right) \cdot 3^2}{2 \cdot 1800} = 0.0025 \cdot M_{\rm{C}} - 0.135 $$

$$ w_{\rm{C}} \left( M_{\rm{C}} \right) = - \cfrac{M_{\rm{C}} \cdot 3^2}{2 \cdot 1800} + \cfrac{\left( - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 \right) \cdot 3^3}{3 \cdot 1800} = -0.00417 \cdot M_{\rm{C}} + 0.27 $$

The rotation just to the right of C, $\varphi_{\rm{C}}^{\rm{BC}}$, is caused by the bending of segment BC due to $M_{\rm{C}}$ and by the deflection at C, $w_{\rm{C}}$:

:::{fetch} {numref}`optie3_balk`
:::

The rotation due to bending can be determined using the forget-me-nots for a simply supported beam subjected to a moment.

$$ \varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}} \right) = \cfrac{w_{\rm{C}}}{3} - \cfrac{M_{\rm{C}} \cdot 3}{3 \cdot 900} = 0.0025 \cdot M_{\rm{C}} -0.09 $$


The deformation condition is: $\varphi_{\rm{C}}^{\rm{AC}} = \varphi_{\rm{C}}^{\rm{BC}} \rightarrow 0.0025 \cdot M_{\rm{C}} - 0.135 = -0.0025 \cdot M_{\rm{C}} + 0.09$.

This gives $M_{\rm{C}} = 45 \rm{kNm}$.

::::

## Force distribution and displacements of the statically indeterminate structure

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

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
:showanswer:

---
MAPE[24/13;0.01;3]

^^^
? Where is the point of contraflexure (where the curvature changes sign)?

$x_{\rm{buigpunt}}= $ {gap} $\rm{m}$

---

::::

::::{admonition} Worked-out solution
:class: solution, dropdown

The slope of the bending-moment diagram between $\rm{A}$ and $\rm{C}$ is equal to the shear force, $V_{\rm{AC}} = 39 \, \rm{kN}$. Thus, the bending moment is zero at $x_{\rm{buigpunt}} = \cfrac{M_{\rm{A}}}{V_{\rm{AC}}} = \cfrac{72}{39} = \cfrac{24}{13} \approx 1.85 \, \rm{m}$.

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
