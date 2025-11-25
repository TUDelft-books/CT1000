```{index} Failure models; Class exercise
```

% Source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsie2

(lesson13.2)=
# Lesson November 25th

Today's we'll demonstrate how to evaluate failure criteria.

## Demonstration failure criteria

Given is the following structure and cross-section:

```{figure} intro_data/constructie.svg
---
align: center
---
Structure and cross-section, with point $\rm{C}$ in the cross-section of $\rm{A}$.
```

Evaluate where the shear force center is located and find the required yield stress of the material in order to prevent failure in point $\rm{C}$ according to Tresca. Draw the required Tresca failure envelope too.

We can start with evaluating the internal forces in the structure:

```{figure} intro_data/VLS_3D.svg
---
align: center
---
Free body diagram in 3D showing internal forces at $\rm{A}$
```

This figure can also be drawn in 2D:

```{figure} intro_data/VLS_2D.svg
---
align: center
---
Free body diagram in 2D showing internal forces at $\rm{A}$
```

$$
\begin{align*}
\sum T_{\rm{y}} &= 0 \\
-M_{z\rm{,A}} - 2 \cdot 4 &= 0 \\
M_{z\rm{,A}} &= -8 \ \rm{kNm} \left( ◠ \right)
\end{align*}
$$

$$
\begin{align*}
\sum F_{\rm{z}} &= 0 \\
-V_{z\rm{,A}} + 2 &= 0 \\
V_{z\rm{,A}} &= 2 \ \rm{kN} \left( ⎺|⎽ \right)
\end{align*}
$$

$$
\begin{align*}
\sum F_{\rm{x}} &= 0 \\
-N_{\rm{A}} -30 &= 0 \\
N_{\rm{A}} &= -30 \ \rm{kN} \left( - \right)
\end{align*}
$$

$$
\begin{align*}
\sum T_{\rm{x}} &= 0 \\
-M_{\rm{t,A}} -0.4 &= 0 \\
M_{\rm{t,A}} &= -0.4 \ \rm{kNm} \left( \twoheadrightarrow \mid \twoheadleftarrow \right)
\end{align*}
$$

The torsional moment distribution can also be shown like the other internal forces distributions:

```{figure} intro_data/Mt.svg
---
align: center
---
Torsional moment distribution along the structure.
```

This cross-section is symetrical in the $y$-axis, therefore the centroid is located at $z=0$. Furthermore, that means that if the structure is loaded in the $y$-direction only, the normal and shear stress will form a symmetrical pattern too. However, that's not true for loading in the $z$-direction. Therefore, the stresses in the whole cross-section are calculated.

$$
\begin{align*}
A &= 200 \cdot 15 \cdot 3 + 50 \cdot 15 \cdot 2 = 10500 \, \rm{mm^2} \\
I_{zz} &= \frac{1}{12} \cdot 15 \cdot 200^3 \\
& \, \, \, + 2 \cdot \left( \frac{1}{12} \cdot 200 \cdot 15^3 + 15 \cdot 200 \cdot 100^2 \right) \\
& \, \, \, + 2 \cdot \left( \frac{1}{12} \cdot 15 \cdot 50^3 + 50 \cdot 15 \cdot 75^2 \right) \\
&= 79 \cdot 10^6 \, \rm{mm^4}
\end{align*}
$$

Now the normal stress distribution can be found:

$$
\begin{align*}
\sigma_{\rm{N}} &=\frac{-30 \cdot 10^3}{10500} = -2.86 \, \rm{MPa} \\
\sigma_{\rm{M,flange}} &= \frac{-8 \cdot 10^6 \cdot 100}{79 \cdot 10^6} = 10.1 \, \rm{MPa} \\
\sigma_{\rm{M,C}} &= \frac{-8 \cdot 10^6 \cdot 50}{79 \cdot 10^6} = 5.06 \, \rm{MPa} \\
\end{align*}
$$

```{figure} intro_data/sigma_N.svg
---
align: center
---
Normal stresses due to axial force
```

```{figure} intro_data/sigma_M.svg
---
align: center
---
Normal stresses due to bending moment
```

Furthermore, the shear stress distribution due to the shear force can be found:

$$
\begin{align*}
\tau_{V\rm{,flange,right}} &= \frac{2 \cdot 10^3 \cdot 50 \cdot 15 \cdot 75}{15 \cdot 79 \cdot 10^6} = 0.095 \, \rm{MPa} \\
\tau_{V\rm{,flange,left}} &= \frac{2 \cdot 10^3 \cdot \left( 50 \cdot 15 \cdot 75 + 200 \cdot 15 \cdot 100 \right) }{3 \cdot 79 \cdot 10^6} = 0.60 \, \rm{MPa} \\
\tau_{V\rm{,C}} &= \frac{2 \cdot 10^3 \cdot \left( 50 \cdot 15 \cdot 75 + 200 \cdot 15 \cdot 100 + 50 \cdot 15 \cdot 75 \right)}{3 \cdot 79 \cdot 10^6} = 0.70 \, \rm{MPa}\\
\tau_{V\rm{,max}} &= \frac{2 \cdot 10^3 \cdot \left( 50 \cdot 15 \cdot 75 + 200 \cdot 15 \cdot 100 + 100 \cdot 15 \cdot 50 \right)}{3 \cdot 79 \cdot 10^6} = 0.73 \, \rm{MPa}\\
\end{align*}
$$

