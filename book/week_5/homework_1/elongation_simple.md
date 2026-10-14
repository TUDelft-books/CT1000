````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_vakwerk/theorie.html.

```
```` 

```{index} Force method; for structures with elongation without need for Williot
```

(krachtenmethode_simpel)=
# Force method for structures with elongation without need for Williot

The force method is an approach used to analyse statically indeterminate structures. In this method, the structure is transformed into a statically determinate system with deformation conditions. Subsequently, the structure can be solved in the same way as for statically determinate structures. The force method always consists of the following steps:

::::::{prf:algorithm} Force method
:nonumber: true
:label: krachtenmethode_algoritme

1. Determine the degree of static indeterminacy.
2. Transform the structure into a statically determinate system by removing supports, splitting the structure at two-force members, or adding hinges: add the unknown statically indeterminate forces and deformation conditions for each support removed, each connection of a two-force member removed, and each hinge added. Be careful not to transform the structure into a (partially) mechanism!

    ```````{tab-set}
    ``````{tab-item} Remove a support

    `````{grid} 2
    :class-container: center-grid

    ````{grid-item}
    :columns: auto

    ```{figure} theorie_data/aanpas_1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    ```` 
    ````{grid-item}

    ```{figure-start} theorie_data/aanpas_1_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    $w_1 \left( N \right) = w_2 \left( N \right) \to N$
    
    ```{figure-end}
    ```

    ````
    `````
    :::{note}
    The direction of $w_1$ and $w_2$ is not necessarily the actual direction of displacement (in this case, $w_2$ would deform in the opposite direction). These arrows only indicate the positive direction so that the two can be set equal without a sign change.
    :::

    ``````
    ``````{tab-item} Split the structure at a two-force member

    `````{grid} 2
    :class-container: center-grid

    ````{grid-item}
    :columns: auto

    ```{figure} theorie_data/aanpas_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    ````
    ````{grid-item}

    ```{figure-start} theorie_data/aanpas_2_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    $$ w \left( B_{\rm{v}} \right) = 0 \to B_{\rm{v}}$$
    
    ```{figure-end}
    ```

    ````
    `````
    ``````
    ``````{tab-item} Add hinges
    `````{grid} 2
    :class-container: center-grid

    ````{grid-item}
    :columns: auto

    ```{figure} theorie_data/aanpas_3.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    ````
    ````{grid-item}

    ```{figure-start} theorie_data/aanpas_3_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    $\varphi_1 \left( M \right) = \varphi_2 \left( M \right) \to M$
    
    ```{figure-end}
    ```

    ````
    `````

    :::{note}
    The direction of $\varphi_1$ and $\varphi_2$ is not necessarily the actual direction of rotation (in this case, $\varphi_2$ would rotate in the opposite direction). These arrows only indicate the positive direction so that the two can be set equal without a sign change.
    :::
    
    ``````
    ```````
    
    There are usually several possibilities for doing this; choose the option that is easiest to calculate. Sketch the deformed structure caused by individual forces, including the statically indeterminate force.

3. Solve the displacement in terms of the unknown indeterminate forces as you would normally do for a statically determinate structure.
4. Use your deformation conditions to solve the statically indeterminate forces.

::::::

We discuss the application to structures evaluated only in axial deformation with the following example.

::::::{prf:example}
:nonumber: true
:label: sd_extsimpel_0

```{figure-start} ./theorie_data/constructie.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
number:
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

```{figure-end}
```

::::::

1. Determine the degree of static indeterminacy.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_1

    For this example, we are interested in the internal force distribution, so we need to evaluate the degree of internal static indeterminacy. However, this structure is open, so there is no difference between internal and external static indeterminacy:

    ```{figure} ./theorie_data/statisch_onbepaaldheid.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    number:
    ---
    
    ```

    There are 4 unknown forces and 3 equilibrium equations.

    This structure is therefore first-order internally statically indeterminate.

    ::::::

2. Transform the structure into a statically determinate system by removing supports, splitting the structure at a two-force member, or adding hinges: add the unknown statically indeterminate forces and deformation conditions for each support removed and each hinge added. Be careful not to transform the structure into a (partially) mechanism!

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_2

    There are several options here, some of which are shown below:

    ::::{grid} 3
    :class-container: center-grid

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie3.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::::

    The possible deformations of each structure can be sketched.
    
    ::::{grid} 3
    :class-container: center-grid

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verpl_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie2_verpl.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie3_verpl.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::::

    None of the options forms a mechanism, and all three options can be solved by considering axial deformations. The first option is chosen.

    ::::::

