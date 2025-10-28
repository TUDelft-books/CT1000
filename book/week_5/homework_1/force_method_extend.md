````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze theorie is aangepast van https://oit.tudelft.nl/CTB2210/2025/krachtenmethode_vakwerk/theorie.html. Deze instructie is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

```
```` 

(krachtenmethode_simpel)=
# ... voor simpele constructies op trek en druk

De krachtenmethode is een aanpak om statisch onbepaalde constructies door te rekenen. In deze methode wordt de constructie aangepast naar een statisch bepaalde constructie met vormveranderingsvoorwaarden. Vervolgens kan je de constructie oplossen zoals je gewend bent van statisch bepaalde constructies. De krachtenmethode bestaat altijd uit de volgende stappen:

::::::{prf:algorithm} Krachtenmethode
:nonumber: true
:label: krachtenmethode_algoritme

1. Bepaal de graad van statische bepaaldheid.
2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij pendelstaven of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaarden toe voor elke oplegging die je hebt weggenomen, aansluiting van de pendelstaven die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    `````{tab-set}
    ````{tab-item} Weghalen oplegging
    % Figures from https://github.com/TUDelft-books/CEG-mechanics-BSc/blob/EN/book/statically_inderminate/force_method/force_method_data/Tekening1.vsdx
    ```{figure} theorie_data/1.svg
    :align: center
    ```
    ````
    ````{tab-item} Splitsen constructie bij pendelstaven
    ```{figure} theorie_data/2.svg
    :align: center
    ```
    ````
    ````{tab-item} Toevoegen scharnieren
    ```{figure} theorie_data/3.svg
    :align: center
    ```
    ````
    `````

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.
4. Gebruik je vervormingsvoorwaarden om de statisch onbepaalde krachten op te lossen.

::::::

We behandelen de toepassing op vakwerkconstructies met het volgende voorbeeld.

::::::{prf:example}
:nonumber: true
:label: sd_extsimpel_0

```{figure} ./theorie_data/constructie.svg
---
align: center
---
Voorbeeldconstructie. Hoewel dit geen vakwerkconstructie is, worden vervorming enkel veroorzaakt door extensie, niet door buiging. $EA = 2.5 \ \rm{MN}, EI = \infty$
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_1

    Voor ons voorbeeld zijn we geïnteresseerd in de interne krachtenverdeling, dus moeten we de graad van interne statische onbepaaldheid evalueren.

    ```{figure} ./theorie_data/statisch_onbepaaldheid.svg
    ---
    align: center
    ---
    Er zijn 6 onbekende krachten en 5 evenwichtsvergelijkingen
    ```

    Deze constructie is dus 1e orde intern statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_2

    Er zijn hier enkele opties, waarvan er enkele hieronder worden getoond:

    ```{figure} ./theorie_data/options.svg
    :align: center
    ```

    De eerste optie wordt gekozen.

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_4

    We hebben de volgende statisch bepaalde constructie gekozen met vervormingsvoorwaarde $w_{\rm{B}}\left( B_{\rm{v}} \right) = 0$:

    ```{figure} ./theorie_data/SB-systeem.svg
    ---
    align: center
    ---
    De statisch bepaalde constructie met vervormingsvoorwaarde, $EA = 2.5 \ \rm{MN}, EI = \infty$
    ```

    Om de verplaatsing van $\rm{B}$ te vinden, kunnen eerst de normaalkrachten worden geëvalueerd als functie van $B_{\rm{v}}$ met behulp van verticaal krachtenevenwicht:

    - $N_{\rm{AC}}\left( B_{\rm{v}} \right) = - B_{\rm{v}} + 6 - 3 \cdot x $
    - $N_{\rm{BC}} \left( B_{\rm{v}} \right) = - B_{\rm{v}}$

    Dit leidt tot de volgende uitrekking van de elementen, met behulp van $\Delta L = \cfrac{N \ L}{EA}$:
    - $\Delta L_{\rm{AC}}\left( B_{\rm{v}} \right) = - \cfrac{B_{\rm{v}} \cdot 2}{2500} + \cfrac{6 \cdot 2}{2500} - \int\limits_0^2 {\cfrac{ 3 \cdot x}{2500}dx} = - \cfrac{B_{\rm{v}}}{1250} + \cfrac{3}{1250} $
    - $\Delta L_{\rm{BC}}\left( B_{\rm{v}} \right) = -\cfrac{B_{\rm{v}}}{1250}$

    Dit leidt tot een verplaatsing van:

    - $w_{\rm{C}}\left( B_{\rm{v}} \right) = \cfrac{B_{\rm{v}}}{1250} - \cfrac{3}{1250}  $
    - $w_{\rm{B}}\left( B_{\rm{v}} \right) = \cfrac{B_{\rm{v}}}{625} - \cfrac{3}{1250} $

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_5

    $$
    \begin{align*}
    w_{\rm{B}}\left( B_{\rm{v}} \right) &= 0 \\
    \cfrac{B_{\rm{v}}}{625} - \cfrac{3}{1250} &= 0 \\
    B_{\rm{v}} &= 1.5 \ \rm{kN}
    \end{align*}
    $$

    Dit leidt tot de volgende andere resultaten:

    $w_{\rm{C}} = 1.2 \ \rm{mm} \left( \downarrow \right) $

    ```{figure} ./theorie_data/Nlijn.svg
    :align: center
    ```

    ::::::

## Meer voorbeelden

In hoofdstuk 2.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` wordt de krachtemethode in het algemeen behandeld. Specifiek voor simpele vakwerkconstructies wordt behandeld in hoofdstuk 2.2.8 - 2.2.9.

## Instructies in collegevorm

Dit onderwerp is gepresenteerd in college vanaf 11:30 tot 43:10 [hier](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/b59d1e6849ba4f92957d462f07f7e37f1d?sortBy=most-recent) in het Nederlands.

## Oefeningen

- Opgaves 2.31 - 2.39, in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Antwoorden zijn [hier beschikbaar](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).