
```{index} Displacement method
```

````{margin}
```{attributiongrey} Attribution
:class: attribution

This page is translated from https://oit.tudelft.nl/CTB2210/2026/verplaats2/theorie.html

```
````

# Apply displacement method

A major disadvantage of the force method is that the statically indeterminate structure must be modified into a statically determinate structure. This can sometimes be difficult. The displacement method does not require this. Instead of solving for a statically indeterminate force, we solve for one or more independent degrees of freedom that define the deformation of the structure.

::::::{prf:algorithm} Displacement method using degrees of freedom
:nonumber: true
:label: verplaatsingenmethode_algoritme_2

1. Choose one or more independent degrees of freedom that define the deformation of the structure, and split the structure into the part that deforms according to those degrees of freedom and the remaining parts. Choose the degrees of freedom so that:
    - The parts of the split structure are as easy as possible to analyse, preferably using forget-me-nots and member extensions. A broad set of forget-me-nots can be used, including cases for statically indeterminate structures and support settlements.
    - Together, the chosen degrees of freedom describe the deformation of the entire structure.
    - The degrees of freedom are independent: deformations caused by one degree of freedom do not also follow from one or more of the other degrees of freedom.
2. Calculate the forces at the split in terms of the unknown degrees of freedom. If you have defined multiple degrees of freedom, calculate the effect of each one separately, setting the other degrees of freedom to zero.
3. Use equilibrium conditions to solve for the degrees of freedom.

::::::

An example demonstrates how to apply this displacement method to a statically indeterminate structure.

::::::{prf:example}
:nonumber: true
:label: verplaats_2_0

```{figure} ./theorie_data/structure.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
number:
figclass: sticky-margin
---

```

::::::

1. Choose one or more independent degrees of freedom that define the deformation of the structure, and split the structure into the part that deforms according to those degrees of freedom and the remaining parts. Choose the degrees of freedom so that:
    - The parts of the split structure are as easy as possible to analyse, preferably using forget-me-nots and member extensions. A broad set of forget-me-nots can be used, including cases for statically indeterminate structures and support settlements.
    - Together, the chosen degrees of freedom describe the deformation of the entire structure.
    - The degrees of freedom are independent: deformations caused by one degree of freedom do not also follow from one or more of the other degrees of freedom.

    ::::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_1

    If we sketch the deformations of the entire structure:

    ```{figure} ./theorie_data/schets.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    number:
    ---
    ```

    we see that point $\rm{B}$ undergoes a displacement and a rotation. The displacement and rotation at $\rm{B}$ are sufficient to determine the displacement of the entire structure. The rotation at $\rm{C}$ then follows automatically.

    We can identify forget-me-nots in the deformations caused by the individual degrees of freedom and the applied load. The numbering corresponds to that used in the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

    :::::::{grid} 1
    :gutter: 1

    ::::::{grid-item-card} Rotation at $\rm{B}$
    
    The rotation at $\rm{B}$, without accounting for the displacement at $\rm{B}$, produces the following deformation:

    ```{figure} ./theorie_data/verplaats_1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    This can be represented by:

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto
    
    ```{figure-start} ./theorie_data/verplaats_1_VMN1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    :name: verplaats_1_VMN1
    ```

    This corresponds to forget-me-not (7).

    ```{figure-end}
    ```

    ::::

    ::::{grid-item}
    :columns: auto
    
    ```{figure-start} ./theorie_data/verplaats_1_VMN2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    :name: verplaats_1_VMN2
    ```

    This corresponds to forget-me-not (4), reflected horizontally and vertically.

    ```{figure-end}
    ```

    ::::
    
    :::::

    ::::::

    ::::::{grid-item-card} Displacement at $\rm{B}$
    :columns: 12

    The displacement at $\rm{B}$, without accounting for the rotation at $\rm{B}$, produces the following deformation:

    ```{figure} ./theorie_data/verplaats_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    This can be represented by:

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto
    
    ```{figure-start} ./theorie_data/verplaats_2_VMN1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    :name: verplaats_2_VMN1
    ```

    This corresponds to forget-me-not (g).

    ```{figure-end}
    ```

    ::::

    ::::{grid-item}
    :columns: auto
    
    ```{figure-start} ./theorie_data/verplaats_2_VMN2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    :name: verplaats_2_VMN2
    ```

    This corresponds to forget-me-not (4), reflected vertically, with the fixed support moved on the left instead of the roller support on the right.

    ```{figure-end}
    ```

    ::::
    
    :::::

    ::::::

    ::::::{grid-item-card} Displacement due to the $44.8 \ \rm{kN}$ point load
    :columns: 12

    The displacement due to the $44.8 \ \rm{kN}$ point load, with both degrees of freedom restrained, produces the following deformation:

    ```{figure} ./theorie_data/verplaats_3.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    The deformation of $\rm{BC}$ can be represented by:
    
    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure-start} ./theorie_data/verplaats_3_VMN.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    :name: verplaats_3_VMN
    ```

    This corresponds to forget-me-not (8).

    ```{figure-end}
    ```

    ::::
    :::::

    ::::::

    :::::::

    We therefore choose the displacement $w_{\rm{B}}$ and rotation $\varphi_{\rm{B}}$ at joint $\rm{B}$ as the independent degrees of freedom and split the structure at $\rm{B}$. These degrees of freedom prescribe the displacements at $\rm{B}$, and the remaining parts are separated there.

    ```{figure} ./theorie_data/splits.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    :figclass: sticky-margin
    ```

    ::::::::

