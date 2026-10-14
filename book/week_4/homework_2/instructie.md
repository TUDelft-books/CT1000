````{margin}
```{attributiongrey} Attribution
:class: attribution
This page originates from https://oit.tudelft.nl/CTB2210/2026/statisch_onbepaald/instructie.html
```
````

```{index} Static indeterminacy
```
```{index} Degree of static indeterminacy
```
# Static Indeterminacy

A structure is statically indeterminate when it can no longer be solved using only equilibrium equations. A distinction can be made between:

- Only support reactions can be determined (externally statically determinate)
- Internal forces can be determined (internally statically determinate)

Determining internal static determinacy requires more work. If the structure is open, meaning that it contains no closed “loops,” internal static determinacy is equal to external static determinacy. Since calculating internal static determinacy requires more work, this can be avoided by calculating external static determinacy.

```{figure} ./determinancy_data/gesloten_vs_open.svg
---
name: gesloten_vs_open
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
---

```

If equilibrium equations are not sufficient, a structure is statically indeterminate. The degree of static indeterminacy expresses the extent of the static indeterminacy.

It is necessary to determine the degree of static indeterminacy in order to solve these structures using the force method.

These two categories are discussed together in sections 4.5.2 and 4.5.3 of the book *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. For trusses, the analysis is simplified as described in section 9.2.2 of the book *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Although the equations shown with $r$, $v$, and $e$ are simple, they are not fully correct and do not always lead to the correct results. An approach that always works is shown below for separately determining external and internal static indeterminacy.

## Determining the Degree of External Static Indeterminacy

For the calculation of external static indeterminacy, follow these steps:

::::::{prf:algorithm} Degree of external static indeterminacy
:nonumber: true
:label: graad_uitwendig_stat_onbepaaldheid

1. Split the structure into all rigid parts that can rotate relative to each other if the supports were removed. Draw the free-body diagram of these hinged parts.
2. Count the number of unknown forces: the support reactions and connection forces at the hinges (equal and opposite reaction forces are not counted separately).
3. Count the equilibrium equations: 3 equilibrium equations per rigid part of the structure.
4. The degree of static indeterminacy is the number of support reactions + connection forces - the number of equilibrium equations.

::::::

As an example, we determine the external static indeterminacy of the structure below.

::::::{prf:example}
:nonumber: true

```{figure} ./determinancy_data/Example.svg
---
name: example_sd
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
figclass: sticky-margin
---

```

::::::

1. Split the structure into all rigid parts that can rotate relative to each other if the supports were removed. Draw the free-body diagram of these hinged parts.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_1.svg
   ---
   name: example_sd_1
   align: center
   number:
   source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
   ---

   ```

   The structure can be divided into two rigid, hinge-connected parts. The supports are replaced by support reactions, and the hinged connection by a horizontal and vertical force (and reaction forces). The external force can be drawn, but has no effect on the subsequent calculations and acts only on one of the two parts.

   ::::::

2. Count the number of unknown forces: the support reactions and connection forces at the hinges (equal and opposite reaction forces are not counted separately).

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_2.svg
   ---
   name: example_sd_2
   align: center
   number:
   source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
   ---
   
   ```

   There are a total of 6 support reactions and 2 connection forces. Note that the connection forces are shown twice, but these forces are equal at both ends of the connection, so they can be counted as one.
   ::::::

3. Count the equilibrium equations: 3 equilibrium equations per rigid part of the structure.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_3.svg
   ---
   name: example_sd_3
   align: center
   number:
   source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
   ---
   
   ```

   There are two rigid parts, so there are 6 equilibrium equations.

   ::::::

4. The degree of static indeterminacy is the number of support reactions + connection forces - the number of equilibrium equations.

   ::::::{prf:example}
   :nonumber: true

   The degree of external static indeterminacy for this example is $6 + 2 - 6 = 2$.

   ::::::

```{hide-sticky-margin}
```

```{index} Degree of internal static indeterminacy
```
## Determining the Degree of Internal Static Indeterminacy
For the calculation of internal static indeterminacy, follow these steps:

::::::{prf:algorithm} Degree of internal static indeterminacy
:nonumber: true
:label: graad_inwendig_stat_onbepaaldheid

1. Check whether the structure is open. If the structure is open, internal static determinacy is equal to external static determinacy, and the simpler calculation for external static indeterminacy is sufficient. If not, continue with step 2.
2. Split the structure into all separate nodes and members, and draw the free-body diagram for possible forces on the nodes. Take hinges, supports, and free ends into account.
3. Draw the free-body diagram for the members: draw the equal and opposite reaction forces on the members resulting from the forces on the nodes.
4. Count the number of unknown forces: support reactions and member forces (equal and opposite reaction forces are not counted separately).
5. Count the number of independent equilibrium equations that can be applied to each free-body diagram to determine the unknown forces.
6. The degree of static indeterminacy is the number of unknown support reactions + unknown member forces - the number of equilibrium equations.

Optionally, a distinction can also be made between two-force members and regular members. In that case, there are fewer unknown forces at the nodes and at the ends of the members, but there is also only 1 equilibrium equation per two-force member. In that case, make sure not to include too many equilibrium equations for the connected nodes.

::::::

::::::{prf:example}
:nonumber: true

```{figure} ./determinancy_data/Example_abc.svg
---
name: example_sd_abc
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
figclass: sticky-margin
---

