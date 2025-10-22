```{index} Force method; demonstration bending
```

(lesson5.2)=
# Lesson Wednesday Oktober 1st

During today's lesson it's demonstrated how you to use the force method for statically indeterminate problems which involve bending.

````{margin}
```{attributiongrey} Attribution
:class: attribution

This demonstration is adapted from https://oit.tudelft.nl/CTB2210/toz/TOZ/opgave.html

```
```` 

## Demonstration
Given a structure as shown below:

% Source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/matrix

```{figure} ./intro_data/structure.svg
:align: center

Structure
```

First, the degree of statically indeterminacy must be determined.

```{figure} ./intro_data/SB2.svg
:align: center

Free body diagrams of hinged parts
```
There are 7 unknown support reactions and 6 unknown internal forces. This gives an external degree of statical indeterminacy of 1. Since this structure is not a closed structure, the internal degree of statical indeterminacy is also equal to 1.

Now we can apply the force method. For this we need to transform the structure into a statically determinate structure. There are several ways to do this, of which some are incorrect when the transformed structure becomes a (partial) mechanism.

Some correct ways to transform the structure are:

`````{tab-set}
````{tab-item} Replace the fixed support at $\rm{A}$ with a hinged support
```{figure} intro_data/optie1.svg
:align: center
```
````
````{tab-item} Split the two-force member $\rm{BD}$
```{figure} intro_data/optie2.svg
:align: center
```
````
````{tab-item} Add hinge between $\rm{A}$ and $\rm{D}$
```{figure} intro_data/optie4.svg
:align: center
```
````
`````

Some incorrect ways to transform the structure are:

`````{tab-set}
````{tab-item} Split two two-force member $\rm{CD}$
```{figure} intro_data/optie3.svg
:align: center
```
This creates a partial mechanism!
````
````{tab-item} Add hinge between $\rm{D}$ and $\rm{E}$
```{figure} intro_data/optie5.svg
:align: center
```
This creates a partial mechanism!
````
````{tab-item} Add hinge between $\rm{E}$ and $\rm{G}$
```{figure} intro_data/optie6.svg
:align: center
```
This creates a partial mechanism!
````
````{tab-item} Replaced hinged support at $\rm{C}$ with a vertical roller support
```{figure} intro_data/optie7.svg
:align: center
```
This creates a partial mechanism!
````
`````

The following statically determinate structure is chosen, including a statically indeterminate force $B_{\rm{v}}$ and a displacement constraint at point $\rm{B}$, $w_{\rm{B}} = 0$:

```{figure} ./intro_data/transformed_structure.svg
:align: center
```

Now, the force distribution and displacement can be solved for.

The normal force in member $\rm{BD}$ is found with:

```{figure} ./intro_data/BD.svg
:align: center
```

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{BD}} &= 0 \\
B_{\rm{v}} + N_{\rm{BD}}&= 0 \\
N_{\rm{BD}} &= -B_{\rm{v}}
\end{align}
$$

The normal force in member $\rm{CG}$ is found with:

```{figure} ./intro_data/CG.svg
:align: center
```

$$
\begin{align}
\sum \left. T \right|_{\rm{E}}^{\rm{EG}} &= 0 \\
10.5 \cdot 8 \cdot 4 - N_{\rm{CG}} \cdot 8 &= 0 \\
N_{\rm{CG}} &= 42 \ \rm{kN}
\end{align}
$$

The shear force and bending moment just left of point $\rm{D}$ is found with:

```{figure} ./intro_data/DG.svg
:align: center
```

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{DG}} &= 0 \\
V_{\rm{D}}^{\rm{AD}}-B_{\rm{v}} - 84 + 42 &= 0 \\
V_{\rm{D}}^{\rm{AD}} &= B_{\rm{v}} + 42
\end{align}
$$

$$
\begin{align}
\sum \left. T \right|_{\rm{D}}^{\rm{DG}} &= 0 \\
M_{\rm{D}} + 84 \cdot 8 - 42 \cdot 12 &= 0 \\
M_{\rm{D}} &= -168 \ \rm{kNm}
\end{align}
$$

The displacement at point $\rm{D}$ is found with a forget-me-not:

```{figure} ./intro_data/AD.svg
:align: center
```

$$
\begin{align}
w_{\rm{D}} &= \cfrac{168 \cdot 4^2}{2 \cdot 64000} + \cfrac{\left( B_{\rm{v}} + 42 \right) \cdot 4^3}{3 \cdot 64000} \\
w_{\rm{D}} &= \cfrac{1}{3000} \cdot B_{\rm{v}} + 0.035 \\
w_{\rm{D}} & \approx 0.000333 \cdot B_{\rm{v}} + 0.035
\end{align}
$$

The displacement of $\rm{B}$ can be found with the extension of a member due to axial forces:

```{figure} ./intro_data/wB.svg
:align: center
```

$$
\begin{align}
w_{\rm{B}} &= - w_{\rm{D}} - \Delta L_{\rm{BD}} \\
w_{\rm{B}} &= - w_{\rm{D}} -  \cfrac{-B_{\rm{v}} \cdot 8}{4000} \\
w_{\rm{B}} &= \cfrac{7}{3000} \cdot B_{\rm{v}} + 0.035 \\
w_{\rm{B}} & \approx 0.00233\cdot B_{\rm{v}} + 0.035 \\
\end{align}
$$

Now, the displacement constraint at point $\rm{B}$ can be used to solve for the statically indeterminate force $B_{\rm{v}}$:

$$
\begin{align}
w_{\rm{B}} &= 0 \\
\cfrac{7}{3000} \cdot B_{\rm{v}} + 0.035 &= 0 \\
B_{\rm{v}} &= -15 \ \rm{kN}
\end{align}
$$

Finally, with the found value for $B_{\rm{v}}$, the internal forces and displacements can be calculated. For example, the displacement at $\rm{E}$. The rotation at $\rm{D}$ is found with a forget-me-not:

```{figure} ./intro_data/phi_D.svg
:align: center
```

$$
\begin{align}
\varphi_{\rm{D}} &= \cfrac{168 \cdot 4}{64000} + \cfrac{\left( -15 + 42 \right) \cdot 4^2}{2 \cdot 64000} \\
\varphi_{\rm{D}} &= 0.03 \ \rm{rad}
\end{align}
$$

The shear force at $\rm{E}$ is found with:

```{figure} ./intro_data/EG_2.svg
:align: center
```

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{EG}} &= 0 \\
V_{\rm{E}}- 84 + 42 &= 0 \\
V_{\rm{E}} &= 42 \ \rm{kN}
\end{align}
$$

The displacement at $\rm{E}$ is found with a forget-me-not:

```{figure} ./intro_data/we.svg
:align: center
```

$$
\begin{align}
w_{\rm{E}} &= w_{\rm{D}} + \varphi_{\rm{D}} \cdot 4 + \cfrac{ 42 \cdot 4^3}{3 \cdot 64000} \\
w_{\rm{E}} &= 0.0995 \ \rm{m} \\
\end{align}
$$