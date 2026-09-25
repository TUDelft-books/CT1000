````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_vakwerk/lesoefeningen.html.

```
```` 

# Guided exercise

The following structure is given:

```{figure-start} lesoefeningen_data/structure.svg
---
align: center
figclass: sticky-margin
number:
name: rekoefening
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

```{figure-end}
```

Determine the support reactions and internal force diagrams. You will do this for three different statically indeterminate forces.

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[1]
^^^
?
The structure is statically indeterminate to the {gap} degree internally
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_data/graad.svg
---
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

There are 10 unknown forces and 9 equilibrium equations. The structure is therefore first-order statically indeterminate.

::::

We consider the following alternatives for transforming the structure into a statically determinate system:

- Remove the vertical support at $\rm{A}$
- Remove the support at $\rm{B}$
- Remove the vertical support at $\rm{C}$
- Add a hinge at $\rm{B}$ (in the continuous beam $\rm{DBEG}$)
- Add a hinge at $\rm{E}$ (in the continuous beam $\rm{DBEG}$)
- Split the structure at the two-force member $\rm{AD}$
- Split the structure at the two-force member $\rm{CE}$

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option of removing the vertical support at $\rm{A}$.
---
=

```{figure} ./lesoefeningen_data/optie_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option of removing the support at $\rm{B}$.
---
=

```{figure} ./lesoefeningen_data/optie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option of removing the vertical support at $\rm{C}$.
---
=

```{figure} ./lesoefeningen_data/optie_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option of adding a hinge at $\rm{B}$ (in the continuous beam $\rm{DBEG}$).
---
=

```{figure} ./lesoefeningen_data/optie_4.svg
:align: center
:name: optie_4
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option of adding a hinge at $\rm{E}$ (in the continuous beam $\rm{DBEG}$).
---
=

```{figure} ./lesoefeningen_data/optie_5.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option of splitting the structure at the two-force member $\rm{AD}$.
---
=

```{figure} ./lesoefeningen_data/optie_6.svg
:align: center
:name: optie_6
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the possible deformations for the option of splitting the structure at the two-force member $\rm{CE}$.
---
=

```{figure} ./lesoefeningen_data/optie_7.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

::::{question} Exercise
:variant: multiple-select
:columns: 1
:admonition:
:class: exercise
:nocaption:
:showanswer:

Which of the following is not an option for making the structure statically determinate?
---
[ ] Remove the vertical support at $\rm{A}$
[x] Remove the support at $\rm{B}$
> Correct! Removing the entire support creates a mechanism that can move to the left and right.
[ ] Remove the vertical support at $\rm{C}$
[ ] Add a hinge at $\rm{B}$ (in the continuous beam $\rm{DBEG}$)
[x] Add a hinge at $\rm{E}$ (in the continuous beam $\rm{DBEG}$)
> Correct! Adding a hinge here creates a mechanism in which $\rm{EG}$ can rotate about $\rm{E}$.
[ ] Split the structure at the two-force member $\rm{AD}$
[ ] Split the structure at the two-force member $\rm{CE}$
---

::::

## Statically indeterminate force $B_{\rm{v}}$

The following statically determinate system is chosen:

```{figure-start} lesoefeningen_data/stat_bepaald_Bv.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

```{figure-end}
```

::::{question} Exercise
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the deformation condition? Use the variable $w_{\rm{...}}$ for a vertical displacement.
---
M[w_B = 0]
---

::::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the deformed statically determinate structure under the $26 \, \rm{kN}$ load and, separately, under the statically indeterminate force.
---
=

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./lesoefeningen_data/optie_8.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

:::
:::{grid-item}

