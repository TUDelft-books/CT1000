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

Provide three valid variants to make this structure statically determinate for the purpose of the force method. Provide three different variants: over all variants, you must have adjusted at least each node and element once.
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

Draw the displaced statically indeterminate structure for which you indicate the displacements of node $\rm{C}$ and the location of the point of inflection (the point for which the curvature changes sign).

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

```{hide-sticky-margin}
```

## Exam assignment 3 Continuum mechanics
Your own submission and its grading will be available on [<img height="12px" src="../../figures/ANS.svg" alt="ANS">](https://ans.app/universities/1/courses/576319/assignments/.../go_to) after the exam.


Given is the following structure:

::::{grid}
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} continuum_data/cross-section.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/continuum_exam
```

:::

:::{grid-item}
:columns: auto

```{figure-start} continuum_data/structure.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/continuum_exam
```

Forces and support reactions are acting on the normal force centre.
The cross-section can be regarded as thin-walled

```{figure-end}
```

:::

::::

:::::{exercise}
:nonumber: true

Show that $A = 150 \sqrt{2} \, \rm{cm}^2$, $\bar z_{\rm{N.C.}} = 0 \, \rm{mm}$ and $I_{zz} = 31250 \sqrt{2} \, \rm{cm}^4$.

:::::

::::{admonition} Solution
:class: solution, dropdown

The area of the cross section is:

$$ A = 2 \cdot 50 \cdot \sqrt{2} \cdot 1.5 = 150 \sqrt{2} \, \rm{cm}^2 $$

There is as much material above as below the $y$-axis, which gives $\bar z_{\rm{N.C.}} = 0 \, \rm{mm}$.

The second moment of area $I_{zz}$ is (taking into account the projected horizontal thickness of the parts):

$$I_{zz} = 2 \cdot \cfrac{1}{12} \cdot 1.5 \sqrt{2} \cdot 50^3 = 31250 \cdot \sqrt{2} \, \rm{cm}^4$$

::::

:::::{exercise}
:nonumber: true

Show that $V_{\rm{B}}^{\rm{SB}} = -60 \, \rm{kN}$ and $M_{\rm{B}} = -240 \, \rm{kNm}$.

:::::

::::{admonition} Solution
:class: solution, dropdown

Using equilibrium equation you can find:

- $ V_{\rm{B}}^{\rm{SB}} = -60 \, \rm{kN}$
- $ M_{\rm{B}} = -240 \, \rm{kNm}$

::::

:::::{exercise}
:nonumber: true

Determine the 3D stress tensor on a positive cross section just left of $\rm{B}$ in point $\rm{E}$. Indicate the directions of this stress tensor.

:::::

::::{admonition} Solution
:class: solution, dropdown

To find the shear stress in $\rm{E}$, the part below $\rm{E}$ can be seen as sliding off, this gives:

$$\tau = \cfrac{\left| -60000 \cdot 0.125 \cdot 0.015 \cdot \sqrt{2} \cdot \cfrac{0.125}{2} \right|}{0.015 \cdot 31250 \cdot \sqrt{2} \cdot 10^{-8}} = 2 \cdot 10^6 \, \rm{Pa} = 2 \, \rm{MPa}$$

As the shear force acts upwards on a positive cross section, the shear stress acts in in top right direction in $\rm{E}$

The normal force can be found with:

$$\sigma = \cfrac{ -240 \cdot 10^3\cdot 0.125}{31250 \cdot \sqrt{2} \cdot 10^{-8}} = -48 \cdot 10^6 \cdot \sqrt{2} \, \rm{Pa} \approx -67.88 \, \rm{MPa}$$

So the 3D stress tensor is:

$$\sigma = \begin{bmatrix} -67.88 & 0 & -2 \\ 0 & 0 & 0 \\ -2 & 0 & 0 \end{bmatrix} \, \rm{MPa}$$

With the $x$-axis in the original $x$-direction, the $z$-axis along the edge to the bottom left and the $y$-axis perpendicular to the edge to the top left:

```{figure} continuum_data/direction.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/continuum_exam
```

::::

:::::{exercise}
:nonumber: true

Determine the deviatoric stress tensor on a positive cross section just left of $\rm{B}$ in point $\rm{E}$. Include the direction of the coordinate system of this deviatoric stress tensor.

:::::

::::{admonition} Solution
:class: solution, dropdown

The principle stresses are:

- $\sigma_1 = \frac{1}{2} \cdot 67.88 + \frac{1}{2} \cdot \sqrt{68^2 + 4 \cdot 1.5^2} \approx 67.92 \, \rm{MPa}$
- $\sigma_2 = \frac{1}{2} \cdot 67.88 - \frac{1}{2} \cdot \sqrt{68^2 + 4 \cdot 1.5^2} \approx -0.033 \, \rm{MPa}$
- $\sigma_3 = 0 \, \rm{MPa}$

This gives the isotropic stress:

$$\sigma_{\rm{o}} = \cfrac{67.92 - 0.033 + 0}{3} \approx 22.63 \, \rm{MPa}$$

This gives the deviatoric stress tensor:

$$\sigma_{\rm{d}} = \begin{bmatrix} 67.92 - 22.63 \\ -0.033 -22.63 \\ 0 - 22.63 \end{bmatrix} = \begin{bmatrix} 45.29 \\ -22.66 \\ -22.63 \end{bmatrix} \, \rm{MPa}$$

This stress tensor is coordinated in the principle stress directions, which are not the same as the original stress tensor.

The coordination system of the deviatoric stress tensor is the principle stress direction. This is the original coordinate system rotated over an angle of $\theta = \frac{1}{2} \cdot \arctan \left( \cfrac{1.5}{\frac{1}{2} \left(67.88 - 0\right)} \right) \approx 1.26^{\circ}$ around the $y$-axis of the 3D stress tensor in the direction from $z$ to $x$.

::::