```

As an example, we determine the internal static indeterminacy of this structure.

::::::

1. Check whether the structure is open. If the structure is open, internal static determinacy is equal to external static determinacy, and the simpler calculation for external static indeterminacy is sufficient. If not, continue with step 2.

   ::::::{prf:example}
   :nonumber: true

   The structure is closed because of the loop $\rm{BDC}$. Internal static determinacy is therefore not equal to external static determinacy, and the simpler calculation for external static indeterminacy cannot be used. Continue with step 2.

   ::::::

2. Split the structure into all separate nodes and members, and draw the free-body diagram for possible forces on the nodes. Take into account which members and supports are connected to the nodes.

   ::::::{prf:example}
   :nonumber: true

   The structure consists of 4 nodes:
   - Unknown support reactions act on nodes $\rm{A}$ and $\rm{B}$.
   - Node $\rm{A}$ is a hinged support and end, so no bending moments act there.
   - At node $\rm{B}$, bending moments from $\rm{BC}$ and $\rm{BD}$ can occur and be in equilibrium, even though the support is a hinge.
   - No bending moment from member $\rm{DB}$ acts on node $\rm{C}$ because of the hinged connection.
   - Node $\rm{D}$ is hinged, so no bending moments act there.
   
   The external force can be drawn, but has no effect on the subsequent calculations. This gives:

   ```{figure} ./determinancy_data/Example_4.svg
   ---
   name: example_sd_4
   align: center
   number:
   source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
   ---
   
   ```

   ::::::

3. Draw the free-body diagram for the members: draw the equal and opposite reaction forces on the members resulting from the forces on the nodes.

   ::::::{prf:example}
   :nonumber: true

   The forces and moments shown on the nodes can be drawn in the opposite direction on the members.

   ```{figure} ./determinancy_data/Example_5.svg
   ---
   name: example_sd_5
   align: center
   source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
   number:
   ---
   
   ```

   ::::::

4. Count the number of unknown forces: support reactions and member forces (equal and opposite reaction forces are not counted separately).

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_6.svg
   ---
   name: example_sd_6
   align: center
   source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
   number:
   ---

   ```

   There are $\left(2+2\right)=4$ unknown support reactions and $\left( 2 + 3 + 3 + 2 + 2 + 2 +3 +3\right)=20$ unknown member forces.

   ::::::

5. Count the number of independent equilibrium equations that can be applied to each free-body diagram to determine the unknown forces.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_9.svg
   ---
   name: example_sd_9
   align: center
   source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/graad_statisch
   number:
   ---
   
   ```

   - At nodes $\rm{A}$ and $\rm{D}$, no moments act, so the forces there can be determined using only vertical and horizontal equilibrium.
   - Moments do act at nodes $\rm{B}$ and $\rm{C}$, so $3$ equilibrium equations are needed there to determine the forces.
   - Since the members are rigid bodies, $3$ equilibrium equations are also needed for each member to determine the forces.
   
   In total, there are therefore $\left(2 + 3 +3 + 3 +2 + 3 + 3 +3 \right) = 22$ equilibrium equations.

   ::::::

6. The degree of static indeterminacy is the number of unknown support reactions + unknown member forces - the number of equilibrium equations.

   ::::::{prf:example}
   :nonumber: true

   The degree of internal static indeterminacy for this example is $4 + 20 - 22 = 2$.

   ::::::

```{hide-sticky-margin}
```

## Instructions from lecture

This topic is presented in a lecture available from 0:34:40 - 1:00:40 [here in Dutch](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/391bc9ef53a54caf8d556ba2f0088e0a1d?academicYear=2026-2027-ctb2210) from 0:02:40 to 0:39:10 (TU Delft login required).

## Exercises
The exercises on the next subpages form a set of basic exercises to check your understanding.

For more practice, you can also do the following exercises:
- Exercises 4.11 - 4.22, from chapter 4 of the book *Mechanics: Evenwicht* {cite:p}`Hartsuijker1999`. Ignore the questions about kinematic determinacy. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter4/).
- Exercise 9.6, from chapter 9 of the book *Mechanics: Evenwicht* {cite:p}`Hartsuijker1999`. Ignore the questions about kinematic determinacy. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter9/).

