```{index} Poisson's ratio; Class exercise
```
```{index} Stress-Strain relations; Class exercise
```

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

This exercise is from the course CTB2210 2025-2026 {cite:p}`Francesco_stress_strain`.

```
````

(lesson13.1)=
# Lesson November 24th

During today's lesson you'll work on a complex exercise on the topic of the stress-strain relations. Please ask your questions regarding the [homework](homework13.1) as well!

## Exercise tensor

Given is the following structure and cross-section:

% source files on https://brightspace.tudelft.nl/d2l/le/content/774702/viewContent/4617411/View

```{figure} intro_data/constructie.png
---
align: center
width: 400px
---
- $L = 4 \ \rm{ }$
- $F = 200 \ \rm{ kN}$
- $q = 20 \ \rm{ kN/m}$
```

````{figure} intro_data/doorsnede.png
---
align: center
width: 200px
---
- $E = 30 \ \rm{ GPa}$
- $\nu = 0.2 \ \rm{(-)}$
- $b = 200 \ \rm{ mm}$
- $h = 600 \ \rm{ mm}$
````

1. Find the internal forces in cross-section $\rm{A}$.
2. Find the stresses in point $\rm{P}$ in cross-section $\rm{A}$.
3. Find the stress matrix in point $\rm{P}$ in cross-section $\rm{A}$.

````{admonition} Solution assignment 1
:class: tip, dropdown

Normal force centre is given by:
```{figure} intro_data/NC.svg
:align: center
```

- $A \approx  17500 \ \rm{ mm}^2$
- $I_{zz} \approx 655 \cdot 10^6 \ \rm{ mm}^4$

````

````{admonition} Solution assignment 2
:class: tip, dropdown

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
:class: tip, dropdown

- $\sigma_{\rm{1,} \ \rm{just} \ \rm{below} \ \rm{G}} = +6.73 \ \rm{ MPa}$
- $\sigma_{\rm{2,} \ \rm{just} \ \rm{below} \ \rm{G}} = -0.0040 \ \rm{ MPa}$
- $\sigma_{\rm{1,} \ \rm{H}} = +6.73 \ \rm{ MPa}$
- $\sigma_{\rm{2,} \ \rm{H}} = 0 \ \rm{ MPa}$
- $\sigma_{\rm{1,} \ \rm{I}} = 0.59 \ \rm{ MPa}$
- $\sigma_{\rm{2,} \ \rm{I}} = -2.06 \ \rm{ MPa}$
- $\sigma_{\rm{1,} \ \rm{just} \ \rm{right} \ \rm{of} \ \rm{C}} = 0.0018 \ \rm{ MPa}$
- $\sigma_{\rm{2,} \ \rm{just} \ \rm{right} \ \rm{of} \ \rm{C}} = -8.5 \ \rm{ MPa}$

````