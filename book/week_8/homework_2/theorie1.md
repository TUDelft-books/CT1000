````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/steunpuntszetting_stijfheden/theorie1.html

```
````

# Apply support settlements in statically indeterminate structures

Support settlements do not cause forces or axial deformations in statically determinate structures; they only cause rigid-body displacements and rotations of the elements.

```{figure} ./theorie_data/SB.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
:figclass: sticky-margin
:number:
```

In externally statically indeterminate structures, displacement and rotation without strain are not possible. However, since displacements must be evaluated when analysing statically indeterminate structures, these additional displacements can be included without changing the solution process. Support displacements are naturally included in the deformation conditions when calculating displacements.

An example demonstrates how to account for support settlements in a statically indeterminate structure using the force method, specifically using 'hoekveranderingsvergelijkingen'. Other methods are also possible.

::::::{prf:example}
:nonumber: true
:label: steunpunt_0

```{figure-start} ./theorie_data/constructie.svg
---
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
---
```

- $EI = 34000 \ \rm{kNm^2}$
- $EA \gg EI$

```{figure-end}
```

::::::

1. Determine the degree of static indeterminacy.

    ::::::{prf:example}
    :nonumber: true
    :label: steunpunt_1

    ```{figure} ./theorie_data/statisch_onbepaaldheid.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```

    There are 5 unknown forces and 3 equilibrium equations, so this structure is second-order internally statically indeterminate.

    ::::::

2. Transform the structure into a statically determinate system by removing supports, splitting it at a two-force member, or adding hinges. Add unknown statically indeterminate forces and deformation conditions for each support removed and each hinge added. Be careful not to transform the structure into a (partially) mechanism! Choose a statically determinate system that is easy to solve: preferably, members should not translate if they also rotate, and you should be able to identify forget-me-nots for the system.

    ::::::{prf:example}
    :nonumber: true
    :label: steunpunt_2

    Here, t'hoekveranderingsvergelijkingen' is chosen. This gives the following statically determinate system.

    ```{figure-start} ./theorie_data/SB-systeem.svg
    ---
    align: center
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ---
    ```

    - $EI = 34000 \ \rm{kNm^2}$
    - $EA \gg EI$

    ```{figure-end}
    ```


3. Solve for the displacement in terms of the unknown statically indeterminate forces, as you would normally do for a statically determinate structure.

    ::::::{prf:example}
    :nonumber: true
    :label: steunpunt_3

    The rotations caused by the moments and distributed load can be found using forget-me-nots. The member also undergoes rigid-body rotation, which must be included as well.

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verplaatsing_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```

    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verplaatsing_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verplaatsing_3.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verplaatsing_4.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```
    ::::

    :::::

    - $\varphi _{\rm{B}}^{{\rm{AB}}}  = \cfrac{{ - {M_{\rm{B}}} \cdot 4}}{{3 \cdot EI}} + \cfrac{{17 \cdot {4^3}}}{{24 \cdot EI}} - \cfrac{{{w_{\rm{B}}}}}{4}  = -\cfrac{M_{\rm{B}}}{25500} -\cfrac{7}{1500}$
    - $\varphi _{\rm{B}}^{{\rm{BC}}}  = \cfrac{{{M_{\rm{B}}} \cdot 6}}{{3 \cdot EI}} - \cfrac{{{M_{\rm{C}}} \cdot 6}}{{6 \cdot EI}} + \cfrac{{{w_{\rm{B}}}}}{6} = \cfrac{M_{\rm{B}}}{17000} - \cfrac{M_{\rm{C}}}{34000} + \cfrac{1}{250}$
    - $\varphi_{\rm{C}} = -\cfrac{M_\text{B} \cdot 6}{3 \cdot EI} + \cfrac{M_\text{C} \cdot 6}{6 \cdot EI} + \cfrac{w_\text{B}}{6} = -\cfrac{M_{\rm{B}}}{34000} + \cfrac{M_{\rm{C}}}{17000} + \cfrac{1}{250}$

    ::::::

4. Use the deformation conditions to solve for the statically indeterminate forces.

    ::::::{prf:example}
    :nonumber: true
    :label: steunpunt_4

    $\varphi _{\rm{B}}^{{\rm{AB}}} = \varphi _{\rm{B}}^{{\rm{BC}}}$ and $ \varphi_{\rm{C}} = 0$ give:

    - $M_{\rm{B}} = -128 \ \rm{kNm}$
    - $M_{\rm{C}} = -132 \ \rm{kNm}$

    ::::::

## More examples

Support settlements are covered in chapter 6.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Example 6.1.3 can be skipped.

## Lecture recording

This topic was presented in Dutch in [lecture 11 in CTB2210](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/6ec64d00cb1b4f48af6a3583bd0d32051d?sortBy=most-recent), from 0:24:00 to 0:42:30.

## Additional exercises
- The guided exercise on the next page is a first exercise to check your understanding.
- For more practice:
  - Exercises: 6.1–6.18, 6.20 and 6.22–6.24 in section 6.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Unfortunately, no answers are available.
  - Problems 1a and 1b from [the Dutch 2018 Structural Mechanics 3 exam](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/CM3_jan2018_tentamenopgaven.pdf). The solutions are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/CM3_jan2018_tentamenopgaven_uitwerkingen.pdf) {cite:p}`Exam_2018`.
  - Question 1 from [the Dutch first 2020 Structural Mechanics 3 exam](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/CM3_januari_2020_tentamenopgaven.pdf). The solutions are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/Uitwerkingen_tentamen_CM3_januari_2020.pdf) {cite:p}`Exam_2020_A`.