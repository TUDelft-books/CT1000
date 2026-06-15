```{index} Displacement method using statically indeterminate displacement; Demonstration
```
```{index} Displacement method using degrees of freedom; Demonstration
```
```{index} Matrix method; Demonstration
```
```{index} Temperature influences; demonstration for statically indeterminate structures
```
```{index} Support settlement; demonstration
```
```{index} Stiffness influences; demonstration
```

(lesson7.1)=
# Lesson October 12th

During today's lesson it's demonstrated how you to handle temperature influences, stiffness discontinuities and support settlement for statically indeterminate structures. Furthermore, we'll introduce two more methods for solving statically indeterminate structures: the displacement method using degrees of freedom and the matrix method.

% source files at https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

## Stiffness discontinuities

Let's investigate the stiffness discontinuities first. Consider the following structure:

```{figure} intro_data/temp_infl.svg
:align: center
```

In which we will investigate the influence of a varying stiffness of $\rm{AC}$ on the displacement of $\rm{D}$. There are two approaches to do this: (1) do the calculation including a multiplication factor $n$ for the stiffness of $\rm{AC}$, or (2) investigating the extremes by simplifying the structure by replacing $\rm{AC}$ with an infinite stiff member and a zero stiff member.

### Multiplication factor

Let's start with this first approach.

We'll solve the structure by using the displacement method with the rotation of $\varphi_{\rm{C}}$ as degree of freedom:

```{figure} intro_data/phi_C.svg
:align: center
```

For $\rm{AC}$ this gives:

```{figure} intro_data/AC.svg
:align: center
```

$$\varphi_{\rm{C}} = \cfrac{M_{\rm{AC}} \cdot 4}{3 \cdot n \cdot 320000} \to M_{\rm{AC}} = 240000 \cdot n \cdot \varphi_{\rm{C}}$$

For $\rm{BC}$ this gives:

```{figure} intro_data/BC.svg
:align: center
```

$$\varphi_{\rm{C}} = \cfrac{M_{\rm{AC}} \cdot 5}{4 \cdot 320000} \to M_{\rm{AC}} = 256000 \varphi_{\rm{C}}$$

Now $\varphi_{\rm{C}}$ can be determined:

```{figure} intro_data/Meven.svg
:align: center
```

$$
\sum \left. T \right|_{\rm{C}}^{\rm{DC}} = 0 \to \varphi_{\rm{C}} = \cfrac{279}{10000 \cdot \left( 15 \cdot n + 16 \right)}
$$

Now, the displacement of $\rm{D}$ can be determined by extending the rotation of $\varphi_{\rm{C}}$ over member $\rm{CD}$ and add vertical displacement due to the load:

```{figure} intro_data/CD.svg
:align: center
```

$$
\begin{align*}
w_{\rm{D}} &= \varphi_{\rm{C}} \cdot 4 + \cfrac{111.6 \cdot 4^3}{3 \cdot 320000} \\
w_{\rm{D}} & = \cfrac{93}{12500} + \cfrac{279}{2500 \cdot \left( 15 \cdot n + 16 \right)} \\
w_{\rm{D}} & = 0.00744 + \cfrac{0.1116}{15 \cdot n + 16}
\end{align*}
$$

This result can be plotted for different values of $n$:

```{figure} intro_data/plot.svg
:align: center
```

#### Extreme cases

Instead of evaluating the displacement for different values of $n$, we can also investigate the extreme cases: $n \to \infty$ and $n = 0$.

For $n \to \infty$, no rotation is allowed in $\rm{C}$, which reduces the structure to a statically determinate structure:

```{figure} intro_data/CD.svg
:align: center
```

Which gives a displacement using forget-me-nots of:

$$
\begin{align*}
w_{\rm{D}} &= \cfrac{111.6 \cdot 4^3}{3 \cdot 320000} \\
w_{\rm{D}} & = \cfrac{279}{2500 \cdot \left( 15 \cdot n + 16 \right)} \\
w_{\rm{D}} & = 0.00744
\end{align*}
$$

This could also be reasoned by taking the limit of the previous expression for $w_{\rm{D}}$ when $n \to \infty$:

$$
\begin{align*}
\lim_{n \to \infty} w_{\rm{D}} &= \lim_{n \to \infty} \left( 0.00744 + \cfrac{0.1116}{15 \cdot n + 16} \right) \\
\lim_{n \to \infty} w_{\rm{D}}&= 0.00744 + 0 \\
\lim_{n \to \infty} w_{\rm{D}}&= 0.00744
\end{align*}
$$

For $n = 0$, member $\rm{AC}$ doesn't give rotational stiffness to node $\rm{C}$, which reduces the structure to:

