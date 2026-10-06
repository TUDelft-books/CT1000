````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/verplaats2/lesoefening2.html

```
````

# Guided exercise 2

Consider the following structure:

```{figure-start} lesoefening2_data/structure.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden_2
:number:
```

$ EI \gg EA$

```{figure-end}
```

::::{question} Exercise
:label: verplaats3_1
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

What is the degree of internal static indeterminacy?
---
M[3]
^^^
? The structure is {gap}st/nd/rd/th order internally statically indeterminate.
---

::::

::::{admonition} Solution
:class: solution, dropdown

This is an open structure, so the degree of internal static indeterminacy is equal to the degree of external static indeterminacy. There are 6 unknown support reactions and 3 equilibrium equations, so the structure is third-order statically indeterminate.

::::

The two-force members are replaced by springs, giving the following structure:

```{figure-start} lesoefening2_data/springs.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden_2
:number:
:figclass: sticky-margin
```

$ EI \gg EA$

```{figure-end}
```

::::{question} Exercise
:label: verplaats3_2
:variant: multiple-select
:columns: 1 1 2 2
:admonition:
:class: exercise
:nocaption:
:showanswer:

Which degrees of freedom can you choose for this structure?
---
[x] Vertical displacement of $\rm{A}$
[x] Vertical displacement of $\rm{B}$
[x] Vertical displacement of $\rm{C}$
[x] Vertical displacement of $\rm{D}$
[x] Vertical displacement of $\rm{E}$
[x] Rotation of member $\rm{ABCDE}$
^^^
= Any combination of two degrees of freedom is valid!
---

::::

::::{question} Exercise
:label: verplaats3_3
:variant: multiple-select
:columns: 1
:admonition:
:class: exercise
:nocaption:
:showanswer:

What are the advantages of the displacement method over the force method when analysing this structure?
---
[x] Fewer equations need to be set up for the displacement method than for the force method.
> Correct, but this is specific to this structure. Other structures may require more equations instead.
[x] The degree of static indeterminacy does not need to be determined for the displacement method, unlike for the force method.
[ ] Forces do not need to be determined for the displacement method, but they do for the force method.
> Incorrect. The displacement method uses equilibrium equations involving forces.
[ ] Forget-me-nots do not need to be used for the displacement method, unlike for the force method.
> Incorrect. No forget-me-nots are needed for this structure with either the force method or the displacement method.
---

::::

The following degrees of freedom are chosen: $w_{\rm{A}}$ and $\varphi$:

```{figure-start} lesoefening2_data/dof.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden_2
:number:
:figclass: sticky-margin
```

$ EI \gg EA$

```{figure-end}
```

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Split the structure between the part that deforms according to the degrees of freedom and the remaining parts. Sketch the structure after splitting it.
---
=
```{figure} lesoefening2_data/gesplitst.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden_2
:number:
```

---

::::

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the deformed, split structure due to the as-yet-unknown $w_{\rm{A}}$
---
=
```{figure} lesoefening2_data/vervorm_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden_2
:number:
```

---

::::

::::{question} Exercise
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Sketch the deformed, split structure due to the as-yet-unknown $\varphi$
---
=
```{figure} lesoefening2_data/vervorm_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden_2
:number:
```

---

::::

:::::{question} Exercise
:label: verplaats3_35
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[100]
M[0]
M[0]
M[200]
M[400]
M[0]
M[300]
M[1500]
M[0]
M[400]
M[3600]
M[0]
M[500]
M[5000]
M[0]
^^^
? Determine the axial forces in the springs as functions of $w_{\rm{A}}$ and $\varphi$. Use kN, m and rad for your answers, and take upward force as positive.

- $ N_{\rm{A}} \left( w_{\rm{A}}, \varphi \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot w_{\rm{A}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{rad}}\right) \cdot \varphi + $ {gap} $ \left(\rm{in \ kN}\right) $
- $ N_{\rm{B}} \left( w_{\rm{A}}, \varphi \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot w_{\rm{A}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{rad}}\right) \cdot \varphi + $ {gap} $ \left(\rm{in \ kN}\right) $
- $ N_{\rm{C}} \left( w_{\rm{A}}, \varphi \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot w_{\rm{A}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{rad}}\right) \cdot \varphi + $ {gap} $ \left(\rm{in \ kN}\right) $
- $ N_{\rm{D}} \left( w_{\rm{A}}, \varphi \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot w_{\rm{A}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{rad}}\right) \cdot \varphi + $ {gap} $ \left(\rm{in \ kN}\right) $
- $ N_{\rm{E}} \left( w_{\rm{A}}, \varphi \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot w_{\rm{A}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{rad}}\right) \cdot \varphi + $ {gap} $ \left(\rm{in \ kN}\right) $

---
:::::

::::{question} Exercise
:label: verplaats3_4
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-1500]
M[-10500]
M[-2580]
^^^
? Write the vertical equilibrium equation. Use kN, m and rad for your answers, and take upward force as positive.

$ ${gap}$ \cdot w_{\rm{A}} + ${gap}$ \cdot \varphi + ${gap}$ = 0 $
---
::::

::::{admonition} Solution
:class: solution, dropdown

Vertical force equilibrium:

$$
\begin{align}
\sum  \left. F \right|  _ {\rm{v}} &= 0 \\
- N_{\rm{A}} - N_{\rm{B}} - N_{\rm{C}} - N_{\rm{D}} - N_{\rm{E}} - 2580 &= 0 \\
- 100 \cdot w_{\rm{A}} - 200 \cdot w_{\rm{B}} - 300 \cdot w_{\rm{C}} - 400 \cdot w_{\rm{D}} - 500 \cdot w_{\rm{E}} - 2580 &= 0 \\
- 100 \cdot w_{\rm{A}} - 200 \cdot \left(w_{\rm{A}} + 2 \cdot \varphi \right) - 300 \cdot \left(w_{\rm{A}} + 5 \cdot \varphi \right) - 400 \cdot \left(w_{\rm{A}} + 9 \cdot \varphi \right) - 500 \cdot \left(w_{\rm{A}} + 10 \cdot \varphi \right) - 2580 &= 0 \\
-1500 \cdot w_{\rm{A}} - 10500 \cdot \varphi - 2580 &= 0
\end{align}
$$

::::

::::{question} Exercise
:variant: single-select
:columns: 1
:admonition:
:class: exercise
:nocaption:
:showanswer:

Also write the moment equilibrium equation. You cannot check this answer, however. Why is there no unique answer for the other equilibrium equation?
---
[x] Moments can be summed about any point.
[ ] Moments can be summed about A or B.
> Moments can always be summed about any point, not only points where the internal bending moment is zero.
[ ] The values of $w_{\rm{A}}$ and $\varphi$ are unknown.
> $w_{\rm{A}}$ and $\varphi$ are precisely what these equilibrium equations are used to solve for, so they are supposed to be unknown.
---
::::

::::{admonition} Solution
:class: solution, dropdown

One possibility, taking moments about point $\rm{A}$, is shown below:

$$
\begin{align}
\sum  \left. T \right|  _ {\rm{A}} &= 0 \\
- 2 \cdot N_{\rm{B}} - 5 \cdot N_{\rm{C}} - 9\cdot N_{\rm{D}} - 10 \cdot N_{\rm{E}} - 8 \cdot 2580 &= 0 \\
- 2 \cdot 200 \cdot w_{\rm{B}} - 5 \cdot 300 \cdot w_{\rm{C}} - 9 \cdot 400 \cdot w_{\rm{D}} - 10 \cdot 500 \cdot w_{\rm{E}} - 8 \cdot 2580 &= 0 \\
- 2 \cdot 200 \cdot \left(w_{\rm{A}} + 2 \cdot \varphi\right) - 5 \cdot 300 \cdot \left(w_{\rm{A}} + 5 \cdot \varphi\right) - 9 \cdot 400 \cdot \left(w_{\rm{A}} + 9 \cdot \varphi\right) - 10 \cdot 500 \cdot \left(w_{\rm{A}} + 10 \cdot \varphi\right) - 8 \cdot 2580 &= 0 \\
-10500 \cdot w_{\rm{A}} - 90700 \cdot \varphi - 20640 &= 0
\end{align}
$$

::::

::::{question} Exercise
:label: verplaats3_5
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-67]
M[-0.15]
^^^
? Determine $w_{\rm{A}}$ and $\varphi$.

- $ w_{\rm{A}} = $ {gap} $ \rm{cm} $
- $ \varphi = $ {gap} $ \rm{rad} $
---

::::

::::{admonition} Solution
:class: solution, dropdown

The two equilibrium equations can be solved for the unknowns $w_{\rm{A}}$ and $\varphi$. One possible solution, using moment equilibrium about point $\rm{A}$, is shown here.

Het stelsel vergelijkingen is:

$$\begin{cases} -1500 \cdot w_{\rm{A}} -10500 \cdot \varphi -2580 = 0\\ -10500 \cdot w_{\rm{A}} -90700 \cdot \varphi -20640  = 0 \end{cases}$$

Multiplying the top equation by -7 and adding the equations gives:

$$ 0 \cdot w_{\rm{A}} - 17200 \cdot \varphi - 2580 = 0 \rightarrow \varphi = -0.15 \, \rm{rad} $$

Substituting this into the top equation gives the solution for $w_{\rm{A}}$:

$$ -1500 \cdot w_{\rm{A}} -10500 \cdot -0.15 -2580 = 0 \rightarrow w_{\rm{A}} = -67 \, \rm{cm}$$

::::


::::{question} Exercise
:label: verplaats3_6
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-67]
M[-194]
M[-426]
M[-808]
M[-1085]
^^^
? What are the forces in the springs? Take tension as positive and compression as negative.

- $ N_{\rm{A}}  = $ {gap} $ \rm{kN}$
- $ N_{\rm{B}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{C}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{D}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{E}} = $ {gap} $ \rm{kN}$
---

::::

::::{admonition} Solution
:class: solution, dropdown

- $ N_{\rm{A}} = 100 \cdot w_{\rm{A}} = -67 \, \rm{kN}$
- $ N_{\rm{B}} = 200 \cdot w_{\rm{B}} = 200 \cdot \left(w_{\rm{A}} + 2 \cdot \varphi\right) =-194 \, \rm{kN}$
- $ N_{\rm{C}} = 300 \cdot w_{\rm{C}} = 300 \cdot \left(w_{\rm{A}} + 5 \cdot \varphi\right) =-426 \, \rm{kN}$
- $ N_{\rm{D}} = 400 \cdot w_{\rm{D}} = 400 \cdot \left(w_{\rm{A}} + 9 \cdot \varphi\right) =-808 \, \rm{kN}$
- $ N_{\rm{E}} = 500 \cdot w_{\rm{E}} = 500 \cdot \left(w_{\rm{A}} + 10 \cdot \varphi\right) =-1085 \, \rm{kN}$

::::
