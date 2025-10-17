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

::::{solution} raam_1_1
:class: dropdown

- Met het koppel is het niet mogelijk verplaatsingen te berekenen.
- Er zijn geen vergeet-me-nietjes voor deze situatie.
  - Juist, de vorm van deze constructie als geheel én delen ervan zijn geen vergeet-me-nietjes. 
- Het is überhaupt niet mogelijk verplaatsingen te berekeningen.

::::

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

::::{solution} raam_1_2
:class: dropdown

$M _{\rm{C}} ^{\rm{BC}} \left( M _{\rm{C}} ^{\rm{AC}} \right) = M _{\rm{C}} ^{\rm{AC}} + 30$. 

::::

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

::::{solution} raam_1_3
:class: dropdown

Er is 1 statisch onbepaald moment, omdat de twee verschillende momenten van elkaar afhankelijk zijn door het momentenevenwicht van knoop C.  

::::

:::::{exercise}
:label: raam_1_4
:nonumber: true

Los de verplaatsingen van deze constructie uit als functie van $M_{\rm{C}}^{\rm{AC}}$ en $M_{\rm{C}}^{\rm{BC}}$

```{h5p} https://tudelft.h5p.com/content/1292652223605026557/embed
```

:::::

::::{solution} raam_1_4
:class: dropdown

De uitdrukkingen voor de hoekverdraaiingen kunnen worden gevonden met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel. 

$$ \varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = \cfrac{M_{\rm{C}}^{\rm{AC}} \cdot 6}{3 \cdot 2000} = 0.001 \cdot M_{\rm{C}}^{\rm{AC}} $$
$$ \varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}}^{\rm{BC}} \right) = - \cfrac{M_{\rm{C}}^{\rm{BC}} \cdot \sqrt{13}}{3 \cdot \cfrac{2000 \cdot \sqrt{13}}{3}} = -0.0005 \cdot M_{\rm{C}}^{\rm{BC}} $$

::::


:::::{exercise}
:label: raam_1_5
:nonumber: true

Los je vormveranderingsvoorwaarde op samen met je eerder opgestelde evenwichtsvergelijking om $M_{\rm{C}}^{\rm{AC}}$ en $M_{\rm{C}}^{\rm{BC}}$ te vinden.


```{h5p} https://tudelft.h5p.com/content/1292652234901684787/embed
```

:::::

::::{solution} raam_1_5
:class: dropdown

De vormveranderingsvoorwaarde is: $\varphi_{\rm{C}}^{\rm{AC}} = \varphi_{\rm{C}}^{\rm{BC}} \rightarrow 0.001 \cdot M_{\rm{C}}^{\rm{AC}} = -0.0005 \cdot M_{\rm{C}}^{\rm{BC}}$


Hieruit en uit de eerder opgestelde momentenevenwichtsvergelijking volgt: $M_{\rm{C}}^{\rm{AC}} = -10 \rm{kNm}$ en $M_{\rm{C}}^{\rm{BC}} = 20 \rm{kNm}$. 

::::


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

::::{solution} raam_2_1
:class: dropdown

```{figure} lesoefeningen_data/Onbekenden.svg
---
align: center
---
Er zijn 25 onbekende krachten
```

```{figure} lesoefeningen_data/Vergelijkingen.svg
---
align: center
---
Er zijn 22 evenwichtsvergelijkingen
```

Dus de constructie is 3de graads statisch onbepaald. 

::::

:::::{exercise}
:label: raam_2_2
:nonumber: true

Er zijn een aantal opties gegeven voor mogelijke statisch bepaalde systemen. De vormveranderingsvoorwaarden zijn niet getoond

```{h5p} https://tudelft.h5p.com/content/1292652255908105857/embed
```

:::::

::::{solution} raam_2_2
:class: dropdown

```{figure} lesoefeningen_data/Oplosmethode_optie1.svg
---
align: center
---
Juist
```

```{figure} lesoefeningen_data/Oplosmethode_optie2.svg
---
align: center
---
Onjuist
```

```{figure} lesoefeningen_data/Oplosmethode_optie3.svg
---
align: center
---
Juist
```

```{figure} lesoefeningen_data/Oplosmethode_optie4.svg
---
align: center
---
Juist
```

```{figure} lesoefeningen_data/Oplosmethode_optie5.svg
---
align: center
---
Onjuist
```

::::

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

::::{solution} raam_2_3
:class: dropdown

De uitdrukkingen voor de hoekverdraaiingen worden gevonden met behulp van de vergeet-mij-nietjes voor een ligger op twee steunpunten belast door een koppel en door een verdeelde belasting, de positieve richtingen worden genomen zoals in de figuur aangegeven. 

