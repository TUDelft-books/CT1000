```{index} Force method; Class exercise for truss structures
```

(lesson5.1)=
# Lesson Monday September 28th

During today's lesson you'll work on an exercise on the topic of the force method for truss structures with and without the need for Williot. Please ask your questions regarding the [homework](homework5.1) as well!

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/krachtenmethode_vakwerk/lesoefeningen.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

```
```` 

## Exercise force method for truss structures without Williot

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/structure.svg
---
align: center
---
Constructie, $EA = 2.5 \ \rm{MN}, EI = \infty$
```

Bepaal de oplegreacties en het snedekrachtenlijnen. Je gaat dit doen voor drie verschillende statisch onbepaalde krachten.

:::::{exercise}
:label: km_vak_1_1
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292633373580570237/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_data/onbekenden.svg
---
align: center
---
Er zijn 22 onbekende krachten
```

```{figure} lesoefeningen_data/vergelijkingen.svg
---
align: center
---
Er zijn 21 evenwichtsvergelijkingen
```

Dus de constructie is 1ste graads statisch onbepaald

::::

:::::{exercise}
:label: km_vak_1_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292633398746509087/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

- Weghalen oplegging bij A
- Weghalen oplegging bij B
  - Inderdaad! Als je de hele oplegging weghaalt heb je een mechanisme wat naar links en rechts kan bewegen!
- Weghalen oplegging bij C
- Toevoegen scharnier bij B (in doorgaande liggen DBEG)
- Toevoegen scharnier bij E (in doorgaande liggen DBEG)
  - Inderdaad, als je hier een scharnier toevoegt krijg je een mechanisme waarbij EG om E kan draaien
- Splitsen constructie in pendelstaaf AD
- Splitsen constructie in pendelstaaf CE

::::

### Statisch onbepaalde kracht $B_{\rm{v}}$

:::::{exercise}
:label: km_vak_1_3
:nonumber: true

Neem als statisch onbepaalde kracht de verticale oplegreactie bij B (positief omhoog).

```{h5p} https://tudelft.h5p.com/content/1292634255950574927/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De vormveranderingsvoorwaarde is $w_B = 0$.

::::


:::::{exercise}
:label: km_vak_1_4
:nonumber: true

Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $B_{\rm{v}}$.

```{h5p} https://tudelft.h5p.com/content/1292634246594651717/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema1.svg
---
align: center
---

Vrijlichaamsschema $\rm{DG}$ met $B_{\rm{v}}$ als statisch onbepaalde.

```
De gebruikte vergelijkingen zijn:

$$ \sum  \left. T \right|  _ {\rm{E}} = 5 \cdot N_{\rm{AD}} - 2 \cdot B_{\rm{v}} - 3 \cdot26=0 $$ 
$$ \sum F_ {\rm{v}} = - N_{\rm{AD}} + B_{\rm{v}} + N_{\rm{CE}} -26= 0 $$
$$ w_{\rm{E}} = - \Delta l_{\rm{CE}} = \cfrac{-N_{\rm{CE}} \cdot l_{\rm{CE}}}{EA} $$
$$ w_{\rm{D}} = \Delta l_{\rm{AD}} = \cfrac{-N_{\rm{AD}} \cdot l_{\rm{AD}}}{EA} $$ 
$$ w_{\rm{B}} = w_{\rm{D}} + \cfrac{3}{5} \cdot \left( w_{\rm{E}} - w_{\rm{D}} \right) = \cfrac{3}{5} \cdot w_{\rm{E}} + \cfrac{2}{5} \cdot w_{\rm{D}} $$

Hieruit volgt:

$$ N_{\rm{AD}} = 0.4 \cdot B_{\rm{v}} + 15.6 $$
$$ N_{\rm{CE}} = - 0.6 \cdot B_{\rm{v}} + 41.6 $$
$$ w_{\rm{E}} = 0.0006 \cdot B_{\rm{v}} - 0.0416 $$
$$ w_{\rm{E}} = 0.0004 \cdot B_{\rm{v}} - 0.0156 $$
$$ w_{\rm{B}} = 0.00052 \cdot B_{\rm{v}} - 0.01872 $$

::::


