```{index} Displacements truss structures; Class exercise using constitutive equation
```

(lesson4.2)=
# Lesson Wednesday

During today's lesson you'll work on a complex exercise on the topic of Extension. Please ask your questions regarding the [homework](homework4.2) as well!

## Exercise Extension

Given the following structure.

```{figure} intro_data/structure.svg
:align: center
```

1. Find the displacement of $\text{R}$

2. Draw the displaced structure


````{admonition} Solution assignment 1
:class: tip, dropdown

$96.7 \text{ mm}$ ↓

```{admonition} Solution elongations cables
:class: tip, dropdown

| Cable   | Elongation (mm) |
|---------|-----------------|
| BK      | 24           |
| CK      | 24           |
| DH      | 13           |
| GJ      | 52           |
| IM      | 5           |
| JP      | 15           |
| KQ      | 48           |
| OR      | 40            |

```

````

````{admonition} Solution assignment 2
:class: tip, dropdown

```{figure} intro_data/ans.svg
:align: center
```

````

````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://oit.tudelft.nl/CTB2210/2026/statisch_onbepaald/COZ1.html
```
````

## Exercise static indeterminacy 1

The following structure is given:

```{figure} coz_data/constructie1.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_coz
---

```

::::{admonition} Exercise
:class: exercise

What is the degree of external static indeterminacy of this structure?

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} coz_data/uitwerking1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_coz
:number:
```

$8 + 4 - 9 = 3 $

::::

::::{admonition} Exercise
:class: exercise

What is the degree of internal static indeterminacy of this structure?

::::

::::{admonition} Solution
:class: solution, dropdown

The degree of internal static indeterminacy is equal to the degree of external static indeterminacy because the structure is open.

::::


````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://oit.tudelft.nl/CTB2210/2026/statisch_onbepaald/COZ2.html
```
````

## Exercise static indeterminacy 2

The following structure is given:

```{figure} coz_data/constructie2.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
---

```

::::{admonition} Exercise
:class: exercise

What is the degree of external static indeterminacy of this structure?

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} coz_data/uitwerking2deel1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
:number:
```

$ 3 - 3 = 0 $

::::

::::{admonition} Exercise
:class: exercise

What is the degree of internal static indeterminacy of this structure?

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} coz_data/uitwerking2deel2onbekenden.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
:number:

```

There are 33 unknown forces.

```{figure} coz_data/uitwerking2deel2vergelijkingen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
:number:

```

There are 33 equilibrium equations.

$ 33 - 33 = 0 $

If two-force members are not taken into account, 6 unknown forces and 6 equilibrium equations are added.

::::

````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://oit.tudelft.nl/CTB2210/2026/statisch_onbepaald/COZ3.html
```
````

## Exercise static indeterminacy 3

The following structure is given:

```{figure} coz_data/constructie_3.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
---

```

::::{admonition} Exercise
:class: exercise

What is the degree of external static indeterminacy of this structure?

::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} coz_data/uitwerking3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk

```

$ 4 - 3 = 1$

::::

::::{admonition} Exercise
:class: exercise

What is the degree of internal static indeterminacy of this structure?

::::

::::{admonition} Solution
:class: solution, dropdown
:name: stat_onbepaald_raamwerk

```{figure} ../krachtenmethode_raamwerk/lesoefeningen_data/Onbekenden.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_coz
:number:
:name: stat_onbepaald_raamwerk_1
```

There are 25 unknown forces.

```{figure} ../krachtenmethode_raamwerk/lesoefeningen_data/Vergelijkingen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch_coz
:number:
:name: stat_onbepaald_raamwerk_2
```

There are 22 equilibrium equations.

$25 - 22 = 3 $

::::