```{figure} intro_data/EI0.svg
:align: center
```

Which is a statically indeterminate structure which can be solved with any method of your choice. It will lead to:

$$
w_{\rm{D}} = 0.0144
$$

This could also be reasoned by taking the limit of the previous expression for $w_{\rm{D}}$ when $n = 0$:

$$
\begin{align*}
\lim_{n \to 0} w_{\rm{D}} &= \lim_{n \to 0} \left( 0.00744 + \cfrac{0.1116}{15 \cdot n + 16} \right) \\
\lim_{n \to 0} w_{\rm{D}}&= 0.00744 + \cfrac{0.1116}{16} \\
\lim_{n \to 0} w_{\rm{D}}&= 0.0144
\end{align*}
$$

## Support settlement

Next, let's investigate the influence of support settlement. Consider the following structure:

```{figure} intro_data/supp_settlement.svg
:align: center
```

For statically indeterminate structures, the support settlements will cause internal forces and moments in the structure, as opposed to statically determinate structures where support settlements only causes rigid body displacements

The displacements can be taken into account when applying a force or displacement method. Here, we'll use the force method.

The degree of statical determinacy can be found by evaluating the external statical determinacy: the structure is not a closed structure, so the internal statical determinacy is equal to the external statical determinacy.

```{figure} intro_data/stat_onbepaaldheid.svg
:align: center
```

There are 5 support reaction and one rigid body with 3 equilibrium equations, so the structure is statically indeterminate to the second degree. So, the strucutre is made statical determinate by releasing both the horizontal and vertical support at $\rm{A}$:

```{figure} intro_data/stat_bepaald.svg
:align: center
```

The shear force and bending moment just right of $\rm{C}$ can be determined using equilibrium:

```{figure} intro_data/VCMC.svg
:align: center
```

$$
\sum F_{\rm{v}}^{\rm{DCA}} = 0 \to V_{\rm{C}}^{\rm{CD}} = 111.6 - A_{\rm{v}} \\
\sum \left. T \right|_{\rm{C}}^{\rm{DC}} = 0 \to M_{\rm{C}}^{\rm{CD}} = 446.4 - 4 \cdot A_{\rm{h}}
$$

The displacement and rotation of $\rm{C}$ can be determined with forget-me-nots and the support settlement of $\rm{B}$:

```{figure} intro_data/BC2.svg
:align: center
```

$$
\begin{align*}
w_{\rm{C}} &= \cfrac{(111.6 - A_{\rm{v}}) \cdot 5^3}{3 \cdot 320000} + \cfrac{(446.4 - 4 \cdot A_{\rm{h}}) \cdot 5^2}{2 \cdot 320000} + 0.031 \\
w_{\rm{C}} &=-\cfrac{A_{\rm{h}}}{6400} - \cfrac{A_{\rm{v}}}{7680} + \cfrac{403}{6400} \\
w_{\rm{C}} &\approx -0.00015625 \cdot A_{\rm{h}} - 0.00013020833 \cdot A_{\rm{v}} + 0.06296875 \\
\varphi_{\rm{C}} &= \cfrac{(111.6 - A_{\rm{v}}) \cdot 5^2}{2 \cdot 320000} + \cfrac{(446.4 - 4 \cdot A_{\rm{h}}) \cdot 5}{320000} \\
\varphi_{\rm{C}} &= -\cfrac{A_{\rm{h}}}{16000} - \cfrac{A_{\rm{v}}}{25600} + \cfrac{3627}{320000} \\
\varphi_{\rm{C}} &= -0.0000625 \cdot A_{\rm{h}} - 0.0000390625 \cdot A_{\rm{v}} + 0.011334375
\end{align*}
$$

Now, the displacement of $\rm{A}$ can be determined with the vertical displacement of $\rm{C}$, extending the rotation of $\varphi_{\rm{C}}$ over member $\rm{AC}$ and the additional displacement due to $A_{\rm{h}}$:

```{figure} intro_data/AC2.svg
:align: center
```
$$
\begin{align*}
w_{\rm{A_v}} &= w_{\rm{C}} \\
w_{\rm{A_v}} &=-\cfrac{A_{\rm{h}}}{6400} - \cfrac{A_{\rm{v}}}{7680} + \cfrac{403}{6400} \\
w_{\rm{A_v}} &\approx -0.00015625 \cdot A_{\rm{h}} - 0.00013020833 \cdot A_{\rm{v}} + 0.06296875 \\
w_{\rm{A_h}} &= \varphi_{\rm{C}} \cdot 4 - \cfrac{A_{\rm{h}} \cdot 4^3}{3 \cdot 320000} \\
w_{\rm{A_h}} &=-\cfrac{19 \cdot A_{\rm{h}}}{60000} - \cfrac{A_{\rm{v}}}{6400} + \cfrac{3627}{80000} \\
w_{\rm{A_h}} &\approx -0.00031666667 \cdot A_{\rm{h}} - 0.00015625 \cdot A_{\rm{v}} + 0.0453375
\end{align*}
$$