Leading to

```{figure} intro_data/shear.svg
---
name: shear_stress
align: center
---
Shear stresses due to shear force
```

As can be seen from the shear stresses, although they are in horizontal and vertical equilibrium, they create a counter-clockwise rotation around the centroid, effectively leading to a torsional moment. As this torsional moment isn't there in the structure, it can be though of as the shear force itself acting eccentrically:

```{figure} intro_data/V.svg
---
name: shear_eccentric
align: center
---
Shear force acting eccentrically
```

The location of where the shear force acts to have the same torsional moment effect as the shear stresses, is called the shear force centre. It can be calculated by comparing {numref}`shear_stress` with figure {numref}`shear_eccentric`, which both should have the same torsional moment around any point.

$$
\begin{align*}
\sum T_{\bar x\rm{,web,stresses}} &= \sum T_{\bar x\rm{,web,shear} \, \rm{force}} \\
\cfrac{2000 \int_{50}^{100} \left( 15 \ z \cdot \left( 50 + z/2\right) \right) dz }{15 \cdot 79 \cdot 10^6} \ 15 \cdot 200 \\
+ 0.095 \cdot 15 \cdot 200 \cdot 100 \\
+ 0.095 \cdot 15 \cdot 200 \cdot 100 \\
+ \cfrac{2000 \int_{-50}^{-100} \left( 15 \ z \cdot \left( -50 - z/2\right) \right) dz }{15 \cdot 79 \cdot 10^6} \ 15 \cdot 200 &= 2000 \cdot e \\
e &\approx 111 \, \rm{mm}
\end{align*}
$$

So the shear force center is located at approximately $111 \, \rm{mm}$ left of the web.

Now we can continue finding the stresses at point $\rm{C}$, combining the normal and shear stresses, with the stress due to the torsional moment. Note that there's no additional torsion moment other than the $-0.4 \, \rm{kNm}$, as the external force is applied at the shear force center.

We have an open-thin walled cross-section, therefore, the torsional cross-sectional property, the torsion constant $I_{\rm{t}}$, can be calculated with:

$$
\begin{align*}
I_{\rm{t}} &= \frac{1}{3} \cdot \sum \left( t_i^3 \cdot h_i \right) \\
&= \frac{1}{3} \cdot \left( 3 \cdot 15^3 \cdot 200 +  2 \cdot 15^3 \cdot 50 \right) \\
&= 787500 \, \rm{mm^4}
\end{align*}
$$

The shear stress due to torsion can now be calculated as:

$$
\begin{align*}
\tau_{\rm{t,C}} &= \left| \cfrac{M_t \cdot e_{\rm{m}}}{\frac{1}{2} I_{\rm{t}}} \right| \\
\tau_{\rm{t,C}} &= \left|  \cfrac{-0.4 \cdot 10^6 \cdot 7.5}{0.5 \cdot 787500} \right| \\
\tau_{\rm{t,C}} &\approx 7.62 \, \rm{MPa}
\end{align*}
$$

This stress is working counterclockwise in the cross-section, so upwards in $\rm{C}$ (where the shear stress due to bending was acting downwards). The total stress state at point $\rm{C}$ can now be summarised in the following stress tensor:

$$
\sigma  = \left[ \begin{array}{}
{-2.86 + 5.06}&{-0.70 + 7.62}\\
{-0.70 + 7.62}&{0}
\end{array} \right] = \left[ \begin{array}{}
{2.21}&{6.92}\\
{6.92}&{0}
\end{array} \right]
{\ \rm{ MPa}}
$$

```{figure} intro_data/stress-state.svg
---
align: center
---
Stress state at point $\rm{C}$
```

The principal stresses can be calculated as:

$$
\begin{align*}
\sigma_{1,2} &= \frac{2.21 + 0}{2} \pm \sqrt{ \left( \frac{2.21 - 0}{2} \right)^2 + 6.92^2 } \\
\sigma_{1,2} &\approx 8.05 \, \rm{MPa} \, , \, -5.84 \, \rm{MPa}
\end{align*}
$$

According to the Tresca failure criterion in 2D, the material will fail when:

$$
\begin{align*}
\left| \sigma_1 - \sigma_2 \right| &\geq \sigma_{\rm{y}} \\
\left| 8.05 - \left( -5.84 \right) \right| &\geq \sigma_{\rm{y}} \\
14 \geq \sigma_{\rm{y}}
\end{align*}
$$

So the yield stress of the material should be at least $14 \, \rm{MPa}$ to prevent failure in point $\rm{C}$.

```{figure} intro_data/envelope.svg
---
name: shear_eccentric
align: center
---
Tresca failure envelope showing the stress state at point $\rm{C}$
```

