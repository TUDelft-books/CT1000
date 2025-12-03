```{index} Displacement method using statically indeterminate displacement; Demonstration
```
```{index} Displacement method using degrees of freedom; Demonstration
```
```{index} Matrix method; Demonstration
```

(lesson7.1)=
# Lesson October 13th

## Displacement method using statically indeterminate displacements

% source files at https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2

Given is the following structure:

```{figure} intro_data/constructie.svg
:align: center
```

To apply the displacment method using statically indeterminate displacements, we first need to find the degree of statical indeterminacy:

```{figure} intro_data/stat_heid.svg
:align: center
```

This gives 4 support reactions and 1 unknown internal force, while we have 4 equilibrium equations, leading to a degree of statical indeterminacy of 1.

Just as with the force method, we need to add hinges or split two-force members until we've created a statically determinate structure, while making sure it doesn't turn into a mechanism. As opposed to the force method, we define the displacement at this location as a statically determinate displacement, which can be solved for with equilibrium equations.

A possible statically determinate structure is shown below:

```{figure} intro_data/stat_bepaald.svg
:align: center
```

The equilibrium equation for solving this structure is $N_{\rm{C}}^{\rm{BC}} \left( w_{\rm{C}} \right) = N_{\rm{C}}^{\rm{CD}} \left( w_{\rm{C}} \right)$. Normally, we solve for the inverse relations, where the displacements are a function of the internal forces. Most relations are defined in this way, so in general it's useful to first find the relation of $w_{\rm{C}}$ as a function of $N_{\rm{C}}^{\rm{BC}}$ or $N_{\rm{C}}^{\rm{CD}}$, and then invert this relation to find the internal forces as a function of the displacements.

The moment in $\rm{B}$ can be found using equilibrium:

```{figure} intro_data/MB.svg
:align: center
```

$$
\sum \left. T \right|_{\rm{B}}^{\rm{BC}} = 0 \to M_{\rm{B}} = 3 \cdot N_{\rm{C}}^{\rm{BC}}
$$

Using forget-me-nots, the rotation of $\rm{B}$ can be found:

```{figure} intro_data/AB.svg
:align: center
```

$$
\varphi_{\rm{B}} = \cfrac{94.5 \cdot 4^3}{3 \cdot 420000} - \cfrac{N_{\rm{C}}^{\rm{BC}} \cdot 4}{3 \cdot 420000} = \cfrac{3}{500} - \cfrac{N_{\rm{C}}^{\rm{BC}}}{10500} \approx 0.006 - 9.52 \cdot 10^{-5} \cdot N_{\rm{C}}^{\rm{BC}}
$$

The displacement of $\rm{C}$ can be found by extending the rotation of $\rm{B}$ over the length of member $\rm{BC}$ and adding the deflection defined by another forget-me-not:

```{figure} intro_data/BCw.svg
:align: center
```

$$
w_{\rm{C}} = -\varphi_{\rm{B}} \cdot 3 + \cfrac{N_{\rm{C}}^{\rm{BC}} \cdot 3^3}{3 \cdot 420000} = \cfrac{-9}{500} + \cfrac{1}{2000} \cdot N_{\rm{C}}^{\rm{BC}} = -0.018 + 5 \cdot 10^{-4} \cdot N_{\rm{C}}^{\rm{BC}}
$$

Inverting this relation gives:

$$
N_{\rm{C}}^{\rm{BC}} = 2000 \cdot w_{\rm{C}} + 36
$$

For the other part the displacement of $\rm{C}$ can be found using the relations for a bar under tension:

```{figure} intro_data/CD.svg
:align: center
```

$$
w_{\rm{C}} = -\cfrac{N_{\rm{C}}^{\rm{CD}} \cdot 5}{1250} = -{1}{250} \cdot N_{\rm{C}}^{\rm{CD}} = -0.004 \cdot N_{\rm{C}}^{\rm{CD}}
$$

This gives:

$$
N_{\rm{C}}^{\rm{CD}} = -250 \cdot w
$$

Now, the equilibrium equation can be solved:

$$
\begin{align*}
N_{\rm{C}}^{\rm{BC}} \left( w_{\rm{C}} \right) &= N_{\rm{C}}^{\rm{CD}} \left( w_{\rm{C}} \right) \\
2000 \cdot w_{\rm{C}} + 36 &= -250 \cdot w_{\rm{C}} \\
w_{\rm{C}} &= \cfrac{-2}{125} = -0.016 \, \rm{m} 
\end{align*}
$$

Now the statically indeterminate structure is solved. Eventually, the full internal force distribution and displacement can be found.

## Displacement method using degrees of freedom

% source files at https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1

Next to the displacement method using statically indeterminate displacements, there's also the displacement method using degrees of freedom. This method comes with the benefit that there's no need to create a statically determinate structure first. Instead, the degrees of freedom are defined directly on the statically indeterminate structure. As long as the displacement and forces can be solved for the individual parts of the structure, the method can be applied. For the deformations of the individual parts, a larger set of forget-me-nots can be used, including various statically indeterminate cases.

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