3. Solve the displacement in terms of the unknown indeterminate forces as you would normally do for a statically determinate structure.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_4

    We have chosen the following statically determinate structure with deformation condition $w_{\rm{B}}\left( B_{\rm{v}} \right) = 0$:

    ```{figure-start} ./theorie_data/SB-systeem.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    number:
    ---

    ```

    - $EA = 2.5 \ \rm{MN}$
    - $EI \gg EA$

    ```{figure-end}
    ```

    Without performing a calculation, we can sketch the displacements caused by the individual forces:

    ::::{grid} 2
    :class-container: center-grid

    :::{grid-item}

    The distributed load causes extension of the statically determinate structure:

    ```{figure} ./theorie_data/verpl_1.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}

    The statically indeterminate force causes shortening of the statically determinate structure, as was already sketched earlier:

    ```{figure} ./theorie_data/verpl_2.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::::

    To find the displacement of $\rm{B}$, the normal forces can first be evaluated as a function of $B_{\rm{v}}$ using vertical force equilibrium:

    - $N_{\rm{AC}}\left( B_{\rm{v}} \right) = - B_{\rm{v}} + 6 - 3 \cdot x $
    - $N_{\rm{BC}} \left( B_{\rm{v}} \right) = - B_{\rm{v}}$

    This leads to the following elongations of the members, using $\Delta L = \cfrac{N \ L}{EA}$ and the general expression $\Delta L = \int\limits_L {\cfrac{N\left(x\right)}{EA} dx}$:
    - $\Delta L_{\rm{AC}}\left( B_{\rm{v}} \right) = - \cfrac{B_{\rm{v}} \cdot 2}{2500} + \cfrac{6 \cdot 2}{2500} - \int\limits_0^2 {\cfrac{ 3 \cdot x}{2500}dx} = - \cfrac{B_{\rm{v}}}{1250} + \cfrac{3}{1250} $
    - $\Delta L_{\rm{BC}}\left( B_{\rm{v}} \right) = -\cfrac{B_{\rm{v}}}{1250}$

    This leads to a displacement of:

    - $w_{\rm{C}}\left( B_{\rm{v}} \right) = \cfrac{B_{\rm{v}}}{1250} - \cfrac{3}{1250}  $
    - $w_{\rm{B}}\left( B_{\rm{v}} \right) = \cfrac{B_{\rm{v}}}{625} - \cfrac{3}{1250} $

    ::::::

4. Use the deformation conditions to solve the statically indeterminate forces.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_5

    $$
    \begin{align*}
    w_{\rm{B}}\left( B_{\rm{v}} \right) &= 0 \\
    \cfrac{B_{\rm{v}}}{625} - \cfrac{3}{1250} &= 0 \\
    B_{\rm{v}} &= 1.5 \ \rm{kN}
    \end{align*}
    $$

    This leads to the following additional results:

    ```{figure} ./theorie_data/Nlijn.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    $w_{\rm{C}} = 1.2 \ \rm{mm} \left( \downarrow \right) $

    This gives the following deformed structure (to scale):
    
    ```{figure} ./theorie_data/vervormde_constructie.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```
    
    ::::::

## More examples

In chapter 2.1 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`, the force method is treated in general. Specifically, simple truss structures are discussed in sections 2.2.8 - 2.2.9.

## Recording of same instruction

This topic was presented in Dutch in [lesson 6 of CTB2210](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/a90a221aabd741c78bb41c42298d5af41d?academicYear=2026-2027-ctb2210) from 0:05:00 to 0:48:40 (TU Delft login required).

## Exercises

- The guided exercise on the next page is a first exercise to check your understanding
- For more practice, you can work on:
  - if you're a TU Delft student, the following two [<img height="12px" src="/figures/ANS.svg" alt="ANS" class="no-zoomies"> Dutch exercises](https://ans.app/universities/1/courses/436978/assignments/1909859/go_to)
  - exercises 2.31 - 2.39 in chapter 2.3 of the Dutch book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Answers are [available here](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).
