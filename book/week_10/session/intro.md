```{index} Static indeterminate structures; Exam assignment
```

(exam1)=
# Exam Tuesday

Today you'll make the first exam assignment covering Statically indeterminate structures including its prerequisites. For more information about the exam see [the assessment information in course information](exam-general)

## Exam assignment
Your own submission and its grading can be found here: [<img height="12px" src="../../figures/ANS.svg" alt="ANS" class="no-zoomies"> exam assignment Statically indeterminate structures 1](https://ans.app/universities/1/courses/714632/assignments/1937243/go_to). The exam assignment was provided as follows:

Given is the following structure:

```{figure} ./lesson_data/constructie1.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

:::::{exercise}
:label: exam_stat_indet_2025_1
:nonumber: true

Show that this structure is internally statically indeterminate to the second degree.

:::::

::::{admonition} Solution
:class: solution, dropdown

The structure is open, so the internal degree of static indeterminacy is equal to the external degree. The rigid, hinged parts are as follows:

```{figure} ./lesson_data/stat_bepaald.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

There are therefore $3 + 1 + 2 + 2 = 8$ unknowns and $3 + 3 = 6$ equilibrium equations, so the structure is statically indeterminate to the second degree both externally and internally.

:::{admonition} Alternative with internal statical determinacy
:class: note, dropdown

Alternatively, the internal degree of static indeterminacy can be calculated as follows:

```{figure} ./lesson_data/inwendig.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

There are $3 + 3 + 3 + 2 + 1 +  1 + 1 + 1 = 15$ unknowns and $3 + 3 + 3 + 2 + 1 + 1 = 13$ equilibrium equations, so the structure is statically indeterminate to the second degree internally.

:::

::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Static determinacy calculated with # support reactions - 3 equilibrium equations - # hinges**

This approach is not a method that works in general, but it does give the correct answer in this case: 6 support reactions - 3 equilibrium equations - 1 hinges = 2.

**Incorrectly modelled two-force member**

The member $\rm{BC}$ is a two-force member, so the internal forces in this member are only axial. Therefore, the amount of unknowns at the ends of this member can be reduced to one at each end, and the amount of equilibrium equations is one for the member and may reduce for the connected members if the internal statical determinancy is calculated. A correct approach would be:

```{figure} ./lesson_data/pendelstaaf.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Mistakes were made with the amount of unknowns at the connecting ends $\rm{B}$ and $\rm{C}$ and the amount of equilibrium equations.

::::::

:::::{exercise}
:nonumber: true

Provide four different statically determinate variants of this structure for the purpose of the force method. Making an identical change at two points in the same element doesn't count as a different variant.

For each of the variants:

- Provide the necessary compatibility equations to determine the statically indeterminate forces
- Explain why your variants are not mechanisms based on drawings of the deformed structures.

:::::

::::::{admonition} Solution
:class: solution, dropdown

For example the following variants.

:::::{grid}
:class-container: center-grid
:gutter: 1

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

This variant deforms as follows under the distributed load:

```{figure} ./lesson_data/variant1_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Therefore, it is not a mechanism.

::::

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

This variant deforms as follows under the distributed load:

```{figure} ./lesson_data/variant2_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
:name: variant2_def
```

Therefore, it is not a mechanism.

::::

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

This variant deforms as follows under the distributed load:

```{figure} ./lesson_data/variant3_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Therefore, it is not a mechanism.

::::

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant4.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

This variant deforms as follows under the distributed load.

```{figure} ./lesson_data/variant4_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Therefore, it is not a mechanism.

::::

:::::
::::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Created a mechanism**

Replaced the hinged support at $\rm{B}$ with a horizontal roller support or no support at all. This is not a statically determinate variant, because the structure is a mechanism:

:::::{grid}
:class-container: center-grid
:gutter: 1

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant5.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

This variant deforms as follows under the statically indeterminate force:

```{figure} ./lesson_data/variant5_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::

::::{grid-item-card}
:columns: 6


```{figure} ./lesson_data/variant6.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

This variant deforms as follows under the statically indeterminate force:

```{figure} ./lesson_data/variant6_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::
:::::

::::::

```{hide-sticky-margin}
```

Given the following structure. Note that the vertical roller support at $\rm{C}$ is removed.

```{figure-start} ./lesson_data/constructie2.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

- $EA_{\rm{BC}} = 14.4 \, \rm{MN}$
- $EI_{\rm{CDA}} = 62720 \, \rm{kNm}^2$
- $EA_{\rm{CDA}} \gg EI_{\rm{CDA}} $

```{figure-end}
```

:::::{exercise}
:nonumber: true

Solve the statically indeterminate force using the force method using a statically determinate structure of your own choice.

:::::

::::::{admonition} Solution
:class: solution, dropdown

The structure is statically indeterminate to the first degree. It could be modified as follows:

```{figure} ./lesson_data/statisch_bepaald.svg
:align: center
:number:
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

:::{admonition} Alternative with vertical roller support at $\rm{B}$
:class: note, dropdown

Another possible solution is modifying the structure as follows:

```{figure} ./lesson_data/stat_bepaald_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Other solutions are possible too.

:::

This gives the following deformations:

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
:name: vervorming_1
```

::::

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
:name: vervorming_2
```

::::

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
:name: vervorming_3
```

::::

:::::

The rotation $\varphi_{\rm{D}}^{\rm{AD}}$ can be calculated using the forget-me-not for a cantilever beam with an end moment:

$$ \varphi_{\rm{D}}^{\rm{AD}} = - \cfrac{M_{\rm{D}} \cdot 3}{3 \cdot 62720} = - \cfrac{3 \cdot M_{\rm{D}}}{62720} $$

The vertical displacement of $\rm{C}$ can be calculated from the elongation of a rigid bar. First, the axial force in $\rm{BC}$ must be calculated:

```{figure} ./lesson_data/VLS_CD.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

$$
\begin{align*}
\left. T \right|_{\rm{D}} &= 0 \\
N_{\rm{BC}} \cdot 7 - 32 \cdot 7 \cdot 3.5 - M_{\rm{D}} &= 0 \\
N_{\rm{BC}} &= 112 + \cfrac{M_{\rm{D}}}{7}
\end{align*}
$$

The vertical displacement of $\rm{C}$ can now be calculated from the elongation of a rigid bar:

$$ w_{\rm{C}} = \cfrac{N_{\rm{BC}} \cdot 3}{14.4 \cdot 10^3} = \cfrac{7}{300} + \cfrac{M_{\rm{D}}}{33600} \left( \downarrow \right) $$

The rotation $\varphi_{\rm{D}}^{\rm{CD}}$ can be calculated using the forget-me-nots for a simply supported beam with an end moment and a simply supported beam under a distributed load, together with the rigid-body rotation caused by the vertical displacement of $\rm{C}$:

$$ \varphi_{\rm{D}}^{\rm{CD}} = \cfrac{M_{\rm{D}} \cdot 7}{3 \cdot 62720} + \cfrac{32 \cdot 7^3}{24 \cdot 62720} + \cfrac{w_{\rm{C}}}{7} = \cfrac{17}{1600} + \cfrac{13 \cdot M_{\rm{D}}}{313600} $$

The compatibility condition can now be solved:

$$
\begin{align*}
\varphi_{\rm{D}}^{\rm{AD}} &= \varphi_{\rm{D}}^{\rm{CD}} \\
- \cfrac{3 \cdot M_{\rm{D}}}{62720} &= \cfrac{17}{1600} + \cfrac{13 \cdot M_{\rm{D}}}{313600} \\
M_{\rm{D}} &= -119 \, \rm{kNm}
\end{align*}
$$

::::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Missing elongation of $\rm{BC}$**

The elongation of $\rm{BC}$ was not taken into account in the deformations, while this influences the compatibility condition. As can be seen in the figures below, the elongation of $\rm{BC}$ increases the rotation at $\rm{D}$.

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

:::{fetch} {ref}`vervorming_1`
:::

::::

::::{grid-item}
:columns: auto

:::{fetch} {ref}`vervorming_2`
:::

::::
:::::

**Missing deformation of $\rm{AD}$**

The deformation of $\rm{AD}$, or more specifically, the rotation of $\rm{D}$ caused by the bending of $\rm{AD}$, was not taken into account in the deformations, while this influences the compatibility condition. As can be seen in the figures below, the bending of $\rm{AD}$ increases the rotation at $\rm{D}$. This mistake was mostly made when solving the statical determinate system with a vertical roller support at $\rm{B}$.

:::{fetch} {ref}`variant2_def`
:::

**Use of statically indeterminate forget-me-nots**

In the force-method, you've created a statically determinate structure, so the forget-me-nots for statically indeterminate structures are not needed. For example, for the statically determinate system shown here in the answers, for $\rm{AD}$ the forget-me-not for a cantilever beam with an additional support is used, while that should be the forget-me-not for a cantilever beam with an end moment. This becomes visible from the deformed shape:

:::{fetch} {ref}`vervorming_3`
:::

**Statically determinate structure which is not easily solved with forget-me-nots**

```{figure} ./lesson_data/variant7.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

This variant deforms as follows under the statically indeterminate force:

```{figure} ./lesson_data/variant7_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Which is not easily solved with the forget-me-nots.

::::::

:::::{exercise}
:nonumber: true

Due to which restriction(s), for the matrix method as taught in this course, is it not possible to apply the matrix method to this structure. For your information, the matrix method in this course was based on this single stiffness matrix:

$$
\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
$$

:::::

::::{admonition} Solution
:class: solution, dropdown

The structure has:

- Swaying joints
- Hinges
- Loads applied to elements

None of these are accounted for in the element stiffness matrix as taught in this course.

::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Missing numerical values for stiffnesses**

The missing bending stiffness of $\rm{BC}$ and the very high axial stiffness of $\rm{CDA}$ are not a reason why the matrix method cannot be applied. Although values might be required, random or random right values can be used which leads to the correct results.

**Non-uniform stiffnesses**

In the matrix method every element can have it's own unique values for $EI$ and $EA$, so this is not a reason why the matrix method cannot be applied.

::::::
