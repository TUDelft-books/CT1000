````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_raamwerk/lesoefeningen_2.html.

```
````

# Guided exercise 2

Consider the following structure:

```{figure-start} ./lesoefeningen2_data/structure.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:figclass: sticky-margin
:number:
```

- $EI = \cfrac{1000}{3} \, \rm{kNm^2}$
- $EA >> EI $

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
M[3]
^^^
?
The structure is {gap}st/nd/rd/th order internally statically indeterminate.

---
::::

::::{admonition} Solution
:class: solution, dropdown
:name: stat_onbepaald_raamwerk

:::{fetch} {numref}`stat_onbepaald_raamwerk_1`
:::

There are 4 unknown support reactions and 21 unknown member forces, for a total of 25 unknown forces.

:::{fetch} {numref}`stat_onbepaald_raamwerk_2`
:::

There are 22 equilibrium equations.

Therefore, the structure is third-order statically indeterminate ($25 - 22=$).

::::

::::::{admonition} Exercise
:class: exercise

Consider the following possible modification to the structure:

```{figure} ./lesoefeningen2_data/aanpassing1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is this structure statically determinate, statically indeterminate, or a mechanism?
---
[x] This structure is statically determinate.
[ ] This structure is statically indeterminate.
> Three modifications have been made, each reducing the degree of static indeterminacy by 1.
[ ] This structure is a mechanism.
> There are no global or local mechanisms! The hinge halfway between $\rm{B}$ and $\rm{C}$ cannot move freely because member $\rm{AB}$ resists rotation of joint $\rm{B}$.
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Sketch the possible deformations due to the distributed load:

---
=

```{figure} ./lesoefeningen2_data/aanpassing1_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is this modified structure a good choice for the force method?
---
[ ] Yes
> The deflection of the hinge halfway between $\rm{B}$ and $\rm{C}$ makes the displacements harder to calculate.
[x] It is possible, but there are better options
[ ] No
> This structure is statically determinate, so it is suitable!
---

:::::

::::::

::::::{admonition} Exercise
:class: exercise

Consider the following possible modification to the structure:

```{figure} ./lesoefeningen2_data/aanpassing2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is this structure statically determinate, statically indeterminate, or a mechanism?
---
[ ] This structure is statically determinate.
> Only two modifications have been made, each reducing the degree of static indeterminacy by 1.
[x] This structure is statically indeterminate.
[ ] This structure is a mechanism.
> There are no global or local mechanisms!
---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is this modified structure a good choice for the force method?
---
[ ] Yes
> The structure is not yet statically determinate.
[ ] It is possible, but there are better options
> The structure is not yet statically determinate.
[x] No
---

:::::

::::::

::::::{admonition} Exercise
:class: exercise

Consider the following possible modification to the structure:

```{figure} ./lesoefeningen2_data/aanpassing3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is this structure statically determinate, statically indeterminate, or a mechanism?
---
[x] This structure is statically determinate.
[ ] This structure is statically indeterminate.
> Three modifications have been made, each reducing the degree of static indeterminacy by 1.
[ ] This structure is a mechanism.
> There are no global or local mechanisms! $\rm{BC}$ cannot rotate freely about $\rm{B}$ because it is rigidly connected to the other members.
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Sketch the possible deformations due to the distributed load:

---
=

```{figure} ./lesoefeningen2_data/aanpassing3_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is this modified structure a good choice for the force method?
---
[ ] Yes
> The internal forces at $\rm{D}$ and $\rm{B}$ are not immediately obvious. In addition, finding the displacement at $\rm{A}$ requires several steps, including accounting for the rigid-body rotation of $\rm{BAD}$.
[x] It is possible, but there are better options
[ ] No
> This structure is statically determinate, so it is suitable!
---

:::::

::::::

::::::{admonition} Exercise
:class: exercise

Consider the following possible modification to the structure:

```{figure} ./lesoefeningen2_data/aanpassing4.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is this structure statically determinate, statically indeterminate, or a mechanism?
---
[x] This structure is statically determinate.
[ ] This structure is statically indeterminate.
> Three modifications have been made, each reducing the degree of static indeterminacy by 1.
[ ] This structure is a mechanism.
> There are no global or local mechanisms!
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Sketch the possible deformations due to the distributed load:

---
=

```{figure} ./lesoefeningen2_data/aanpassing4_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is this modified structure a good choice for the force method?
---
[x] Yes
[ ] It is possible, but there are better options
> The displacements are easy to calculate using forget-me-nots, and the effects of the forces are even confined to individual members.
[ ] No
> This structure is statically determinate, so it is suitable!
---

:::::

::::::

::::::{admonition} Exercise
:class: exercise

Consider the following possible modification to the structure:

