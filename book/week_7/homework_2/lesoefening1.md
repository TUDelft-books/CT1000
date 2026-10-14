````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/verplaats2/lesoefening1.html

```
````

# Guided exercise 1

Consider the following structure:

```{figure-start} lesoefening_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
:figclass: sticky-margin
```

$ EA = \cfrac{25}{14} \ \rm{MN}$

```{figure-end}
```

The horizontal and vertical displacements of hinge $\rm{S}$ are taken as the degrees of freedom, positive to the right and downward.

```{figure-start} lesoefening_data/displaced.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
:figclass: sticky-margin
```

$ EA = \cfrac{25}{14} \ \rm{MN}$

```{figure-end}
```

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the deformed structure due to the as-yet-unknown displacements of joint $\rm{S}$.
---
=
```{figure} lesoefening_data/vervormd.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
```

---

::::

::::{question} Exercise
:label: verplaats2_1
:type: multiple-choice
:variant: single-select
:admonition:
:class: exercise
:nocaption:
:showanswer:

Why does the rotation of $\rm{S}$ not need to be included as a degree of freedom?
---
[x] The rotation of a hinge has no meaning.
[ ] The members will not rotate.
> The members can indeed rotate. If $\rm{S}$ undergoes a small vertical displacement, the horizontal members will no longer remain horizontal. However, this is not an independent degree of freedom; it can be derived from the horizontal and vertical displacements of $\rm{S}$.
[ ] The structure is statically determinate.
> This is irrelevant to the question.
---

::::


::::{question} Exercise
:label: verplaats2_2
:type: multiple-choice
:variant: single-select
:admonition:
:class: exercise
:nocaption:
:showanswer:

Do you need a Williot diagram to determine the extension or shortening of the members in this case?
---
[ ] Yes, you need a Williot diagram to determine the strain in all members.
> Incorrect. A Williot diagram is needed when the member rotations are unknown even though the extensions or shortenings are known.
[ ] Yes, you only need a Williot diagram to determine the extension or shortening of member SC, not the other members.
> Incorrect. A Williot diagram is needed when the member rotations are unknown even though the extensions or shortenings are known.
[x] No, you do not need a Williot diagram.
> Correct. You already know exactly where $\rm{S}$ moves, so a Williot diagram is not needed to determine the member rotations.
---

::::

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Split the structure and sketch the deformations of each of the three members, including the corresponding displacements and forces.
---
=
```{figure} lesoefening_data/gesplitst.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
```

---

::::

::::{question} Exercise
:label: verplaats2_3
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAPE[2500/7;1;3]
M[0]
M[0]
MAPE[-6250/7;1;3]
M[0]
M[0]
MAPE[-1500/7;1;3]
MAPE[-2000/7;1;3]
M[0]
^^^
? Determine the axial forces in the three members as functions of the displacements $u_{\rm{S,h}}$ and $u_{\rm{S,v}}$.

- $ N_{\rm{AS}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} + $ {gap} $ \left(\rm{in \ kN}\right) $
- $ N_{\rm{SB}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} + $ {gap} $ \left(\rm{in \ kN}\right) $
- $ N_{\rm{SC}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} + $ {gap} $ \left(\rm{in \ kN}\right) $
---

::::

::::{admonition} Solution
:class: solution, dropdown

From the displacement of the hinge, we can determine that:

- $ \Delta L_{\rm{AS}} = + u_{\rm{S,h}} $
- $ \Delta L_{\rm{SB}} = - u_{\rm{S,h}} $

For member $\rm{SC}$, the angle of the member must also be taken into account.

```{figure} lesoefening_data/verplaatst_SC.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
number:
---
```

$$ \Delta L_{\rm{SC}} = - \cfrac{4}{5} \cdot u_{\rm{S,v}} - \cfrac{3}{5} \cdot u_{\rm{S,h}} $$

The extensions and shortenings of the members can be converted into axial forces using $N = EA \cfrac{\Delta L}{L}$.

- $ N_{\rm{AS}} = \cfrac{12500}{7 \cdot 5} \cdot u_{\rm{S,h}} \approx 357 \cdot u_{\rm{S,h}}$
- $ N_{\rm{SB}} = -\cfrac{12500}{7 \cdot 2} \cdot u_{\rm{S,h}} \approx -893 \cdot u_{\rm{S,h}}$
- $ N_{\rm{SC}} = -\cfrac{3 \cdot 12500}{5 \cdot 7 \cdot 5} \cdot u_{\rm{S,h}} -\cfrac{4 \cdot 12500}{5 \cdot 7 \cdot 5} \cdot u_{\rm{S,v}} \approx - 214 \cdot u_{\rm{S,h}} - 286 \cdot u_{\rm{S,v}}$


::::

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Draw the free-body diagram of joint $\rm{S}$, showing the forces in the directions determined above.
---
=
```{figure} lesoefening_data/vrijlichaamsschema_S.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
```

---

::::

::::{question} Exercise
:label: verplaats2_4
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAP[-33.6;1]
MAP[270.2;1]

^^^
? Determine the values of the degrees of freedom $u_{\rm{S,h}}$ and $u_{\rm{S,v}}$.

- $ u_{\rm{S,h}} =  $ {gap} $ \rm{mm} $
- $ u_{\rm{S,v}} =  $ {gap} $ \rm{mm} $
---

::::

::::{admonition} Solution
:class: solution, dropdown

This is solved using equilibrium at joint $\rm{S}$.

$$
\begin{align}
\sum  \left. F \right|  _ {\rm{h}} ^{\rm{S}} &= 0 \\
- N_{\rm{AS}} + N_{\rm{SB}} + \cfrac{3}{5} N_{\rm{SC}} &= 0 \\
- \cfrac{9650}{7} \cdot u_{\rm{S,h}} - \cfrac{1200}{7} \cdot u_{\rm{S,v}} &= 0
\end{align}
$$

$$
\begin{align}
\sum  \left. F \right|  _ {\rm{v}} ^{\rm{S}} &= 0 \\
56 + \cfrac{4}{5} N_{\rm{SC}} &= 0 \\
56 - \cfrac{1200}{7} \cdot u_{\rm{S,h}} - \cfrac{1600}{7} \cdot u_{\rm{S,v}} &= 0
\end{align}
$$

The system of two equations above can be solved for $u_{\rm{S,h}}$ and $u_{\rm{S,v}}$, giving:

- $ u_{\rm{S,h}} = -\cfrac{21}{625} \ \rm{m} \approx -33.6 \ \rm{mm} $
- $ u_{\rm{S,v}} = \cfrac{1351}{5000} \ \rm{m} \approx 270.2 \ \rm{mm} $

::::

::::{question} Exercise
:label: verplaats2_5
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-12]
M[30]
M[-70]
^^^
? Determine the axial forces in the three members.

- $ N_{\rm{AS}}  = $ {gap} $ \rm{kN}$
- $ N_{\rm{SB}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{SC}} = $ {gap} $ \rm{kN}$
---

::::

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Draw the deformed structure to scale.
---
=
```{figure} lesoefening_data/vervormd_schaal.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
```

---

::::