Solving for the displacement conditions gives:

$$
\left\{
\begin{matrix}
{w_{\rm{A_v}}=0} \\
{w_{\rm{A_h}}=0}
\end{matrix}
\right.
\;\to\;
\begin{matrix}
{A_{\rm{v}} = 764.4 \ \rm{kN}} \\
{A_{\rm{h}} = -234 \ \rm{kN}}
\end{matrix}
$$

With solving the displacement conditions the statically indeterminate structures is essentially solved. The other reaction forces and displacement can be solved for too.

## Temperature influences

Finally, let's investigate the influence of temperature changes. Consider the following structure:

```{figure} intro_data/temp.svg
:align: center
```

In this structure, the beam $\rm{DCB}$ is warmed up. The top side expands most, while the bottom fibre doesn't expand. The expansion can be defined with $\epsilon^{\rm{T}}$ and $\kappa^{\rm{T}}$. These can be calculated with:

$$
\epsilon^{\rm{T}} = \alpha \cdot \Delta T = 10^{-5} \cdot 16 = \cfrac{1}{625} = 0.0016 \ (-) \\
\kappa^{\rm{T}} = \alpha \cdot \frac{\Delta T}{h} = 10^{-5} \cdot \cfrac{32}{0.2} = \cfrac{1}{625} = 0.0016\ \rm{(1/m)}
$$

These strains and curvatures wouldn't cause internal forces in a statically determinate structure, but in this statically indeterminate structure they do. When solving with the force method, it could be thought of as the statically indeterminate forces lead to internal forces because of the additional displacement caused by the temperature changes:

```{figure} intro_data/stat_bepaald_temp.svg
:align: center
```

To calculate the displacements based on the known strains, the displacement can simply be calculated with $\Delta L = \epsilon \cdot L$. For the displacement due to curvature, the curvature can be found by including a kinematic equivalent force, which would lead to the same curvature. This force can be found by $M^{\rm{T}} = E I \cdot \kappa^{\rm{T}}$, which gives:

$$
M^{\rm{T}} = E I \cdot \kappa^{\rm{T}} = 320000 \cdot 0.0016 = 512 \ \rm{kNm}
$$

When this moment is added to the structure at $\rm{D}$ in the counterclockwise direction, the curvature caused by this moment is equal to the curvature caused by the temperature change. The moment should only be considered for calculating curvatures, rotations and displacements, not for calculating internal forces as it's just a trick to be able to apply forget-me-nots.

This leads to the following structure, with the kinematically equivalent force indicated with a dashed line:

```{figure} intro_data/kinem.svg
:align: center
```

Now the displacements at $\rm{C}$ can be calculated in the same way as before, but by adding the influence of the temperature changes of the curvature:

$$
\begin{align*}
w_{\rm{C}} &= \cfrac{(111.6 - A_{\rm{v}}) \cdot 5^3}{3 \cdot 320000} + \cfrac{(446.4 - 4 \cdot A_{\rm{h}}) \cdot 5^2}{2 \cdot 320000} + \cfrac{512 \cdot 5^2}{2 \cdot 320000} \\
w_{\rm{C}} &=-\cfrac{A_{\rm{h}}}{6400} - \cfrac{A_{\rm{v}}}{7680} + \cfrac{1663}{32000}\\
\varphi_{\rm{C}} &= \cfrac{(111.6 - A_{\rm{v}}) \cdot 5^2}{2 \cdot 320000} + \cfrac{(446.4 - 4 \cdot A_{\rm{h}}) \cdot 5}{320000} + \cfrac{512 \cdot 5}{320000} \\
\varphi_{\rm{C}} &= -\cfrac{A_{\rm{h}}}{16000} - \cfrac{A_{\rm{v}}}{25600} + \cfrac{6187}{320000}
\end{align*}
$$

The displacements at $\rm{A}$ can be calculated in the same way as before, but including now the temperature expansion of ${\rm{BC}}$:

$$
\begin{align*}
w_{\rm{A_v}} &= w_{\rm{C}} \\
w_{\rm{A_v}} &=-\cfrac{A_{\rm{h}}}{6400} - \cfrac{A_{\rm{v}}}{7680} + \cfrac{1663}{32000} \\
w_{\rm{A_h}} &= \varphi_{\rm{C}} \cdot 4 - \cfrac{A_{\rm{h}} \cdot 4^3}{3 \cdot 320000} - \cfrac{1}{625} \\
w_{\rm{A_h}} &=-\cfrac{256003 \cdot A_{\rm{h}}}{12000} - \cfrac{A_{\rm{v}}}{6400} + \cfrac{6123}{80000}\\
\end{align*}
$$

Again, solving for the displacement conditions gives:

$$
\left\{
\begin{matrix}
{w_{\rm{A_v}}=0} \\
{w_{\rm{A_h}}=0}
\end{matrix}
\right.
\;\to\;
\begin{matrix}
{A_{\rm{v}} \approx 400 \ \rm{kN}} \\
{A_{\rm{h}} \approx 0 \ \rm{kN}}
\end{matrix}
$$

As before, the force distribution and displacement can be solved for. However, the kinematically equivalent force should not be included in the internal force calculations.

## Displacement method using degrees of freedom

% source files at https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1

Next to the force method, there's also the displacement method using degrees of freedom. This method comes with the benefit that there's no need to create a statically determinate structure first. Instead, the degrees of freedom are defined directly on the statically indeterminate structure. As long as the displacement and forces can be solved for the individual parts of the structure, the method can be applied. For the deformations of the individual parts, a larger set of forget-me-nots can be used, including various statically indeterminate cases.

Given is the following structure:

```{figure} intro_data/constructie2.svg
:align: center
```

The deformations of this structure can be described using the rotation of $\rm{D}$: $\rm{D}$ won't displace horizontally / vertically due to the infinite axial stiffness and all parts of the structure can be described using this forget-me-nots. Due to the rotations, bending moments will arrise in $\rm{D}$, which need to be in equilibrium with the external moment of $29 \ \rm{kNm}$:

```{figure} intro_data/phi_D.svg
:align: center
```

For part $\rm{AB}$, a statically indeterminate forget-me-not can be used to find the rotation of $\rm{D}$ as a function of the moment $M_{\rm{D}}^{\rm{AD}}$:

```{figure} intro_data/AD.svg
:align: center
```

$$
\varphi_{\rm{D}} = \cfrac{M_{\rm{D}}^{\rm{AD}} \cdot 5}{4 \cdot 120000} = \cfrac{M_{\rm{D}}^{\rm{AD}}}{96000}
$$

Inverting this relation gives:

$$
M_{\rm{D}}^{\rm{AD}} = 96000 \cdot \varphi_{\rm{D}}
$$

For part $\rm{CD}$, a statically determinate forget-me-not can be used:

```{figure} intro_data/CD2.svg
:align: center
```

$$
\varphi_{\rm{D}} = -\cfrac{M_{\rm{D}}^{\rm{CD}} \cdot 5}{3 \cdot 120000} = -\cfrac{M_{\rm{D}}^{\rm{CD}}}{72000}
$$

Inverting this relation gives:

$$
M_{\rm{D}}^{\rm{CD}} = -72000 \cdot \varphi_{\rm{D}}
$$

Finally, for the part $\rm{DB}$, the same statically determinate forget-me-not can be used:

```{figure} intro_data/BD2.svg
:align: center
```

$$
\varphi_{\rm{D}} = - \cfrac{M_{\rm{D}}^{\rm{BD}} \cdot 2}{3 \cdot 120000} - \cfrac{29 \cdot 2}{6 \cdot 120000} = -\cfrac{M_{\rm{D}}^{\rm{BD}}}{180000} - \cfrac{29}{360000}
$$

Inverting this relation gives:

$$
M_{\rm{D}}^{\rm{BD}} = -180000 \cdot \varphi_{\rm{D}} - 14.5
$$

Now, the moment equilibrium at $\rm{D}$ can be written:

```{figure} intro_data/D.svg
:align: center
```

$$
\begin{align*}
M_{\rm{D}}^{\rm{AD}} - M_{\rm{D}}^{\rm{CD}} - M_{\rm{D}}^{\rm{BD}} + 29 &= 0 \\
\varphi_{\rm{D}} &= \cfrac{-1}{8000} \approx -1.25 \cdot 10^{-4} \ \rm{rad}
\end{align*}
$$

This solves the statically indeterminate structure. Eventually, the full internal force distribution and displacement can be found. Leading to for example the moment distribution:

```{figure} intro_data/Mline.svg
:align: center
```

## Matrix method

Finally, the last method to discuss is the matrix method. This method is very similar to the displacement method using degrees of freedom, but uses matrices to describe the relations between forces and displacements. All of these equations are handled with a strict procedure, with no need to explicitly evaluate the individual equilibrium relations. We'll apply a limited form of the matrix method, only treating rotational degrees of freedom and forces at the nodes.

We'll apply it to the same structure as used in the displacement method using degrees of freedom:

```{figure} intro_data/constructie2.svg
:align: center
```

The first step is to define the degrees of freedom and setup the relation $\mathbf{K} \mathbf{u} = \mathbf{f}$:

$$
\begin{bmatrix}
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
\end{bmatrix}
\begin{bmatrix}
\varphi_{\rm{A}} \\
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
= 
\begin{bmatrix}
0 \\
0 \\
0 \\
0
\end{bmatrix}
$$

In which all rotations and moments are defined positive in the counter-clockwise direction.

The next step is define the stiffness relations of the individual parts, which are all defined as $\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}$. This gives:

$$
\begin{align*}
\mathbf{K^{\rm{(e)}}_{\rm{AD}}} &= \begin{bmatrix} \cfrac{4 \cdot 120000}{5} & \cfrac{2 \cdot 120000}{5} \\ \cfrac{2 \cdot 120000}{5} & \cfrac{4 \cdot 120000}{5}  \end{bmatrix} = \begin{bmatrix} 96000 & 48000 \\ 48000 & 96000  \end{bmatrix} \\
\mathbf{K^{\rm{(e)}}_{\rm{CD}}} &= \begin{bmatrix} \cfrac{4 \cdot 120000}{5} & \cfrac{2 \cdot 120000}{5} \\ \cfrac{2 \cdot 120000}{5} & \cfrac{4 \cdot 120000}{5}  \end{bmatrix} = \begin{bmatrix} 96000 & 48000 \\ 48000 & 96000  \end{bmatrix} \\
\mathbf{K^{\rm{(e)}}_{\rm{BD}}} &= \begin{bmatrix} \cfrac{4 \cdot 120000}{2} & \cfrac{2 \cdot 120000}{2} \\ \cfrac{2 \cdot 120000}{2} & \cfrac{4 \cdot 120000}{2}  \end{bmatrix} = \begin{bmatrix} 240000 & 120000 \\ 120000 & 240000  \end{bmatrix} \\
\end{align*}
$$

All of these can be included in the global stiffness matrix $\mathbf{K}$, linking the columns and rows to the correct degrees of freedom. Let's start with element $\rm{AD}$, linking nodes $\rm{A}$ and $\rm{D}$ (row and column 1 and 4):

$$
\mathbf{K} = 
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
48000 & 0 & 0 & 96000\\
\end{bmatrix}
$$

Now, let's add the second element $\rm{CD}$, linking nodes $\rm{C}$ and $\rm{D}$ (row and column 3 and 4):

$$
\mathbf{K} =
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 0 & 0 & 0\\
0 & 0 & 96000 & 48000\\
48000 & 0 & 48000 & 192000\\
\end{bmatrix}
$$

Finally, let's add the last element $\rm{BD}$, linking nodes $\rm{B}$ and $\rm{D}$ (row and column 2 and 4):

$$
\mathbf{K} =
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 240000 & 0 & 120000\\
0 & 0 & 96000 & 48000\\
48000 & 120000 & 48000 & 432000\\
\end{bmatrix}
$$

Now, the force vector can be defined. First the external forces are added:

$$
\mathbf{f} =
\begin{bmatrix}
0 \\
29 \\
0 \\
-29
\end{bmatrix}
$$

Next, the boundary conditions are applied. The rotation at $\rm{A}$ is zero, with a support bending moment present. This gives:

$$
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 240000 & 0 & 120000\\
0 & 0 & 96000 & 48000\\
48000 & 120000 & 48000 & 432000\\
\end{bmatrix}
\begin{bmatrix}
0 \\
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
M_{\rm{A}} \\
29 \\
0 \\
-29
\end{bmatrix}
$$

To solve for the unknown rotations and support moment, the first row and column can be removed:

$$
\begin{bmatrix}
240000 & 0 & 120000\\
0 & 96000 & 48000\\
120000 & 48000 & 432000\\
\end{bmatrix}
\begin{bmatrix}
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
29 \\
0 \\
-29
\end{bmatrix}
$$

This gives:

$$
\begin{bmatrix}
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
\cfrac{7}{19200} \\
\cfrac{1}{16000} \\
\cfrac{-1}{8000}
\end{bmatrix}
\approx
\begin{bmatrix}
3.65 \cdot 10^{-4} \\
6.25 \cdot 10^{-5} \\
-1.25 \cdot 10^{-4}
\end{bmatrix}
$$