```{figure} ./lesoefeningen2_data/aanpassing5.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is this structure statically determinate, statically indeterminate, or a mechanism?
---
[ ] This structure is statically determinate.
> Although the hinge at $\rm{B}$ reduces the degree of static indeterminacy by 2, in combination with the modified support it creates a mechanism.
[ ] This structure is statically indeterminate.
> The hinge modification at $\rm{B}$ reduces the degree of static indeterminacy by 2, and the support modification reduces it by 1. However, these modifications also have other effects!
[x] This structure is a mechanism.
---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is this modified structure a good choice for the force method?
---
[ ] Yes
> The structure is not yet statically determinate.
[ ] It is possible, but there are better options
> The structure is not yet statically determinate.
[x] No
---

:::::

::::::

The following statically determinate system, including its deformation conditions, is chosen:

```{figure-start} ./lesoefeningen2_data/structure2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:figclass: sticky-margin
:number:
```

- $EI = \cfrac{1000}{3} \, \rm{kNm^2}$
- $EA >> EI $
```{figure-end}
```

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations due to the moments at $\rm{D}$
---
=

```{figure} ./lesoefeningen2_data/vervorming_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
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

Sketch the possible deformations due to $M_{\rm{B}}^{\rm{BD}}$.
---
=

```{figure} ./lesoefeningen2_data/vervorming_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::{note}
Note that the displacements are drawn as if the hinge were just to the left of joint $\rm{B}$, although it is shown slightly farther from the joint.
:::

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations due to $M_{\rm{B}}^{\rm{AB}}$.
---
=

```{figure} ./lesoefeningen2_data/vervorming_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::{note}
Note that the displacements are drawn as if the hinge were just below and to the left of joint $\rm{B}$, although it is shown slightly farther from the joint.
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
M[0.006]
M[0]
M[0]
M[0]
M[-0.008]
M[-0.004]
M[0]
M[0]
M[-0.004]
M[-0.008]
M[0]
M[0]
M[0]
M[0]
M[0.01]
M[0]
M[0]
M[0.006]
M[-0.006]
M[0.297]
^^^
? Determine the rotations $\varphi_{\rm{D}}^{\rm{AD}}$, $\varphi_{\rm{D}}^{\rm{BD}}$, $\varphi_{\rm{B}}^{\rm{BD}}$, $\varphi_{\rm{B}}^{\rm{AB}}$ and $\varphi_{\rm{B}}$ as functions of $M_{\rm{D}}$, $M_{\rm{B}}^{\rm{BD}}$ and $M_{\rm{B}}^{\rm{AB}}$, with moments in $\rm{kNm}$ and $\varphi$ in $\rm{rad}$.

- $\varphi_{\rm{D}}^{\rm{AD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{D}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{B}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{B}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$

---

::::

::::{admonition} Solution
:class: solution, dropdown

The expressions for the rotations are found using the forget-me-nots for a simply supported beam subjected to a moment and a distributed load. The positive directions are as indicated in the figure.

$$ \varphi_{\rm{D}}^{\rm{AD}} \left( M_{\rm{D}}\right) = \cfrac{M_{\rm{D}} \cdot 6}{3 \cdot \cfrac{1000}{3}} = 0.006 \cdot M_{\rm{D}} $$
$$ \varphi_{\rm{D}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}} \right) = - \cfrac{M_{\rm{D}} \cdot 8}{3 \cdot \cfrac{1000}{3}} - \cfrac{M_{\rm{B}}^{\rm{BD}} \cdot 8}{6 \cdot \cfrac{1000}{3}} = -0.008 \cdot  M_{\rm{D}} -0.004 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi_{\rm{B}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}} \right) = - \cfrac{M_{\rm{D}} \cdot 8}{6 \cdot \cfrac{1000}{3}} - \cfrac{M_{\rm{B}}^{\rm{BD}} \cdot 8}{3 \cdot \cfrac{1000}{3}} = -0.004 \cdot  M_{\rm{D}} -0.008 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}}^{\rm{AB}} \right) = \cfrac{M_{\rm{B}}^{\rm{AB}} \cdot 10}{3 \cdot \cfrac{1000}{3}} = 0.01 \cdot M_{\rm{B}}^{\rm{AB}} $$
$$ \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = \cfrac{\left(M_{\rm{B}}^{\rm{BD}} - M_{\rm{B}}^{\rm{AB}}\right) \cdot 6}{3 \cdot \cfrac{1000}{3}} + \cfrac{11 \cdot 6^3}{24 \cdot \cfrac{1000}{3}} = 0.006 \cdot M_{\rm{B}}^{\rm{BC}} - 0.006 \cdot M_{\rm{B}}^{\rm{AB}} + 0.297 $$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[5]
M[-17.5]
M[12]
^^^
? Apply the deformation conditions to find the statically indeterminate forces.

- $M_{\rm{D}}^{\rm{AC}}= $ {gap} $\rm{kNm}$
- $M_{\rm{B}}^{\rm{BD}}= $ {gap} $\rm{kNm}$
- $M_{\rm{B}}^{\rm{AB}}= $ {gap} $\rm{kNm}$

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
M[-29.5]
M[0]
M[34.75]
MAPE[\cfrac{5}{6};0.01;3]
MAPE[\cfrac{1997}{48};0.1;4]
^^^
? Now solve for the other forces as well.

- $M_{\rm{B}}^{\rm{BC}}= $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{A}}= $ {gap} $\rm{kNm}$
- $M_{\rm{halverwege \  BC}}= $ {gap} $\rm{kNm}$ (◡)
- $N_{\rm{BD}}= $ {gap} $\rm{kN}$
- $B_{\rm{v}}= $ {gap} $\rm{kN}$

---

::::
