```{index} Static indeterminate structures; Exam assignment
```

(exam1)=
# Exam Tuesday

Today you'll make the first exam assignment covering Statically indeterminate structures including its prerequisites. For more information about the exam see [the assessment information in course information](exam-general)

## Exam assignment
Your own submission and its grading can be found here: [<img height="12px" src="../../figures/ANS.svg" alt="ANS" class="no-zoomies"> exam assignment Statically indeterminate structures 1](https://ans.app/universities/1/courses/714632/assignments/1937243/go_to). The exam assignment was provided as follows:

Given is the structure as shown in the figure below.

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

::::

:::::{exercise}
:nonumber: true

Provide four different statically determinate variants of this structure for the purpose of the force method. Making an identical change at two points in the same element doesn't count as a different variant.

For each of the variants:

- Provide the necessary compatibility equations to determine the statically indeterminate forces
- Explain why your variants are not mechanisms based on drawings of the deformed structures.

:::::

::::::{admonition} Solution
:class: solution, dropdown

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

This gives the following deformations:

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::

:::::

The angle $\varphi_{\rm{D}}^{\rm{AD}}$ can be calculated using the forget-me-not for a cantilever beam with an end moment:

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

The angle $\varphi_{\rm{D}}^{\rm{CD}}$ can be calculated using the forget-me-nots for a simply supported beam with an end moment and a simply supported beam under a distributed load, together with the rigid-body rotation caused by the vertical displacement of $\rm{C}$:

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
