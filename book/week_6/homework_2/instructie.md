```{index} Force method
```
```{index} Force method; for beam structures
```

````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_balk/instructie.html.

```
````

(krachtenmethode_balk)=
# Apply force method for beam structures

We have already covered the force method for [structures subjected to extension](krachtenmethode_simpel). The method is no different for structures subjected to bending and follows the same four steps. For beams, we can consider the deformations due to extension and bending separately.

The force method for structures subjected to bending is the same as for structures subjected to extension. When choosing a statically determinate system, there is another consideration in addition to preferring members that rotate about a fixed point: the statically determinate structure should be solvable using forget-me-nots. Those are not available for every situation, so avoid choosing a statically determinate structure for which no forget-me-nots can be identified.

There is also a special version of the force method: the 'hoekveranderingsvergelijkingen' method. This method always makes the structure statically determinate by adding hinges. The advantage is that the required rotations can be calculated very easily using forget-me-nots. However, suitable forget-me-nots are not available for every statically determinate structure formed in this way, and this approach does not always produce the simplest displacement pattern.

We will demonstrate the steps of the force method for a beam.

::::::{prf:example}
:nonumber: true
:label: sd_ben_0

```{figure-start} ./bending_data/Example.svg
---
align: center
figclass: sticky-margin
number:
source: bending_data/constructie.py
---

