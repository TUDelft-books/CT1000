````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_raamwerk/instructie.html

```
```` 

```{index} Force method; for frame structures
```

(krachtenmethode_raamwerk)=
# Apply force method for frame structures

We have already covered the force method for [structures subjected to extension](krachtenmethode_simpel) and [beams](krachtenmethode_balk), among other topics. The procedure for frames is the same, except that extension and bending cannot always be considered separately, and when several members and/or external couples meet, we need to think carefully about where to place the hinges. This lesson focuses on frames that deform only due to bending, so $EA >> EI$. In [the next part](./instructie_2.md), we will cover the force method for frames that deform due to both bending and extension.

## Nodes with multiple members and/or external couples

Suppose several members and/or external couples meet at a point in the structure:

```{figure} ./theorie_data/knooppunt.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

If you want to add a hinge and a moment pair there, the usual procedure applies, but we need to consider its location carefully. Placing the hinge at the intersection raises a few questions:

```{figure} ./theorie_data/knooppunt_vraagteken.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

- By how much does this single hinge reduce the degree of static indeterminacy?
- One hinge with three moments? Does that still count as a moment pair?
- Which moments are equal now?
- What should we do with the moment from the external couple? How can a couple act at a hinge?
- All the rotations must be equal, but that does not provide enough equations for three unknown moments.

:::{note}
In the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`, hinges are sometimes placed at the joint using an additional trick. This approach is permitted, but not recommended.
:::

It is better to place these hinges just beside the joint. This ensures that the moment pairs from the members and the external couple do not act at the same point, that each hinge reduces the degree of static indeterminacy by 1, and that, as usual, there are two rotations at each hinge that must be equal:

```{figure} ./theorie_data/knooppunt_nieuw.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

In the example above, two hinges are sufficient to allow the ends of each member to rotate relative to the other members. The only difference from our analyses so far is that multiple moments, rather than a single moment, now act on one of the members. In the figure above, three moments act on the left-hand member: one external couple and two moments from the hinges.

::::{warning}
When adding hinges, make sure not to place one on every side of the joint. This would create a local mechanism in which the joint can rotate:

```{figure} ./theorie_data/knooppunt_mechanisme.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

::::

## Example

We will demonstrate the method for frame structures using the following example.

::::::{prf:example}
:nonumber: true
:label: sd_raam_0

```{figure-start} ./theorie_data/example.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

$$EI = 5 \ \rm{MNm^2}, EA >> EI$$

```{figure-end}
```

::::::

1. Determine the degree of static indeterminacy.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_1

    For this example, we are interested in the internal force distribution, so we need to evaluate the degree of internal static indeterminacy. Since this is an open structure, its degree of internal static indeterminacy is equal to its degree of external static indeterminacy:

    ```{figure} ./theorie_data/graad.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    number:
    ---
    
    ```

    This structure is therefore second-order internally statically indeterminate ($5-3$).

    ::::::

2. Transform the structure into a statically determinate system by removing supports, splitting the structure at a two-force member, or adding hinges. Add unknown statically indeterminate forces and deformation conditions for each support removed and each hinge added. Be careful not to transform the structure into a (partially) mechanism! Choose a statically determinate system that is easy to solve: preferably, members should not translate if they also rotate, and you should be able to identify forget-me-nots for the system.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_2

    There are many options; some of them are shown below:

    `````{tab-set}
    :sync-group: raamwerk

    ````{tab-item} Release the horizontal support at $\rm{B}$ and add a hinge at $\rm{B}$
    :sync: keyraam_1
    ```{figure} ./theorie_data/optie1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ````
    ````{tab-item} Release the horizontal supports at $\rm{B}$ and $\rm{C}$
    :sync: keyraam_2
    ```{figure} ./theorie_data/optie2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```

    ````
    ````{tab-item} Release the horizontal and vertical supports at $\rm{A}$
    :sync: keyraam_3
    ```{figure} ./theorie_data/optie3.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ````
    ````{tab-item} Release the horizontal support at $\rm{A}$ and add a hinge at $\rm{B}$
    :sync: keyraam_4
    ```{figure} ./theorie_data/optie4.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ````
    `````

    For each of these options, we can sketch the displacements and choose the one with the simplest displacement pattern:

    ```````{tab-set}
    :sync-group: raamwerk

    ``````{tab-item} Release the horizontal support at $\rm{B}$ and add a hinge at $\rm{B}$
    :sync: keyraam_1
    
    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_1_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_1_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    :::::

    Beam $\rm{AB}$ does not shorten or lengthen, so this part of the structure does not deform. The remaining part can be analysed using the forget-me-not for a simply supported beam with an end moment and the forget-me-not for a cantilever beam with an end point load. Only the moment at $\rm{C}$ needs to be determined to calculate the displacements.

    ``````

    ``````{tab-item} Release the horizontal supports at $\rm{B}$ and $\rm{C}$
    :sync: keyraam_2

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_2_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_2_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    :::::

    Beam $\rm{AB}$ does not shorten or lengthen, but it can still bend. The displacements can therefore be determined using the forget-me-nots for a simply supported beam with an end moment, a cantilever beam with an end point load, and a cantilever beam with an end moment. The internal moments at $\rm{B}$ and $\rm{C}$ must be determined to calculate the displacements.


    ``````

    ``````{tab-item} Release the horizontal and vertical supports at $\rm{A}$
    :sync: keyraam_3

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_3_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_3_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    :::::

    Beam $\rm{AB}$ does not shorten or lengthen, but it can still bend. The displacements can therefore be determined using the forget-me-nots for a simply supported beam with an end moment and a cantilever beam with an end point load. The internal moments at $\rm{B}$ and $\rm{C}$ must be determined to calculate the displacements.
    ``````

    ``````{tab-item} Release the horizontal support at $\rm{A}$ and add a hinge at $\rm{B}$
    :sync: keyraam_4

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_4_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_4_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    :::::

    Beam $\rm{AB}$ does not shorten or lengthen, so this part of the structure does not deform. The remaining part can be analysed using the forget-me-not for a simply supported beam with an end moment and the forget-me-not for a cantilever beam with an end point load. Only the moment at $\rm{C}$ needs to be determined to calculate the displacements.
    ``````

    ```````

    Although it is not the easiest option, the third option is chosen.

    ::::::

