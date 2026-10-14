````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/steunpuntszetting_stijfheden/lesoefeningen.html

```
````

# Guided exercise 1

Consider the following structure:

```{figure-start} ./lesoefeningen_data/structure2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
:figclass: sticky-margin
```
$EA = 15 \ \rm{MN}$

```{figure-end}
```

::::::{exercise}
:label: steun_1_1
:nonumber: true

The following solution is given:

$N_{\rm{BD}} = \cfrac{90}{6000} \cdot 15000 = 225 \ \rm{kN}$

Equilibrium at joint $\rm{D}$ gives:
- $ N_{\rm{AD}} = -281.25 \ \rm{kN}$
- $ N_{\rm{CD}} = -168.75 \ \rm{kN}$

This gives:
- $\Delta L_{\rm{AD}} = \cfrac{-281.25 \cdot 7.5}{15000} = -0.109125 \ \rm{m}$
- $\Delta L_{\rm{CD}} = \cfrac{-168.75 \cdot 6}{15000} = - 0.0675 \ \rm{m}$

The resulting displacements are:
- Horizontal displacement of $\rm{D}$: $67.5 \ \rm{mm}$ to the right
- Vertical displacement of $\rm{D}$: $109.125 \cdot \cfrac{4}{5} = 87.3 \ \rm{mm} $ downward

:::::{question}
:nocaption:
:showanswer:
:variant: multiple-select
:columns: 1

What is wrong with the solution above?
---
[x] The axial force in $\rm{BD}$ was calculated incorrectly.
[ ] The axial forces in $\rm{AD}$ and $\rm{CD}$ were calculated incorrectly.
> The equilibrium method is applied correctly here, although the answers are wrong because $N_{\rm{BD}}$ is incorrect.
[ ] The extensions of members $\rm{AD}$ and $\rm{CD}$ were calculated incorrectly.
> The constitutive and kinematic equations are applied correctly here, although the answers are wrong because the axial forces are already incorrect.
[x] The displacement of joint $\rm{D}$ was calculated incorrectly.
^^^
! The extension of $\rm{BD}$ does not depend only on the displacement of joint $\rm{B}$. Don't you need a Williot diagram in this case?
---

:::::

::::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[1]
^^^
? 
The structure is {gap}st/nd/rd/th order internally statically indeterminate.

---
::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./lesoefeningen_data/Onbekenden_vergelijkingen.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
```

The structure is first-order internally statically indeterminate.

::::

The following statically determinate system with a deformation condition is chosen:

```{figure-start} ./lesoefeningen_data/statically_determinate2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
:figclass: sticky-margin
```
$EA = 15 \ \rm{MN}$

```{figure-end}
```

This system was chosen so that the support settlement can be included in the deformation condition and does not need to be included when determining the force distribution.

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[1]
M[0]
M[-1.25]
M[0]
M[-0.75]
M[0]
M[0.0004]
M[0]
M[-0.000625]
M[0]
M[-0.0003]
M[0]
M[0.0003]
M[0]
M[0.001]
M[0]
M[0.0014]
M[0]
^^^
? Determine the force distribution and deformations as functions of $B_{\rm{v}}$, with $B_{\rm{v}}$ in $\rm{kN}$.

- $N_{\rm{BD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$ 
- $N_{\rm{AD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $N_{\rm{CD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $\Delta L_{\rm{BD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$
- $\Delta L_{\rm{AD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$
- $\Delta L_{\rm{CD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$
- $w_{D,\rm{h}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (→)
- $w_{D,\rm{v}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (↓)
- $w_{B,\rm{v}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (↓)

---

::::

::::{admonition} Solution
:class: solution, dropdown

The axial forces in members AD and CD can be expressed in terms of $B_{\rm{v}}$ using equilibrium at joint $\rm{D}$.

- $ N_{\rm{BD}} = B_{\rm{v}} $
- $ \sum F_{\rm{v}} = 0 \rightarrow N_{\rm{AD}} = - \cfrac{5}{4} \cdot B_{\rm{v}} $
- $ \sum F_{\rm{h}} = 0 \rightarrow N_{\rm{CD}} = - \cfrac{3}{4} \cdot B_{\rm{v}} $

Now that the axial forces in the members are known, the extension or shortening of each member can be determined. The results are shown in the table below.

| Member | $N\left(B_{\rm{v}}\right)$ (kN)| $\Delta L \left(B_{\rm{v}}\right)\rm{(mm)}$ |
| :-:|:-:|:-:|
|$\rm{AD}$|$-\cfrac{5}{4} \cdot B_{\rm{v}}$|$-\cfrac{5}{8} \cdot B_{\rm{v}}$|
|$\rm{BD}$|$B_{\rm{v}}$|$\cfrac{2}{5} \cdot B_{\rm{v}}$|
|$\rm{CD}$|$- \cfrac{3}{4} \cdot B_{\rm{v}}$|$-\cfrac{3}{10} \cdot B_{\rm{v}}$|

The Williot diagram can be drawn using the calculated extensions and shortenings, as shown below.

```{figure} lesoefeningen_data/williot.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
```

The Williot diagram gives:

- $ w_{D,\rm{h}} = 0.0003 \cdot B_{\rm{v}} \ \rm{m} \ \left(\rightarrow\right)$
- $ w_{D,\rm{v}} \approx 0.001 \cdot B_{\rm{v}} \ \rm{m} \  \left(\downarrow\right)$
- $ w_{B,\rm{h}} = 0 $
- $ w_{B,\rm{v}} \approx 0.0014 \cdot B_{\rm{v}} \ \rm{m} \ \left(\downarrow\right)$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[64]
^^^
? Apply the deformation conditions to find the statically indeterminate forces.

$B_{\rm{v}}= $ {gap} $\rm{kN}$
---

::::

::::{admonition} Solution
:class: solution, dropdown

The deformation condition is: $w_{B,\rm{v}} = 1.4 \cdot B_{\rm{v}} = 90 \rm{mm}$.

This gives: $B_{\rm{v}} = 64 \rm{kN}$.

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[64]
M[-80]
M[-48]
M[19]
M[64]
^^^
? Now determine the remaining force distribution as well.

- $N_{\rm{BD}}= $ {gap} $\rm{kN}$
- $N_{\rm{AD}}= $ {gap} $\rm{kN}$
- $N_{\rm{CD}}= $ {gap} $\rm{kN}$
- $w_{D,\rm{h}} = $ {gap} $\rm{mm}$ (→)
- $w_{D,\rm{v}} = $ {gap} $\rm{mm}$ (↓)

---

::::

::::{admonition} Solution
:class: solution, dropdown

The forces and displacements can be found from the equations derived earlier by substituting the calculated value of $B_{\rm{v}}$.

- $ N_{\rm{BD}}= 64 \rm{kN} $
- $ N_{\rm{AD}}= -80 \rm{kN} $
- $ N_{\rm{CD}}= -48 \rm{kN} $
- $ w_{D,\rm{h}} = 19 \rm{mm} \ \left(\rightarrow\right)$
- $ w_{D,\rm{v}} = 64 \rm{mm} \ \left(\downarrow\right)$

::::

:::::{question} Exercise
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Draw the deformed structure.

---
=

```{figure} ./lesoefeningen_data/vervormd.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
```

---

:::::
