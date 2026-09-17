````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://oit.tudelft.nl/CTB2210/2026/statisch_onbepaald/graad_bepalen_2.html
```
````}````

# Exercise 2

The following structure is given:

```{figure} ./graad_bepalen_data/Oefening_1.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
---

```

Determine the degree of internal static indeterminacy. Although a distinction can be made between two-force members and regular members, reducing the number of unknown forces and equilibrium equations, do not make that distinction in the first part of this exercise. In the second part of this exercise, it will be made.

## Without Distinguishing Between Two-Force Members and Regular Members

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[6]
> Each of the hinged supports has $2$ support reactions.
M[34]
> There are no moments at $\rm{A}$, below $\rm{D}$, around $\rm{E}$, or around $\rm{G}$ because of the hinged connections. The other connections do have moments.
M[40]
^^^
? Split the structure into all separate nodes and members, and draw the free-body diagram for possible forces on the nodes. Take into account which members and supports are connected to the nodes.

There are {gap} unknown support reactions and {gap} unknown member forces. That makes {gap} unknown forces in total
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./graad_bepalen_data/Oefening_2.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
number:
---

```

```{figure} ./graad_bepalen_data/Oefening_3.svg
---
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
---

```

There are *6* unknown support reactions and *34* unknown member forces. That makes *40* unknown forces in total.

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[15]
> For every node where moments act, there are $3$ equilibrium equations; for the other nodes, there are $2$.
M[21]
> There are $3$ equilibrium equations for each member.
M[36]
^^^
? Split the structure into all separate nodes and members, and draw the free-body diagram for possible forces on the nodes. Take into account which members and supports are connected to the nodes.

There are {gap} equilibrium equations from the nodes and {gap} from the members. That makes {gap} equilibrium equations in total
---

::::

::::{admonition} Solution
:class: solution, dropdown

At nodes $\rm{A}$, $\rm{E}$, and $\rm{G}$, forces act only in the vertical and horizontal directions, so there are $2$ equilibrium equations. At the other nodes, moments also act, so there are $3$ equilibrium equations per node. This gives $\left( 2 +2 +2 +3+3+3 \right) = 15$ equilibrium equations from the nodes. All members have three equilibrium equations, giving $\left( 7 \cdot 3 \right) = 21$ equilibrium equations from the members. There are $36$ equilibrium equations in total.

```{figure} ./graad_bepalen_data/Oefening_4.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
number:
---

```

```{figure} ./graad_bepalen_data/Oefening_5.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
number:
---

```

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[4]
^^^
? The degree of static indeterminacy is the number of support reactions + connection forces - the number of equilibrium equations.

The structure is internally statically indeterminate to degree {gap}
---

::::

::::{admonition} Solution
:class: solution, dropdown

$$40 - 36 = 4 $$

::::

## Distinguishing Between Two-Force Members and Regular Members

Now repeat the calculation while distinguishing between two-force members and regular members.

::::{question} Opgave
:variant: multiple-select
:columns: 4
:admonition:
:class: exercise
:nocaption:
:showanswer:

Which member or members are two-force members
---
[ ] $\rm{AD}$
> At $\rm{D}$, $\rm{AD}$ is not connected by a hinge.
[ ] $\rm{DB}$
> At $\rm{B}$, $\rm{BD}$ is not connected by a hinge.
[ ] $\rm{DE}$
> At $\rm{D}$, $\rm{DE}$ is not connected by a hinge.
[ ] $\rm{BE}$
> At $\rm{E}$, $\rm{BE}$ is not connected by a hinge.
[x] $\rm{EG}$
[ ] $\rm{EC}$
> At $\rm{C}$, $\rm{EC}$ is not connected by a hinge.
[ ] $\rm{CG}$
> At $\rm{C}$, $\rm{CG}$ is not connected by a hinge.
---

::::

::::{admonition} Solution
:class: solution, dropdown

Only member $\rm{EG}$ runs from one hinged connection to another hinged connection.

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[6]
M[32]
> The shear forces at the ends of $\rm{EG}$ are now eliminated.
M[38]
^^^
? Split the structure into all separate nodes and members, and draw the free-body diagram for possible forces on the nodes. Take into account which members and supports are connected to the nodes.

There are {gap} unknown support reactions and {gap} unknown member forces. That makes {gap} unknown forces in total
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./graad_bepalen_data/Oefening_2_2.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
number:
---

```

```{figure} ./graad_bepalen_data/Oefening_3_2.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
number:
---

```

There are *6* unknown support reactions and *32* unknown member forces. That makes *38* unknown forces in total.

The two-force member results in 2 fewer unknown forces.

::::

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[15]
> At least two forces in different directions still act at every node.
M[19]
> For the two-force member, $1$ rather than $3$ equilibrium equation now applies.
M[34]
^^^
? Split the structure into all separate nodes and members, and draw the free-body diagram for possible forces on the nodes. Take into account which members and supports are connected to the nodes.

There are {gap} equilibrium equations from the nodes and {gap} from the members. That makes {gap} equilibrium equations in total
---

::::

::::{admonition} Solution
:class: solution, dropdown

Although fewer forces act at nodes $\rm{E}$ and $\rm{G}$ than before, $2$ equilibrium equations can still be applied because forces still act in different directions.

```{figure} ./graad_bepalen_data/Oefening_4_2.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
number:
---

```

Only one equilibrium equation is now needed for member $\rm{EG}$ (force equilibrium in the direction of the two-force member). This is therefore $2$ fewer equilibrium equations than before.

```{figure} ./graad_bepalen_data/Oefening_5_2.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
number:
---

```

::::
  
::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[4]
^^^
? The degree of static indeterminacy is the number of support reactions + connection forces - the number of equilibrium equations.

The structure is internally statically indeterminate to degree {gap}
---

::::

::::{admonition} Solution
:class: solution, dropdown

$$38 - 34 = 4 $$

Thus, the two-force member did not make the structure more or less statically indeterminate.

::::
