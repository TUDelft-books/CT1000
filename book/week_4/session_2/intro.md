```{index} Displacements truss structures; Class exercise using constitutive equation
```

(lesson4.2)=
# Lesson Wednesday September 24th

During today's lesson you'll work on a complex exercise on the topic of Extension. Please ask your questions regarding the [homework](homework4.2) as well!

## Exercise Extension

Given the following structure.

```{figure} intro_data/structure.svg
:align: center
```

1. Find the displacement of $\text{R}$

2. Draw the displaced structure


````{admonition} Solution assignment 1
:class: tip, dropdown

$96.7 \text{ mm}$ ↓

```{admonition} Solution elongations cables
:class: tip, dropdown

| Cable   | Elongation (mm) |
|---------|-----------------|
| BK      | 24           |
| CK      | 24           |
| DH      | 13           |
| GJ      | 52           |
| IM      | 5           |
| JP      | 15           |
| KQ      | 48           |
| OR      | 40            |

```

````

````{admonition} Solution assignment 2
:class: tip, dropdown

```{figure} intro_data/ans.svg
:align: center
```

````

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/statisch_onbepaald/graad_bepalen.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

```
```` 

## Exercise static determinacy 1

Gegeven is de volgende constructie:

```{figure} intro_data/Oefening_6.svg
---
align: center
---
Constructie
```

Bepaal de graad van uitwendig statisch onbepaaldheid.

`````{exercise}
:label: so_2_1
:nonumber: true

Splits de constructie in zo groot mogelijke, vormvaste, scharnierend verbonden delen en teken het vrijlichaamsschema van de scharnierende delen.

```{h5p} https://tudelft.h5p.com/content/1292612545160457437/embed
```

`````

````{solution} so_2_1
:class: dropdown

Er zijn *7* onbekende oplegreacties en *6* onbekende verbindingskrachten. Dat zijn *13* onbekende krachten in totaal.

```{figure} intro_data/Oefening_8.svg
---
align: center
---
Aantal onbekende krachten
```

````

`````{exercise}
:label: so_2_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292612546255043757/embed
```

`````

````{solution} so_2
:class: dropdown

Er zijn *12* evenwichtsvergelijking(en).

```{figure} intro_data/Oefening_9.svg
---
align: center
---
Aantal evenwichtsvergelijkingen
```

````

`````{exercise}
:label: so_2_3
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292612546677182677/embed
```

`````

````{solution} so_2_3
:class: dropdown

De constructie is *1*ste/de graads uitwendig statisch onbepaald

````

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/statisch_onbepaald/graad_bepalen_2.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

```
```` 

## Exercise static determinacy 2


```{figure} ./intro_data/Oefening_1.svg
---
align: center
---
Constructie
```

Bepaal de graad van inwendig statisch onbepaaldheid.

`````{exercise}
:label: so_1
:nonumber: true

Splits constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor alle knopen en teken de vrijlichaamsschema's voor de staven

```{h5p} https://tudelft.h5p.com/content/1292586829246525217/embed
```

`````

````{solution} so_1
:class: dropdown

Er zijn *6* onbekende oplegreacties en *32* onbekende staafkrachten. Dat zijn *38* onbekende krachten in totaal.

```{figure} ./intro_data/Oefening_2.svg
---
align: center
---
Aantal onbekende oplegreacties en staafkrachten op knopen
```

```{figure} ./intro_data/Oefening_3.svg
---
align: center
---
Aantal onbekende staafkrachten op staven
```

````

`````{exercise}
:label: so_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292587403744225227/embed
```

`````

````{solution} so_2
:class: dropdown

Er zijn *0* evenwichtsvergelijkingen vanuit rolscharnieren, *6* evenwichtsvergelijking(en) vanuit scharnierende verbindingen, *9* evenwichtsvergelijking(en) vanuit algemene verbindingen, *1* evenwichtsvergelijking(en) vanuit pendelstaven en *18* evenwichtsvergelijking(en) vanuit algemene staven. Dat zijn *34* evenwichtsvergelijkingen in totaal.

```{figure} ./intro_data/Oefening_4.svg
---
align: center
---
Aantal evenwichtsvergelijkingen voor de knopen
```

```{figure} ./intro_data/Oefening_5.svg
---
align: center
---
Aantal evenwichtsvergelijkingen voor de staven
```

````

`````{exercise}
:label: so_3
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292587410124264777/embed
```

`````

````{solution} so_3
:class: dropdown

De constructie is *4*ste/de graads inwendig statisch onbepaald

````

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/statisch_onbepaald/graad_bepalen_3.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

```
```` 

## Exercise static determinacy 3

Gegeven is de volgende constructie:


```{figure} intro_data/Oefening_10.svg
---
align: center
---
Constructie
```

Bepaal de graad van uitwendig en inwendig statisch onbepaaldheid.

`````{exercise}
:label: so_3_1
:nonumber: true

Splits de constructie in zo groot mogelijke, vormvaste, scharnierend verbonden delen en teken het vrijlichaamsschema van de scharnierende delen.

```{h5p} https://tudelft.h5p.com/content/1292615284867296507/embed
```

`````

````{solution} so_3_1
:class: dropdown

Er zijn *3* onbekende oplegreacties en *0* onbekende verbindingskrachten. Dat zijn *3* onbekende krachten in totaal.

```{figure} intro_data/Oefening_11.svg
---
align: center
---
Aantal onbekende krachten
```

````

`````{exercise}
:label: so_3_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292615285293314797/embed
```

`````

````{solution} so_3_2
:class: dropdown

Er zijn *3* evenwichtsvergelijking(en).

```{figure} intro_data/Oefening_12.svg
---
align: center
---
Aantal evenwichtsvergelijkingen
```

````

`````{exercise}
:label: so_3_3
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292615285591579477/embed
```

`````

````{solution} so_3_3
:class: dropdown

De constructie is *0*ste/de graads uitwendig statisch onbepaald

````

`````{exercise}
:label: so_3_4
:nonumber: true

Splits constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor alle knopen en teken de vrijlichaamsschema's voor de staven

```{h5p} https://tudelft.h5p.com/content/1292615285960301817/embed
```

`````

````{solution} so_3_4
:class: dropdown

Er zijn *3* onbekende oplegreacties en *19* onbekende staafkrachten. Dat zijn *22* onbekende krachten in totaal.

```{figure} intro_data/Oefening_13.svg
---
align: center
---
Aantal onbekende oplegreacties en staafkrachten op knopen
```

```{figure} intro_data/Oefening_15.svg
---
align: center
---
Aantal onbekende staafkrachten op staven
```

````

`````{exercise}
:label: so_3_5
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292615286356377247/embed
```

`````

````{solution} so_3_5
:class: dropdown

Er zijn *1* evenwichtsvergelijking(en) vanuit rolscharnieren, *2* evenwichtsvergelijking(en) vanuit scharnierende verbindingen, *6* evenwichtsvergelijking(en) vanuit algemene verbindingen, *0* evenwichtsvergelijking(en) vanuit pendelstaven en *12* evenwichtsvergelijking(en) vanuit algemene staven. Dat zijn *21* evenwichtsvergelijkingen in totaal.

```{figure} intro_data/Oefening_14.svg
---
align: center
---
Aantal evenwichtsvergelijkingen voor de knopen
```

```{figure} intro_data/Oefening_16.svg
---
align: center
---
Aantal evenwichtsvergelijkingen voor de staven
```

````

`````{exercise}
:label: so_3_6
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292615286690175927/embed
```

`````

````{solution} so_3_6
:class: dropdown

De constructie is *1*ste/de graads inwendig statisch onbepaald

````