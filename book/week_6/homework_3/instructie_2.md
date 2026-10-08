````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/krachtenmethode_rek_raamwerk/instructie.html

```
```` 

```{index} Force method; for frame structures including extension
```

# Apply force method for frame structures which include extension

So far, we have studied statically indeterminate structures subjected either to extension or to bending. In this lesson, we consider structures subjected to both extension and bending. We use the force method to calculate the displacements and internal forces. The approach is the same for these structures, although the displacements can be somewhat more complex. We will demonstrate the method using the following example.

::::::{prf:example}
:nonumber: true
:label: rek_raam_0

% https://oit.tudelft.nl/CTB2210/2025/TOZ/opgave.html

```{figure-start} ./instructie_data/constructie.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
number:
---

```

- $EI = 64 \ \rm{MNm^2}$
- $EA = 4 \ \rm{MN}$

```{figure-end}
```

::::::

1. Determine the degree of static indeterminacy.

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_1

    ```{figure} instructie_data/SB1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    :number:
    ```

    There are 7 unknown support reactions and 6 unknown member forces. This gives a degree of external static indeterminacy of 1. Because this structure is open, its degree of internal static indeterminacy is also 1.

    ::::::

2. Transform the structure into a statically determinate system by removing supports, splitting the structure at a two-force member, or adding hinges. Add unknown statically indeterminate forces and deformation conditions for each support removed and each hinge added. Be careful not to transform the structure into a (partially) mechanism! Choose a statically determinate system that is easy to solve: preferably, members should not translate if they also rotate, and you should be able to identify forget-me-nots for the system.

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_2

    There are many options; some of them are shown below:

    `````{tab-set}
    :sync-group: raamwerk

    ````{tab-item} Replace the fixed support at $\rm{A}$ with a pin support
    :sync: keyraamrek_1
    ```{figure-start} ./instructie_data/optie1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $ \varphi_{\rm{A}} = 0 $

    ```{figure-end}
    ```
    ````
    ````{tab-item} Split member $\rm{BD}$
    :sync: keyraamrek_2
    ```{figure-start} ./instructie_data/optie2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $ w_{\rm{D}}^{\rm{BD}} = w_{\rm{D}}^{\rm{BD}}$

    ```{figure-end}
    ```

    ````
    ````{tab-item} Split member $\rm{CG}$
    ```{figure} ./instructie_data/optie3.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    This structure is a mechanism, so it is not a suitable statically determinate system.
    ````
    ````{tab-item} Add a hinge between $\rm{A}$ and $\rm{D}$
    :sync: keyraamrek_4
    ```{figure-start} ./instructie_data/optie4.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $\varphi_{\rm{S}}^{\rm{AS}} = \varphi_{\rm{S}}^{\rm{SD}}$

    ```{figure-end}
    ```
    ````
    ````{tab-item} Add a hinge between $\rm{D}$ and $\rm{E}$
    ```{figure} ./instructie_data/optie5.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    This structure is a mechanism, so it is not a suitable statically determinate system.
    ````
    ````{tab-item} Add a hinge between $\rm{E}$ and $\rm{G}$
    ```{figure} ./instructie_data/optie6.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    This structure is a mechanism, so it is not a suitable statically determinate system.
    ````
    ````{tab-item} Replace the pin support at $\rm{C}$ with a vertical roller support
    ```{figure} ./instructie_data/optie7.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    This structure is a mechanism, so it is not a suitable statically determinate system.
    ````
    ````{tab-item} Replace the pin support at $\rm{B}$ with a vertical roller support
    :sync: keyraamrek_8
    ```{figure-start} ./instructie_data/optie8.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $w_{\rm{B}} = 0$

    ```{figure-end}
    ```

    ````
    `````

    For each option that is not a mechanism, we can sketch the displacements caused by both the statically indeterminate force and the existing load, and choose the one with the simplest displacement pattern:

    ```````{tab-set}
    :sync-group: raamwerk

    ``````{tab-item} Replace the fixed support at $\rm{A}$ with a pin support
    :sync: keyraamrek_1

    ```{figure} ./instructie_data/optie1_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    The displacement pattern caused by only the moment at $\rm{A}$ is relatively straightforward. The right-hand part undergoes only rigid-body rotation and does not affect the rotation at $\rm{A}$. The left beam can be analysed using the forget-me-not for a simply supported beam with a moment at each end, together with the rigid-body rotation about the fixed point $\rm{A}$. Each of these three effects contributes to the rotation at $\rm{A}$.

    ```{figure} ./instructie_data/optie1_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Under the point load as well, the displacements of the right-hand part do not affect those of the left-hand part. The load does cause extension of $\rm{BD}$ and bending of $\rm{AD}$, both of which contribute to the rotation at $\rm{A}$.

    ``````

    ``````{tab-item} Split member $\rm{BD}$
    :sync: keyraamrek_2


    ```{figure} ./instructie_data/optie2_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    The displacement pattern caused by only the axial force in the split two-force member is relatively straightforward. $\rm{BD}$ only extends, and $\rm{AD}$ can be analysed as a cantilever beam with a force at end $\rm{D}$. The right-hand part undergoes only rigid-body rotation and does not affect the deflection at $\rm{D}$.

    ```{figure} ./instructie_data/optie2_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Under the point load as well, the displacements of the right-hand part do not affect those of the left-hand part. The load does cause bending of $\rm{AE}$ and therefore a displacement at $\rm{D}$.


    ``````

    ``````{tab-item} Add a hinge between $\rm{A}$ and $\rm{D}$
    :sync: keyraamrek_4

    ```{figure} ./instructie_data/optie3_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    This displacement pattern is quite complex, even when considering only the deformations caused by the moment pair. The vertical displacement of the new hinge between $\rm{A}$ and $\rm{D}$ affects the rotations about the hinge, but calculating it also requires finding the shear force at the new hinge. In addition, $\rm{BD}$ will extend. The members to the right of $\rm{D}$ are unloaded. The right-hand part undergoes only rigid-body rotation and does not affect the rotations at the new hinge.

    ```{figure} ./instructie_data/optie3_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    The displacement pattern to the left of $\rm{E}$ is also complex under only the $84 \ \rm{kN}$ point load, although it is somewhat simpler than under the statically indeterminate moment pair. Again, the displacements of the right-hand part do not affect those of the left-hand part, but the right-hand part does cause a shear force and moment at $\rm{D}$, resulting in similarly complex rotations at the hinge.
    ``````

    ``````{tab-item} Replace the pin support at $\rm{B}$ with a vertical roller support
    :sync: keyraamrek_2


    ```{figure} ./instructie_data/optie4_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    This option is very similar to splitting $\rm{BD}$. The force is assumed to act in the opposite direction, but the approach is the same: $\rm{AD}$ can be analysed as a cantilever beam with a force at its end, causing a deflection at $\rm{B}$ when the shortening of $\rm{BD}$ is also taken into account. Considering only the statically indeterminate force $\B_{\rm{v}}$, the right-hand part undergoes only rigid-body rotation and does not affect the deflection at $\rm{B}$.

    ```{figure} ./instructie_data/optie4_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    When considering only the $84 \ \rm{kN}$ point load, the displacements of the part to the right of $\rm{D}$ do not affect the displacement at $\rm{B}$. However, they do cause a shear force and moment at $\rm{D}$, which make $\rm{B}$ deflect.


    ``````

    ```````

    The last option is chosen.

    ::::::

3. Solve for the displacement in terms of the unknown statically indeterminate forces, as you would normally do for a statically determinate structure.

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_3

    ```{figure-start} ./instructie_data/stat_bepaald.svg
    ---
    align: center
    figclass: sticky-margin
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ---

    ```
    
    - $EA = 4 \ \rm{MN}$
    - $EI = 64 \ \rm{MNm^2}$

    ```{figure-end}
    ```

    To find the displacement at $\rm{B}$, we first need to determine the internal forces at $\rm{D}$, from which we can find the deflection at $\rm{D}$. We can then determine the displacement at $\rm{B}$.

    First, determine the axial force in $\rm{BD}$ as a function of $B_{\rm{v}}$:

    ```{figure} instructie_data/BD.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    \sum F_{\rm{v}}^{\rm{BD}} &= 0 \\
    B_{\rm{v}} + N_{\rm{BD}}&= 0 \\
    N_{\rm{BD}} &= -B_{\rm{v}}
    \end{align}
    $$

    We can also determine the axial force in $\rm{CG}$:

    ```{figure} instructie_data/EG.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    \sum \left. T \right|_{\rm{E}}^{\rm{EG}} &= 0 \\
    84 \cdot 4 - N_{\rm{CG}} \cdot 8 &= 0 \\
    N_{\rm{CG}} &= 42 \ \rm{kN}
    \end{align}
    $$

    We can then determine the shear force and bending moment just to the left of $\rm{D}$:

    ```{figure} instructie_data/DG.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    \sum F_{\rm{v}}^{\rm{DG}} &= 0 \\
    V_{\rm{D}}^{\rm{AD}}-B_{\rm{v}} - 84 + 42 &= 0 \\
    V_{\rm{D}}^{\rm{AD}} &= B_{\rm{v}} + 42
    \end{align}
    $$

    $$
    \begin{align}
    \sum \left. T \right|_{\rm{D}}^{\rm{DG}} &= 0 \\
    M_{\rm{D}} + 84 \cdot 8 - 42 \cdot 12 &= 0 \\
    M_{\rm{D}} &= -168 \ \rm{kNm}
    \end{align}
    $$
    
    The displacement at $\rm{D}$ now follows from a forget-me-not:

    ```{figure} ./instructie_data/wAD.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    w_{\rm{D}} &= \cfrac{168 \cdot 4^2}{2 \cdot 64000} + \cfrac{\left( B_{\rm{v}} + 42 \right) \cdot 4^3}{3 \cdot 64000} \\
    w_{\rm{D}} &= \cfrac{1}{3000} \cdot B_{\rm{v}} + 0.035 \\
    w_{\rm{D}} & \approx 0.000333 \cdot B_{\rm{v}} + 0.035 \ (\downarrow)
    \end{align}
    $$

    The displacement at $\rm{B}$ can be found from the extension of a member due to axial forces:

    ```{figure} ./instructie_data/BD2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    w_{\rm{B}} &= - w_{\rm{D}} + \Delta L_{\rm{BD}} \\
    w_{\rm{B}} &= - w_{\rm{D}} +  \cfrac{-B_{\rm{v}} \cdot 8}{4000} \\
    w_{\rm{B}} &= - \cfrac{7}{3000} \cdot B_{\rm{v}} - 0.035 \\
    w_{\rm{B}} & \approx 0.00233\cdot B_{\rm{v}} - 0.035 \\
    \end{align}
    $$

    ::::::

