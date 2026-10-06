````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/temperatuur/theorie.html

```
````

# Solve statically indeterminate structures subjected to temperature influences

Under a uniform temperature change, elements undergo an additional strain of $\epsilon^{\rm{T}} = \alpha \ \Delta T$, where $\alpha$ is the coefficient of linear thermal expansion. When the temperature varies over an element's height, its fibres expand by different amounts, causing the element to bend with an additional curvature of $\kappa^{\rm{T}} = \alpha \ \cfrac{\Delta T}{h}$, where $h$ is the element height. In statically determinate structures, these effects cause additional stress-free strains (and therefore deformations) without affecting the force distribution, because the force distribution is independent of the deformations.

The deformation can be found by integrating the stress-free strains using the differential equations. The approach is otherwise the same as for statically determinate structures.

Alternatively, an equivalent load that produces the same curvature can be used, allowing forget-me-nots to be applied. This requires a kinematically equivalent load that does not affect the support reactions or internal forces:

```{figure} ./theorie_data/kin_eq_load_SB.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur
:number:
```

In statically indeterminate structures, deformation and force distribution are coupled. As a result, the restrained deformations caused by temperature changes produce support reactions and internal stresses. These forces can again be found by integrating the strains (both stress-producing strains and stress-free thermal strains) using the differential equations. Alternatively, as for statically determinate structures, a kinematically equivalent load can be used with the force method: temperature-induced displacements are included in the deformation conditions.

```{figure} ./theorie_data/kin_eq_load_SO.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur
:number:
```

Temperature effects can be included in the force method using the following steps. Steps 1 and 4 are additions to the standard force method:

::::::{prf:algorithm} Temperature effects and the force method
:nonumber: true
:label: krachtenmethode_temperatuur

1. **Determine the curvature and strain caused by the temperature effect, independently of all supports.**
2. Determine the degree of static indeterminacy.
3. Transform the structure into a statically determinate system by removing supports, splitting the structure at two-force members, or adding hinges.
4. **Determine kinematically equivalent loads that produce the same deformation as the temperature effect.**
5. Solve for the displacement in terms of the unknown statically indeterminate forces.
6. Use the deformation conditions to solve for the statically indeterminate forces.

::::::

An example demonstrates how to account for temperature effects in a statically indeterminate structure using the force method.


::::::{prf:example}
:nonumber: true
:label: temp_0

```{figure-start} ./theorie_data/structure2.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
number:
---

```

- $EI = 6 \ \rm{MNm^2}$
- $EA \gg EI$
- $\Delta T = 20 \ ^{\circ} \rm{C}$
- $h = 0.2 \ \rm{m}$
- $\alpha = 10^{-5} \ ^{\circ} \rm{C}^{-1}$

```{figure-end}
```

The temperature difference across the beam height produces a curvature of $\kappa^{\rm{T}} = 10^{-3} \ \rm{m}^{-1}$ over the entire beam length:

```{figure} ./theorie_data/curv_sun.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
:number:
```

To find the kinematically equivalent load, we first need to make the structure statically determinate. This is a first-order statically indeterminate structure, so we need to modify it at one location. For example, we can use the following statically determinate system:

```{figure-start} ./theorie_data/structure_deter2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
:number:
```

- $EI = 6 \ \rm{MNm^2}$
- $EA \gg EI$
- $\Delta T = 20 \ ^{\circ} \rm{C}$
- $h = 0.2 \ \rm{m}$
- $\alpha = 10^{-5} \ ^{\circ} \rm{C}^{-1}$

```{figure-end}
```

For this system, applying a clockwise couple at the end of the beam produces the same curvature diagram. The couple must have a magnitude of $M = \kappa \cdot EI = 6 \ \rm{kNm}$ to produce the same curvature. This gives the following statically determinate system:

```{figure-start} ./theorie_data/structure_deter3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
:number:
:figclass: sticky-margin
```

- $EI = 6 \ \rm{MNm^2}$
- $EA \gg EI$

```{figure-end}
```

We can now proceed with the force method as usual. First, we can sketch the displacements caused by the forces:

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure} ./theorie_data/verplaats_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

::::

::::{grid-item}
:columns: auto

```{figure} ./theorie_data/verplaats_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```
::::

:::::


The displacement at $\rm{B}$ can be found using forget-me-nots:

$$
\begin{align*}
w_{\rm{B}} &= 0 \\
- \cfrac{6 \cdot 6 ^2}{2 \cdot 6000} + \cfrac{B_{\rm{v}} \cdot 6^3}{3 \cdot 6000}&= 0 \\
-0.018 + \cfrac{3}{250}B_{\rm{v}} &= 0 \\
B_{\rm{v}} &= 1.5 \ \rm{kN}
\end{align*}$$

The bending-moment diagram and displacements can now be determined. The kinematically equivalent load of $6 \ \rm{kNm}$ must be excluded when drawing the bending-moment diagram, but included when calculating the displacements. This gives:

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure} theorie_data/M-line.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

::::

::::{grid-item}
:columns: auto

```{figure} theorie_data/disp_total.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```
::::

:::::

::::::

## Derivation and more examples
The derivation of temperature effects is covered in chapter 4.12 of the book Mechanica: spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013`. A simplified version for statically determinate structures is repeated in section 6.2.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. The moment-area method is not covered in this course. The standard cases for a simply supported beam and a cantilever beam are also not used. Statically indeterminate structures are covered in section 6.2.2; the moment-area method is not part of this course there either.

## Lecture recording

This topic was presented in Dutch in [lecture 12 of CTB2210](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/319e6b623c2e48a4be53ba74023ab4901d?sortBy=most-recent), from 0:04:25 to 0:33:00.

## Additional exercises
- The guided exercises on the next two pages are a first exercise to check your understanding.
- For more practice, you can work on exercises 6.25–6.30, 3.32–6.39, and 6.41–6.43 in section 6.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Unfortunately, no answers are available.
