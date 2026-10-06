# Matrix method

The matrix method can be used to analyse all types of structures and is very similar to the displacement method. One disadvantage of that displacement method is that the structure is split into parts with different deformation behaviours, making the analysis laborious. The matrix method addresses this by standardising the degrees of freedom and the split parts, and consequently the equilibrium equations at every joint. The method also expresses these relationships directly in matrix form. Together, these features make the matrix method convenient for computer calculations.

## Theory

### Restriction to rotations and nodal moments
In this course, we restrict the matrix method to structures in which joint rotation is the only degree of freedom (the joints cannot translate) and no forces act between the joints. We also model only rigid connections. The matrix method can also be applied to structures with multiple degrees of freedom per joint, forces acting between joints, and hinged or spring connections. These more general applications are covered in the Civil Engineering master's programme.

### Number of degrees of freedom

The first difference between the matrix method and the displacement method is the number of degrees of freedom. Whereas the displacement method uses only a few selected degrees of freedom, the matrix method uses the rotations of all joints as degrees of freedom. All rotations and moments are taken positive in the same direction.

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure-start} ./theorie_data/verplaats.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrix
:number:
```

Displacement method

```{figure-end}
```

::::

::::{grid-item}
:columns: auto

```{figure-start} ./theorie_data/matrixmethode.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrix
:number:
```

Matrix method

```{figure-end}
```

::::
:::::

In the structure above, the displacement method uses only one joint rotation as a degree of freedom, whereas the matrix method uses the rotations of all joints.

### Matrix formulation

The second difference is that, in the matrix method, moment equilibrium is written in matrix form. The equilibrium equations are divided into a stiffness matrix $\mathbf{K}$ (the coefficients of the $\varphi$ terms) and a force vector $\mathbf{f}$ (the constant terms).

$$
\begin{array}{cc}
\mbox{Displacement method} & \mbox{Matrix method} \\
\begin{aligned}
\sum M_{\rm{B}} &= 0 \\
\downarrow \\
k \cdot \varphi  &= f
\end{aligned}
&
\begin{aligned}
\sum M_{\rm{A}} &= 0 \\
\sum M_{\rm{B}} &= 0 \\
\sum M_{\rm{C}} &= 0 \\
\downarrow \\
\mathbf{K}
\begin{bmatrix}
\varphi_{\rm{A}} \\
\varphi_{\rm{B}} \\
\varphi_{\rm{C}}
\end{bmatrix}
&= \mathbf{f}
\end{aligned} \\
\end{array}
$$

This gives the matrix equation $\mathbf{K} \mathbf{u} = \mathbf{f}$. The terms in the global stiffness matrix $\mathbf{K}$ can be interpreted as the rotational stiffness each element contributes to its adjacent joints. The terms in the force vector $\mathbf{f}$ represent the external moments acting at the joints. The displacement vector $\mathbf{u}$ contains the unknown joint rotations.

### Direct assembly of the stiffness matrix
Instead of writing out the moment equilibrium step by step for each split part, as in the displacement method, the matrix method lets us assemble $\mathbf{K} \mathbf{u} = \mathbf{f}$ directly. We do this by adding the rotational stiffnesses of the individual elements to the rows and columns associated with their joints. Each member contributes stiffness against joint rotation; once its stiffness is known, its shape is no longer relevant. Under the restrictions used here, all elements have the same form: a bending member of unknown length $L$ and flexural rigidity $EI$, with moments applied at its ends. We can therefore derive one formula for every element, with $EI$ and $L$ as the only variables. All rotations and moments use the same sign convention (counter-clockwise positive).

```{figure-start} ./theorie_data/staaf.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaats2
:number:
```

With variable $EI$ and $L$.

```{figure-end}
```

:::{note}
This standard element applies under our restrictions: rigid connections, no forces acting between joints, and rotations as the only degrees of freedom. The standard element changes for more general applications.
:::

For this standard element, we need to determine the stiffness terms once. As in the displacement method, we can find the relationships between the end moments and rotations of an element by applying each rotation separately. For each element of length $L$ and flexural rigidity $EI$, we can construct the element stiffness matrix. As in the displacement method, we do this for each degree of freedom separately: when one end is rotated, the rotation at the other end is held fixed.

:::::::{grid} 1 2 2 2
:gutter: 1 1 1 2

::::::{grid-item-card} Relationship between the end moments and $\varphi_2$
:columns: 12 12 6 6

With the left end held fixed, the deformation corresponds to forget-me-not (7) in the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`:

