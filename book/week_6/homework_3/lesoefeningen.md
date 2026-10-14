````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_raamwerk/lesoefeningen.html.

```
````

# Guided exercise 1

Consider the following first-order statically indeterminate structure:

```{figure-start} ./lesoefeningen_data/oefening_1.svg
:align: center
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

- $EI_{\rm{AC}} = 2000 \ \rm{kNm^2}$
- $EI_{\rm{BC}} = \cfrac{2000 \sqrt{13}}{3} \ \rm{kNm^2}$
- $EA \gg EI $

```{figure-end}
```

::::{question} Exercise
:variant: multiple-select
:admonition:
:class: exercise
:nocaption:
:showanswer:
:columns: 1

The following statically determinate systems are given.

`````{grid} 2
:class-container: center-grid

````{grid-item}
:columns: auto

```{figure} ./lesoefeningen_data/statisch_bepaald_systeem_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

```` 
````{grid-item}

```{figure} ./lesoefeningen_data/statisch_bepaald_systeem_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```
 
````
`````

Why are these structures difficult to solve?

---
[ ] It is not possible to calculate displacements when a moment is applied.
> Incorrect. There are also forget-me-nots for beams subjected to moments.
[x] There are no forget-me-nots for this situation.
> Correct. Neither the overall structure nor its parts match a forget-me-not formula.
[ ] It is not possible to calculate displacements for a structure like this at all.
> Incorrect. Although there are no forget-me-nots for this structure, it can always be solved using differential equations or other methods.
---

::::

Let us solve the structure using the 'hoekveranderingsvergelijkingen' by adding a hinge at corner $\rm{C}$. However, an external couple also acts there, so we add the hinge just to the left of the joint:

```{figure-start} ./lesoefeningen_data/scharnier_links_C.svg
:align: center
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

- $EI_{\rm{AC}} = 2000 \ \rm{kNm^2}$
- $EI_{\rm{BC}} = \cfrac{2000 \sqrt{13}}{3} \ \rm{kNm^2}$
- $EA \gg EI $

```{figure-end}
```

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations of the statically determinate structure due to the moment pair $M_{\rm{C}}^{\rm{AC}}$
---
=

```{figure} ./lesoefeningen_data/verpl_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

:::{note}
Note that the displacements are drawn as if the hinge were right next to joint $\rm{C}$, although it is shown slightly farther from the joint.
:::

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations of the statically determinate structure due to the external couple of $30 \, \rm{kNm}$
---
=

```{figure} ./lesoefeningen_data/verpl_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

:::{note}
Note that the displacements are drawn as if the hinge were right next to joint $\rm{C}$, although it is shown slightly farther from the joint.
:::

---

:::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[0.001]
M[0]
M[-0.0005]
M[-0.015]
^^^
? Determine the rotations $\varphi_{\rm{C}}^{\rm{AC}}$ and $\varphi_{\rm{C}}^{\rm{BC}}$ as functions of $M_{\rm{C}}^{\rm{AC}}$, with $M_{\rm{C}}^{\rm{AC}}$ in $\rm{kNm}$ and $\varphi$ in $\rm{rad}$.

- $\varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot M_{\rm{C}}^{\rm{AC}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot M_{\rm{C}}^{\rm{AC}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$

---

::::

::::{admonition} Solution
:class: solution, dropdown

The expressions for the rotations can be found using the forget-me-not for a simply supported beam subjected to a moment.

$$ \varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = \cfrac{M_{\rm{C}}^{\rm{AC}} \cdot 6}{3 \cdot 2000} = 0.001 \cdot M_{\rm{C}}^{\rm{AC}} $$
$$ \varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = - \cfrac{\left(M_{\rm{C}}^{\rm{AC}} + 30 \right) \cdot \sqrt{13}}{3 \cdot \cfrac{2000 \cdot \sqrt{13}}{3}} = -0.0005 \cdot M_{\rm{C}}^{\rm{AC}} - 0.015  $$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-10]
^^^
? Apply the deformation condition to find $M_{\rm{C}}^{\rm{AC}}$.

$M_{\rm{C}}^{\rm{AC}}= $ {gap} $\rm{kNm}$

---

::::

::::{admonition} Solution
:class: solution, dropdown

The deformation condition is: $\varphi_{\rm{C}}^{\rm{AC}} = \varphi_{\rm{C}}^{\rm{BC}} \rightarrow M_{\rm{C}}^{\rm{AC}} = -10 \ \rm{kNm}$.

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-20]
^^^
? What is the moment just below joint $\rm{C}$? Give a positive answer for a moment that causes tension at the lower right side.

$M_{\rm{C}}^{\rm{BC}}= $ {gap} $\rm{kNm}$

---

::::

::::{admonition} Solution
:class: solution, dropdown

The moment is $-10 + 30 = 20 \ \rm{kNm}$, with compression at the lower right side.

::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Determine the bending-moment diagram for the structure
---
=

```{figure} ./lesoefeningen_data/Momentenlijn.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

---

:::::
