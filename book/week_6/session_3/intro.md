```{index} Force method; Class exercise for frame structures
```

(lesson6.3)=
# Lesson Friday October 10th

During today's lesson you'll work on a complex exercise on the topic of force method for frame structures. Please ask your questions regarding the [homework](homework6.2) as well!

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/krachtenmethode_raamwerk/lesoefeningen.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

```
```` 

## Oefening 1

Gegeven is de volgende 1ste graads statisch onbepaalde constructie:

```{figure} ./lesoefeningen_data/oefening_1.svg
:align: center

Constructie, $EI_{\rm{AC}} = 20000 \ \rm{kNm^2}, EI_{\rm{BC}} = \cfrac{2000 \sqrt{13}}{3} \ \rm{kNm^2}$
```

:::::{exercise}
:label: raam_1_1
:nonumber: true

Gegeven zijn de volgende statisch bepaalde systeem.

```{figure} ./lesoefeningen_data/statisch_bepaalde_systemen.svg
:align: center

Twee statisch bepaalde systemen
```

```{h5p} https://tudelft.h5p.com/content/1292652217804730007/embed
```

:::::

:::::{exercise}
:label: raam_1_2
:nonumber: true

Laten we de constructie oplossing met hoekveranderingsvergelijkingen, door een scharnier toe te voegen bij hoek $\rm{C}$. Daar werkt echter ook een uitwendig koppel. Het moment net links en onder $\rm{C}$ is dus niet gelijk aan elkaar. Als we het heel netjes zouden doen zouden we het scharnier net links of net onder het scharnier kunnen aanbrengen. Laten we de situatie bekijken met het scharnier net links van $\rm{C}$.

```{figure} ./lesoefeningen_data/scharnier_links_C.svg
:align: center

Statisch bepaald systeem met scharnier net links van $\rm{C}$
```

Gegeven is het vrijlichaamsschema van knoop $\rm{C}$:

```{figure} ./lesoefeningen_data/VLS_C_1.svg
:align: center

Vrijlichaamsschema van knoop $\rm{C}$ vergroot weergegeven
```

```{h5p} https://tudelft.h5p.com/content/1292652219570406177/embed
```

:::::

Om het gedoe met dat scharnier net links/net onder $\rm{C}$ te voorkomen kunnen we het scharnier ook direct in C plaatsen. Deze aanpak wordt aangeraden.

```{figure} ./lesoefeningen_data/scharnier_in_C.svg
:name: statisch_onbepaald_C
:align: center

Statisch bepaald systeem met scharnier in $\rm{C}$, $EI_{\rm{AC}} = 20000 \ \rm{kNm^2}, EI_{\rm{BC}} = \cfrac{2000 \sqrt{13}}{3} \ \rm{kNm^2}$
```

Nadeel van deze aanpak is dat de locatie van het scharnier niet meer match met de momenten in het vrijlichaamsschema. Echter is de situatie praktisch ongewijzigd. Merk op dat de richtingen van de momenten in het vrijlichaamsschema van $\rm{C}$ omgedraaid zijn ten opzichte van de momenten in het statisch bepaalde systeem:

```{figure} ./lesoefeningen_data/VLS_C_2.svg
:align: center

Vrijlichaamsschema van knoop $\rm{C}$ vergroot weergegeven
```

:::::{exercise}
:label: raam_1_3
:nonumber: true

Ga uit van [het statisch bepaalde systeem met het scharnier in $\rm{C}$](statisch_onbepaald_C)?

```{h5p} https://tudelft.h5p.com/content/1292652221281662937/embed
```

:::::

:::::{exercise}
:label: raam_1_4
:nonumber: true

Los de verplaatsingen van deze constructie uit als functie van $M_{\rm{C}}^{\rm{AC}}$ en $M_{\rm{C}}^{\rm{BC}}$

```{h5p} https://tudelft.h5p.com/content/1292652223605026557/embed
```

:::::

:::::{exercise}
:label: raam_1_5
:nonumber: true

Los je vormveranderingsvoorwaarde op samen met je eerder opgestelde evenwichtsvergelijking om $M_{\rm{C}}^{\rm{AC}}$ en $M_{\rm{C}}^{\rm{BC}}$ te vinden.


```{h5p} https://tudelft.h5p.com/content/1292652234901684787/embed
```

:::::

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/krachtenmethode_raamwerk/lesoefeningen_2.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

```
```` 


## Oefening 2

Gegeven is de volgende constructie:

```{figure} ./lesoefeningen_data/structure.svg
:align: center

Constructie, $EI = \cfrac{1000}{3} \ \rm{kNm^2}, EA >> EI $
```

:::::{exercise}
:label: raam_2_1
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292652260765673357/embed
```


:::::

:::::{exercise}
:label: raam_2_2
:nonumber: true

Er zijn een aantal opties gegeven voor mogelijke statisch bepaalde systemen. De vormveranderingsvoorwaarden zijn niet getoond

```{h5p} https://tudelft.h5p.com/content/1292652255908105857/embed
```

:::::

:::::{exercise}
:label: raam_2_3
:nonumber: true

Er wordt gekozen voor het volgende statisch bepaalde systeem inclusief vormveranderingsvoorwaarden:

```{figure} ./lesoefeningen_data/structure2.svg
:align: center

Statisch bepaald systeem, $EI = \cfrac{1000}{3} \ \rm{kNm^2}, EA >> EI $
```

Er is hier wederom een scharnier in een knoop geplaatst zoals ook in [het statisch bepaalde systeem van oefening 1](statisch_onbepaald_C). Bepaal de rotaties als functie van $M_{\rm{D}}$, $M_{\rm{B}}^{\rm{BD}}$, $M_{\rm{B}}^{\rm{AB}}$ en $M_{\rm{B}}^{\rm{BC}}$.

```{h5p} https://tudelft.h5p.com/content/1292652275086136557/embed
```

:::::

:::::{exercise}
:label: raam_2_4
:nonumber: true

Er mist nog een vergelijking om de vier onbekenden (waarvan 3 statisch onbepaalden) op te lossen. Wat is die vergelijking?

```{h5p} https://tudelft.h5p.com/content/1292652280843962007/embed
```

:::::

:::::{exercise}
:label: raam_2_5
:nonumber: true

Los met de vormveranderingsvoorwaarden en evenwichtsvergelijking de onbekenden $M_{\rm{D}}$, $M_{\rm{B}}^{\rm{BD}}$, $M_{\rm{B}}^{\rm{AB}}$ en $M_{\rm{B}}^{\rm{BC}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292652282254607197/embed
```

:::::

:::::{exercise}
:label: raam_2_6
:nonumber: true

Los de volledige krachtsverdeling op.

```{h5p} https://tudelft.h5p.com/content/1292652285215101017/embed
```

:::::