2. Calculate the forces at the split in terms of the unknown degrees of freedom. If you have defined multiple degrees of freedom, calculate the effect of each one separately, setting the other degrees of freedom to zero.

    ::::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_2

    For each degree of freedom, calculate its effect on the internal forces at joint $\rm{B}$.

    :::::::{grid} 1
    :gutter: 1

    ::::::{grid-item-card} Rotation at $\rm{B}$ on segment $\rm{AB}$

    First, consider the effect of the rotation $\varphi_{\rm{B}}$ on segment $\rm{AB}$. The following forget-me-not applies:

    :::{fetch} {numref}`verplaats_1_VMN1`
    :::

    We need the external moment and support reaction as functions of the rotation. In our structure, these correspond to the internal moment and shear force at that end:

    ```{figure} ./theorie_data/VMN1_krachten.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    This gives:

    - $\varphi = \cfrac{1}{4} \cfrac{M_{\rm{B,1}} \cdot L}{EI} \to M_{\rm{B,1}} = \varphi_{\rm{B}} \cdot \cfrac{4EI}{L} = \varphi_{\rm{B}} \cdot \cfrac{4 \cdot 1500}{3} = 2000 \cdot \varphi_{\rm{B}}$
    - $V_{\rm{B,1}} = \cfrac{3}{2} \cfrac{M_{\rm{B,1}}}{L} = \cfrac{3}{2} \cdot \cfrac{2000 \cdot \varphi_{\rm{B}}}{3} = 1000 \cdot\varphi_{\rm{B}}$

    ::::::

    ::::::{grid-item-card} Displacement at $\rm{B}$ on segment $\rm{AB}$

    Next, consider the effect of the displacement $w_{\rm{B}}$ on segment $\rm{AB}$. The following forget-me-not applies:
      
    :::{fetch} {numref}`verplaats_2_VMN1`
    :::

    We need both support reactions at $\rm{B}$ as functions of the displacement. In our structure, these correspond to the internal moment and shear force at that end:

    ```{figure} ./theorie_data/VMN2_krachten.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    This gives:

    - $M_{\rm{B,2}} = \cfrac{6 \cdot EI}{L^2} \cdot w_{\rm{B}} = \cfrac{6 \cdot 1500}{3^2} \cdot w_{\rm{B}} = 1000 \cdot w_{\rm{B}}$
    - $V_{\rm{B,2}} = \cfrac{12 \cdot EI}{L^3} \cdot w_{\rm{B}} = \cfrac{12 \cdot 1500}{3^3} \cdot w_{\rm{B}} = \cfrac{2000}{3} \cdot w_{\rm{B}}$

    ::::::

    ::::::{grid-item-card} Rotation at $\rm{B}$ on segment $\rm{BC}$

    On the right-hand side, we begin with the effect of the rotation $\varphi_{\rm{B}}$ on segment $\rm{BC}$. The following forget-me-not applies:
      
    :::{fetch} {numref}`verplaats_1_VMN2`
    :::

    We need the external moment and support reaction as functions of the rotation. In our structure, these correspond to the internal moment and shear force at that end:

    ```{figure} ./theorie_data/VMN3_krachten.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    This gives:
    - $\varphi_{\rm{B}} = \cfrac{1}{3} \cfrac{M_{\rm{B,3}} \cdot L}{EI} \to M_{\rm{B,3}} = \varphi_{\rm{B}} \cdot \cfrac{3EI}{L} = \varphi_{\rm{B}} \cdot \cfrac{3 \cdot 3000}{3} = 3000 \cdot \varphi_{\rm{B}}$
    - $ \left. T \right|_{\rm{C}} = 0 \to V_{\rm{B,3}} = \cfrac{M_{\rm{B,3}}}{3} = 1000 \cdot \varphi_{\rm{B}}$

    ::::::
    
    ::::::{grid-item-card} Displacement at $\rm{B}$ on segment $\rm{AB}$

    Third, consider the effect of the displacement $w_{\rm{B}}$ on segment $\rm{AB}$. The following forget-me-not applies, giving internal forces in the directions shown:

    :::{fetch} {numref}`verplaats_2_VMN2`
    :::

    We need both support reactions at $\rm{B}$ as functions of the displacement. In our structure, these correspond to the internal moment and shear force at that end:

    ```{figure} ./theorie_data/VMN4_krachten.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    This gives:
    - $M_{\rm{B,4}} = \cfrac{3 \cdot EI}{L^2} \cdot w_{\rm{B}} = \cfrac{3 \cdot 3000}{3^2} \cdot w_{\rm{B}} = 1000 \cdot w_{\rm{B}}$
    - $V_{\rm{B,4}} = \cfrac{3 \cdot EI}{L^3} \cdot w_{\rm{B}} = \cfrac{3 \cdot 3000}{3^3} \cdot w_{\rm{B}} = \cfrac{1000}{3} \cdot w_{\rm{B}}$

    ::::::

    ::::::{grid-item-card} Effect of $44.8 \ \rm{kN}$ on segment $\rm{BC}$

    Finally, we must also account for the effect of the $44.8 \ \rm{kN}$ point load on segment $\rm{BC}$:

    :::{fetch} {numref}`verplaats_3_VMN`
    :::

    We need both support reactions at $\rm{B}$ as functions of the displacement. In our structure, these correspond to the internal moment and shear force at that end:

    ```{figure} ./theorie_data/VMN5_krachten.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    This gives:
    - $M_{\rm{B,5}} = \cfrac{3}{16} \cdot {F} \cdot L = \cfrac{3}{16} \cdot 44.8 \cdot 3 = 25.2 \ \rm{kNm}$
    - $V_{\rm{B,5}} = \cfrac{11}{16} \cdot {F} = \cfrac{11}{16} \cdot 44.8 = 30.8 \ \rm{kN}$

    ::::::

    :::::::
    
    ::::::::

3. Use equilibrium conditions to solve for the degrees of freedom.

    ::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_3

    Now that all internal forces at $\rm{B}$ are known, we can write the equilibrium conditions for joint $\rm{B}$:

     ```{figure} ./theorie_data/evenwicht_B.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    This gives:
    
    $$
    \begin{aligned}
    \Sigma M &= 0 \\
    -M_{\rm{B,1}} - M_{\rm{B,2}} - M_{\rm{B,3}} + M_{\rm{B,4}} - M_{\rm{B,5}} &= 0 \\
    5000 \varphi_{\rm{B}} + 25.2 &= 0 \\
    \varphi_{\rm{B}} &= -0.00504 \ \rm{rad}
    \end{aligned}
    $$

    and:

    $$
    \begin{aligned}
    \Sigma F_{\rm{v}} &= 0 \\
    -V_{\rm{B,1}} - V_{\rm{B,2}} + V_{\rm{B,3}} + V_{\rm{B,4}} - V_{\rm{B,5}} &= 0 \\
    1000 w_{\rm{B}} - 30.8 &= 0 \\
    w_{\rm{B}} &= 0.0308 \ \rm{m} = 30.8 \ \rm{mm}
    \end{aligned}
    $$

    ::::::

