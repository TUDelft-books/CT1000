````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_balk/lesoefeningen.html.

```
````

# Guided exercise

Consider the following structure:

```{figure-start} ./bending_data/Example.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
---

```

- $EI = \cfrac{16}{3} \ \rm{MNm^2}$
- $EA \gg EI $

```{figure-end}
```

Determine the force distribution and displacements.

Use the following statically determinate system:

```{figure-start} ./bending_data/SB-systeem2.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
---

```

- $EI = \cfrac{16}{3} \ \rm{MNm^2}$
- $EA \gg EI $

```{figure-end}
```

The deformations due to the force $A_{\rm{v}}$ were already sketched in the instructions.

:::{fetch} {numref}`optie2_balk`
:::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations due to the distributed load on the statically determinate structure
---
=

```{figure} ./bending_data/disp_25.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
:number:
```

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
M[4]
M[-200]
M[0.0015]
M[-0.075]
M[0.01]
M[-0.45]
^^^
? Determine the axial forces in all members as a function of $A_{\rm{v}}$, with $A_{\rm{v}}$ in $\rm{kN}$, $M_{\rm{B}}$ in $\rm{kNm}$, $\varphi_{\rm{B}}$ in $\rm{rad}$ and $w_{\rm{A}}$ in $\rm{m}$.

- $M_{\rm{B}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◡)
- $\varphi_{\rm{B}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↻)
- $w_{\rm{A}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (↑)

---

::::

::::{admonition} Worked-out solution
:class: solution, dropdown

```{figure} bending_data/VrijlichaamsschemaBC.svg
---
align: center
number:
---
```

$$ M_{\rm{B}} \left( A_{\rm{v}} \right) = 4 \cdot A_{\rm{v}} -200 $$

The rotation at $\rm{B}$, $\varphi_{\rm{B}}$, can be determined from $M_{\rm{B}}$ using the forget-me-not for a simply supported beam subjected to a moment:

```{figure} bending_data/BC.svg
---
align: center
number:
---
```

$$ \varphi_{\rm{B}} \left( A_{\rm{v}} \right) = \cfrac{1}{3} \cdot \cfrac{\left(4 \cdot A_{\rm{v}} -200\right) \cdot6}{\cfrac{16}{3} \cdot 10^3} = 0.0015 \cdot A_{\rm{v}} -0.0750 $$

The deflection at $\rm{A}$, $w_{\rm{A}}$, can be determined by inclining the fixed end of segment $\rm{AB}$ at $\rm{B}$ by the angle $\varphi_{\rm{B}}$, and accounting for the deflections caused by the distributed load and $A_{\rm{v}}$. To do this, use the forget-me-not for a cantilever beam subjected to a distributed load and a cantilever beam subjected to a point load:

$$ w_{\rm{A}} \left( A_{\rm{v}} \right) = \varphi_{\rm{B}} \cdot 4 - \cfrac{25 \cdot 4^4}{8 \cdot \cfrac{16}{3} \cdot 10^3} + \cfrac{A_{\rm{v}} \cdot 4^3}{3 \cdot \cfrac{16}{3} \cdot 10^3}  =0.01 \cdot A_{\rm{v}} -0.45 $$

::::

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
? Apply the deformation condition to find $A_{\rm{v}}$.

$A_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)

---

::::

::::{admonition} Worked-out solution
:class: solution, dropdown

The deformation condition is: $w_{\rm{A}} = 0.01 \cdot A_{\rm{v}} -0.45 = 0$.

This gives $A_{\rm{v}} = 45 \rm{kN}$.

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAPE[175/3;0.1;4]
MAPE[-10/3;0.1;2]
M[20]
M[-40]
M[-0.0075]
M[11.875]
M[-8.4375]

^^^
? Now solve for the other support reactions and determine the moments and displacements.

- $B_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)
- $C_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)
- $M_{\rm{B}}= $ {gap} $\rm{kNm}$ (◠)
- $M_{\rm{halverwege \ AB}}= $ {gap} $\rm{kNm}$ (◠)
- $\varphi_{\rm{B}}= $ {gap} $\rm{rad}$ (↻)
- $w_{\rm{halverwege \ AB}}= $ {gap} $\rm{mm}$ (↓)
- $w_{\rm{halverwege \ BC}}= $ {gap} $\rm{mm}$ (↓)

---

::::

::::{admonition} Worked-out solution
:class: solution, dropdown

Now that $A_{\rm{v}}$ is known, the other support reactions can be determined. Take $B_{\rm{v}}$ and $C_{\rm{v}}$ as positive upwards. The equations used are:

$$ \sum \left. T \right|  _ {\rm{C}} = -45 \cdot 10 + 25 \cdot 4 \cdot 8 - B_{\rm{v}} \cdot 6 = 0 \rightarrow B_{\rm{v}} = 58.3 \, \rm{kN} $$ 

$$ \sum F_ {\rm{v}} = 45 - 4 \cdot 25 + 58.3 + C_{\rm{v}} = 0 \rightarrow C_{\rm{v}} = -3.3 \, \rm{kN} $$

The moment $M_{\rm{B}}$ can be determined by summing moments about B for segment AB, giving $M_{\rm{B}} = - 20 \, \rm{kNm}$. Similarly, $M_{\rm{halverwege \ AB}}$ can be determined by summing moments about the midpoint of AB: $M_{\rm{halverwege \ AB}} = 40 \, \rm{kNm}$.

The deflection at the midpoint of AB, $w_{\rm{halverwege} \ \rm{AB}}$, can be found in several ways. Here, it is determined using the forget-me-not for a simply supported beam subjected to a moment and a simply supported beam subjected to a distributed load.

$$ w_{\rm{halverwege \ AB}} = \cfrac{5}{384} \cdot \cfrac{25 \cdot 4^4}{\cfrac{16}{3}} - \cfrac{1}{16} \cdot \cfrac{20 \cdot 4^2}{\cfrac{16}{3}} = 11.875 \, \rm{mm} $$

The deflection at the midpoint of BC can be determined using the forget-me-not for a simply supported beam subjected to a moment:

$$ w_{\rm{halverwege \ BC}} =  - \cfrac{1}{16} \cdot \cfrac{20 \cdot 6^2}{\cfrac{16}{3}} = -8.4375 \, \rm{mm} $$

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

```{figure} ./bending_data/disp.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
```

This is exactly the same drawing as when the structure is solved using the 'hoekveranderingsvergelijkingen' method
---

::::