3. Solve for the displacement in terms of the unknown statically indeterminate forces, as you would normally do for a statically determinate structure.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_4

    We have chosen the following statically determinate structure with the deformation conditions $w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $ and $w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $:

    ```{figure-start} ./theorie_data/SB-systeem.svg
    ---
    align: center
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    figclass: sticky-margin
    ---
    
    ```
    $$EI = 5 \ \rm{MNm^2}, EA >> EI$$
    ```{figure-end}
    ```

    The force distribution can be found using equilibrium:

    - $M_{\rm{C}} = 90 \ \rm{kNm}$ (◠/ᑐ)
    - $M_{\rm{B}} = 6A_{\rm{v}}$ (◡/ᑐ)

    The rotations can now be evaluated using the forget-me-nots:

    - $\varphi_{\rm{B}} = \cfrac{90 \cdot 3}{6 \cdot 5000} + \cfrac{6A_{\rm{v}} \cdot 3}{3 \cdot 5000} = 0.0012 A_{\rm{v}} + 0.009$ (↻)
    - $w_{\rm{A}} = \varphi_{\rm{B}} \cdot 6 + \cfrac{A_{\rm{v}} \cdot 6^3}{3 \cdot 5000}= 0.0216 A_{\rm{v}} + 0.054$

    The horizontal displacement is given by: $w_{\rm{A,h}}  = \cfrac{6A_{\rm{h}}}{EA} $

    ::::::

4. Use the deformation conditions to solve for the statically indeterminate forces.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_5

    $$
    \begin{align*}
    w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) &= 0 \\
    0.0216 A_{\rm{v}} + 0.054 &= 0 \\
    A_{\rm{v}} &= -2.5 \ \rm{kN} \\
    \\
    w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) &= 0 \\
    \cfrac{6A_{\rm{h}}}{EA} &= 0 \\
    A_{\rm{h}} &\to 0 \ \rm{kN}
    \end{align*}
    $$

    Because $EA \gg EI$, $A_{\rm{h}}$ approaches $0$. We often simplify the notation and write $A_{\rm{h}} = 0 \ \rm{kN}$.

    The deformations of the statically indeterminate structure can also be sketched. In this case, this could even have been done beforehand (without exact values), since the directions of the displacements can be determined without calculation:

    ```{figure} ./theorie_data/vervormd.svg
    ---
    align: center
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ---
    
    ```
    ::::::

## More examples

The general concept of the force method is covered in section 2.1. The force method for frames is covered in sections 2.2.5–2.2.7, and the more specific 'hoekveranderingsvergelijkingen' in section 3.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

When the book refers to the 'moment-area method' in examples 2.2.6 and 2.2.7, the displacements can also be found using forget-me-nots. The method with translating joints ('hoekveranderingsvergelijkingen' with translating joints), which was taught in the past, is no longer covered.

## Lecture recording

This topic was presented in Dutch in [lecture 9 of CTB2210](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/2dabd45be53f4c368ddb2bc325231cfa1d?sortBy=most-recent), from 0:04:35 to 0:39:40.

## Additional exercises

- The guided exercises on the next two pages are a first exercise to check your understanding
- For more practice, you can work on:
    - Exercises 2.15–2.21, 2.42, 2.45 and 2.46 in section 2.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).
    - Exercises 3.11–3.15, 3.22, 3.23, 3.25–3.33/1, 3.35, 3.36, 3.45, 3.47-1, 3.47-2, 3.47-4, 3.50 and 3.51 in section 3.4 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-3/).