## More examples
This displacement method is covered in sections 4.1 and 4.3 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

## Lecture recording

This topic was presented in Dutch in [lecture 13 of CTB2210](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/05c3e6cf5ce24160aa99c3432c3a7a041d?sortBy=most-recent), from 0:11:00 to 0:57:45.

## Additional exercises
- The guided exercises on the next two pages are a first exercise to check your understanding
- For more practice:
  - Exercises 4.4–4.33, 4.35 and 4.36 in section 4.5 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Unfortunately, no answers are available. You can analyse the structures using MatrixFrame to check your answers.
  - Exercises 4.4–4.33, 4.35 and 4.36 in section 4.5 of the book Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Unfortunately, no solutions are available. You can analyse the structures using MatrixFrame to check your answers.
  - Question 3 of [the Dutch 2013 resit exam for Structural Mechanics 3](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/Opgaven_Apr2013.pdf). The solutions are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/Uitwerkingen_Apr2013.pdf) {cite:p}`Exam_jan_2013_2`.
  - Part 1 of Question 1 of [the Dutch 2016 resit exam for Structural Mechanics 3](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/Opgaven_Apr_2016.pdf). The solutions are available [here](https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/old_exams_CM3/Uitwerkingen_Apr2016.pdf) {cite:p}`Exam_jan_2016`.
