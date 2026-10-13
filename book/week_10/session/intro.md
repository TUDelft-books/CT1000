```{index} Static indeterminate structures; Exam assignment
```

(exam1)=
# Exam Friday November 7th

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

:::::{exercise}
:nonumber: true

Provide five different statically determinate variants of this structure for the purpose of the force method. Making an identical change at two points in the same element doesn't count as a different variant.

For each of the variants:

- Provide the necessary compatibility equations to determine the statically indeterminate forces
- Explain why your variants are not mechanisms based on drawings of the deformed structures.

:::::

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

:::::{exercise}
:nonumber: true

Due to which restriction(s), for the matrix method as taught in this course, is it not possible to apply the matrix method to this structure. For your information, the matrix method in this course was based on this single stiffness matrix:

$$
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
$$

:::::

::::{admonition} Solution
:class: solution, dropdown

- Moveable nodes
- Hinges
- Loads on elements

::::
