````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/steunpuntszetting_stijfheden/lesoefeningen_2.html

```
````

# Guided exercise 2

Consider the following structure:

```{figure-start} ./lesoefeningen_data/structure.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:figclass: sticky-margin
```
$EI = \cfrac{250}{3} \ \rm{MNm}^2$

```{figure-end}
```

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[2]
^^^
?
The structure is {gap}st/nd/rd/th order internally statically indeterminate.

---
::::

## Limiting cases

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[0]
M[0]
M[0]
M[0]
M[0]
M[0]
M[25]
M[0]
^^^
? For the case $nEI \to 0$, determine the force distribution and displacements:

- $A_{\rm{v}} \left( nEI \to 0 \right)= $ {gap} $\rm{kN}$ (↑)
- $B_{\rm{v}} \left( nEI \to 0 \right)= $ {gap} $\rm{kN}$ (↑)
- $C_{\rm{v}} \left( nEI \to 0 \right)= $ {gap} $\rm{kN}$ (↑)
- $D_{\rm{v}} \left( nEI \to 0 \right)= $ {gap} $\rm{kN}$ (↑)
- $M_{\rm{B}} \left( nEI \to 0 \right)= $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{D}} \left( nEI \to 0 \right)= $ {gap} $\rm{kNm}$ (◡)
- $w_{\rm{halverwege \ AB}} \left( nEI \to 0 \right)= $ {gap} $\rm{mm}$ (↓)
- $w_{\rm{halverwege \ CD}} \left( nEI \to 0 \right)= $ {gap} $\rm{mm}$ (↓)

---

::::

::::{admonition} Solution
:class: solution, dropdown

If segment $\rm{BC}$ has no flexural stiffness, the structure effectively consists of two separate small beams, and the left one deflects by 25 $\rm{mm}$. This gives the following forces and displacements:

- $A_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$
- $B_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$
- $C_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$
- $D_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$
- $M_{\rm{B}} \left( nEI \to 0 \right) = 0 \rm{kNm}$
- $M_{\rm{D}} \left( nEI \to 0 \right) = 0 \rm{kNm}$
- $w_{\rm{halverwege} \ \rm{AB}} \left( nEI \to 0 \right) = 25 \rm{mm}$
- $w_{\rm{halverwege} \ \rm{CD}} \left( nEI \to 0 \right) = 0 \rm{mm}$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[6.25]
M[-18.75]
M[18.75]
M[-6.25]
M[62.5]
M[-62.5]
M[29.6875]
M[-4.6875]
^^^
? For the case $nEI \to \infty$, determine the force distribution and displacements:

- $A_{\rm{v}} \left( nEI \to \infty \right)= $ {gap} $\rm{kN}$ (↑)
- $B_{\rm{v}} \left( nEI \to \infty \right)= $ {gap} $\rm{kN}$ (↑)
- $C_{\rm{v}} \left( nEI \to \infty \right)= $ {gap} $\rm{kN}$ (↑)
- $D_{\rm{v}} \left( nEI \to \infty \right)= $ {gap} $\rm{kN}$ (↑)
- $M_{\rm{B}} \left( nEI \to \infty \right)= $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{D}} \left( nEI \to \infty \right)= $ {gap} $\rm{kNm}$ (◡)
- $w_{\rm{halverwege \ AB}} \left( nEI \to \infty \right)= $ {gap} $\rm{mm}$ (↓)
- $w_{\rm{halverwege \ CD}} \left( nEI \to \infty \right)= $ {gap} $\rm{mm}$ (↓)

---

::::

::::{admonition} Solution
:class: solution, dropdown

The following statically determinate system is chosen, with hinges and unknown moment pairs added at $\rm{B}$ and $\rm{C}$.

```{figure-start} ./lesoefeningen_data/SB_systeem1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
```

- $EI_{\rm{AB}} = EI_{\rm{CD}} = \cfrac{250}{3} \ \rm{MNm^2}$
- $EI_{\rm{BC}} = \infty$

```{figure-end}
```

The corresponding deformation conditions are:

- $\varphi_{\rm{B}}^{\rm{AB}}=\varphi_{\rm{B}}^{\rm{BC}}$
- $\varphi_{\rm{C}}^{\rm{BC}}=\varphi_{\rm{C}}^{\rm{CD}}$

Because segment $\rm{BC}$ is infinitely stiff, $\varphi_{\rm{B}}^{\rm{BC}}=\varphi_{\rm{C}}^{\rm{BC}}=\cfrac{25}{10000}=0.0025\rm{rad}$.

Using the forget-me-not for a simply supported beam subjected to a moment gives: $\varphi_{\rm{B}}^{\rm{AB}}=\cfrac{M_{\rm{B}}\cdot10}{3\cdot\cfrac{250}{3}\cdot1000} \rightarrow M_{\rm{B}}=62.5 \rm{kNm}$.

Moment equilibrium of segment $\rm{AB}$ gives: $\sum \left. T \right| _ {\rm{B}} ^{\rm{AB}} = - A_{\rm{v}} \cdot 10 + 62.5=0 \rightarrow A_{\rm{v}} =6.25 \rm{kN}$.

By symmetry, $M_{\rm{C}}=-M_{\rm{B}}=-62.5 \rm{kNm}$ and $D_{\rm{v}}=-A_{\rm{v}}=-6.25 \rm{kN}$.

Moment equilibrium of the entire structure now gives $B_{\rm{v}}=-18.75 \rm{kN}$ and $C_{\rm{v}}=18.75 \rm{kN}$.

The deflections at the midpoints of segments $\rm{AB}$ and $\rm{CD}$ can be determined by superposing the bending deformation and the support settlements.

- $w_{\rm{halverwege} \ \rm{AB}} = 25 + \cfrac{62.5\cdot 10^2}{16\cdot\cfrac{250}{3}}=29.6875 \ \rm{mm}$
- $w_{\rm{halverwege} \ \rm{CD}} = - \cfrac{62.5\cdot 10^2}{16\cdot\cfrac{250}{3}}=-4.6875 \ \rm{mm}$

::::

## Scaling factor

For a variable $n$, use the following statically determinate system:

```{figure-start} ./lesoefeningen_data/SB.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:figclass: sticky-margin
```

$EI = \cfrac{250}{3} \ \rm{MNm}^2$

```{figure-end}
```

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[25]
M[0]
^^^
? What are the deformation conditions?

- Bij $\rm{A}: w_A = $ {gap} $\rm{mm}$ (↓)
- Bij $\rm{D}: w_D = $ {gap} $\rm{mm}$ (↓)

---

::::

::::::{admonition} Exercise
:class: exercise

For the support settlements only:

```{figure} ./lesoefeningen_data/belasting_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Sketch the possible deformations:

