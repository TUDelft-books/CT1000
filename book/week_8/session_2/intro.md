```{index} Support settlement; Class exercise
```
```{index} Stiffness influences; Class exercise
```


(lesson8.2)=
# Lesson October 23th

During today's lesson you'll work on an exercise on the topic of Stiffness influences and Support settlement. Please ask your questions regarding the [homework](homework8.2) as well!

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/steunpuntszetting_stijfheden/lesoefeningen.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpuntzetting

```
````

## Exercise Support settlement


Gegeven is de volgende constructie:

```{figure} ./lesoefeningen_data/structure2.svg
:align: center

Constructie, $EA = 15 \ \rm{MN}$
```

:::::{exercise}
:label: steun_1_1
:nonumber: true

Gegeven is de volgende uitwerking:

$N_{\rm{BD}} = \cfrac{90}{6000} \cdot 15000 = 225 \ \rm{kN}$

Evenwicht van knoop D levert:
- $ N_{\rm{AD}} = -281.25 \ \rm{kN}$
- $ N_{\rm{CD}} = -168.75 \ \rm{kN}$

Hieruit volgt:
- $\Delta L_{\rm{AD}} = \cfrac{-281.25 \cdot 7.5}{15000} = -0.109125 \ \rm{m}$
- $\Delta L_{\rm{CD}} = \cfrac{-168.75 \cdot 6}{15000} = - 0.0675 \ \rm{m}$

Met als resultaat:
- Horizontale verplaatsing van $\rm{D}$ van $67.5 \ \rm{mm}$ naar rechts
- Verticale verplaatsing van $\rm{D}$ van $109.125 \cdot \cfrac{4}{5} = 87.3 \ \rm{mm} $ naar beneden

```{h5p} https://tudelft.h5p.com/content/1292653910239346277/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

- De normaalkracht in $\rm{BD}$ is niet juist berekend
  - De verlenging van $\rm{BD}$ is niet enkel afhankelijk van de verplaatsing van knoop $\rm{B}$
- De normaalkrachten in $\rm{AD}$ en $\rm{CD}$ zijn niet juist berekend
- De verlengingen van de staven $\rm{AD}$ en $\rm{CD}$ zijn niet juist berekend
- De verplaatsing van knoop $\rm{D}$ is niet juist berekend
  - Om de verplaatsing van knoop $\rm{D}$ te berekenen dient Williot te worden gebruikt

::::

:::::{exercise}
:label: steun_1_2
:nonumber: true

Wat is de graad van statisch onbepaaldheid?

```{h5p} https://tudelft.h5p.com/content/1292653934022070767/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} ./lesoefeningen_data/Onbekenden.svg
:align: center

Er zijn 6 onbekende krachten. 
```

```{figure} ./lesoefeningen_data/Vergelijkingen.svg
:align: center

Er zijn 5 evenwichtsvergelijkingen. 
```

De constructie is 1ste graads inwendig statisch onbepaald. 

::::

:::::{exercise}
:label: steun_1_3
:nonumber: true

Gekozen is het volgende statisch bepaalde systeem met vormveranderingsvoorwaarde:

```{figure} ./lesoefeningen_data/statically_determinate2.svg
:align: center

Statisch bepaalde constructie, $EA = 15 \ \rm{MN}$
```

Er is gekozen voor dit systeem zodat we de steunpuntszetting in de vormveranderingsvoorwaarde mee kunnen nemen en niet mee hoeven te nemen in bepalen van krachtsverdeling.

Bepaal de krachtsverdeling en vervormingen als functie van $B_{\rm{v}}$. Het williot-diagram is gegeven (maar zou je zelf moeten kunnen tekenen).

```{h5p} https://tudelft.h5p.com/content/1292653940023500187/embed
```

