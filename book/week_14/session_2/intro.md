```{index} Shear stress torsion; Class exercise
```

% Source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/torsion_stress

(lesson14.2)=
# Lesson Tuesday

During today's lesson you'll work on a complex exercise on the topic of the Stresses due to torsion. Please ask your questions regarding the [homework](homework14.2) as well!

## Exercise Stresses due to torsion (in Dutch)

Gegeven is de volgende constructie en doorsnede

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/constructie.svg
:class: sticky-margin
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

De verdeelde belasting en oplegreacties grijpen aan in het normaalkrachtencentrum.

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/doorsnede.svg
:align: center
:class: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Deze doorsnede moet als dunwandige doorsnede worden beschouwd.

```{figure-end}
```

:::

::::

Gevraagd zijn de schuifspanningen ten gevolge van buiging en wringing op een positieve doorsnede in $\rm{B}$

:::::{exercise}
:label: TOZ_2
:nonumber: true

Wat is de locatie van het normaalkrachtencentrum in $y$-richting?
% Geef de coördinaten in het $y,z$-assenstelsel in $\rm{mm}$

:::::

::::{admonition} Oplossing
:class: solution, dropdown

$$\bar y_{\rm{N.C.}} = 75 \, \rm{mm}$$

::::

## Buiging

:::::{exercise}
:label: TOZ_3_5
:nonumber: true

De volgende vraag gaat over de absolute waarde van de maximale spanning in doorsnede $\rm{B}$ ten gevolge van buiging. Wat is de absolute waarde van het statisch moment van het afschuivende gedeelte voor deze maximale schuifspanning?

:::::

::::{admonition} Oplossing
:class: solution, dropdown

$$ S_z^{\rm{a}} = 135000 \, \rm{mm^3} $$

::::

:::::{exercise}
:label: TOZ_3
:nonumber: true

Wat is de absolute waarde van de maximale spanning in doorsnede $\rm{B}$ ten gevolge van buiging?
% Geef je antwoord in $\rm{MPa}$.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De maximale schuifspanning bevindt zich ter hoogte van het normaalkrachtencentrum in de verticale wanden:

```{figure} ./toz_data/verdeling.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```
$$\left| \tau \right| = 18.75 \, \rm{MPa}$$
::::

:::::{exercise}
:label: TOZ_4
:nonumber: true

Wat is/zijn de richting(en) van de maximale schuifspanning ten gevolge van alleen buiging op een positieve doorsnede in $\rm{B}$?

% kies één of meerdere antwoorden aan

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De dwarskracht werkt op een negatieve doorsnede omhoog, dus op een positieve doorsnede omlaag. Voor de eerder afgeleide spanningsverdeling moet de maximale schuifspanning dan ook naar beneden lopen

::::

## Wringing

:::::{exercise}
:label: TOZ_1
:nonumber: true

Gegeven zijn drie 2D-weergaves van de constructie. Welk model is de juiste om de snedekrachten en oplegreacties te bepalen?

::::{grid} 3
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Optie 1

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/optie2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Optie 2

```{figure-end}
```

:::

:::{grid-item}
:columns: auto

```{figure-start} ./toz_data/optie3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Optie 3

```{figure-end}
```

:::

::::

:::::

::::{admonition} Oplossing
:class: solution, dropdown

```{figure-start} ./toz_data/optie2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/TOZ_schuifspanningen
:number:
```

Optie 2

```{figure-end}
```

::::

:::::{exercise}
:label: TOZ_5
:nonumber: true

Wat is het wringend moment in $\rm{B}$?
% Geef je antwoord in $\rm{Nm}$. Ga uit van de standaard tekenafspraken.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

$$
M_{\rm{t,B}} = 2775.6 \, \rm{Nm}
$$

::::

:::::{exercise}
:label: TOZ_42
:nonumber: true


Wat is de absolute waarde van de maximale spanning in doorsnede $\rm{B}$ ten gevolge van wringing?
% Geef je antwoord in $\rm{MPa}$.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

$$ \tau = 96.375 \, \rm{MPa}$$

::::


:::::{exercise}
:label: TOZ_7
:nonumber: true

Wat is/zijn de richting(en) van de schuifspanning ten gevolge van alleen wringing op een positieve doorsnede in $\rm{B}$?

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Op een negatieve doorsnede werkt een negatief wringend moment, dus van $y$ naar $z$. Op een positieve doorsnede werkt dan ook een negatief wringend moment, van $z$ naar $y$. Deze werkt op alle uiterste randen van de wanden dus zowel omhoog, omlaag, naar links als naar rechts.

::::
