````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_vakwerk/instructie.html.

```
````

```{index} Force method; for truss structures
```

# Force method for truss structures

We previously treated the force method for [simple structures](krachtenmethode_simpel). We now discuss its application to more complex truss structures which require Williot to find the deformations. For a Williot diagram, it is useful to choose a statically determinate system that is easy to calculate: preferably, members should not translate if they also rotate. This situation will also occur in the example below.

::::::{prf:example}
:nonumber: true
:label: sd_ext_0

```{figure-start} ./extension_data/Example.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
---
```

- $EI \gg EA_{\rm{CD}}, EA_{\rm{BE}}$
- $EA_{\rm{ADE}} \gg EA_{\rm{CD}}, EA_{\rm{BE}}$

```{figure-end}
```

::::::

1. Determine the degree of static indeterminacy.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_1

    For this example, we are interested in the internal force distribution, so we need to evaluate the degree of internal static indeterminacy. Because this is an open structure, there is no difference between internal and external static indeterminacy:

    ```{figure} ./extension_data/uitwerking4.svg
    ---
    align: center
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    ---

    ```

    There are 10 unknown forces and 9 equilibrium equations, so this structure is first-order statically indeterminate.
    ::::::

2. Transform the structure into a statically determinate system by removing supports, splitting the structure at two-force members, or adding hinges: add the unknown statically indeterminate forces and deformation conditions for each support removed, each connection of a two-force member removed, and each hinge added. Be careful not to transform the structure into a (partially) mechanism! Choose a statically determinate system that is easy to calculate: preferably, members should rotate about a fixed point.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_2

    There are many options here, some of which are shown below:

    `````{tab-set}
    :sync-group: rek_williot

    ````{tab-item} Split the structure at a two-force member
    :sync: key1

    ```{figure} ./extension_data/option1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    ````

    ````{tab-item} Add a hinge
    :sync: key2

    ```{figure} ./extension_data/option2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    ````

    ````{tab-item} Release the horizontal displacement at a support
    :sync: key4
    ```{figure} ./extension_data/option3.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    ````

    ````{tab-item} Remove a vertical support
    :sync: key4

    ```{figure} ./extension_data/option4.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```
    ````
    `````

    For each of these, the deformed structure can be sketched so that the simplest possible displacement pattern can be selected:

    `````{tab-set}
    :sync-group: rek_williot

    ````{tab-item} Split the structure at a two-force member
    :sync: key1

    ```{figure} ./extension_data/verplaatsingen_1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    These deformations are fairly simple to solve: all members have a clear pivot point and do not translate.
    ````

    ````{tab-item} Add a hinge
    :sync: key2

    ```{figure} ./extension_data/verplaatsingen_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    These deformations are not as simple. The pivot point for $\rm{DE}$ is not immediately clear; this member both rotates and translates.

    ````

    ````{tab-item} Release the horizontal displacement at a support
    :sync: key4
    ```{figure} ./extension_data/verplaatsingen_3.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    These deformations are not as simple: $\rm{ADE}$ translates and rotates.

    ````

    ````{tab-item} Remove a vertical support
    :sync: key4

    ```{figure} ./extension_data/verplaatsingen_4.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    These deformations are simple: all members have a clear pivot point and do not translate.
    ````
    `````

    The last option is chosen.

    ::::::