```{figure} lesoefeningen_data/williot.svg
---
align: center
---
Williot diagram voor het bepalen van de verplaatsing van $\rm{D}$ en $\rm{B}$.
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De normaalkrachten in de staven AD en CD kunnen met behulp van het knoopevenwicht van $\rm{D}$ worden uitgedrukt in $B_{\rm{v}}$. 

$$ N_{\rm{BD}} = B_{\rm{v}} $$
$$ \sum F_{\rm{v}} = 0 \rightarrow N_{\rm{AD}} = - \cfrac{5}{4} \cdot B_{\rm{v}} $$
$$ \sum F_{\rm{h}} = 0 \rightarrow N_{\rm{CD}} = - \cfrac{3}{4} \cdot B_{\rm{v}} $$

Nu de normaalkrachten in de staven bekend zijn kan de verlenging/verkorting per staaf worden bepaald. De resultaten zijn weergegeven in de onderstaande tabel. 

| Staaf | $N\left(B_{\rm{v}}\right)$ (kN)| $\Delta L \left(B_{\rm{v}}\right)\rm{(mm)}$ |
| :-:|:-:|:-:|
|$\rm{AD}$|$-\cfrac{5}{4} \cdot B_{\rm{v}}$|$-\cfrac{5}{8} \cdot B_{\rm{v}}$|
|$\rm{BD}$|$B_{\rm{v}}$|$\cfrac{2}{5} \cdot B_{\rm{v}}$|
|$\rm{CD}$|$- \cfrac{3}{4} \cdot B_{\rm{v}}$|$-\cfrac{3}{10} \cdot B_{\rm{v}}$|

Met behulp van de berekende verlenging/verkorting kan het williot diagram worden getekend, zie de figuur hieronder. 

```{figure} lesoefeningen_data/williot.svg
---
align: center
---
Williot diagram voor het bepalen van de verplaatsing van $\rm{D}$ en $\rm{B}$.
```

Uit het williot diagram kan worden afgelezen:

$$ w_{D,\rm{h}} = 0.0003 \cdot B_{\rm{v}} \ \rm{m} \left(\rightarrow\right)$$
$$ w_{D,\rm{v}} \approx 0.001 \cdot B_{\rm{v}} \ \rm{m} \left(\downarrow\right)$$
$$ w_{B,\rm{h}} = 0 $$
$$ w_{B,\rm{v}} \approx 0.0014 \cdot B_{\rm{v}} \ \rm{m} \left(\downarrow\right)$$

::::

:::::{exercise}
:label: steun_1_4
:nonumber: true

Los met de vormveranderingsvoorwaarde de onbekende $B_{\rm{v}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292654002392449027/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De vormveranderingsvoorwaarde is: $w_{B,\rm{v}} = 1.4 \cdot B_{\rm{v}} = 90 \rm{mm}$.

Hieruit volgt: $B_{\rm{v}} = 64 \rm{kN}$

::::

:::::{exercise}
:label: steun_1_5
:nonumber: true

Los de volledige krachtsverdeling en verplaatsingen op.

```{h5p} https://tudelft.h5p.com/content/1292654005235840357/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De krachten en verplaatsingen kunnen worden opgelost uit de eerder opgestelde vergelijkingen door daar de berekende waarde voor $B_{\rm{v}}$ in in te vullen.

$$ N_{\rm{BD}}= 64 \rm{kN} $$
$$ N_{\rm{AD}}= -80 \rm{kN} $$
$$ N_{\rm{CD}}= -48 \rm{kN} $$
$$ w_{D,\rm{h}} = 19 \rm{mm} \left(\rightarrow\right)$$
$$ w_{D,\rm{v}} = 64 \rm{mm} \left(\downarrow\right)$$
$$ w_{B,\rm{h}} = 0 \rm{mm} $$
$$ w_{B,\rm{v}} = 90 \rm{mm} \left(\downarrow\right)$$

::::


````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/steunpuntszetting_stijfheden/lesoefeningen_2.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/stijfheid_steunpunt

```
````

## Exercise support settlement and stiffness influences

Gegeven is de volgende constructie:

```{figure} ./lesoefeningen_data/structure.svg
:align: center

Constructie, $EI = \cfrac{250}{3} \ \rm{MNm^2}$
```

:::::{exercise}
:label: steun_2_1
:nonumber: true

Wat is de graad van statisch onbepaaldheid?

```{h5p} https://tudelft.h5p.com/content/1292654698994250327/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De constructie is 2e graads inwendig statisch onbepaald. 

::::

:::::{exercise}
:label: steun_2_2
:nonumber: true

Voor het geval dat $nEI \to 0$, bepaal de krachtsverdeling en verplaatsingen:

