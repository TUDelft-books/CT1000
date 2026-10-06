````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/steunpuntszetting_stijfheden/theorie2.html

```
````

# Apply stiffness effects in statically indeterminate structures

Differences in stiffness do not cause a redistribution of forces in statically determinate structures; they only affect the displacements. In statically indeterminate structures, stiffness differences also affect the force distribution. Analysing these effects can be very interesting.

There are two ways to analyse stiffness effects:

1. Solve the structure with an unknown scaling factor $n \cdot EI$ or $n \cdot EA$. This gives expressions for the forces and displacements and makes it possible to plot their asymptotic behaviour as a function of $n$. With this approach, a statically determinate structure must be solved using a method of your choice.
2. Examine the limiting cases: consider $EI \to 0$ or $EA \to 0$, and $EI \to \infty$ or $EA \to \infty$. This gives the extreme force values and the envelope of internal forces and displacements. All actual stiffness values must lie within this envelope. In this analysis, the structure sometimes simplifies to a statically determinate structure.

We will demonstrate both approaches using the following structure:

::::::{prf:example}
:nonumber: true
:label: stijfheid_0

```{figure} ./theorie_data/systeem.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
:figclass: sticky-margin
```

::::::

## Scaling factor

1. Determine the degree of static indeterminacy.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_1

    ```{figure} ./theorie_data/statisch_onbepaaldheid_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```

    This structure is first-order internally statically indeterminate.

    ::::::

2. Transform the structure into a statically determinate system by removing supports, splitting the structure at a two-force member, or adding hinges. Add unknown statically indeterminate forces and deformation conditions for each support removed and each hinge added. Be careful not to transform the structure into a (partially) mechanism! Choose a statically determinate system that is easy to solve: preferably, members should not translate if they also rotate, and you should be able to identify forget-me-nots for the system.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_2

    Here, the slope-deflection method ('hoekveranderingsvergelijkingen') is chosen. This gives the following statically determinate system.

    ```{figure} ./theorie_data/SB_systeem_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    :figclass: sticky-margin
    ```

    ::::::

3. Solve for the displacement in terms of the unknown statically indeterminate forces, as you would normally do for a statically determinate structure.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_3

    The rotations caused by the moments and distributed load can be found using forget-me-nots.

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verplaatsing_5.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```

    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verplaatsing_6.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```
    ::::

    :::::

    - $\varphi _{\rm{B}}^{{\rm{AB}}}  = \cfrac{4 M_{\rm{B}}}{3 EI} + \cfrac{8}{EI}$
    - $\varphi _{\rm{B}}^{{\rm{BC}}}  = \cfrac{-4 M_{\rm{B}}}{3 n EI}$

    ::::::


4. Use the deformation conditions to solve for the statically indeterminate forces.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_4

    $\varphi _{\rm{B}}^{{\rm{AB}}} = \varphi _{\rm{B}}^{{\rm{BC}}}$ gives $M_{\rm{B}} = -\cfrac{6n}{n+1}$. Then $M_{\rm{D}} = -\cfrac{3n}{n+1}+8$ (◡).

    For $n=0$, this gives:
    
    - $M_{\rm{B}} = 0 \ \rm{kNm}$
    - $M_{\rm{D}} = 8 \ \rm{kNm}$

    For $\mathop {\lim }\limits_{n \to \infty } $, this gives:
    
    - $M_{\rm{B}} = -6 \ \rm{kNm}$
    - $M_{\rm{D}} = 5 \ \rm{kNm}$

    These results can be plotted:

    ```{figure} ./theorie_data/steunpuntszetting.svg
    ---
    align: center
    ---
    Bending-moment diagram for different values of $n$
    ```


    ::::::

## Limiting cases

::::::{prf:example}
:nonumber: true
:label: stijfheid_5

**Case $nEI \to 0$**

In the first case, $nEI \to 0$, the right-hand part of the structure has no stiffness. We can therefore treat segment $\rm{AB}$ as a statically determinate simply supported beam:

```{figure} ./theorie_data/systeem_0.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

This directly gives the moment at $\rm{D}$ as $\cfrac{1}{4}FL = 8 \ \rm{kNm}$, and the following bending-moment diagram:

```{figure} ./theorie_data/M_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

**Case $nEI \to \infty$**

In the second case, $nEI \to \infty$, the right-hand part becomes infinitely stiff:

```{figure} ./theorie_data/systeem_inf.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

This gives the following rotations for the statically determinate system with deformation condition $\varphi _{\rm{B}}^{{\rm{AB}}} = \varphi _{\rm{B}}^{{\rm{BC}}}$ (see [the slope-deflection method ('hoekveranderingsvergelijkingen') with a scaling factor](stijfheid_3)):

 - $\varphi _{\rm{B}}^{{\rm{AB}}}  = \cfrac{4 M_{\rm{B}}}{3 EI} + \cfrac{8}{EI}$
 - $\varphi _{\rm{B}}^{{\rm{BC}}}  = 0$

This results in $M_{\rm{B}} = 6 \ \rm{kNm}$ and $M_{\rm{D}} = 5 \ \rm{kNm}$:

```{figure} ./theorie_data/M_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

::::::

## Bending-moment envelope

::::::{prf:example}
:nonumber: true
:label: stijfheid_6

The extreme moments can be combined to form a bending-moment envelope, with all possible moment values for $n$ lying within the shaded region.

```{figure} ./theorie_data/omhullende.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

The same can be done for other force and displacement quantities.

::::::

## More examples

Stiffness effects are covered in chapter 7 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. The slope-deflection method ('hoekveranderingsvergelijkingen') with translating joints, used in example 2 of section 7.1, can be replaced by one of the methods covered in this course.

## Lecture recording

This topic was presented in Dutch in [lecture 11 in CTB2210](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/6ec64d00cb1b4f48af6a3583bd0d32051d?sortBy=most-recent), from 0:42:30 to 1:03:10.

## Additional exercises
- The guided exercise on the next page is a first exercise to check your understanding.