3. Solve the displacement in terms of the unknown indeterminate forces as you would normally do for a statically determinate structure.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_4

    We have chosen the following statically determinate structure with deformation condition $w_{\rm{B}}\left( B_{\rm{v}} \right) = 0$:

    ```{hide-sticky-margin}
    ```
    ```{figure-start} ./extension_data/SD-struc.svg
    ---
    align: center
    number:
    figclass: sticky-margin
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    ---
    
    ```

    - $EI \gg EA_{\rm{CD}}, EA_{\rm{BE}}$
    - $EA_{\rm{ADE}} \gg EA_{\rm{CD}}, EA_{\rm{BE}}$

    ```{figure-end}
    ```

    Because $\rm{AE}$ is infinitely stiff, all deformations result from members elongating or shortening. This follows from the earlier sketch of the deformed structure under the statically indeterminate force. The deformations caused by the distributed load can also be sketched:

    ```{figure} ./extension_data/verplaatsingen_4_2.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    number:
    ---
    
    ```
    
    To calculate the deformations, the normal forces can first be evaluated as functions of $B_{\rm{v}}$, for example using moment equilibrium about $\rm{A}$ for member $\rm{ADE}$:

    - $N_{\rm{CD}}\left( B_{\rm{v}} \right) = 210 - 2.5 B_{\rm{v}}$
    - $N_{\rm{BE}} \left( B_{\rm{v}} \right) = - B_{\rm{v}}$

    This leads to the following elongations of the members, using $\Delta L = \cfrac{N \ L}{EA}$:

    - $\Delta L_{\rm{CD}}\left( B_{\rm{v}} \right) = \cfrac{1400}{EA} - \cfrac{50 B_{\rm{v}}}{3 EA}$
    - $\Delta L_{\rm{BE}}\left( B_{\rm{v}} \right) = -\cfrac{5 B_{\rm{v}}}{EA}$

    This leads to the following displacement using a Williot diagram:

    ```{figure} ./extension_data/williot.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    number:
    ---
    
    ```

    This gives a displacement of $\rm{D}$ equal to $\cfrac{5}{4} \Delta L_{\rm{CD}} $.

    - $w_{\rm{D}}\left( B_{\rm{v}} \right) = \cfrac{1750}{EA} - \cfrac{125 B_{\rm{v}}}{6 EA} \left( \downarrow \right) $
    - $w_{\rm{E}}\left( B_{\rm{v}} \right) = 2 \cdot w_{\rm{D}} = \cfrac{3500}{EA} - \cfrac{125 B_{\rm{v}}}{3 EA} \left( \downarrow \right) $
    - $w_{\rm{B}}\left( B_{\rm{v}} \right) = w_{\rm{E}} + \Delta L_{\rm{BE}} = \cfrac{3500}{EA} - \cfrac{140 B_{\rm{v}}}{3 EA} \left( \downarrow \right) $

    ::::::

4. Use the deformation conditions to solve the statically indeterminate forces.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_5

    $$
    \begin{align*}
    w_{\rm{B}}\left( B_{\rm{v}} \right) &= 0 \\
    \cfrac{3500}{EA} - \cfrac{140 B_{\rm{v}}}{3 EA} &= 0 \\
    B_{\rm{v}} &= 75 \ \rm{kN}
    \end{align*}
    $$

    This leads to the following additional results:

    - $N_{\rm{CD}} = 22.5 \ \rm{kN}$
    - $N_{\rm{BE}} -75 \ \rm{kN} $
    - $w_{\rm{D}} = \cfrac{375000}{2 \cdot EA \, \left( \rm{in} \, \rm{N} \right)} \, \rm{mm} \, \left( \downarrow \right) $
    - $w_{\rm{E}} = \cfrac{375000}{EA \, \left( \rm{in} \, \rm{N} \right)} \, \rm{mm} \,  \left( \downarrow \right) $

    And the deformations to scale:
    
    ```{figure} ./extension_data/verplaatsingen.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    ::::::

## More examples

Chapter 2.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` treats the force method in general. Truss structures requiring a Williot diagram are specifically treated in chapter 2.2.10.

## Recording of same instruction

This topic was presented in Dutch in [lesson 7 of CTB2210](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/7c8045df2d0e4483a703a836fc273b2e1d?academicYear=2026-2027-ctb2210) from 0:03:50 to 0:53:10 (TU Delft login required).

## Exercises

- To check your understanding, you can work on exercises 2.40 and 2.41, in chapter 2.3 of the Dutch book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Answers are [available here](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).
