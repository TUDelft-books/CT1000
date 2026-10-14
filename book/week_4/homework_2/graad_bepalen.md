````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://oit.tudelft.nl/CTB2210/2026/statisch_onbepaald/graad_bepalen.html
```
````

# Exercise 1

The following structure is given:

```{figure} graad_bepalen_data/Oefening_6_2.svg
---
align: center
figclass: sticky-margin
source: graad_bepalen_data/Oefening_6_2.py
number:
---

```

Determine the degree of external static indeterminacy.

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[7]
> The fixed support has $3$ support reactions, the roller supports have $1$ each, and the hinged support has $2$ support reactions.
M[6]
> Without the supports, the structure consists of 4 rigid parts that can rotate relative to each other, with $2 \cdot 3 = 6$ connection forces between them.
M[13]
^^^
? Split the structure into all rigid parts that can rotate relative to each other if the supports were removed. Draw the free-body diagram of these hinged parts.

There are {gap} unknown support reactions and {gap} unknown connection forces. That makes {gap} unknown forces in total
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} graad_bepalen_data/Oefening_8.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_2
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
M[12]
^^^
? Count the equilibrium equations: 3 equilibrium equations per rigid part of the structure.

There are {gap} equilibrium equations
---

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} graad_bepalen_data/Oefening_9.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_2
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

The structure is externally statically indeterminate to degree {gap}
---

::::

::::{admonition} Solution
:class: solution, dropdown

$$13 - 12 = 1 $$

::::
