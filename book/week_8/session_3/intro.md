```{index} Temperature influences; Class exercise for statically indeterminate structures
```

(lesson8.3)=
# Lesson Friday

During today's lesson you'll work on two complex exercises on the topic of Temperature influences. Please ask your questions regarding the [homework](homework8.3) as well!

````{margin}
```{attributiongrey} Attribution
:class: attribution

This exercise is translated from https://oit.tudelft.nl/CTB2210/2026/temperatuur/COZ1_temp.html

```
````

## Exercise 1

Given is the following statically structure:

```{figure-start} ./COZ1_data/constructie.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_temp_1
---

```

- $ EI = 20 \, \rm{MNm}^2 $
- $ EA \gg EI $
- $ \alpha = 0.0003 \ ^{\circ} \rm{C}^{-1} $
- $ \Delta T = 35 \ ^{\circ} \rm{C} $

```{figure-end}
```

::::{admonition} Exercise
:class: exercise

Determinate the reaction moment in $\rm{A}$.

::::

::::{admonition} Solution
:class: solution, dropdown

$ \left| M_{\rm{A}} \right| = 350 \ \rm{kNm} $

::::

````{margin}
```{attributiongrey} Attribution
:class: attribution

This exercise is translated from https://oit.tudelft.nl/CTB2210/2026/temperatuur/COZ2_temp.html

```
````

## Exercise 2

Given is the following structure:

```{figure-start} ./COZ2_data/constructie.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_temp_2
---

```

- $ EA = 15 \, \rm{MN} $
- $ EI \gg EA $
- $ \alpha = 0.0002 \ ^{\circ} \rm{C}^{-1} $
- $ \Delta T = 12.1 \ ^{\circ} \rm{C} $


```{figure-end}
```

::::{admonition} Exercise
:class: exercise

Determine the displacement of $\rm{D}$ solely due to the point load.

::::

% solution_start

::::{admonition} Solution
:class: solution, dropdown

- $ \cfrac{\sqrt{5} \cdot 100}{12} \approx 18.6 \ \rm{mm} $ (→)
- No vertical displacement

::::

% solution_end

::::{admonition} Exercise
:class: exercise

Determine the displacement of $\rm{D}$ solely due to the temperature change.

::::

% solution_start

::::{admonition} Solution
:class: solution, dropdown

- No horizontal displacement
- $2 \cdot \sqrt{5} +  5.25\approx 9.72 \ \rm{mm} $ ↑

::::
% solution_end