```{h5p} https://tudelft.h5p.com/content/1292654700974801967/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Als deel $\rm{BC}$ geen buigstijfheid meer heeft ontstaan er feitelijk twee losse liggertjes waarvan de linker 25 $\rm{mm}$ zakt. Dit levert de onderstaande krachten en verplaatsingen:

$$A_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$$
$$B_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$$
$$C_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$$
$$D_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$$
$$M_{\rm{B}} \left( nEI \to 0 \right) = 0 \rm{kNm}$$
$$M_{\rm{D}} \left( nEI \to 0 \right) = 0 \rm{kNm}$$
$$w_{\rm{halverwege} \ \rm{AB}} \left( nEI \to 0 \right) = 25 \rm{mm}$$
$$w_{\rm{halverwege} \ \rm{CD}} \left( nEI \to 0 \right) = 0 \rm{mm}$$

::::


:::::{exercise}
:label: steun_2_3
:nonumber: true

Voor het geval dat $nEI \to \infty$, kies zelf een statisch bepaald systeem met vormveranderingsvoorwaardes en bepaal de krachtsverdeling:

```{h5p} https://tudelft.h5p.com/content/1292654703279142367/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Er wordt gekozen voor het onderstaande statisch bepaalde systeem, waarbij scharnieren en onbekende momentenparen zijn toegevoegd in $\rm{B}$ en $\rm{C}$. 

```{figure} ./lesoefeningen_data/SB_systeem1.svg
:align: center

Statisch bepaald systeem met onbekende momenten, $EI_{\rm{AB}} = EI_{\rm{CD}} = \cfrac{250}{3} \ \rm{MNm^2}, EI_{\rm{BC}} = \infty$
```

De bijbehorende vormveranderingsvoorwaarden zijn:

$$\varphi_{\rm{B}}^{\rm{AB}}=\varphi_{\rm{B}}^{\rm{BC}}$$
$$\varphi_{\rm{C}}^{\rm{BC}}=\varphi_{\rm{C}}^{\rm{CD}}$$

Omdat deel $\rm{BC}$ oneindig stijf is geldt: $\varphi_{\rm{B}}^{\rm{BC}}=\varphi_{\rm{C}}^{\rm{BC}}=\cfrac{25}{10000}=0.0025\rm{rad}$

Met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel wordt het volgende gevonden: $\varphi_{\rm{B}}^{\rm{AB}}=\cfrac{M_{\rm{B}}\cdot10}{3\cdot\cfrac{250}{3}\cdot1000} \rightarrow M_{\rm{B}}=62.5 \rm{kNm}$

Uit momentenevenwicht van deel $\rm{AB}$ volgt: $\sum \left. T \right| _ {\rm{B}} ^{\rm{AB}} = - A_{\rm{v}} \cdot 10 + 62.5=0 \rightarrow A_{\rm{v}} =6.25 \rm{kN}$

Uit symmetrie volgt: $M_{\rm{C}}=-M_{\rm{B}}=-62.5 \rm{kNm}$ en $D_{\rm{v}}=-A_{\rm{v}}=-6.25 \rm{kN}$

Met momentenevenwicht van de hele constructie kan nu worden bepaald dat $B_{\rm{v}}=-18.75 \rm{kN}$ en $C_{\rm{v}}=18.75 \rm{kN}$.  

De zakkingen in het midden van de delen $\rm{AB}$ en $\rm{CD}$ kunnen worden bepaald uit de superpositie van de vervorming door buiging en de zakking van de opleggingen. 

$$w_{\rm{halverwege} \ \rm{AB}} = 25 + \cfrac{62.5\cdot 10^2}{16\cdot\cfrac{250}{3}}=29.6875 \rm{mm}$$
$$w_{\rm{halverwege} \ \rm{CD}} = - \cfrac{62.5\cdot 10^2}{16\cdot\cfrac{250}{3}}=-4.6875 \rm{mm}$$

::::

:::::{exercise}
:label: steun_2_4
:nonumber: true

Voor het geval van variabele $n$ is het volgende statisch bepaalde systeem:

```{figure} ./lesoefeningen_data/SB.svg
:align: center

Constructie
```

```{h5p} https://tudelft.h5p.com/content/1292654763617550697/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De vormveranderingsvoorwaardes zijn:

$$w_{\rm{A}}=25 \rm{mm}$$
$$w_{\rm{D}}=0 \rm{mm}$$

::::

:::::{exercise}
:label: steun_2_5
:nonumber: true

Bepaal de krachtsverdeling en verplaatsingen als $A_{\rm{v}}$ en $D_{\rm{v}}$ gelijk zijn aan 0 en je de opgelegde zakking/vormveranderingsvoorwaarde voor $\rm{A}$ negeert.

```{h5p} https://tudelft.h5p.com/content/1292654762901470137/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Als $A_{\rm{v}}$ en $D_{\rm{v}}$ gelijk zijn aan 0 dan kan de constructie vrij vervormen en onstaat er geen buiging. Hieruit volgt:

