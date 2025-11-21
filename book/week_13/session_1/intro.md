```{index} Poisson's ratio; Class exercise
```
```{index} Stress-Strain relations; Class exercise
```


(lesson13.1)=
# Lesson November 24th

During today's lesson you'll work on a complex exercise on the topic of the stress-strain relations. Please ask your questions regarding the [homework](homework13.1) as well!

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

This exercise is from the course CTB2210 2025-2026 {cite:p}`Francesco_stress_strain`.

```
````

## Exercise stress-strain relations

Given is the following stress element:

% source files on https://brightspace.tudelft.nl/d2l/le/content/774702/viewContent/4617411/View

```{figure} intro_data/image.png
---
align: center
width: 400px
---
Aluminium plate with strain gauges: $E = 70 \ \rm{ GPa}$,  $\nu = 0.33 \ \rm{(-)}$, $\varepsilon_{\rm{G1}} = -1.0 \cdot 10^{-3}$, $\varepsilon_{\rm{G2}} = 2 \cdot 10^{-3}$, $\varepsilon_{\rm{G3}} = +2 \cdot 10^{-3}$.
```


1. Find the strain tensor
2. Find the principal strains
3. Find the stress tensor
4. Find the principal stresses

````{admonition} Solution assignment 1
:class: solution, dropdown

$$
\boldsymbol{\varepsilon} = \begin{bmatrix}
    2 & 1.5 \\
    1.5 & -1
\end{bmatrix} \cdot 10^{-3}
$$

```` 

````{admonition} Solution assignment 2
:class: solution, dropdown

- $\varepsilon_{1} = 2.62 \cdot 10^{-3}$
- $\varepsilon_{2} = -1.62 \cdot 10^{-3}$

```` 

````{admonition} Solution assignment 3
:class: solution, dropdown

$$
\begin{bmatrix}
    \sigma_{xx} \\
    \sigma_{yy} \\
    \sigma_{xy}
\end{bmatrix} =  \begin{bmatrix}
    131.2 \\
    -26.7 \\
    79.0
\end{bmatrix} \, \rm{ MPa}
$$

```` 

````{admonition} Solution assignment 4
:class: solution, dropdown

- $\varepsilon_{1} = 163.9 \, \rm{MPa}$
- $\varepsilon_{2} = -59.4 \, \rm{MPa}$

````

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

This exercise is from the [exam Q1 of CTB2210 2025-2026](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/blob/main/old_exams_CM3/2025-2026_Q1_Tentamenvraag_BS.pdf) {cite:p}`Francesco_exam_Q1_2025`.

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
