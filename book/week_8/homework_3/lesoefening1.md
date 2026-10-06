````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/temperatuur/lesoefening1.html

```
````

# Guided exercise 2

Consider the following structure:

```{figure-start} intro_data/struct.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
:figclass: sticky-margin
```

- $EI = 20 \ \rm{MNm^2}$
- $EA = 10 \ \rm{MN}$
- $\Delta T_{\rm{AC}} = 8 \ ^{\circ} \rm{C} (◠)$
- $\Delta T_{\rm{CD}} = 8 \ ^{\circ} \rm{C} (ᑐ)$
- $\Delta T_{\rm{CD}} = 50 \ ^{\circ} \rm{C} (+)$
- $h = 0.4 \ \rm{m}$
- $\alpha = 10^{-5} \ ^{\circ} \rm{C}^{-1}$

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
M[0]
M[0.0005]
M[0.0002]
M[0.0002]
^^^
?
What is the curvature caused by the temperature change?

- $\epsilon^{\rm{T}}_{\rm{AC}} = $ {gap} $\rm{m}/\rm{m}$
- $\epsilon^{\rm{T}}_{\rm{CD}} = $ {gap} $\rm{m}/\rm{m}$
- $\kappa^{\rm{T}}_{\rm{AC}} = $ {gap} $\rm{m}^{-1}$
- $\kappa^{\rm{T}}_{\rm{CD}} = $ {gap} $\rm{m}^{-1}$

---
::::

The following statically determinate system with its deformation condition has been chosen. Equivalent forces for the temperature effect have not yet been added.

```{hide-sticky-margin}
```
```{figure-start} intro_data/SD.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
:figclass: sticky-margin
```

- $EI = 20 \ \rm{MNm^2}$
- $EA = 10 \ \rm{MN}$
- $\Delta T_{\rm{AC}} = 8 \ ^{\circ} \rm{C} (◠)$
- $\Delta T_{\rm{CD}} = 8 \ ^{\circ} \rm{C} (ᑐ)$
- $\Delta T_{\rm{CD}} = 50 \ ^{\circ} \rm{C} (+)$
- $h = 0.4 \ \rm{m}$
- $\alpha = 10^{-5} \ ^{\circ} \rm{C}^{-1}$

```{figure-end}
```

::::::{question} Exercise
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Sketch the deformed structure due separately to the distributed load and $N_{\rm{CD}}$.

---
=

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure} intro_data//verplaats_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
```

::::

::::{grid-item}
:columns: auto

```{figure} intro_data/verplaats_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
```

::::

:::::

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
M[-6]
M[-144]
M[0.0004]
M[0.0096]
M[-6]
M[-122.4]
M[0.4]
M[0]
^^^
? What are the force distributions and displacements due to the distributed load as functions of $N_{\rm{CD}}$ in $\rm{kN}$? Do not include the kinematically equivalent forces due to the temperature effect.

- $M_{\rm{B}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◡)
- $\varphi_{\rm{B}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↻)
- $w_{\rm{C}}^{\rm{BC}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $w_{\rm{C}}^{\rm{CD}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$

---

::::

::::::{question} Exercise
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Sketch the curvature distribution due to the temperature change.

---
=

```{figure} ./intro_data/kromming.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
```

---

::::::

::::::{question} Exercise
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Sketch the structure including the kinematically equivalent forces due to the temperature effect.

---
=

```{figure-start} intro_data/statisch_onbepaald.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
```

- $EI = 20 \ \rm{MNm^2}$
- $EA = 10 \ \rm{MN}$

```{figure-end}
```

---

::::::

::::::{question} Exercise
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Sketch the deformations due to the kinematically equivalent forces representing the temperature effect.

---
=

```{figure} intro_data/verplaats_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
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
M[-6]
M[-144]
M[0.0004]
M[0.01]
M[-6]
M[-128.4]
M[0.4]
M[2]
^^^
? What are the force distributions and displacements due to the distributed load as functions of $N_{\rm{CD}}$ in $\rm{kN}$, including the kinematically equivalent forces representing the temperature effect?

- $M_{\rm{B}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$  (◡)
- $\varphi_{\rm{B}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↻)
- $w_{\rm{C}}^{\rm{BC}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $w_{\rm{C}}^{\rm{CD}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$

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
M[-20.375]
^^^
? Apply the deformation condition to find the statically indeterminate force.

$N_{\rm{CD}}= $ {gap} $\rm{kN}$

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
M[-21.75]
M[0]
M[-0.0012875]
M[0.0002]
M[-6.15]
M[0.4]

^^^
? Now determine the remaining force distribution and displacements as well.

- $M_{\rm{B}}= $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{halverwege \ CD}}= $ {gap} $\rm{kNm}$ (ᑐ)
- $\kappa_{\rm{B}} = $ {gap} $\rm{m}^{-1}$ (◡)
- $\kappa_{\rm{halverwege \ CD}} = $ {gap} $\rm{m}^{-1}$ (ᑐ)
- $w_{\rm{C}}= $ {gap} $\rm{mm}$ (↑)
- $w_{\rm{halverwege \ CD}}= $ {gap} $\rm{mm}$ (→)

---

::::