```{figure} ./lesoefeningen_data/optie_8_26.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

:::
::::

---

:::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[0.4]
M[15.6]
M[-0.6]
M[41.6]
M[0.0006]
M[-0.0416]
M[0.0004]
M[0.0156]
M[0.00052]
M[-0.01872]
^^^
? Determine the normal forces and displacements as functions of $B_{\rm{v}}$.

- $ N_{\rm{AD}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ N_{\rm{CE}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ w_{\rm{E}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positive upwards)
- $ w_{\rm{D}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positive upwards)
- $ w_{\rm{B}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positive upwards)
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema1.svg
---
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

$$
\begin{align}
\sum  \left. T \right|  _ {\rm{E}} &= 0 \\
5 \cdot N_{\rm{AD}} - 2 \cdot B_{\rm{v}} - 3 \cdot26& =0 \\
N_{\rm{AD}} &= 0.4 \cdot B_{\rm{v}} + 15.6
\end{align}
$$ 

$$
\begin{align}
\sum F_ {\rm{v}} &=0 \\
- N_{\rm{AD}} + B_{\rm{v}} + N_{\rm{CE}} -26&= 0 \\
N_{\rm{CE}} &= - 0.6 \cdot B_{\rm{v}} + 41.6
\end{align}
$$


$$ w_{\rm{E}} = - \Delta L_{\rm{CE}} = \cfrac{-N_{\rm{CE}} \cdot L_{\rm{CE}}}{EA} = 0.0006 \cdot B_{\rm{v}} - 0.0416  $$

$$ w_{\rm{D}} = \Delta L_{\rm{AD}} = \cfrac{N_{\rm{AD}} \cdot L_{\rm{AD}}}{EA} = 0.0004 \cdot B_{\rm{v}} + 0.0156 $$ 

$$ w_{\rm{B}} = w_{\rm{D}} + \cfrac{3}{5} \cdot \left( w_{\rm{E}} - w_{\rm{D}} \right) = \cfrac{3}{5} \cdot w_{\rm{E}} + \cfrac{2}{5} \cdot w_{\rm{D}} = 0.00052 \cdot B_{\rm{v}} - 0.01872 $$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[36]
^^^
? Use the deformation condition to solve for the statically indeterminate force.

$ B_{v} = $ {gap} $\rm{kN}$ (positive upwards)
---

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[30]
M[20]
M[-2]
M[3]
M[0]
^^^
? Now also solve for the normal forces and displacements.

- $ N_{\rm{AD}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{CE}}  = $ {gap} $ \rm{kN}$
- $ w_{\rm{E}} = $ {gap} $ \rm{cm}$ (positive upwards)
- $ w_{\rm{D}} = $ {gap} $ \rm{cm}$ (positive upwards)
- $ w_{\rm{B}} = $ {gap} $ \rm{cm}$ (positive upwards)
---

::::

## Statically indeterminate moment $M_{\rm{B}}$

The following statically determinate system is chosen:

```{hide-sticky-margin}
```
```{figure-start} lesoefeningen_data/stat_bepaald_Mb.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

```{figure-end}
```

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
DS[{φ};w]
DS[{B on the BD side};D]
DS[{φ};w]
DS[G;E on the EG side;E on the BE side;{B on the BE side}]
^^^
? What is the deformation condition?

{gap}$(${gap}$) = ${gap}$(${gap}$)$
---

::::

You have already drawn the deformed structure under the statically indeterminate force $M_{\rm{B}}$ in one of the first exercises:

:::{fetch} {numref}`optie_4`
:::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the deformed statically determinate structure under the $26 \, \rm{kN}$ load.
---
=

```{figure} ./lesoefeningen_data/optie4_26.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAPE[-1/3;0.01;2]
M[0]
M[0.5]
M[65]
MAPE[1/9000;0.00001;2]
M[0]
M[-0.00025]
M[-0.0325]
^^^
? Determine the normal forces and rotations as functions of $M_{\rm{B}}$.

- $ N_{\rm{AD}} \left( M_{\rm{B}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kNm}}\right) \cdot M_{\rm{B}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ N_{\rm{CE}} \left( M_{\rm{B}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kNm}}\right) \cdot M_{\rm{B}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ \varphi _ {\rm{B}} ^{\rm{DB}} \left( M_{\rm{B}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right)\cdot M_{\rm{B}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↺)
- $ \varphi _ {\rm{B}} ^{\rm{BE}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right)\cdot M_{\rm{B}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↺)
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema2.svg
---
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---
```
$$
\begin{align}
\sum  \left. M \right| _ {\rm{B}} ^{\rm{BD}} &= 0 \\
3 \cdot N_{\rm{AD}} + M_{\rm{B}} &= 0 \\
N_{\rm{AD}} = -0.33 \cdot M_{\rm{B}}
\end{align}
$$

$$
\begin{align}
\sum  \left. M \right| _ {\rm{B}} ^{\rm{BG}} &= 0 \\
- M_{\rm{B}} + 2 \cdot N_{\rm{CE}} - 5 \cdot 26 &= 0 \\
N_{\rm{CE}} &= 0.5 \cdot M_{\rm{B}} + 65
\end{align}
$$

$$ \varphi _ {\rm{B}} ^{\rm{DB}} = -\cfrac{w_{\rm{D}}}{3} = -\cfrac{\Delta L_{\rm{AD}}}{3} = -\cfrac{N_{\rm{AD}} \cdot L_{\rm{AD}}}{3 \cdot EA} = 0.00011 \cdot M_{\rm{B}} $$
$$ \varphi _ {\rm{B}} ^{\rm{BE}} = \cfrac{w_{\rm{E}}}{2} = - \cfrac{\Delta L_{\rm{CE}}}{2} = -\cfrac{N_{\rm{CE}} \cdot L_{\rm{CE}}}{2 \cdot EA} = -0.00025 \cdot M_{\rm{B}} - 0.0325 $$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-90]
^^^
? Use the deformation condition to solve for the statically indeterminate force $M_{\rm{B}}$.