:::::{exercise}
:label: km_vak_1_5
:nonumber: true

Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $B_{\rm{v}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292634259801752997/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Oplossen van de vergelijkingen geeft:

$$ B_{\rm{v}} = 36 \rm{kN} $$
$$ N_{\rm{AD}} = 30 \rm{kN} $$
$$ N_{\rm{CE}} = 20 \rm{kN} $$
$$ w_{\rm{E}} = -2 \rm{cm} $$
$$ w_{\rm{D}} = 3 \rm{cm} $$
$$ w_{\rm{B}} = 0 $$

::::

### Statisch onbepaald moment $M_{\rm{B}}$

:::::{exercise}
:label: km_vak_1_6
:nonumber: true

Neem als statisch onbepaalde kracht het moment $M_{\rm{B}}$ (positief zorgt voor trek aan de onderkant).

```{h5p} https://tudelft.h5p.com/content/1292634286050413117/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De vormveranderingsvoorwaarde is: 

$$ \varphi _ {\rm{B}} ^ {\rm{BD}} = \varphi _ {\rm{{B}}} ^ {\rm{BE}} $$

::::

:::::{exercise}
:label: km_vak_1_7
:nonumber: true

Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $M_{\rm{B}}$.

```{h5p} https://tudelft.h5p.com/content/1292634293341890027/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema2.svg
---
align: center
---
Constructie vrijgemaakt van pendelstaven met $M_{\rm{B}}$ als statisch onbepaalde. 
```

De gebruikte vergelijkingen zijn:

$$ \sum  \left. M \right| _ {\rm{B}} ^{\rm{BD}} = 3 \cdot N_{\rm{AD}} + M_{\rm{B}} =0 $$ 
$$ \sum  \left. M \right| _ {\rm{B}} ^{\rm{BG}} = - M_{\rm{B}} + 2 \cdot N_{\rm{CE}} - 5 \cdot26=0 $$ 
$$ \varphi _ {\rm{B}} ^{\rm{DB}} = \cfrac{w_{\rm{D}}}{3} $$
$$ \varphi _ {\rm{B}} ^{\rm{BE}} = \cfrac{w_{\rm{E}}}{2} $$

Hieruit volgt:

$$ N_{\rm{AD}} = -0.33 \cdot M_{\rm{B}}$$
$$ N_{\rm{CE}} = 0.5 \cdot M_{\rm{B}} + 65 $$
$$ \varphi _ {\rm{B}} ^{\rm{DB}} = -0.00011 \cdot M_{\rm{B}} $$
$$ \varphi _ {\rm{B}} ^{\rm{BE}} = 0.00025 \cdot M_{\rm{B}} + 0.0325 $$

::::


:::::{exercise}
:label: km_vak_1_8
:nonumber: true

Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $M_{\rm{B}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292634306404351337/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Oplossen van de vergelijkingen geeft:

$$ N_{\rm{AD}} = 30 \rm{kN} $$
$$ N_{\rm{CE}} = 20 \rm{kN} $$
$$ \varphi_{\rm{B}} = 0.01 \rm{rad} $$
$$ M_{\rm{B}} = -90 \rm{kNm} $$

::::

### Statisch onbepaalde normaalkracht $N_{\rm{AD}}$

:::::{exercise}
:label: km_vak_1_9
:nonumber: true

Neem als statisch onbepaalde kracht de normaalkracht $N_{\rm{AD}}$ door de pendelstaaf in het scharnier los te maken van de balk.

```{h5p} https://tudelft.h5p.com/content/1292634312901581657/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De vormveranderingsvoorwaarde is: 

$$ w _ {\rm{{D}}}^{\rm{AD}} = w _ {\rm{{D}}}^{\rm{BD}} $$

::::


:::::{exercise}
:label: km_vak_1_10
:nonumber: true

Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $N_{\rm{AD}}$.

```{h5p} https://tudelft.h5p.com/content/1292634315769955647/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema3.svg
---
align: center
---
Constructie met $N_{\rm{AD}}$ als statisch onbepaalde en vrijgemaakt van pendelstaaf CE. 
```

De gebruikte vergelijkingen zijn:

$$ \sum \left.  M \right| _ {\rm{B}} = 3 \cdot N_{\rm{AD}} + 2 \cdot N_{\rm{CE}} - 5 \cdot 26 = 0 $$ 
$$ w_{\rm{E}} = - \Delta l_{\rm{CE}} = \cfrac{-N_{\rm{CE}} \cdot l_{\rm{CE}}}{EA} $$
$$ w_{\rm{D}} ^ {\rm{AD}} = \Delta l_{\rm{AD}} = \cfrac{N_{\rm{AD}} \cdot l_{\rm{AD}}}{EA} $$ 
$$ w_{\rm{D}} ^ {\rm{BD}} = \varphi_{\rm{B}} \cdot 3 = - \cfrac{3}{2} w_{\rm{E}} $$

Hieruit volgt:

$$ N_{\rm{CE}} = - 1.5 \cdot N_{\rm{AD}} + 65 $$
$$ w_{\rm{E}} = 0.0015 \cdot N_{\rm{AD}} -0.065 $$
$$ w_{\rm{D}} ^{\rm{AD}} = 0.001 \cdot N_{\rm{AD}} $$
$$ w_{\rm{D}} ^{\rm{BD}} = -0.00225 \cdot N_{\rm{AD}} + 0.0975 $$

::::


:::::{exercise}
:label: km_vak_1_11
:nonumber: true

Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $N_{\rm{AD}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292634317462305007/embed
```

:::::


::::{admonition} Solution
:class: solution, dropdown

Oplossen van de vergelijkingen geeft:

$$ N_{\rm{AD}} = 30 \rm{kN} $$
$$ N_{\rm{CE}} = 20 \rm{kN} $$
$$ w_{\rm{E}} = -2 \rm{cm} $$
$$ w_{\rm{D}} = 3 \rm{cm} $$

::::

## Exercise force method for truss structures with Williot

Given the following structure.

```{figure} intro_data/structure.svg
:align: center
```

1. Find the normal force in element $\text{BC}$ and $\text{BE}$
2. Find the displacement of joint $\text{E}$

````{admonition} Solution assignment 1
:class: tip, dropdown

$N_\text{BE} \approx 3.074 \text{ kN}$

$N_\text{BC} \approx 2.273 \text{ kN}$

````

````{admonition} Solution assignment 2
:class: tip, dropdown

$w_\text{E} \approx 6.147 \text{ mm}$ ↓

````