```{figure} ./theorie_data/fmn.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaats2
:number:
```

The support moment in the forget-me-not corresponds to the internal moment at the left end:

```{figure} ./theorie_data/rechts.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaats2
:number:
```

The forget-me-not then gives:

- $\varphi_2 = \cfrac{L \cdot T_2}{4 \cdot EI} \to T_2 = \cfrac{4 \cdot EI}{L} \cdot \varphi_2 $
- $ T_1 = \cfrac{1}{2} \cdot T_2 \to T_1 = \cfrac{2 \cdot EI}{L} \cdot \varphi_2 $

::::::

::::::{grid-item-card} Relationship between the end moments and $\varphi_1$
:columns: 12 12 6 6

With the left end held fixed, the deformation corresponds to the mirrored version of forget-me-not (7) in the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`:

```{figure} ./theorie_data/fmn2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaats2
:number:
```

The support moment in the forget-me-not corresponds to the internal moment at the right end:

```{figure} ./theorie_data/links.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaats2
:number:
```

The forget-me-not then gives:

- $ \varphi_1 = \cfrac{L \cdot T_1}{4 \cdot EI} \to T_1 = \cfrac{4 \cdot EI}{L} \cdot \varphi_1 $
- $ T_2 = \cfrac{1}{2} \cdot T_1 \to T_2 = \cfrac{2 \cdot EI}{L} \cdot \varphi_1 $

::::::

:::::::


Together, these give two equations:

$$
\begin{aligned}
T_1 &= \cfrac{4 EI}{L} \cdot \varphi_1 + \cfrac{2 EI}{L} \cdot \varphi_2 \\
T_2 &= \cfrac{2 EI}{L} \cdot \varphi_1 + \cfrac{4 EI}{L} \cdot \varphi_2 \\
\end{aligned}
$$

These can be written together as an element stiffness matrix:

$$
\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}
$$

Multiplying this by the displacement vector $\mathbf{u^{\rm{(e)}}} = \begin{bmatrix} \varphi_1 \\ \varphi_2  \end{bmatrix}$ gives the end moments in the force vector $\mathbf{f^{\rm{(e)}}} = \begin{bmatrix} T_1 \\ T_2  \end{bmatrix}$.

We can use the individual terms of this standard element stiffness matrix directly. Add them to the global stiffness matrix $\mathbf{K}$, matching the row and column indices to the corresponding element ends.

$$
\begin{aligned}
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix} \\
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
\qquad
\rightarrow
\qquad
\begin{bmatrix}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\varphi_1 \\
\varphi_2 \\
\vdots \\
\varphi_n
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0
\end{bmatrix}
\\
&\vdots \\
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
\end{aligned}
$$

### Direct assembly of the force vector
Since the force vector contains all the separate moments, we can assemble the external moments and support moments directly. As with the stiffness terms, this can be done without explicitly writing out the equilibrium equations. We only need to add the external moments and support moments to the appropriate entries in the force vector.

$$
\begin{bmatrix}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\varphi_1 \\
\varphi_2 \\
\vdots \\
\varphi_n
\end{bmatrix}
=
\begin{bmatrix}
0 \\
0 \\
\vdots \\
0
\end{bmatrix}
\leftarrow
\begin{matrix}
\mbox{External moments} \\
\mbox{Support moments}
\end{matrix}
$$

### Procedure

The steps of the matrix method are:

::::::{prf:algorithm} Matrix method
:nonumber: true
:label: matrixmethode_algoritme

1. Determine the degrees of freedom (rotations). These form the unknown displacement vector $ \mathbf{u} =  \begin{bmatrix}  \varphi_1 \\  \varphi_2 \\ \vdots \\ \varphi_n  \end{bmatrix} $
2. Initialize the system of equations $\mathbf{K} \mathbf{u} = \mathbf{f}$ with a zero matrix for $\mathbf{K}$ and a zero vector for $\mathbf{f}$.
3. Determine the element stiffness matrix for each element, $\left(\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}\right)$, and add it to the global stiffness matrix $\mathbf{K}$ at the entries corresponding to its joints.
4. Construct the global force vector $\mathbf{f}$ by adding the external forces (and moments) at the corresponding joints.
5. Add the prescribed degrees of freedom (rotations) and unknown support reactions (support moments) to the system of equations.
6. Solve the system of equations $\mathbf{K} \mathbf{u} = \mathbf{f}$ for the unknown degrees of freedom (rotations) in $\mathbf{u}$.

::::::

## Example

An example demonstrates how to apply the matrix method to a statically indeterminate structure.

::::::{prf:example}
:nonumber: true
:label: matrix_0

```{figure-start} ./theorie_data/voorbeeld.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrix
:number:
:figclass: sticky-margin
```

- $EI = 4290 \ \rm{kNm}^2$
- $EA >> EI$

```{figure-end}
```

::::::

1. Determine the degrees of freedom (rotations). These form the unknown displacement vector $ \mathbf{u} =  \begin{bmatrix}  \varphi_1 \\  \varphi_2 \\ \vdots \\ \varphi_n  \end{bmatrix} $

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_1

    This structure has three joints, so the displacement vector is: $ \mathbf{u} =  \begin{bmatrix}  \varphi_A \\  \varphi_B \\  \varphi_C  \end{bmatrix} $

    Rotations are taken as positive clockwise.

    ::::::

2. Initialize the system of equations $\mathbf{K} \mathbf{u} = \mathbf{f}$ with a zero matrix for $\mathbf{K}$ and a zero vector for $\mathbf{f}$.


    ::::::{prf:example}
    :nonumber: true
    :label: matrix_2

    For this structure, this gives a 3×3 matrix for $\mathbf{K}$ and a 3×1 vector for $\mathbf{f}$:
    
    $$
    \begin{bmatrix}
    0 & 0 & 0 \\
    0 & 0 & 0 \\
    0 & 0 & 0
    \end{bmatrix}
    \begin{bmatrix}
    \varphi_{\rm{A}} \\
    \varphi_{\rm{B}} \\
    \varphi_{\rm{C}}
    \end{bmatrix}
    = 
    \begin{bmatrix}
    0 \\
    0 \\
    0
    \end{bmatrix}
    $$

    ::::::

3. Determine the element stiffness matrix for each element, $\left(\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}\right)$, and add it to the global stiffness matrix $\mathbf{K}$ at the entries corresponding to its joints.

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_3

    For element $\rm{AB}$, with length $5 \ \rm{m}$, the element stiffness matrix is:

    $$
    \mathbf{K^{\rm{(e)}}_{\rm{AB}}} = \begin{bmatrix} \cfrac{4 \cdot 4290}{5} & \cfrac{2 \cdot 4290}{5} \\ \cfrac{2 \cdot 4290}{5} & \cfrac{4 \cdot 4290}{5}  \end{bmatrix} = \begin{bmatrix} 3432 & 1716 \\ 1716 & 3432  \end{bmatrix} 
    $$

    We can add this directly to the global stiffness matrix $\mathbf{K}$. Joints $\rm{A}$ and $\rm{B}$ correspond to the first and second rows and columns of the global stiffness matrix. This gives:

    $$
    \mathbf{K} =
    \begin{bmatrix}
    3432 & 1716 & 0 \\
    1716 & 3432 & 0 \\
    0 & 0 & 0
    \end{bmatrix}
    $$

    For element $\rm{BC}$, with length $6.6 \ \rm{m}$, the element stiffness matrix is:

    $$
    \mathbf{K^{\rm{(e)}}_{\rm{BC}}} = \begin{bmatrix} \cfrac{4 \cdot 4290}{6.6} & \cfrac{2 \cdot 4290}{6.6} \\ \cfrac{2 \cdot 4290}{6.6} & \cfrac{4 \cdot 4290}{6.6}  \end{bmatrix} = \begin{bmatrix} 2600 & 1300 \\ 1300 & 2600  \end{bmatrix}
    $$

    We can also add this directly to the global stiffness matrix $\mathbf{K}$. Joints $\rm{B}$ and $\rm{C}$ correspond to the second and third rows and columns of the global stiffness matrix. This gives:

    $$
    \mathbf{K} =
    \begin{bmatrix}
    3432 & 1716 & 0 \\
    1716 & 6032 & 1300 \\
    0 & 1300 & 2600
    \end{bmatrix}
    $$

    Finally, add element $\rm{AC}$, with length $10.4 \ \rm{m}$. Its element stiffness matrix is:

    $$
    \mathbf{K^{\rm{(e)}}_{\rm{AC}}} = \begin{bmatrix} \cfrac{4 \cdot 4290}{10.4} & \cfrac{2 \cdot 4290}{10.4} \\ \cfrac{2 \cdot 4290}{10.4} & \cfrac{4 \cdot 4290}{10.4}  \end{bmatrix} = \begin{bmatrix} 1650 & 825 \\ 825 & 1650  \end{bmatrix}
    $$

    We can also add this directly to the global stiffness matrix $\mathbf{K}$. Joints $\rm{A}$ and $\rm{C}$ correspond to the first and third rows and columns of the global stiffness matrix. This gives:

    $$
    \mathbf{K} =
    \begin{bmatrix}
    5082 & 1716 & 825 \\
    1716 & 6032 & 1300 \\
    825 & 1300 & 4250
    \end{bmatrix}
    $$

    ::::::

4. Construct the global force vector $\mathbf{f}$ by adding the external forces (and moments) at the corresponding joints.

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_4

    An external moment of $209.924 \ \rm{kNm}$ acts at joint $\rm{B}$. It acts clockwise and is therefore positive in our force vector. This gives:

    $$
    \mathbf{f} =
    \begin{bmatrix}
    0 \\
    209.924 \\
    0
    \end{bmatrix}
    $$
    ::::::

5. Add both the prescribed degrees of freedom (rotations) and the unknown support reactions (support moments) to the system of equations.

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_5

    At joint $\rm{C}$, the rotation is prescribed as $\varphi_{\rm{C}} = 0$. We add this to the system of equations by replacing the second row and including the unknown support moment at $\rm{C}$, which we take as positive:

    $$
    \begin{bmatrix}
    5082 & 1716 & 825 \\
    1716 & 6032 & 1300 \\
    825 & 1300 & 4250
    \end{bmatrix}
    \begin{bmatrix}
    \varphi_{\rm{A}} \\
    \varphi_{\rm{B}} \\
    0
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    209.924 \\
    M_{\rm{C}}
    \end{bmatrix}
    $$

    :::::: 

6. Solve the system of equations $\mathbf{K} \mathbf{u} = \mathbf{f}$ for the unknown degrees of freedom (rotations) in $\mathbf{u}$.

    ::::::{prf:example}
    :nonumber: true
    :label: matrix_6

    Only the first and second rows are relevant for solving for the unknown rotations. We can therefore omit the third row and column and rewrite the equation as:

    $$
    \begin{bmatrix}
    5082 & 1716 \\
    1716 & 6032
    \end{bmatrix}
    \begin{bmatrix}
    \varphi_{\rm{A}} \\
    \varphi_{\rm{B}}
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    209.924
    \end{bmatrix}
    $$

    This gives:
    - $\varphi_{\rm{A}} = -0.0013 \ \rm{rad}$
    - $\varphi_{\rm{B}} = 0.0385 \ \rm{rad}$

## More examples
The matrix method is covered in chapter 5 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. In section 5.5, the material in example 1 after finding the $\varphi$ values is not part of this course. The same applies to example 1 in section 5.6.1 after finding the $\varphi$ values. Sections 5.5.2 and 5.7 are also not covered.

## Lecture recording

This topic was presented in Dutch in [lecture 14 of CTB2210](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/d58276f89e0b48f094298b82bec162841d?sortBy=most-recent), from 0:16:50 to 0:52:40.

## Additional exercises
- The guided exercise on the next pages is a first exercise to check your understanding
- For more practice, you can work on exercises 5.1–5.5 in section 5.8 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Exercises e–i are not part of this course. For exercises 5.2–5.5, replace the cantilever section with a moment and ignore the shear force. Unfortunately, no answers are available. You can analyse the structures using MatrixFrame to check your answers.