4. Use the deformation conditions to solve for the statically indeterminate forces.

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_4

    The deformation condition gives:

    $$
    \begin{align}
    w_{\rm{B}} &= 0 \\
    -\cfrac{7}{3000} \cdot B_{\rm{v}} - 0.035 &= 0 \\
    B_{\rm{v}} &= -15 \ \rm{kN}
    \end{align}
    $$

    ::::::

## Lecture recording

This topic was presented in Dutch in [lecture 10 of CTB2210](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/f6562fd68aa643d9ac4970b6a618cf111d?sortBy=most-recent), from 0:14:10 to 0:57:10.

## Additional exercises

- The guided exercises on the next two pages are a first exercise to check your understanding
- For more practice, you can work on:
  - Exercises 2.22 and 2.25–2.28 in section 2.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).
  - Exercises 2.22 and 2.25–2.28 in section 2.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Answers are available on [this website](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).
  - Question 1 of [the Dutch 2024 Structural Mechanics 3 exam](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/CM3_31januari_2024_tentamenopgaven.pdf). The solutions are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/CM3_31januari2024_uitwerkingen.pdf) {cite:p}`Exam_2024`.
  - Exam assignment 2 on statically indeterminate structures from [the 2024 Structural Mechanics exam](https://oit.tudelft.nl/CT1000/2024/week_15/session/intro.html#exam-assignment-2-statically-indeterminate-structures). The solutions are available on the same page {cite:p}`CT1000_2024`.
  - Exam assignment 3 on statically indeterminate structures from [the 2024 Structural Mechanics exam](https://oit.tudelft.nl/CT1000/2024/week_30/session/intro.html#exam-assignment-3-statically-indeterminate-structures). The solutions are available on the same page {cite:p}`CT1000_2024`.
  - Exam assignment on statically indeterminate structures from [the Dutch 2025 Structural Mechanics 3 exam](https://oit.tudelft.nl/CTB2210/2025/exam/exam.html). The solutions are available on the same page {cite:p}`CTB2210_2025`.
  - Exam assignment on statically indeterminate structures from [the Dutch 2025 Structural Mechanics 3 resit exam](https://oit.tudelft.nl/CTB2210/2025/exam2/lesson.html). The solutions are available on the same page {cite:p}`CTB2210_2025`.