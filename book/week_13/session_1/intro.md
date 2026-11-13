```{index} Poisson's ratio; Class exercise
```
```{index} Stress-Strain relations; Class exercise
```


(lesson13.1)=
# Lesson Monday

During today's lesson you'll work on a complex exercise on the topic of the stress-strain relations. Please ask your questions regarding the [homework](homework13.1) as well!

````{margin}
```{attributiongrey} Attribution
:class: attribution

This exercise is from the course CTB2210 2025-2026 {cite:p}`Francesco_stress_strain`.

```
````

## Exercise stress-strain relations

Given is the following stress element:

% source files on https://brightspace.tudelft.nl/d2l/le/content/774702/viewContent/4617411/View

```{figure} https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/CM3_Francesco/COZ1_1_Figure.jpg
---
align: center
width: 400px
---
Steel plate with strain gauges: $E = 210 \ \rm{ GPa}$,  $\nu = 0.3 \ \rm{(-)}$, $\varepsilon_{\rm{G1}} = 3.0 \cdot 10^{-4}$, $\varepsilon_{\rm{G2}} = -2.0 \cdot 10^{-4}$, $\varepsilon_{\rm{G3}} = -3.0 \cdot 10^{-4}$.
```


1. Find the strain tensor
2. Find the principal strains
3. Find the stress tensor
4. Find the principal stresses

````{admonition} Solution assignment 1
:class: solution, dropdown

$$
\boldsymbol{\varepsilon} = \begin{bmatrix}
    3.0 & -2.6 \\
    -2.6 & -8.0
\end{bmatrix} \cdot 10^{-4}
$$

```` 

````{admonition} Solution assignment 2
:class: solution, dropdown

- $\varepsilon_{1} = 3.58 \cdot 10^{-4}$
- $\varepsilon_{2} = -8.6 \cdot 10^{-4}$

```` 

````{admonition} Solution assignment 3
:class: solution, dropdown

$$
\begin{bmatrix}
    \sigma_{xx} \\
    \sigma_{yy} \\
    \sigma_{xy}
\end{bmatrix} =  \begin{bmatrix}
    13.8 \\
    -42.0 \\
    -163.8
\end{bmatrix} \, \rm{ MPa}
$$

```` 

````{admonition} Solution assignment 4
:class: solution, dropdown

- $\sigma_{1} = 23.3 \, \rm{MPa}$
- $\sigma_{2} = -173.3 \, \rm{MPa}$

````

````{margin}
```{attributiongrey} Attribution
:class: attribution

```
````

## Exercise stress-strain relations 2

Given is the following stress element:

% source files on https://ans.app/repo_questions/52579671/generator

```{figure} intro_data/Figure_exam_general.jpg
---
align: center
width: 500px
---
This plate of steel ($ E =210000 \, \rm{MPa}, \nu = 0.3, f_y =275 \, \rm{MPa}$) is tested in homogeneous plane stress conditions. It is measured that $ \sigma_{xx} = 60 \, \rm{MPa}$ and $\sigma_{yy} = -20 \, \rm{ MPa}$. (Note: in the drawing, the normal stress in y-direction is already represented in compression) We also know that the value of the minimum principal stress is $\sigma_2=−70 \, \rm{ MPa}$
```


1. Compute the value of the shear stress $\sigma_{xy}$ (assume a positive value for $\sigma_{xy}$).
2. Compute $\varepsilon_{xx}$, $\varepsilon_{yy}$, $\varepsilon_{xy}$ and $\varepsilon_{zz}$.


````{admonition} Solution assignment 1
:class: solution, dropdown

$$ \sigma_{xy} \approx 80.62 \, \rm{MPa}$$

```` 

````{admonition} Solution assignment 2
:class: solution, dropdown

- $\varepsilon_{xx} = 0.000314$
- $\varepsilon_{yy} = -0.000181$
- $\varepsilon_{xy} = 0.000499$
- $\varepsilon_{zz} = -0.000057$

```` 
