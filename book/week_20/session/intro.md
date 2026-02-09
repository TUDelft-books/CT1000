```{index} Continuum mechanics; Exam assignment
```
```{index} Buckling; Exam assignment
```

(exam3)=
# Exam Friday January 30th

Today you'll make the second exam assignment covering Continuuum mechanics including its prerequisites and/or the first exam assignment covering Buckling including its prerequisites. For more information about the exam see [the assessment information in course information](exam-general)

## Exam assignment 2 Continuum mechanics

Your own submission and its grading will be available on [<img height="12px" src="../../figures/ANS.svg" alt="ANS"> exam assignment Continuum mechanics 2](https://ans.app/universities/1/courses/576319/assignments/1649807/go_to) after the exam.

Given is the following structure:

::::{margin}
:::{note}
In the original exam, the $y$-axis was incorrectly pointing in the opposite direction. This does not affect the solution of the exercises.
:::
::::

```{figure} intro_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/shear_2
```

:::::{exercise}
:nonumber: true

Show that $A = 78750 \, \rm{mm^2}$, $\bar z_{\rm{NC}} \approx 167 \, \rm{mm}$ and $I_{zz} = 1.1 \cdot 10^9 \, \rm{mm^4}$.

:::::

::::{admonition} Solution
:class: solution, dropdown

$$
A = 100 \cdot 75 \cdot 4 + 2 \cdot \frac{1}{2} \cdot 75 \cdot 50 + 2 \cdot 75 \cdot 50 + 250 \cdot 2 \cdot 75 = 78750 \, \rm{mm}^2
$$

$$
\begin{align*}
\bar z_{\rm{N.C.}} = &\cfrac{S_{\bar z}}{A} \\
= &\cfrac{\frac{1}{2}\cdot 100 \cdot100 \cdot 75 \cdot 4}{78750} \\
&+ 2\cdot \cfrac{\left(100 + \frac{1}{3}\cdot 50\right) \cdot \frac{1}{2} \cdot 75 \cdot 50}{78750}\\
& + \cfrac{\left(100+\frac{1}{2} \cdot 50 \right) \cdot 2 \cdot 75 \cdot 50}{78750}\\
& + \cfrac{\left( 100 + 50 + \frac{1}{2}\cdot 250 \right) \cdot 250 \cdot 2 \cdot 75 }{78750} \\ 
\approx &167 \, \rm{mm}
\end{align*}
$$

$$
\begin{align*}
I_{zz} = &\frac{1}{12} \cdot 4 \cdot 75 \cdot 100^3 + 4 \cdot 75 \cdot 100 \cdot \left( \frac{1}{2} \cdot 100 - 167 \right)^2 \\
&+ 2 \cdot \left( \frac{1}{36} \cdot 75 \cdot 50^3 +  \frac{1}{2} \cdot 75 \cdot 50 \cdot \left( 100 + \frac{1}{3}\cdot 50 - 167 \right)^2\right) \\
&+ \frac{1}{12} \cdot 2 \cdot 75 \cdot 50^3 + 2 \cdot 75 \cdot 50 \cdot \left(100+\frac{1}{2} \cdot 50 - 167 \right)^2 \\
&+ \frac{1}{12} \cdot 2 \cdot 75 \cdot 250^3 + 250 \cdot 2 \cdot 75 \cdot \left( 100 + 50 + \frac{1}{2}\cdot 250 - 167 \right)^2 \\
\approx & 1093 \cdot10^6\, \rm{mm^4}
\end{align*}
$$
    
::::

:::::{exercise}
:nonumber: true

Show that $M_{\rm{C}} = 1800 \, \rm{kNm}$ (◡) and $V_{\rm{C}} = 600 \, \rm{kN}$ (⎽|⎺).

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./intro_data/VLS_1.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/shear_2
```

$$
\sum {T_{\rm{A}}} = 0 \to B_{\rm{v}} = 600 \, \rm{kN} (↑)
$$

```{figure} ./intro_data/VLS_2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/shear_2
```

$$
\sum {F_{\rm{v}}^{\rm{CB}}} = 0 \to V_{\rm{C}} = 600 \, \rm{kN} (⎽|⎺)
$$

$$
\sum {T_{\rm{C}}^{\rm{CB}}} = 0 \to M_{\rm{C}} = 1800 \, \rm{kNm} (◡)
$$
    
::::

:::::{exercise}
:nonumber: true

Find the 3D principal stress tensor at point $\rm{D}$ in cross-section $\rm{C}$ and indicate the direction.

:::::

::::{admonition} Solution
:class: solution, dropdown

$$ S_{\rm{z}}^{\rm{a}} = 150 \cdot 75 \cdot 2 \cdot \left( 100+50+100+\frac{1}{2}\cdot150 - 167\right) \approx 3.54 \cdot 10^6 \, \rm{mm}^3$$

$$ \tau_{\rm{D}} = \cfrac{ 600000 \cdot 3.54 \cdot 10^6 }{ 1093 \cdot 10^6 \cdot 2 \cdot 75 } \approx 13 \, \rm{MPa} (↑) $$

$$ \sigma_{\rm{D}} = \cfrac{ 1800 \cdot 10^6 \cdot \left( 100 + 50 + 100 - 167 \right) }{ 1093 \cdot 10^6 } \approx +136 \, \rm{MPa} $$

This leads to the following stress tensor at point $\rm{D}$ in cross-section $\rm{C}$ according to the given coordinate system:

$$
\boldsymbol{\sigma} =
\begin{bmatrix}
136 & 0 & -13 \\
0 & 0 & 0 \\
-13 & 0 & 0
\end{bmatrix} \, \rm{MPa}
$$

In an upward $y$, rightward $x$ coordinate system, the stress tensor is:

$$
\boldsymbol{\sigma} =
\begin{bmatrix}
136 & 13 & 0 \\
13 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix} \, \rm{MPa}
$$

The direction of the principal stresses can be found using:

$$
\alpha = \frac{1}{2} \cdot \arctan \left( \cfrac{13}{\frac{1}{2} \cdot\left(136 - 0\right)} \right) = 5.4^\circ
$$

The principal stresses can be found using:

$$
\begin{align*}
\sigma_1 &= \frac{1}{2} \cdot \left( 136 - 0 \right) + \frac{1}{2} \cdot \left(136 - 0 \right) \cdot \cos \left( 2 \cdot 5.4 \right) + 13 \cdot \sin \left( 2 \cdot 5.4 \right) = 137 \, \rm{MPa} \\
\sigma_2 &= \frac{1}{2} \cdot \left( 136 - 0 \right) - \frac{1}{2} \cdot \left(136 - 0 \right) \cdot \cos \left( 2 \cdot 5.4 \right) - 13 \cdot\sin \left( 2 \cdot 5.4 \right) = -1.2 \, \rm{MPa} \\
\end{align*}
$$

Leading to:

$$
\boldsymbol{\bar \sigma} =
\begin{bmatrix}
137 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & -1.2
\end{bmatrix} \, \rm{MPa}
$$

In the following direction:

```{figure} ./intro_data/direction.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/shear_2
```

::::

## Exam assignment 1 Buckling
The exam assignment was provided as shown [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/stab_exam/CT1000S-stab-deeltentamen-JAN2026.pdf). The solution is included in the same file.