$$ \varphi_{\rm{D}}^{\rm{AD}} \left( M_{\rm{D}}\right) = \cfrac{M_{\rm{D}} \cdot 6}{3 \cdot \cfrac{1000}{3}} = 0.006 \cdot M_{\rm{D}} $$
$$ \varphi_{\rm{D}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}} \right) = - \cfrac{M_{\rm{D}} \cdot 8}{3 \cdot \cfrac{1000}{3}} - \cfrac{M_{\rm{B}}^{\rm{BD}} \cdot 8}{6 \cdot \cfrac{1000}{3}} = -0.008 \cdot  M_{\rm{D}} -0.004 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi_{\rm{B}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}} \right) = - \cfrac{M_{\rm{D}} \cdot 8}{6 \cdot \cfrac{1000}{3}} - \cfrac{M_{\rm{B}}^{\rm{BD}} \cdot 8}{3 \cdot \cfrac{1000}{3}} = -0.004 \cdot  M_{\rm{D}} -0.008 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}}^{\rm{AB}} \right) = \cfrac{M_{\rm{B}}^{\rm{AB}} \cdot 10}{3 \cdot \cfrac{1000}{3}} = 0.01 \cdot M_{\rm{B}}^{\rm{AB}} $$
$$ \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}}^{\rm{BC}} \right) = \cfrac{M_{\rm{B}}^{\rm{BC}} \cdot 6}{3 \cdot \cfrac{1000}{3}} + \cfrac{11 \cdot 6^3}{24 \cdot \cfrac{1000}{3}} = 0.006 \cdot M_{\rm{B}}^{\rm{BC}} + 0.297 $$

::::

:::::{exercise}
:label: raam_2_4
:nonumber: true

Er mist nog een vergelijking om de vier onbekenden (waarvan 3 statisch onbepaalden) op te lossen. Wat is die vergelijking?

```{h5p} https://tudelft.h5p.com/content/1292652280843962007/embed
```

:::::

::::{solution} raam_2_4
:class: dropdown

$M_{\rm{B}}^{\rm{BD}} - M_{\rm{B}}^{\rm{AB}} - M_{\rm{B}}^{\rm{BC}}  = 0$

::::

:::::{exercise}
:label: raam_2_5
:nonumber: true

Los met de vormveranderingsvoorwaarden en evenwichtsvergelijking de onbekenden $M_{\rm{D}}$, $M_{\rm{B}}^{\rm{BD}}$, $M_{\rm{B}}^{\rm{AB}}$ en $M_{\rm{B}}^{\rm{BC}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292652282254607197/embed
```

:::::

::::{solution} raam_2_5
:class: dropdown

Er zijn 4 onbekenden en 4 vergelijkingen. De vergelijkingen bestaan uit de momentenevenwichtsvergelijking uit de vorige deelvraag en de onderstaande vormveranderingsvoorwaarden:

$$ \varphi _ {\rm{B}} ^{\rm{BC}} = \varphi _ {\rm{B}} ^{\rm{AB}} \rightarrow 0.01 \cdot M_{\rm{B}}^{\rm{AB}} = 0.006 \cdot M_{\rm{B}}^{\rm{BC}} + 0.297 $$
$$ \varphi _ {\rm{B}} ^{\rm{AB}} = \varphi _ {\rm{B}} ^{\rm{BD}} \rightarrow 0.01 \cdot M_{\rm{B}}^{\rm{AB}} = -0.004 \cdot  M_{\rm{D}} -0.008 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi _ {\rm{D}} ^{\rm{AD}} = \varphi _ {\rm{D}} ^{\rm{BD}} \rightarrow  0.006 \cdot M_{\rm{D}} = -0.008 \cdot  M_{\rm{D}} -0.004 \cdot M_{\rm{B}}^{\rm{BD}} $$

Hieruit volgt:

$$ M_{\rm{D}} = 5 \rm{kNm} $$
$$ M_{\rm{B}}^{\rm{BD}} = -17.5 \rm{kNm} $$
$$ M_{\rm{B}}^{\rm{AB}} = 12 \rm{kNm} $$
$$ M_{\rm{B}}^{\rm{BC}} = -29.5 \rm{kNm} $$

::::

:::::{exercise}
:label: raam_2_6
:nonumber: true

Los de volledige krachtsverdeling op.

```{h5p} https://tudelft.h5p.com/content/1292652285215101017/embed
```

:::::

::::{solution} raam_2_6
:class: dropdown

$$ M_{\rm{A}} = 0 \rm{kNm} $$
$$ M_{\rm{halverwege} \ \rm{BC}} = 34.75 \rm{kNm} (◡) $$ 
$$ N_{\rm{BD}} \approx 0.83  \rm{kN} $$
$$ B_{\rm{v}} \approx 41.60 \rm{kN} $$

::::
