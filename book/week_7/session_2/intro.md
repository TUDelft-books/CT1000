```{index} Displacement method with statically indeterminate displacements; Class exercise
```

(lesson7.2)=
# Lesson October 15th

During today's lesson you'll work on a complex exercise on the topic of the Displacement method with statically determinate displacements. Please ask your questions regarding the [homework](homework7.2) as well!

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/verplaatsingenmethode/lesoefening.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_4

```
```` 

(verpl_gecorrigeerd)=
## Exercise 1

Gegeven is de volgende constructie:

:::::{margin}
::::{versionchanged} v2025.13.0
31-10-2025: aangepast afmetingen, stijfheden en belasting.
::::
:::::

```{figure} ./lesoefening_data/structure.svg
:align: center

Constructie, lijkend op het voorbeeld in hoofdstuk 4.3.1 uit het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`, $EI >> EA, EA = 25 \ \rm{kN}, EA_{\rm{BE}} = 125 \ \rm{kN}$
```

:::::{exercise}
:label: verpl_1_0
:nonumber: true

Wat is de graad van inwendig statisch onbepaaldheid?

```{h5p} https://tudelft.h5p.com/content/1292672317004902577/embed
```

:::::

:::::{exercise}
:label: verpl_1_1
:nonumber: true

Welke van de volgende statisch bepaalde systemen kan gebruikt worden voor toepassing van de verplaatsingenmethode?

```{h5p} https://tudelft.h5p.com/content/1292672294506274407/embed
```

:::::

:::::{margin}
::::{versionchanged} v2025.13.0
31-10-2025: antwoord $N_{\rm{F}}^{\rm{EF}}$ aangepast.
::::
:::::

:::::{exercise}
:label: verpl_1_2
:nonumber: true

Er wordt gekozen voor het volgende statisch bepaalde systeem inclusief evenwichtsvoorwaarde:

```{figure} ./lesoefening_data/stat_deter.svg
:align: center

Statisch bepaald systeem, $EI >> EA, EA = 25 \ \rm{kN}, EA_{\rm{BE}} = 125 \ \rm{kN}$
```

Los $N_{\rm{F}}^{\rm{CF}}$ en $N_{\rm{F}}^{\rm{EF}}$ op als functie van $w$.

Tip: als het lastig is om direct $N_{\rm{F}}^{\rm{EF}}$ als functie van $w$ op te lossen. Los dan eerst $w$ op als functie van $N_{\rm{F}}^{\rm{EF}}$ en schrijf die aan het eind om.

```{h5p} https://tudelft.h5p.com/content/1292672288753185597/embed
```

:::::

:::::{exercise}
:label: verpl_1_3
:nonumber: true

Los $w$ op met behulp van de evenwichtsvoorwaarde.

```{h5p} https://tudelft.h5p.com/content/1292672300743185617/embed
```

:::::

:::::{exercise}
:label: verpl_1_4
:nonumber: true

Los nu ook de krachtsverdeling op.

```{h5p} https://tudelft.h5p.com/content/1292672302845199397/embed
```

:::::

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/verplaatsingenmethode/lesoefening2.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_3

```
````

## Exercise 2

Gegeven is de volgende constructie:

```{figure} ./lesoefening_data/structure2.svg
:align: center

Constructie, $EI = 500 \ \rm{MNm^2}, EA = 20 \ \rm{MN}$
```

:::::{exercise}
:label: verpl_2_0
:nonumber: true

Wat is de graad van inwendig statisch onbepaaldheid?

```{h5p} https://tudelft.h5p.com/content/1292672317004902577/embed
```

:::::

:::::{exercise}
:label: verpl_2_1
:nonumber: true

Er wordt gekozen voor het volgende statisch bepaalde systeem inclusief evenwichtsvoorwaarde:

```{figure} ./lesoefening_data/SD.svg
:align: center

Statisch bepaald systeem, $EI = 500 \ \rm{MNm^2}, EA = 20 \ \rm{MN}$
```

Los $N_{\rm{D}}^{\rm{CD}}$ en $N_{\rm{D}}^{\rm{BD}}$ op als functie van $w_{\rm{D}}$.

```{h5p} https://tudelft.h5p.com/content/1292695434407103557/embed
```

:::::

:::::{exercise}
:label: verpl_2_3
:nonumber: true

Los $w_{\rm{D}}$ op met behulp van de evenwichtsvoorwaarde.

```{h5p} https://tudelft.h5p.com/content/1292695437737624837/embed
```

:::::

:::::{exercise}
:label: verpl_2_4
:nonumber: true

Los nu ook de krachtsverdeling op.

```{h5p} https://tudelft.h5p.com/content/1292695438255292327/embed
```

:::::