```{index} Static indeterminate structures; Exam assignment
```
```{index} Continuum mechanics; Exam assignment
```

(exam2)=
# Exam Tuesday December 9th

Today you'll make the second exam assignment covering Statically indeterminate structures including its prerequisites and/or the first exam assignment covering Continuum mechanics including its prerequisites. For more information about the exam see [the assessment information in course information](exam-general)

## Exam assignment 2 Statically indeterminate structures

Your own submission and its grading will be available on [<img height="12px" src="../../figures/ANS.svg" alt="ANS"> exam assignment Statically indeterminate structures 2](https://ans.app/universities/1/courses/576319/assignments/1584858/go_to) after the exam.

Given is the following structure:

```{figure} intro_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

:::::{exercise}
:nonumber: true

Show that this structure is statically indeterminate to the second degree.

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} intro_data/stat_onbepaald.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

For this structure, the external static indeterminacy is equal to the internal static indeterminacy.

There are 8 unknowns and 6 equilibrium equations, making the structure statically indeterminate to the second degree.

::::

:::::{exercise}
:nonumber: true

Provide two alternative valid variants to make this structure statically determinate for the purpose of the force method or displacement method with statically indeterminate displacements. Provide two different variants: your adjustments must each modify a different part of the structure.
For each of the variants, provide the necessary equation(s) to determine the statically indeterminate force(s) or statically indeterminate displacement(s).

:::::

::::{admonition} Solution
:class: solution, dropdown

A few potential variants are:

```{figure} ./intro_data/variant1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

```{figure} ./intro_data/variant2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
```

::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Creating a mechanism**

Many students created a mechanism by replacing the fixed support in A with a horizontal roller support.

```{figure} ./intro_data/mechanisme.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Mechanism created when replacing fixed support in A with horizontal roller support
```

::::::

:::::{exercise}
:nonumber: true

Determine the support bending moment in $\rm{A}$ using the force- or a displacement method.

:::::

::::{admonition} Solution
:class: solution, dropdown

As an example, the displacement method with as degree of freedom the horizontal displacement in $\rm{B}$, but other methods could be used too:

```{figure} ./intro_data/vrijheidsgraad.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Structure with degree of freedom the horizontal displacement in $\rm{B}$
```

The free body diagram of the split structure is:

```{figure} ./intro_data/gesplitst.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Split structure
```

For both parts we can now find internal forces at $\rm{B}$ as a function of $w_{\rm{B}}$. We are especially interested in the horizontal forces, since there will also be an unknown vertical support reaction in $\rm{B}$ to be solved for in the vertical direction.

First, the effect of the horizontal displacement on segment $\rm{AB}$ is considered. For this, the following forget-me-not applies, leading to internal forces in the shown direction:

```{figure} ./intro_data/AB.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

On the left the forget-me-not to calculate the internal forces due to on segment  corresponding to forget-me-not (2) from the book Mechanics, Statically indeterminate structures and failure analysis {cite:t}`Hartsuijker2016`. On the right the split segment with the resulting internal forces.
```

$$
V_{\rm{B}}^{\rm{AB}} = w_{\rm{B}} \cdot \cfrac{3 EI}{L_{\rm{AB}}^3} = w_{\rm{B}} \cdot \cfrac{3 768 \cdot 10^3}{4^3} = 36000 w_{\rm{B}} \, \rm{kN}
$$

For $\rm{BC}$:

```{figure} ./intro_data/BC.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Part $\rm{BC}$ loaded with an axial force, shortened and rotated.
```

We can use Williot to find the shortening:

```{figure} ./intro_data/williot.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Williot diagram of the displacement in $\rm{B}$ and the shortening of $\rm{BC}$
```
$$
\Delta L_{\rm{BC}} = -\cfrac{3}{5} w_{\rm{B}}
$$

And thus:

$$
N_{\rm{BC}} = E A \cfrac{\Delta L_{\rm{BC}}}{L_{\rm{BC}}} = 125 \cdot 10^3 \cdot \cfrac{\cfrac{3}{5} w_{\rm{B}}}{5} = 15000 w_{\rm{B}} \, \rm{kN} \, \rm{(compression)} 
$$

Now that we have the horizontal internal forces, we can set up the equilibrium equations for node $\rm{B}$:

```{figure} ./intro_data/B.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Free body diagram of node $\rm{B}$
```

$$
\begin{align*}
\sum F_{\rm{h}} &= 0: \\
90 - 36000 w_{\rm{B}} - 15000 w_{\rm{B}} \cdot \cfrac{3}{5} &= 0 \\
w_{\rm{B}} &= 0.002 \, \rm{m} = 2 \, \rm{mm} \, \rm{(→)} \\
\end{align*}
$$

Now, the horizontal reaction in $\rm{A}$ can be determined using another forget-me-not:

```{figure} ./intro_data/AB_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

On the left the forget-me-not to calculate the internal forces due to on segment  corresponding to forget-me-not (f) from the book Mechanics, Statically indeterminate structures and failure analysis {cite:t}`Hartsuijker2016`. On the right the split segment with the resulting internal forces and support reactions.
```

$$
A_{\rm{h}} = \cfrac{3 EI}{L_{\rm{AB}}^3} \cdot w_{\rm{B}} = \cfrac{3 \cdot 768 \cdot 10^3}{4^3} \cdot 0.002 = 72 \, \rm{kN} \, \rm{(←)}
$$

::::

::::{admonition} Alternative solution
:class: solution, dropdown

An alternative solution is to use the force method with as statically indeterminate forces the moment and vertical force in $\rm{A}$. This is shown [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/exam_SOB/resolution.pdf).

::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Trying to solve displacement of mechanism**

The mechanism created in the previous exercise cannot be used to determine displacements, since it is a mechanism. Some students still tried to determine displacements of this mechanism, which is not possible.

```{figure} ./intro_data/mechanisme.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Mechanism created when replacing fixed support in A with horizontal roller support
```

**Incomplete Williot diagram**

When the structure is made statically determinate by removing the roller support at $\rm{B}$ and splitting the two-force member $\rm{BC}$, like so:

```{figure} ./intro_data/williot_complex.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Statically determinate structure after removing roller support in $\rm{B}$ and splitting two-force member $\rm{BC}$
```

The williot diagram in which $\rm{B}$ only moves horizontally is incomplete: beam $\rm{AB}$ will also shorten, leading to a vertical displacement in $\rm{B}$ as well. This vertical displacement must also be taken into account in the williot diagram.

::::::

:::::{exercise}
:nonumber: true

Determine the support bending moment in $\rm{A}$ in the extreme cases that $EA_{\rm{BC}} \to 0$ and $EA_{\rm{BC}} \to \infty$.

:::::

::::{admonition} Solution
:class: solution, dropdown

For $EA_{\rm{BC}} \to 0$, segment $\rm{BC}$ can be ignored for the purpose of load transfer. The structure then simplified to:

```{figure} ./intro_data/AB_0.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Simplified structure for $EA_{\rm{BC}} \to 0$
```

And the support moment in $\rm{A}$ can be found using static equilibrium:

```{figure} ./intro_data/FBD_AB_0.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Free body diagram of the simplified structure for $EA_{\rm{BC}} \to 0$
```

$$
\begin{align*}
\left. \sum T \right|_{\rm{A}} &= 0: \\
A_{\rm{m}} - 90 \cdot 4 &= 0 \\
A_{\rm{m}} &= 360 \, \rm{kNm} \, \rm{(↻)}
\end{align*}
$$

For $EA_{\rm{BC}} \to \infty$, support $\rm{B}$ can be considered as a hinged support. The structure then simplified to:

```{figure} ./intro_data/AB_inf.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB

Simplified structure for $EA_{\rm{BC}} \to \infty$
```

This gives $A_{\rm{m}} = 0 \, \rm{kNm}$ because the load is fully carried by the hinged support in $\rm{B}$.
::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Not simplified**

Although not wrong, some student redid their calculations as done in exercise 3 instead of explicitly simplifying the structure. For the cases $EA_{\rm{BC}} \to 0$, only equilibrium can be used. For $EA_{\rm{BC}} \to \infty$, a forget-me-not can be used.

::::::



## Exam assignment 1 Continuum mechanics

Your own submission and its grading will be available on [<img height="12px" src="../../figures/ANS.svg" alt="ANS"> exam assignment Continuum mechanics 1](https://ans.app/universities/1/courses/576319/assignments/1584881/go_to) after the exam.

Given is the following structure and cross-section:

```{figure} intro_data/constructie2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
```

:::::{exercise}
:nonumber: true

Show that $A = 21600 \, \rm{mm^2}$, $\bar z_{\rm{N.C.}} = \cfrac{650}{3} \approx 217 \, \rm{mm}$ and $I_{zz} = 858.072 \cdot 10^6 \, \rm{mm^4}$.

:::::

::::{admonition} Solution
:class: solution, dropdown

$$
A = 500 \cdot 12 + 2 \cdot \sqrt{600^2 + 250^2} \cdot 12= 21600
$$

$$
\bar z_{\rm{N.C.}} = \cfrac{2\cdot \sqrt{600^2 + 250^2} \cdot 12 \cdot 300}{A} = \cfrac{650}{3} \approx 217 \, \rm{mm}
$$

```{figure} intro_data/wand.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum
```

$$
\begin{align*}
I_{zz} &= \cfrac{1}{12} \cdot 500 \cdot 12^3 + 500 \cdot 12 \cdot \left( -\cfrac{650}{3} \right)^2 \\
& \quad + 2 \cdot \left( \cfrac{1}{12} \cdot \cfrac{13}{12} \cdot 12 \cdot 600^3 + \sqrt{600^2 + 250^2} \cdot 12 \cdot \left( 300 - \cfrac{650}{3} \right)^2 \right) \\
& = 85.8072 \cdot 10^6 \, \rm{mm^4}
\end{align*}
$$
    
::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Calculating $I_{zz}$ incorrectly**

Many studenten calculated $I_{zz}$ of the diagonal parts of the cross-section with the incorrect formula: $I_{zz} = \frac{1}{12} b h^3 \sin^2\left(\theta\right)$. This formula is incorrect. $I_{zz}$ is actually part of a tensor (with $I_{yy}$ and $I_{yz}$) and the correct transformation formulas could be used to find $I_{zz}$ in the global coordinate system. However, looking at the diagonal element as a parallelogram would also work.

::::::

:::::{exercise}
:nonumber: true

Find the strain tensor at point $\rm{D}$ in cross-section $\rm{A}$ and indicate the coordinate system for this strain tensor.

:::::

::::{admonition} Solution
:class: solution, dropdown

The section force can be found using equilibrium:

```{figure} intro_data/FBD_continuum.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum

Free body diagram with the section force at cross-section $\rm{A}$
```

$$
\begin{align*}
\sum F_{\rm{z}} &= 0 \to V_{z,\rm{A}} = 120 \, \rm{kN} \\
\sum M_{\rm{y}} &= 0 \to M_{y,\rm{A}} = 120 \cdot 10 = 1200 \, \rm{kNm} \\
\sum M_{\rm{x}} &= 0 \to M_{\rm{t,A}} = 72 \, \rm{kNm} \\
\end{align*}
$$

This gives the following normal and shear stresses (excluding the torsion for now):

$$
\begin{align*}
\sigma &= \cfrac{1200 \cdot 10^6 \cdot \cfrac{650}{3}}{85.8072 \cdot 10^6} \approx 303 \, \rm{MPa} \, \rm{(tension)} \\
\tau &= \cfrac{120 \cdot 10^3 \cdot 500 \cdot 12 \cdot \cfrac{650}{3}}{2 \cdot 12 \cdot 85.8072 \cdot 10^6} = 7.58 \, \rm{MPa}
\end{align*}
$$

For the torsional shear stresses, we can use the model for thin-walled, closed, non-circular cross-sections:

$$
\tau = \cfrac{72 \cdot 10^6}{2 \cdot 500 \cdot 600 \cdot \frac{1}{2} \cdot 12} = 20 \, \rm{MPa}
$$

The shear stress due to bending and due to torsion act in the same direction, so they can be added. Leading to:

$$
\boldsymbol{\sigma} = \begin{bmatrix}
    303 & 27.58 \\
    27.58 & 0
\end{bmatrix} \rm{MPa} \, \text{(in the xy-coordinate system)}
$$

This gives the following strain tensor using Hooke's law for plane stress:

$$
\boldsymbol{\varepsilon} = \cfrac{1}{210000} \begin{bmatrix}
    1 & -0.3 & 0 \\
    -0.3 & 1 & 0 \\
    0 & 0 & 1 + 0.3
\end{bmatrix}
\begin{bmatrix}
    303 \\
    0 \\
    27.58
\end{bmatrix} = \begin{bmatrix}
    1.44 \\
    -0.43 \\
    0.17
\end{bmatrix}
\cdot 10^{-3} \, \text{(in the xy-coordinate system)}
$$

::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Shear stresses due to bending forgotten**

Some students only calculated the shear stresses due to torsion, forgetting the shear stresses due to bending.

**Directions of shear stresses mixed up**

Some students mixed up the directions of the shear stresses due to bending and torsion, leading to incorrect addition of the shear stresses or stresses in the wrong direction.

The internal forces act on a negative cut as follows:

```{figure} intro_data/directions.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum

Directions of internal forces
```

Leading to shear stresses for both bending and torsion in the negative y-direction on a negative cut and in the positive y-direction on a positive cut.

**Direction of tensor not clear**

Many students wrote down a strain tensor without clearly indicating the coordinate system in which this tensor is acting (which should have been the $xy$-coordinate system) as the normal stresses in (thin-walled) point $\rm{D}$ work in the $x$-direction and the shear stresses in the $xy$-plane. The strain tensor could have been described in the full 3D coordinate system too.

::::::

:::::{exercise}
:nonumber: true

Find the principle strains in point $\rm{D}$ in cross-section $\rm{A}$ and indicate their directions.

:::::

::::{admonition} Solution
:class: solution, dropdown

In an upward $y$, rightward $x$ coordinate system, the strain tensor is:

$$
\boldsymbol{\varepsilon} = \begin{bmatrix}
    1.44 & -0.17 \\
    -0.17 & -0.43
\end{bmatrix} \cdot 10^{-3}
$$

The direction of the principal strains can be found using:

$$
\alpha = \cfrac{1}{2} \arctan \left( \cfrac{-0.17}{\frac{1}{2} \left(1.44 - (-0.43)\right)} \right) = -5.2^\circ
$$

The principal strains can be found using:

$$
\begin{align*}
\varepsilon_1 &= \frac{1}{2} \left( 1.44 - 0.43 \right) + \frac{1}{2} \left(1.44 + 0.43 \right) \cos \left( 2 \cdot -5.2 \right) - 0.17 \sin \left( 2 \cdot -5.2 \right) = 1.46 \cdot 10^{-3} \\
\varepsilon_2 &= \frac{1}{2} \left( 1.44 - 0.43 \right) - \frac{1}{2} \left(1.44 + 0.43 \right) \cos \left( 2 \cdot -5.2 \right) + 0.17 \sin \left( 2 \cdot -5.2 \right) = -0.45 \cdot 10^{-3} \\
\end{align*}
$$

With $\varepsilon_1$ at $-5.2^\circ$ (clockwise) from the $x$-axis and $\varepsilon_2$ at $84.8^\circ$ (counterclockwise) from the $x$-axis.

::::

::::::{admonition} Frequently made mistakes
:class: remark, dropdown

**Used transformation formula for $x-y$ coordinate system for mirrored coordinate system**

Many students applied the transformation formulas (which are valid for a rightward $x$, upward $y$ coordinate system) on another coordinate system (for example upward $y$, rightward $x$). This can lead to incorrect results.

```{figure} ./intro_data/coordinate.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_continuum

THe transformation formulas are only valid for a rightward $x$, upward $y$ coordinate system.
```

**Not clear why $\varepsilon_1$ is in the principle direction or at $90^\circ$ from that one**

Many students calculated the principal strains correctly and a direction. But from the direct formulas for principle strains it cannot be found which strain corresponds to which direction. This can only be found by substituting the directions back into the transformation formulas to see which strain corresponds to which direction.

::::::
