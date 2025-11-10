```{index} Static indeterminate structures; Exam assignment
```
```{index} Transformations; Class exercise using Mohr's circle and analytical formulas
```


(lesson11.1)=
# Lesson November 10th

Today we'll discuss the results of the first [exam assignment on Statically indeterminate structures](exam1).

## Results first exam assignment on Statically indeterminate structures

### Question 2

```{figure} student_data/1.png
---
align: center
---
Structure not statically determinate
```

```{figure} student_data/2.png
---
align: center
---
Statically indeterminate force / displacement missing
```

### Question 3

```{figure} student_data/3.png
---
align: center
---
Displacements due to forces in two-force member forgotten
```

```{figure} student_data/4.png
align: center
---
Rotation of two-force member not taken into account (Williot not used)
```

```{figure} student_data/5.png
---
align: center
---
Kinematically equivalent moment doesn't give correct curvature
```

```{figure} student_data/6.png
---
align: center
---
Express forces and displacements in other unknowns than the statically indeterminate ones
```

```{figure} student_data/7.png
---
align: center
---
Solving just one equilibrium or compatibility equation
```

## Demonstration transforming stresses

Given the following structure and cross section.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/transforming_stresses

```{figure} intro_data/structure.svg
:align: center
```

We'll find the maximum stresses in point $\rm{E}$ in cross-section $\rm{A}$ and its direction.

### Internal forces
First, let's find the internal forces:

```{figure} intro_data/Mline.svg
:align: center
```

```{figure} intro_data/Vline.svg
:align: center
```

At cross-section $\rm{A}$ this gives a moment of $-14.6 \rm{ kNm}$ and shear force of $+16 \ \rm{ kN}$.

### Cross-sectional properties

For this thin-walled cross-section, the second moment of area of the cross-section can be calculated with:

$$ I_{\rm{zz}} = 2 \cdot \cfrac{1}{12} \cdot 4 \cdot 300 ^3 + 2 \cdot \left(\cfrac{1}{12} \cdot 100 \cdot 12^3 + 12 \cdot 100 \cdot 150^2 \right) = 72.0288 \cdot 10^6 \ \rm{ mm}^4$$

### Normal and shear stresses

The normal stresses can be calculated as:

$$\sigma_{\rm{E}} = \cfrac{-14600 \cdot -0.075}{72.0288 \cdot 10^{-6}} \approx +15 \cdot 10^6 \ \rm{ Pa}$$

$$\sigma_{\rm{max}} = \cfrac{-14600 \cdot -0.150}{72.0288 \cdot 10^{-6}} \approx +30 \cdot 10^6 \ \rm{ Pa}$$

Leading to the following diagram:

```{figure} intro_data/normall_stress.svg
:align: center
```

The shear forces can be calculated as:

$$\sigma_{\rm{xm,max,flange}} = - \cfrac{16000 \cdot 12 \cdot 100 \cdot 150}{2 \cdot 12 \cdot 72.0288 \cdot 10^{-6}} \approx 1.7 \cdot 10^6 \ \rm{ Pa}$$

$$\sigma_{\rm{xm,min,web}} = - \cfrac{16000 \cdot 12 \cdot 100 \cdot 150}{2 \cdot 4 \cdot 72.0288 \cdot 10^{-6}} \approx 5.0 \cdot 10^6 \ \rm{ Pa}$$

$$\sigma_{\rm{xm,E}} = - \cfrac{16000 \cdot \left(12 \cdot 100 \cdot 150 + 2\cdot 4\cdot 75 \cdot 112.5 \right)}{2 \cdot 4 \cdot 72.0288 \cdot 10^{-6}} \approx 6.9 \cdot 10^6 \ \rm{ Pa}$$

$$\sigma_{\rm{xm,max,web}} = - \cfrac{16000 \cdot \left(12 \cdot 100 \cdot 150 + 2\cdot 4\cdot 150 \cdot 75 \right)}{2 \cdot 4 \cdot 72.0288 \cdot 10^{-6}} \approx 7.5 \cdot 10^6 \ \rm{ Pa}$$

Leading to the following diagram:

```{figure} intro_data/shear_stresses.svg
:align: center
```

The stress state for a rectangular element at point $\rm{E}$ is therefore:

```{figure} intro_data/element.svg
:align: center
```

#### Find maximum stress

As the stress can be represented as a tensor. Therefore, a $x,y$-coordinate system is introduced:

```{figure} intro_data/element2.svg
:align: center
```

Leading to the tensor $\sigma$:

$$\sigma  = \left[ \begin{array}{}
{15}&{-6.9}\\
{-6.9}&{0}
\end{array} \right]{\ \rm{ MPa}}$$

The maximum stress can be found by applying the transformation rules:

$$\sigma_1 = \frac{1}{2} \left(15 + 0\right) + \sqrt{\left(\frac{1}{2}\left(15-0\right)\right)^2 + \left(-6.9\right)^2} \approx 17 \ \rm{ MPa}$$

With a corresponding angle $\alpha$:

$$
\alpha = \frac{1}{2} \arctan\left(\cfrac{-6.9}{\frac{1}{2}\left(15-0\right)}\right) \approx 21^{\rm{o}}
$$
