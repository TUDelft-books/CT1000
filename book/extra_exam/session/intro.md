```{index} Buckling; Exam assignment
```
```{index} Static indeterminate structures; Exam assignment
```
```{index} Continuum mechanics; Exam assignment
```

(exam6)=
# Exam Friday

Today some studnets make an additional exam assignment covering static indeterminate structures, continuum mechanics or stability including its prerequisites. For more information about the exam see [the assessment information in course information](exam-general)

## Exam assignment 3 Statically indeterminate structures
Your own submission and its grading will be available on [<img height="12px" src="../../figures/ANS.svg" alt="ANS">](https://ans.app/universities/1/courses/576319/assignments/.../go_to) after the exam.

Given is the following structure:

```{figure-start} stat_deter_data/constructie.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_combi
```

- $EA_{\rm{AC}} = 240 \, \rm{MN}$
- $EI_{\rm{AC}} = 1200 \, \rm{MNm}^2$
- $EA_{\rm{BC}}, EI_{\rm{BC}} \gg EA_{\rm{AC}}, EI_{\rm{AC}}$

```{figure-end}
```

:::::{exercise}
:nonumber: true

Show that this structure is statically indeterminate to the second degree.

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} stat_deter_data/stat_det.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

For this structure, the external static indeterminacy is equal to the internal static indeterminacy.

There are 5 unknowns and 3 equilibrium equations, making the structure statically indeterminate to the second degree.

::::

:::::{exercise}
:nonumber: true

Provide three alternative valid variants to make this structure statically determinate for the purpose of the force method. Provide three different variants: over all variants, you must have adjusted at least each node and element once.
For each of the variants, provide the necessary compatibility equation(s) to determine the statically indeterminate force(s).

:::::

:::::{admonition} Solution
:class: solution, dropdown

Potential alternatives could be:

::::{grid}
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} stat_deter_data/option_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

:::

:::{grid-item}
:columns: auto

```{figure} stat_deter_data/option_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

:::

:::{grid-item}
:columns: auto

```{figure} stat_deter_data/option_3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

:::

::::

:::::

:::::{exercise}
:nonumber: true

Find the displacement of $\rm{C}$ using the force method.

:::::

:::::{admonition} Solution
:class: solution, dropdown

The following statically indeterminate structure is chosen:

```{figure-start} stat_deter_data/system.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_combi
```

- $EA_{\rm{AC}} = 240 \, \rm{kN}$
- $EI_{\rm{AC}} = 1200 \, \rm{kNm}^2$
- $EA_{\rm{BC}}, EI_{\rm{BC}} \gg EA_{\rm{AC}}, EI_{\rm{AC}}$

```{figure-end}
```

First, the internal forces in $\rm{C}$ are determined:

```{figure} stat_deter_data/FBD.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

This gives:

- $V_{\rm{C}}^{\rm{AC}} = B_{\rm{h}}$
- $N_{\rm{C}}^{\rm{AC}} = B_{\rm{v}}$
- $M_{\rm{C}}^{\rm{AC}} = 3 \cdot B_{\rm{h}} + 4 \cdot B_{\rm{v}}$

Now, the displacements of node $\rm{C}$ can be determined based on the elongation of a bar and forget-me-nots for part $\rm{AC}$:

```{figure} stat_deter_data/AC.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

This gives:

- $u_{\rm{C,h}} = \cfrac{21}{200} B_{\rm{h}} + \cfrac{3}{50} B_{\rm{v}}$ (→)
- $u_{\rm{C,v}} = \cfrac{1}{40} B_{\rm{v}} + \cfrac{243}{200}$ (↓)
- $\theta_{\rm{C}} = \cfrac{3}{100} B_{\rm{h}} + \cfrac{1}{50} B_{\rm{v}}$ (↻)

As $\rm{CB}$ doesn't deform but can rotate, this leads to:

- $u_{\rm{B,h}} = u_{\rm{C,h}} + \theta_{\rm{C}} \cdot 3 = \cfrac{39}{200} B_{\rm{h}} + \cfrac{3}{25} B_{\rm{v}}$ (→)
- $u_{\rm{B,v}} = u_{\rm{C,v}} + \theta_{\rm{C}} \cdot 4 = \cfrac{3}{25} B_{\rm{h}} + \cfrac{21}{200} B_{\rm{v}} + \cfrac{243}{200}$ (↓)

Equating the displacements of node $\rm{B}$ to zero gives:

- $B_{\rm{h}} = 24 \, \rm{kN}$
- $B_{\rm{v}} = - 39 \, \rm{kN}$

This gives:

- $u_{\rm{C,h}} = 0.18 \, \rm{m}$ (→)
- $u_{\rm{C,v}} = 0.24 \, \rm{m}$ (↓)

:::::

:::::{exercise}
:nonumber: true

Draw the displaced statically indeterminate structure for which you indicate the displacements of node $\rm{C}$ and indicate the location of the point of inflection (buigpunt): the point for which the curvature changes sign.

:::::

::::{admonition} Solution
:class: solution, dropdown

As the bending moment in $\rm{C}$ is $3 \cdot B_{\rm{h}} + 4 \cdot B_{\rm{v}} = - 84 \, \rm{kNm}$ with a shear force of $B_{\rm{h}} = 24 \, \rm{kN}$ (which equates the slope of the bending moment diagram), the bending moment is $0$ at $\cfrac{84}{24} = 3.5 \, \rm{m}$ to the bottom of node $\rm{C}$, which is the point of inflection.

For a more correct representation of the deformed structure, the rotation of node $\rm{C}$ can be taken into account, which is $-0.06 \, \rm{rad}$ (↺).

This gives:

```{figure} stat_deter_data/deformed.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

::::

## Exam assignment 3 Continuum mechanics
Your own submission and its grading will be available on [<img height="12px" src="../../figures/ANS.svg" alt="ANS">](https://ans.app/universities/1/courses/576319/assignments/.../go_to) after the exam.


