```{index} Shear force centre; Class exercise
```

(lesson13.3)=
# Lesson Thursday

During today's lesson you'll work on a complex exercise on the topic of the Shear force centre. Please ask your questions regarding the [homework](homework13.3) as well!

## Exercise Shear force centre (in Dutch)

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/shear_force_centre](https://oit.tudelft.nl/CTB1310/2025/exam/2026-06-24.html

Gegeven is de volgende constructie, doorsnede en schuifspanningsprofiel:

::::{grid} 3
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/SFC/SFC_Figure_1.jpg
---
align: center
width: 400px
---
De puntlast en oplegreacties grijpen aan in het dwarskrachtencentrum.
```

```

:::

:::{grid-item}
:columns: auto

```{figure-start} https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/SFC/SFC_Figure_2.jpg
:class: sticky-margin
:align: center
:number:
```

De doorsnede dient als dunwandig te worden beschouwd.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure} https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/SFC/SFC_Figure_3.jpg
:class: sticky-margin
:align: center
:number:

Schuifspanningsverdeling op positieve doorsnede
```

:::

::::

:::::{exercise}
:label: exam_2_2
:nonumber: true

Bepaal de locatie van het dwarskrachtencentrum.

:::::

:::::{admonition} Uitwerking
:class: solution, dropdown

Het dwarskrachtencentrum ligt vanwege symmetrie sowieso op een hoogte $\bar z = 0$. De locatie in de $y$-richting kan worden bepaald door werklijn van de resultante van de schuifspanningen te vinden.

Voor het berekenen van het totale moment van de spanningen wordt het middenpunt gekozen (waar de twee diagonale randen elkaar snijden). De spanningen in die diagonale randen hebben dus geen effect op het totale moment rondom dat punt. Daarom worden enkel de resultanten van de horizontale spanningen in de flenzen bepaald:

```{figure} https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/SFC/SFC_Figure_4.jpg
:align: center
:number:
```

$$ F_1 = 50 \cdot 12 \cdot 300 \cdot \frac{1}{2} = 90000 \, \rm{N} $$

Dit geeft:

```{figure} https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/SFC/SFC_Figure_5.jpg
:align: center
:number:
```

Dat statisch equivalent moet zijn aan de resultante van alle spanningen die gelijk is aan de dwarskracht:

```{figure} https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/SFC/SFC_Figure_6.jpg
:align: center
:number:
```

$$
\begin{align*}
\left. \sum T \right| _{\rm{midden}}^{\rm{spanningen}} &= \left. \sum T \right| _{\rm{middagen}}^{270 \, \rm{kN}}\\
90 \cdot 400 &= 270 \cdot y_{\rm{D.C.}} \\
y_{\rm{D.C.}} &= \cfrac{400}{3} \approx 133.33 \, \rm{mm}
\end{align*}
$$

Het dwarskrachtencentrum is daarmee bepaald:

```{figure} https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/raw/refs/heads/main/SFC/SFC_Figure_1.jpg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_shear_2
:number:
```

:::::

```{hide-sticky-margin}
```
