```{index} Displacement method with degrees of freedom; Class exercise
```
```{index} Matrix method; Class exercise
```

(lesson7.3)=
# Lesson October 17th

During today's lesson you'll work on a complex exercise on the topic of the Displacement method with degrees of freedom and the matrid method. Please ask your questions regarding the [homework](homework7.3) as well!

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/verplaats2/lesoefening1.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1

```
````

# Exercise 1

Gegeven is de volgende constructie:

```{figure} lesoefening_data/constructie.svg
:align: center

Constructie, $EA = \cfrac{12.5}{7} \ \rm{MN}$
```

Waarvoor de horizontale en verticale verplaatsingen van scharnier $\rm{S}$ als vrijheidsgraden worden genomen, met positief naar rechts en naar beneden.

```{figure} lesoefening_data/displaced.svg
:align: center
```

:::::{exercise}
:label: verplaats2_1
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292696418426282527/embed
```

:::::

:::::{exercise}
:label: verplaats2_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292696398678085167/embed
```

:::::

:::::{exercise}
:label: verplaats2_3
:nonumber: true

Bepaal de normaalkrachten in de drie staven in de constructie als functie van de verplaatsingen $u_{\rm{S,h}}$ en $u_{\rm{S,v}}$.

```{h5p} https://tudelft.h5p.com/content/1292696401512703007/embed
```

:::::

:::::{exercise}
:label: verplaats2_4
:nonumber: true

Bepaal de waarde van de vrijheidsgraden $u_{\rm{S,h}}$ en $u_{\rm{S,v}}$.

```{h5p} https://tudelft.h5p.com/content/1292696421277079527/embed
```

:::::

:::::{exercise}
:label: verplaats2_5
:nonumber: true

Bepaal de normaalkrachten in de drie staven.

```{h5p} https://tudelft.h5p.com/content/1292696424454641397/embed
```

:::::

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/verplaats2/lesoefening2.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden_2

```
````

## Exercise 2


Gegeven is de volgende constructie:

```{figure} lesoefening2_data/structure.svg
:align: center

Constructie, $EI = \infty$
```

:::::{exercise}
:label: verplaats3_1
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292698940455607667/embed
```

:::::

De pendelstaven worden vervangen door veren, leidend tot de volgende constructie:

```{figure} lesoefening2_data/springs.svg
:align: center

Constructie met veren, $EI = \infty$
```

:::::{exercise}
:label: verplaats3_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292698941864978077/embed
```

:::::

:::::{exercise}
:label: verplaats3_3
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292698958152327607/embed
```

:::::

:::::{exercise}
:label: verplaats3_4
:nonumber: true

Er wordt gekozen voor de volgende vrijheidsgraden: $w_{\rm{A}}$ en $\varphi$:

```{figure} lesoefening2_data/dof.svg
:align: center

Constructie met veren en vrijheidsgraden $w_{\rm{A}}$ en $\varphi$. $EI = \infty$
```

Bepaal de evenwichtsvergelijkingen

```{h5p} https://tudelft.h5p.com/content/1292698960957442047/embed
```

```{h5p} https://tudelft.h5p.com/content/1292698964473888827/embed
```

:::::

:::::{exercise}
:label: verplaats3_5
:nonumber: true

Bepaal met evenwicht $w_{\rm{A}}$ en $\varphi$.

```{h5p} https://tudelft.h5p.com/content/1292698966957649137/embed
```

:::::

:::::{exercise}
:label: verplaats3_6
:nonumber: true

Wat zijn de krachten in de veren?

```{h5p} https://tudelft.h5p.com/content/1292698967999474487/embed
```

:::::

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/matrix/lesoefening1.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/matrix_2

```
````

## Exercise 3

Gegeven is de volgende constructie:

```{figure} lesoefening1_data/constructie.svg
:align: center

Constructie, $EI = 4 \ \rm{MNm}^2, EA >> EI$
```

Gegeven is $\mathbf{u} = \begin{bmatrix} \varphi_{\rm{A}} & \varphi_{\rm{B}} & \varphi_{\rm{C}} & \varphi_{\rm{D}} & \varphi_{\rm{E}} \end{bmatrix}^T$.

:::::{exercise}
:label: matrix_1
:nonumber: true

Bepaal de elementstijfheidsmatrix $\mathbf{K}^{(e)}$ voor een willekeurig element.

```{h5p} https://tudelft.h5p.com/content/1292700774193421697/embed
```

:::::

:::::{exercise}
:label: matrix_2
:nonumber: true

Bepaal de globale stijfheidsmatrix $\mathbf{K}$.

```{h5p} https://tudelft.h5p.com/content/1292700781022982687/embed
```

:::::

:::::{exercise}
:label: matrix_3
:nonumber: true

Bepaal de krachtvector $\mathbf{F}$.

```{h5p} https://tudelft.h5p.com/content/1292700781680029277/embed
```

:::::

:::::{exercise}
:label: matrix_4
:nonumber: true

Bepaal de waarde van de vrijheidsgraden $\varphi_{\rm{B}}$, $\varphi_{\rm{C}}$, $\varphi_{\rm{D}}$ en $\varphi_{\rm{E}}$.

```{h5p} https://tudelft.h5p.com/content/1292700784091212317/embed
```

:::::