```{index} Transformations; Class exercise using analytical formulas
```

(lesson12.3)=
# Lesson November 21th

During today's lesson you'll work on a complex exercise on the topic of the Transforming tensors. Please ask your questions regarding the [homework](homework12.3) as well!

## Exercise Transforming tensors

Given is the following structure and cross-section:

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/shear_stresses/transform_stress

```{figure} intro_data/structure.svg
:align: center
```

1. Find the relevant cross-sectional properties.
2. Find the normal and shear stresses just below $\rm{G}$, in $\rm{H}$, in $\rm{I}$ and just right of $\rm{C}$ in cross-section $\rm{A}$.
3. Find the principal values of the stresses in the points just below $\rm{G}$, in $\rm{H}$, in $\rm{I}$ and just right of $\rm{C}$ in cross-section $\rm{A}$.

````{admonition} Solution assignment 1
:class: solution, dropdown

Normal force centre is given by:
```{figure} intro_data/NC.svg
:align: center
```

- $A \approx  17500 \ \rm{ mm}^2$
- $I_{zz} \approx 655 \cdot 10^6 \ \rm{ mm}^4$

````

````{admonition} Solution assignment 2
:class: solution, dropdown

- $\sigma_{\rm{just} \ \rm{below} \ \rm{G}} = +6.73 \ \rm{ MPa}$
- $\tau_{\rm{just} \ \rm{below} \ \rm{G}} = +0.164 \ \rm{ MPa}$
- $\sigma_{\rm{H}} = +6.73 \ \rm{ MPa}$
- $\tau_{\rm{H}} = 0 \ \rm{ MPa}$
- $\sigma_{\rm{I}} = -2 \ \rm{ MPa}$
- $\tau_{\rm{I}} = +0.35 \ \rm{ MPa}$
- $\sigma_{\rm{just} \ \rm{right} \ \rm{of} \ \rm{C}} = -8.53 \ \rm{ MPa}$
- $\tau_{\rm{just} \ \rm{right} \ \rm{of} \ \rm{C}} = -0.12 \ \rm{ MPa}$

````

````{admonition} Solution assignment 3
:class: solution, dropdown

- $\sigma_{\rm{1,} \ \rm{just} \ \rm{below} \ \rm{G}} = +6.73 \ \rm{ MPa}$
- $\sigma_{\rm{2,} \ \rm{just} \ \rm{below} \ \rm{G}} = -0.0040 \ \rm{ MPa}$
- $\sigma_{\rm{1,} \ \rm{H}} = +6.73 \ \rm{ MPa}$
- $\sigma_{\rm{2,} \ \rm{H}} = 0 \ \rm{ MPa}$
- $\sigma_{\rm{1,} \ \rm{I}} = 0.59 \ \rm{ MPa}$
- $\sigma_{\rm{2,} \ \rm{I}} = -2.06 \ \rm{ MPa}$
- $\sigma_{\rm{1,} \ \rm{just} \ \rm{right} \ \rm{of} \ \rm{C}} = 0.0018 \ \rm{ MPa}$
- $\sigma_{\rm{2,} \ \rm{just} \ \rm{right} \ \rm{of} \ \rm{C}} = -8.5 \ \rm{ MPa}$

````

## Exercise stress tensor

Given is the following structure and cross-section:

% source files on https://brightspace.tudelft.nl/d2l/le/content/774702/viewContent/4617411/View

```{figure} intro_data/constructie.png
---
align: center
width: 400px
---
Structure, with properties:

- $L = 4 \ \rm{ }$
- $F = 200 \ \rm{ kN}$
- $q = 20 \ \rm{ kN/m}$

```

````{figure} intro_data/doorsnede.png
---
align: center
width: 200px
---
Cross-section, with properties:

- $E = 30 \ \rm{ GPa}$
- $\nu = 0.2 \ \rm{(-)}$
- $b = 200 \ \rm{ mm}$
- $h = 600 \ \rm{ mm}$

````

1. Find the internal forces in cross-section $\rm{A}$.
2. Find the stresses in point $\rm{P}$ in cross-section $\rm{A}$.
3. Find the stress tensor in the $xyz$-coordinates in point $\rm{P}$ in cross-section $\rm{A}$.
4. Find the isotropic and deviatoric components.

````{admonition} Solution assignment 1
:class: solution, dropdown

- $N_{\rm{A}} = 200 \ \rm{ kN}$
- $V_{\rm{A}} = 80 \ \rm{ kN}$
- $M_{\rm{A}} = -160 \ \rm{ kNm}$

```` 

````{admonition} Solution assignment 2
:class: solution, dropdown

- $\sigma_{yy} = \sigma_{xy} = \sigma_{yz} = \sigma_{zz} = 0 \ \rm{ MPa}$
- $\sigma_{xx} = -5 \ \rm{ MPa}$
- $\sigma_{xz} = 0.75 \ \rm{ MPa}$

```` 

````{admonition} Solution assignment 3
:class: solution, dropdown

$$
\boldsymbol{\sigma} = \begin{bmatrix}
    -5 & 0 & 0.75 \\
    0 & 0 & 0 \\
    0.75 & 0 & 0
\end{bmatrix} \ \rm{ MPa}
$$

```` 

````{admonition} Solution assignment 4
:class: solution, dropdown

$$
\boldsymbol{\sigma} = \begin{bmatrix}
    -1.67 & 0 & 0 \\
    0 & -1.67 & 0 \\
    0 & 0 & -1.67
\end{bmatrix} + \begin{bmatrix}
    -3.33 & 0 & 0.45 \\
    0 & 1.67 & 0 \\
    024 & 0 & 1.67
\end{bmatrix}\ \rm{ MPa}
$$

````
