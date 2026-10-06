````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/temperatuur/lesoefening.html

```
````

# Guided exercise 1

Consider the following structure:

```{figure-start} ./lesoefening_data/structure.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur3
:number:
```

- $EI = \cfrac{800}{3} \ \rm{kNm^2}$
- $\Delta T = 30 \ ^{\circ} \rm{C}$
- $h = 0.2 \ \rm{m}$
- $\alpha = 10^{-4} \ ^{\circ} \rm{C}^{-1}$

```{figure-end}
```

We will analyse this structure using differential equations.

::::::{question} Exercise
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Sketch the curvature distribution due to the temperature change.

---
=

```{figure} ./lesoefening_data/kromming.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur3
:number:
```

---

::::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-0.015]
^^^
?
What is the curvature due to the temperature change?

$\kappa_{\rm{T}} = $ {gap} $\rm{m}^{-1}$

---
::::

::::{admonition} Solution
:class: solution, dropdown

$$\kappa^T = -\cfrac{\alpha \cdot T}{h} = - \cfrac{0.0001 \cdot 30}{0.2} = -0.015 \ m^{-1}$$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[1]
M[0.00375]
M[0.0075]
M[0.001875]
M[0.0075]
M[-0.000625]
M[-0.00375]
M[-1]

^^^
?
Use the differential equations to determine expressions for the internal forces and displacements. Note that two boundary conditions ($M\left(0\right) = 6$ and $w\left(0\right) = 0$) have already been applied. Use $\rm{kN}$, $\rm{m}$ and $\rm{rad}$ as units.

- $V\left( x  \right) = C_1 $
- $M\left( x  \right) = $ {gap} $ \cdot C_1 \cdot x + 6 $
- $ \kappa \left( x \right) = $ {gap} $ \cdot C_1 \cdot x+ $ {gap}
- $ \varphi \left( x \right) = $ {gap} $ \cdot C_1 \cdot x^2 + $ {gap} $ \cdot x + C_3 $
- $ w \left( x \right) = $ {gap} $ \cdot C_1 \cdot x^3 + $ {gap} $ \cdot x^2 + $ {gap} $ \cdot C_3 \cdot x + 0 $

---
::::

::::{admonition} Solution
:class: solution, dropdown

The following boundary conditions apply to this structure:

$$ w \left( 0 \right) = 0 $$
$$ M \left( 0 \right) = +6 \rm{kNm} $$
$$ w \left( 8 \right) = 0 $$
$$ \varphi \left( 8 \right) = 0 $$

This gives the following expressions for the internal forces and displacements:

$$ V\left( x  \right) = C_1 $$ 
$$ M\left( x  \right) = C_1 \cdot x + 6 $$
$$ \kappa \left( x \right) = \cfrac{M}{EI} = \cfrac{3}{800} \cdot C_1 \cdot x + \cfrac{6 \cdot 3}{800} - 0.015 = 0.00375 \cdot C_1 \cdot x + 0.0075 $$
$$ \varphi \left( x \right) = 0.001875  C_1 \cdot x^2 + 0.0075 \cdot x + C_3 $$
$$ w \left( x \right) = -0.000625 \cdot C_1 \cdot x^3 -0.00375 \cdot x^2 - C_3 \cdot x + 0 $$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-0.375]
M[-0.015]
^^^
?
What is the curvature due to the temperature change?

- $C_1 = $ {gap} $\rm{kNm}$
- $C_3 = $ {gap} $\rm{rad}$

---
::::

:::::{question} Exercise
:nocaption:
:showanswer:
:columns: 1
:admonition:
:class: exercise


As the temperature increases further, the absolute value of the maximum displacement becomes one of the following
---
[ ] Greater
[ ] Smaller
[ ] First greater, then smaller
[x] First smaller, then greater
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
MAPE[16/3;0.01;3]
^^^
?
The deformation has a point of contraflexure. Where is it?

$x_{\rm{buigpunt}} = $ {gap} $\rm{m}$

---
::::