$ M_{v} = $ {gap} $\rm{kNm}$ (positive indicates tension at the bottom; round to whole numbers)
---

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[30]
M[20]
M[-0.01]
^^^
? Now also solve for the normal forces and rotation.

- $ N_{\rm{AD}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{CE}}  = $ {gap} $ \rm{kN}$
- $ \varphi_{\rm{B}} = $ {gap} $ \rm{rad}$ (↺)
---

::::

## Statically indeterminate normal force $N_{\rm{AD}}$

The following statically determinate system is chosen:

```{hide-sticky-margin}
```
```{figure-start} lesoefeningen_data/stat_bepaald_N_AD.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

```{figure-end}
```

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
DS[φ;{w}]
DS[{D on the AD side};D on the BD side;B on the DB side]
DS[φ;{w}]
DS[{D on the BD side};B on the DB side]
^^^

? What is the deformation condition?

{gap}$(${gap}$) = ${gap}$(${gap}$)$
---

::::

You have already drawn the deformed structure under the statically indeterminate force $N_{\rm{AD}}$ in one of the first exercises:

:::{fetch} {numref}`optie_6`
:::

:::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the deformed statically determinate structure under the $26 \, \rm{kN}$ load.
---
=

```{figure} ./lesoefeningen_data/optie6_26.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-1.5]
M[65]
M[0.015]
M[-0.0650]
M[0.001]
M[0]
M[-0.00225]
M[0.09750]
^^^
? Determine the normal forces and displacements as functions of $N_{\rm{AD}}$.

- $ N_{\rm{CE}} \left( N_{\rm{AD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot N_{\rm{AD}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ w_{\rm{E}} \left( N_{\rm{AD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot N_{\rm{AD}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positive upwards)
- $ w_{\rm{D}} ^{\rm{AD}} \left( N_{\rm{AD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot N_{\rm{AD}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positive upwards)
- $ w_{\rm{D}} ^{\rm{BD}} \left( N_{\rm{AD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot N_{\rm{AD}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positive upwards)
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema3.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
number:
---

```

$$
\begin{align}
\sum  \left. T \right|  _ {\rm{B}} &= 0 \\
3 \cdot N_{\rm{AD}} + 2 \cdot N_{\rm{CE}} - 5 \cdot 26 &=0 \\
N_{\rm{CE}} &= - 1.5 \cdot N_{\rm{AD}} + 65
\end{align}
$$ 

$$ w_{\rm{E}} = - \Delta L_{\rm{CE}} = \cfrac{-N_{\rm{CE}} \cdot L_{\rm{CE}}}{EA} = 0.0015 \cdot N_{\rm{AD}} -0.065  $$

$$ w_{\rm{D}} ^{\rm{AD}} = \Delta L_{\rm{AD}} = \cfrac{N_{\rm{AD}} \cdot L_{\rm{AD}}}{EA} = 0.001 \cdot N_{\rm{AD}} $$ 

$$ w_{\rm{D}} ^{\rm{BD}} = -\varphi_{\rm{B}} \cdot 3 = - \cfrac{w_{\rm{E}}}{2} \cdot 3 = -0.00225 \cdot N_{\rm{AD}} + 0.0975 $$

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[30]
^^^
? Use the deformation condition to solve for the statically indeterminate force $N_{\rm{AD}}$.

$ N_{\rm{AD}} = $ {gap} $\rm{kN}$
---

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[20]
M[-2]
M[3]
M[3]
^^^
? Now also solve for the normal force $N_{\rm{CE}}$ and the displacements.

- $ N_{\rm{CE}}  = $ {gap} $ \rm{kN}$
- $ w_{\rm{E}} = $ {gap} $ \rm{cm}$ (positive upwards)
- $ w_{\rm{D}} ^{\rm{AD}} = $ {gap} $ \rm{cm}$ (positive upwards)
- $ w_{\rm{D}} ^{\rm{BD}} = $ {gap} $ \rm{cm}$ (positive upwards)
---

::::

## Deformed structure

Now that we have made the structure statically determinate in several ways, we can use one or more of the solutions to draw the deformed statically indeterminate structure.

:::{fetch} {numref}`rekoefening`
:::

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Draw the deformed **statically indeterminate** structure to scale.
---
=
```{figure} lesoefeningen_data/verplaatsingen.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
```

---

::::