```

- $EI = \cfrac{16}{3} \ \rm{MNm^2}$
- $EA \gg EI $

```{figure-end}
```

::::::

1. Determine the degree of static indeterminacy.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_1

    For this example, we are interested in the internal force distribution, so we need to evaluate the degree of internal static indeterminacy. Because this is an open structure, the degree of external static indeterminacy is equal to the degree of internal static indeterminacy:

    ```{figure} ./bending_data/graad.svg
    ---
    align: center
    source: bending_data/graad.py
    number:
    ---
    
    ```

    There are 4 unknown forces and 3 equilibrium equations, so this structure is first-order internally statically indeterminate.

    ::::::

2. Transform the structure into a statically determinate system by removing supports, splitting the structure at a two-force member, or adding hinges. Add unknown statically indeterminate forces and deformation conditions for each support removed and each hinge added. Be careful not to transform the structure into a (partially) mechanism! Choose a statically determinate system that is easy to solve: preferably, members should not translate if they also rotate, and you should be able to identify applicable forget-me-nots.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_2

    There are many options; the most obvious ones are shown below:

    `````{tab-set}
    :sync-group: balk

    ````{tab-item} Release the vertical support at $\rm{A}$
    :sync: keybalk_1
    
    ```{figure} ./bending_data/optie2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    ````

    ````{tab-item} Release the vertical support at $\rm{B}$
    :sync: keybalk_2
    ```{figure} ./bending_data/optie3.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    ````

    ````{tab-item} Release the vertical support at $\rm{C}$
    :sync: keybalk_3

    ```{figure} ./bending_data/optie4.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    ````

    ````{tab-item} Add a hinge at $\rm{B}$
    :sync: keybalk_4
    
    ```{figure} ./bending_data/optie1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    If only hinges are added, this approach is called the 'hoekveranderingsvergelijkingen' method.
    ````

    `````

    For each of these options, we can sketch the deformations to choose the one with the simplest displacement pattern:

    `````{tab-set}
    :sync-group: balk

    ````{tab-item} Release the vertical support at $\rm{A}$
    :sync: keybalk_1
    
    ```{figure} ./bending_data/optie2_verplaatsingen.svg
    :align: center
    :number:
    :name: optie2_balk
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```

    The deformations of this structure can be calculated using the forget-me-not for a simply supported beam subjected to a moment, together with the forget-me-not for a cantilever beam subjected to a point load.

    To use the forget-me-not for the simply supported beam, we first need to calculate the internal moment at $\rm{B}$.

    ````

    ````{tab-item} Release the vertical support at $\rm{B}$
    :sync: keybalk_2
    ```{figure} ./bending_data/optie3_verplaatsingen.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    This option is not very convenient because no forget-me-nots are available for finding the displacement at $\rm{B}$ under these loads; there are no forget-me-nots for a simply supported beam subjected to a distributed load over only part of its span.
    ````

    ````{tab-item} Release the vertical support at $\rm{C}$
    :sync: keybalk_3

    ```{figure} ./bending_data/optie4_verplaatsingen.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```

    This option is similar to releasing the vertical support at $\rm{A}$.
    ````

    ````{tab-item} Add a hinge at $\rm{B}$
    :sync: keybalk_4
    
    ```{figure} ./bending_data/optie1_verplaatsingen.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    If only hinges are added, this approach is called the 'hoekveranderingsvergelijkingen' method. Here, we only need the forget-me-not for a simply supported beam subjected to a moment.
    
    The value of the moment is already given, so there is no need to calculate an internal moment. This makes it the simplest option.
    ````

    `````

    The last option is chosen.

    ::::::

3. Solve for the displacement in terms of the unknown indeterminate forces, as you would normally do for a statically determinate structure.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_4

    We have chosen the following statically determinate structure with the deformation condition $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) = \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) $:

    ```{figure-start} ./bending_data/SB-systeem.svg
    ---
    align: center
    figclass: sticky-margin
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ---
    
    ```
    
    - $EI = \cfrac{16}{3} \ \rm{MNm^2}$
    - $EA \gg EI $
    - $\varphi_{\rm{B}}^{\rm{AB}} = \varphi_{\rm{B}}^{\rm{BC}}$

    ```{figure-end}
    ```

    We can sketch the deformations caused by the distributed load on this statically determinate structure:

    ```{figure} ./bending_data/disp_q.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```

    Using forget-me-nots, the rotations can be evaluated directly without calculating internal forces:

    - $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) = \cfrac{4M_{\rm{B}}}{3EI} + \cfrac{1}{24}\cfrac{25 \cdot 4^3}{EI} =  \cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI}$
    - $\varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) = -\cfrac{2M_{\rm{B}}}{EI}$

    ::::::

4. Use the deformation conditions to solve for the statically indeterminate forces.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_5

    $$
    \begin{align*}
    \varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) &= \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) \\
    \cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI} &= -\cfrac{2M_{\rm{B}}}{EI} \\
    M_{\rm{B}} &= -20 \ \rm{kNm}
    \end{align*}
    $$

    Using forget-me-nots, the same standard beam formula can also be used to calculate the rotations and displacements:

    $$
    \varphi_{\rm{B}} = - \cfrac{2 \cdot -20}{\frac{16}{3} \cdot 10^3} = 0.0075 \ \rm{rad} (↺)
    $$

    $$
    w_{\rm{halverwege \, \rm{AB}}} = \cfrac{5}{384} \cfrac{25 \cdot 4^3}{\frac{16}{3} \cdot 10^3} - \cfrac{1}{16} \cfrac{20 \cdot 4^3}{\frac{16}{3} \cdot 10^3} = 0.011875 \, \rm{m}
    $$

    This can be drawn as follows:

    ```{figure} ./bending_data/disp.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```

    ::::::

## More examples
The general concept of the force method is covered in section 2.1. The force method for beams is covered in sections 2.2.1–2.2.4, and the more specific 'hoekveranderingsvergelijkingen' in section 3.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. The examples in section 3.1 are covered later.

## Lecture recording

This topic was presented in Dutch in [lesson 6 of CTB2210](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/7b2e3e8833384bb9b131fbde502a9c551d?sortBy=most-recent), from 0:19:00 to 0:43:10.

## Additional exercises

- The guided exercise on the next page is a first exercise to check your understanding
- For more practice, you can work on:
    - if you're a TU Delft student, the following [<img height="12px" src="/figures/ANS.svg" alt="ANS" class="no-zoomies"> Dutch exercises](https://ans.app/universities/1/courses/436978/assignments/1924250/go_to)
    - Exercises 2.1–2.14 and 2.23 in section 2.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.
    - Exercises 3.1–3.10 and 3.16–3.21 in section 3.4 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Answers are available on [this website for chapter 2](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/) and [here for chapter 3](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-3/).
