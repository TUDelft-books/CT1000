<!-- Start of inserted Teachbooks header -->

````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://github.com/TUDelft-books/CEG-mechanics-BSc, version: EN
```
````


<!-- End of inserted Teachbooks header -->

```{index} Poisson's ratio
```
```{index} Stress-Strain relations
```

# Stress-Strain relations
Poisson's ratio $\nu$ relates strains with stresses in perpendicular directions.

The complete stress strain relation in 3D is defined as:

$$\begin{bmatrix}
\epsilon_{xx} \\
\epsilon_{yy} \\
\epsilon_{zz} \\
2\epsilon_{xy} \\
2\epsilon_{yz} \\
2\epsilon_{zx}
\end{bmatrix} = 
\frac{1}{E}
\begin{bmatrix}
1 & -\nu & -\nu & 0 & 0 & 0 \\
-\nu & 1 & -\nu & 0 & 0 & 0 \\
-\nu & -\nu & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 2(1+\nu) & 0 & 0 \\
0 & 0 & 0 & 0 & 2(1+\nu) & 0 \\
0 & 0 & 0 & 0 & 0 & 2(1+\nu) \\
\end{bmatrix}
\begin{bmatrix}
\sigma_{xx} \\
\sigma_{yy} \\
\sigma_{zz} \\
\sigma_{xy} \\
\sigma_{yz} \\
\sigma_{zx}
\end{bmatrix}$$

This is discussed in chapter 4 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.

## Instructions from lecture
This topic is presented in Dutch in a lecture available from 0:39:05 to 1:14:45 [here](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/afa01c66a9434fae8e4a95c0b0a3348b1d?academicYear=2025-2026-ctb2210).
 - Slides are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/CM3_Francesco/Theory_elasticity_2.pdf).
 - Worked out resolutions for the guided exercises are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/CM3_Francesco/Theory_elasticity_exercise_L2.pdf).
 - Additionally, problems 1-3 in Chapter 5 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con` can be solved by applying the transformation formulas instead of the circle of Mohr (not covered by this course). Answers are available in Chapter 5 of the lecture notes.
