````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://oit.tudelft.nl/CTB2210/2026/statisch_onbepaald/graad_bepalen_3.html
```
````

# Exercise 3

The following structure is given:

```{figure} graad_bepalen_data/Oefening_10.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_3
number:
---

```

Determine the degrees of external and internal static indeterminacy.

## External Static Indeterminacy

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[3]
M[0]
> Although the structure consists of two parts connected by hinges, these two parts cannot rotate relative to each other.
M[3]
^^^
? Split the structure into all rigid parts that can rotate relative to each other if the supports were removed. Draw the free-body diagram of these hinged parts.

There are {gap} unknown support reactions and {gap} unknown connection forces. That makes {gap} unknown forces in total.
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} graad_bepalen_data/Oefening_11.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_3
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
M[3]
^^^
? Count the equilibrium equations: 3 equilibrium equations per rigid part of the structure.

There are {gap} equilibrium equations.
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} graad_bepalen_data/Oefening_12.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_3
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
M[0]
^^^
? The degree of static indeterminacy is the number of support reactions + connection forces - the number of equilibrium equations.

The structure is internally statically indeterminate to degree {gap}.
---

::::

::::{admonition} Solution
:class: solution, dropdown

$3 - 3 = 0$

::::

## Internal Static Indeterminacy

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[3]
M[20]
> At the member connections around $\rm{A}$, above $\rm{D}$, and to the left of $\rm{C}$, there are no moments because of the hinged connections. The other connections do have moments.
M[23]
^^^
? Split the structure into all separate nodes and members, and draw the free-body diagram for possible forces on the nodes. Take into account which members and supports are connected to the nodes.

There are {gap} unknown support reactions and {gap} unknown member forces. That makes {gap} unknown forces in total.
---

::::

::::{admonition} Solution
:class: solution, dropdown

There are *3* unknown support reactions and *19* unknown member forces. That makes *22* unknown forces in total.

```{figure} graad_bepalen_data/Oefening_13.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_3
number:
---

```

```{figure} graad_bepalen_data/Oefening_15.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_3
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
M[10]
> For every node where moments act, there are $3$ equilibrium equations; for the other nodes, there are $2$.
M[12]
> There are $3$ equilibrium equations for each member.
M[22]
^^^
? Split the structure into all separate nodes and members, and draw the free-body diagram for possible forces on the nodes. Take into account which members and supports are connected to the nodes.

There are {gap} equilibrium equations from the nodes and {gap} from the members. That makes {gap} equilibrium equations in total.
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} graad_bepalen_data/Oefening_14.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_3
number:
---

```

```{figure} graad_bepalen_data/Oefening_16.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_3
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
M[1]
^^^
? The degree of static indeterminacy is the number of support reactions + connection forces - the number of equilibrium equations.

The structure is externally statically indeterminate to degree {gap}.
---

::::

::::{admonition} Solution
:class: solution, dropdown

$23 - 22 = 1 $

::::
