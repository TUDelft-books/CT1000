````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_rek_raamwerk/lesoefening_1.html.

```
````

# Guided exercise

```{figure-start} ./lesoefening_data/constructie.svg
:align: center
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/exam_SOB
:number:
```

- $EI = 768 \ \rm{MNm^2}$
- $EA = 125 \ \rm{MN}$

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


% https://oit.tudelft.nl/CT1000/2025/week_15/session/intro.html

::::::{admonition} Exercise
:class: exercise

Consider the following possible modification to the structure:

```{figure} ./lesoefening_data/optie_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
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
[ ] This structure is a mechanism.
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Sketch the possible deformations due to the moment $M_{\rm{A}}$:

---
=

```{figure} ./lesoefening_data/optie_1_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
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
> $\rm{AB}$ will both bend and undergo rigid-body rotation about $\rm{A}$, making the displacements more difficult to calculate.
[x] It is possible, but there are better options
[ ] No
> This structure is statically determinate, so it is suitable!
---

:::::

::::::

::::::{admonition} Exercise
:class: exercise

Consider the following possible modification to the structure:

```{figure} ./lesoefening_data/optie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is this structure statically determinate, statically indeterminate, or a mechanism?
---
[ ] This structure is statically determinate.
[ ] This structure is statically indeterminate.
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
[ ] It is possible, but there are better options
[x] No
---

:::::

::::::

::::::{admonition} Exercise
:class: exercise

Consider the following possible modification to the structure:

```{figure} ./lesoefening_data/optie_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
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
[ ] This structure is a mechanism.
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Sketch the possible deformations due to the statically indeterminate force $B_{\rm{v}}$:

---
=

```{figure} ./lesoefening_data/optie_3_verplaatsingen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
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
[ ] No
> This structure is statically determinate, so it is suitable!
---

:::::

::::::

The following statically determinate system, including its deformation conditions, is chosen:

```{figure-start} ./lesoefening_data/stat_bepaald.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
:figclass: sticky-margin
:number:
```

- $EI = 768 \ \rm{MNm^2}$
- $EA = 125 \ \rm{MN}$

```{figure-end}
```

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations due to the $90 \ \rm{kN}$ load.
---
=

```{figure} ./lesoefening_data/verplaatsingen_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
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

Sketch the possible deformations due to the statically indeterminate force $N_{\rm{C}}$.
---
=

```{figure} ./lesoefening_data/verplaatsingen_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
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
M[0]
ME[\cfrac{3}{5};1]
M[90]
M[-1]
ME[\cfrac{-4}{5};1]
M[0]
ME[\cfrac{4}{125};2]
ME[\cfrac{16}{625};3]
M[0]
M[0]
MAPE[\cfrac{1}{60};0.0001;3]
ME[\cfrac{5}{2};2]
M[0]
ME[\cfrac{1}{25};1]
M[0]
ME[\cfrac{16}{625};3]
ME[\cfrac{881}{12500};4]
ME[\cfrac{3}{2};2]
^^^
? Determine the displacements in $\rm{mm}$, with $B_{\rm{v}}$ and $N_{\rm{C}}$ in $\rm{kN}$.

- $V_{\rm{B}}^{\rm{AB}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$ (causes point $\rm{B}$ to shear to the right relative to $\rm{A}$)
- $N_{\rm{AB}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $w_{\rm{B}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$ (↑)
- $w_{\rm{B,h}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$ (→)
- $\Delta L_{\rm{BC}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $w_{\rm{C}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$ (↗)

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
M[24]
M[-30]
^^^
? Apply the deformation conditions to find the statically indeterminate forces.

- $B_{\rm{v}}= $ {gap} $\rm{kN}$
- $N_{\rm{C}}= $ {gap} $\rm{kN}$

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
M[288]
M[0]
M[72]
^^^
? Now solve for the remaining forces as well.

- $M_{\rm{A}}= $ {gap} $\rm{kNm}$ (ᑐ)
- $N_{\rm{AB}}= $ {gap} $\rm{kN}$
- $\left| V_{AB} \right|= $ {gap} $\rm{kNm}$

---

::::
