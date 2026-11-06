<!-- Start of inserted Teachbooks header -->

````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://github.com/TUDelft-books/CEG-mechanics-BSc, version: EN
```
````


<!-- End of inserted Teachbooks header -->

```{index} Transformations
```
```{index} Tensors
```

# Analytical Transformations
The rotation matrix R is defined as:

$$\mathrm{R}=\begin{bmatrix}
\cos(\alpha) & \sin(\alpha) \\
-\sin(\alpha) & \cos(\alpha)
\end{bmatrix}$$

Rotating a first-order tensor (for example force $F$) by an angle $\alpha$ is defined as:

$$\bar{F} = \mathrm{R} \cdot F $$

The transformation rule for a second order tensor (for example stiffness matrix $K$) is defined in matrix notation as:

$$\bar{\mathrm{K}} = \mathrm{R} \cdot \mathrm{K} \cdot \mathrm{R}^T$$

This is treated in chapter 2.1 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.

The individual terms of $\bar{\mathrm{K}}$ can be written out as:

- $k_{\bar x \bar x} = \cfrac{1}{2}\left(k_{xx} + k_{yy}\right) + \cfrac{1}{2}\left(k_{xx} - k_{yy}\right) \cos \left(2\alpha\right) + k_{xy} \sin \left(2 \alpha\right)$
- $k_{\bar y \bar y} = \cfrac{1}{2}\left(k_{xx} + k_{yy}\right) - \cfrac{1}{2}\left(k_{xx} - k_{yy}\right) \cos \left(2\alpha\right) - k_{xy} \sin \left(2 \alpha\right)$
- $k_{\bar x \bar y} = -\cfrac{1}{2}\left(k_{xx} - k_{yy}\right) \sin \left(2 \alpha \right) + k_{xy} \cos \left(2 \alpha\right)$

The principal values of the second order tensor $\bar{\mathrm{K}}$ are defined by:

$$k_{1,2} = \frac{1}{2}\left(k_{xx} + k_{yy}\right) \pm \sqrt{\left(\frac{1}{2}\left(k_{xx} - k_{yy}\right)\right)^2 + k_{xy}^2}$$

The principal directions of the second order tensor $\bar{\mathrm{K}}$ are defined by:

$$\tan{2\alpha_0} = \frac{k_{xy}}{\frac{1}{2}\left(k_{xx} - k_{yy}\right)}$$

This is treated in chapter 2.3 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.

## Instructions from lecture

This topic is presented from 0:39:00 to 1:14:45 in [Constructiemechanica 3 2026/2027, lesson 2 September](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/15ec6b80f1f0485cbaa59f369a2abc561d?academicYear=2026-2027-ctb2210):
  - Slides are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/CM3_Francesco/Theory_elasticity_2.pdf).
  - Worked out resolutions for the guided exercises are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/CM3_Francesco/Theory_elasticity_exercise_L2.pdf).