---
=

```{figure} ./lesoefeningen_data/vervorming_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

---

:::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:nocaption:
:showanswer:

---
M[0]
M[0]
M[0.0025]
M[0.0025]
M[37.5]
M[-12.5]
^^^
? Determine the force distribution and displacements.

- $M_{\rm{B}} = $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{D}} = $ {gap} $\rm{kNm}$ (◡)
- $\varphi_{\rm{B}} = $ {gap} $\rm{rad}$ (↺)
- $\varphi_{\rm{C}} = $ {gap} $\rm{rad}$ (↺)
- $w_{\rm{halverwege \ AB}} = $ {gap} $\rm{mm}$ (↓)
- $w_{\rm{halverwege \ CD}} = $ {gap} $\rm{mm}$ (↓)

---

::::

::::::

::::{admonition} Solution
:class: solution, dropdown

If $A_{\rm{v}}$ and $D_{\rm{v}}$ are both zero, the structure can deform freely and no bending occurs.

::::

::::::{admonition} Exercise
:class: exercise

For the statically indeterminate forces only (so no support settlements):

```{figure} ./lesoefeningen_data/belasting_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Sketch the possible deformations:

---
=

```{figure} ./lesoefeningen_data/vervorming_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

---

:::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:nocaption:
:showanswer:

---
M[10]
M[0]
M[0]
M[10]
M[0]
M[0]
M[-0.0004]
M[-0.0002]
M[0]
M[0.0002]
M[0.0004]
M[0]
M[0.004]
M[0.002]
M[0]
M[-0.002]
M[-0.004]
M[0]
^^^
? Determine the force distribution and displacements as functions of $A_{\rm{v}}$ and $D_{\rm{v}}$ in $\rm{kN}$.

- $M_{\rm{B}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◡)
- $M_{\rm{D}} \left(A_{\rm{v}}, D_{\rm{v}}\right)= $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◡)
- $\varphi_{\rm{B}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↺)
- $\varphi_{\rm{C}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↺)
- $w_{\rm{halverwege \ AB}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{m} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{m} \, \rm{rad}\right)$ (↓)
- $w_{\rm{halverwege \ CD}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{m} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{m} \, \rm{rad}\right)$ (↓)

---

::::

::::::

::::{admonition} Solution
:class: solution, dropdown

The moments $M_{\rm{B}}$ and $M_{\rm{C}}$ can be determined by moving $A_{\rm{v}}$ and $D_{\rm{v}}$ to $\rm{B}$ and $\rm{C}$, respectively.

$$M_{\rm{B}} = 10 \cdot A_{\rm{v}}$$
$$M_{\rm{C}} = 10 \cdot D_{\rm{v}}$$

The rotations at $\rm{B}$ and $\rm{C}$ can be determined by superposing the bending deformation and the free deformation calculated in the previous exercise. For the bending deformation, use the forget-me-not for a simply supported beam subjected to a moment.

$$ \varphi_{\rm{B}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = -\cfrac{10 \cdot A_{\rm{v}} \cdot 10}{3 \cdot \cfrac{250}{3} \cdot n\cdot 1000} - \cfrac{10 \cdot D_{\rm{v}} \cdot 10}{6 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + 0.0025 = -0.0004 \cdot \cfrac{A_{\rm{v}}}{n} -0.0002 \cdot \cfrac{D_{\rm{v}}}{n} + 0.0025 $$
$$ \varphi_{\rm{C}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = \cfrac{10 \cdot A_{\rm{v}} \cdot 10}{6 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + \cfrac{10 \cdot D_{\rm{v}} \cdot 10}{3 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + 0.0025 = 0.0002 \cdot \cfrac{A_{\rm{v}}}{n} + 0.0004 \cdot \cfrac{D_{\rm{v}}}{n} + 0.0025 $$

The deflections at $\rm{A}$ and $\rm{D}$ can be determined by superposing the free deformation of the structure, the bending deformation of segment $\rm{BC}$, and the bending deformations of segments $\rm{AB}$ and $\rm{CD}$.

$$ w_{\rm{A}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = 0.05 + 10 \cdot \left( -0.0004 \cdot \cfrac{A_{\rm{v}}}{n} -0.0002 \cdot \cfrac{D_{\rm{v}}}{n} \right) - \cfrac{ A_{\rm{v}} \cdot 10^3}{3 \cdot \cfrac{250}{3} \cdot 1000} =-0.004  \cdot A_{\rm{v}} -0.004 \cdot \cfrac{A_{\rm{v}}}{n} -0.002 \cdot \cfrac{D_{\rm{v}}}{n} + 0.05 $$
$$ w_{\rm{D}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = -0.025 - 10 \cdot \left( 0.0002 \cdot \cfrac{A_{\rm{v}}}{n} + 0.0004 \cdot \cfrac{D_{\rm{v}}}{n} \right) - \cfrac{ D_{\rm{v}} \cdot 10^3}{3 \cdot \cfrac{250}{3} \cdot 1000} =-0.002 \cdot \cfrac{A_{\rm{v}}}{n} + -0.004 \cdot D_{\rm{v}} + -0.004\cdot \cfrac{D_{\rm{v}}}{n} -0.025 $$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[25]
M[0]
M[4]
M[2]
M[25]
M[0]
M[4]
M[2]
^^^
? Use the deformation conditions to solve for the unknowns $A_{\rm{v}}$ and $D_{\rm{v}}$ in $\rm{kN}$. This is a challenging algebraic problem; using a tool such as SymPy is recommended.

- $A_{\rm{v}} = ( $ {gap} $ \cdot n + $ {gap} $ ) / ( $ {gap} $ \cdot n + $ {gap} $ )$
- $D_{\rm{v}} = ( - $ {gap} $ \cdot n + $ {gap} $ ) / ( $ {gap} $ \cdot n + $ {gap} $ )$

---

::::

::::{admonition} Solution
:class: solution, dropdown

Solving the equations gives:

- $ A_{\rm{v}}= \cfrac{25 \cdot n}{4 \cdot n + 2} $
- $ D_{\rm{v}}= -\cfrac{25 \cdot n}{4 \cdot n + 2} $

These functions can also be plotted:

```{figure} lesoefeningen_data/steunpuntszetting.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

::::