$$ M_{\rm{B}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 0 \rm{kNm} $$
$$ M_{\rm{C}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 0 \rm{kNm} $$
$$ \varphi_{\rm{B}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 0.0025 \rm{rad} $$
$$ \varphi_{\rm{C}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 0.0025 \rm{rad} $$
$$ w_{\rm{A}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 50 \rm{mm} $$
$$ w_{\rm{D}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = -25 \rm{mm} $$

::::

:::::{exercise}
:label: steun_2_6
:nonumber: true

Bepaal de krachtsverdeling en verplaatsingen als functie van $A_{\rm{v}}$ en $D_{\rm{v}}$.

```{h5p} https://tudelft.h5p.com/content/1292654774240819917/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De momenten $M_{\rm{B}}$ en $M_{\rm{C}}$ kunnen worden bepaald door respectievelijk $A_{\rm{v}}$ en $D_{\rm{v}}$ te verplaatsen naar $\rm{B}$ en $\rm{C}$. 

$$M_{\rm{B}} = 10 \cdot A_{\rm{v}}$$
$$M_{\rm{C}} = 10 \cdot D_{\rm{v}}$$

De hoekverdraaiingen in $\rm{B}$ en $\rm{C}$ kunnen worden bepaald uit een superpositie van de vervorming door buiging en de vrije vervorming zoals in de vorige opgave berekend. Voor de vervorming door buiging wordt het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel gebruikt. 

$$ \varphi_{\rm{B}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = -\cfrac{10 \cdot A_{\rm{v}} \cdot 10}{3 \cdot \cfrac{250}{3} \cdot n\cdot 1000} - \cfrac{10 \cdot D_{\rm{v}} \cdot 10}{6 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + 0.0025 = -0.0004 \cdot \cfrac{A_{\rm{v}}}{n} -0.0002 \cdot \cfrac{D_{\rm{v}}}{n} + 0.0025 $$
$$ \varphi_{\rm{C}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = \cfrac{10 \cdot A_{\rm{v}} \cdot 10}{6 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + \cfrac{10 \cdot D_{\rm{v}} \cdot 10}{3 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + 0.0025 = 0.0002 \cdot \cfrac{A_{\rm{v}}}{n} + 0.0004 \cdot \cfrac{D_{\rm{v}}}{n} + 0.0025 $$

De zakkingen in $\rm{A}$ en $\rm{D}$ kunnen worden bepaald uit de superpositie van vrije vervorming van de constructie, vervorming door buiging van deel $\rm{BC}$ en vervorming door buiging van de delen $\rm{AB}$ en $\rm{CD}$. 

$$ w_{\rm{A}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = 0.05 + 10 \cdot \left( -0.0004 \cdot \cfrac{A_{\rm{v}}}{n} -0.0002 \cdot \cfrac{D_{\rm{v}}}{n} \right) - \cfrac{ A_{\rm{v}} \cdot 10^3}{3 \cdot \cfrac{250}{3} \cdot 1000} =-0.004  \cdot A_{\rm{v}} -0.004 \cdot \cfrac{A_{\rm{v}}}{n} -0.002 \cdot \cfrac{D_{\rm{v}}}{n} + 0.05 $$
$$ w_{\rm{D}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = -0.025 - 10 \cdot \left( 0.0002 \cdot \cfrac{A_{\rm{v}}}{n} + 0.0004 \cdot \cfrac{D_{\rm{v}}}{n} \right) - \cfrac{ D_{\rm{v}} \cdot 10^3}{3 \cdot \cfrac{250}{3} \cdot 1000} =-0.002 \cdot \cfrac{A_{\rm{v}}}{n} + -0.004 \cdot D_{\rm{v}} + -0.004\cdot \cfrac{D_{\rm{v}}}{n} -0.025 $$

::::

:::::{exercise}
:label: steun_2_7
:nonumber: true

Los met de vormveranderingsvoorwaardes de onbekende $A_{\rm{v}}$ en $D_{\rm{v}}$ op. Let op, dit is een lastige wiskundige exercitie. Je wordt aangeraden gebruik te maken van een tool zoals SymPy.


```{h5p} https://tudelft.h5p.com/content/1292654782286977977/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Oplossen van de vergelijkingen levert:

$$ A_{\rm{v}}= \cfrac{25 \cdot n}{4 \cdot n + 2} $$
$$ D_{\rm{v}}= -\cfrac{25 \cdot n}{4 \cdot n + 2} $$

Deze functies kunnen ook geplot worden:

```{figure} lesoefeningen_data/steunpuntszetting.svg
---
align: center
---
Oplegreacties als functie van $n$
```

::::
