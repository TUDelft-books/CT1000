```{index} Temperature influences; Class exercise for statically indeterminate structures
```

(lesson7.3)=
# Lesson October 16th

During today's lesson you'll work on two complex exercises on the topic of Temperature influences. Please ask your questions regarding the [homework](homework7.3) as well!

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CTB2210/2025/temperatuur/lesoefening.html. Deze oefening is niet vertaald omdat er geen Engelstalige studenten zijn in de klas.

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/temperatuur3

```
````

## Exercise 1

Gegeven is de volgende constructie:

```{figure} ./intro_data/structure.svg
:align: center

Constructie, $EI = \cfrac{800}{3} \ \rm{kNm^2}$
```

We gaan deze constructie doorrekenen met behulp van differentiaalvergelijkingen

:::::{exercise}
:label: temp_2_1
:nonumber: true

Wat is $\kappa_{\rm{T}}$?

```{h5p} https://tudelft.h5p.com/content/1292671259091838977/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

$$\kappa^T = -\cfrac{\alpha \cdot T}{h} = - \cfrac{0.0001 \cdot 30}{0.2} = -0.015 \ m^{-1}$$

::::

:::::{exercise}
:label: temp_2_2
:nonumber: true

Bepaal met behulp van de differentiaalvergelijkingen de uitdrukkingen voor de snedekrachten en verplaatsingen. Merk op dat twee randvoorwaarden direct twee integratieconstantes geven.

```{h5p} https://tudelft.h5p.com/content/1292671251572754907/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Voor deze constructie gelden den onderstaande randvoorwaarden:

$$ w \left( 0 \right) = 0 $$
$$ M \left( 0 \right) = +6 \rm{kNm} $$
$$ w \left( 8 \right) = 0 $$
$$ \varphi \left( 8 \right) = 0 $$

Hieruit volgt voor de snedekrachten en verplaatsingen:

$$ V\left( x  \right) = C_1 $$ 
$$ M\left( x  \right) = C_1 \cdot x + 6 $$
$$ \kappa \left( x \right) = \cfrac{M}{EI} = \cfrac{3}{800} \cdot C_1 \cdot x + \cfrac{6 \cdot 3}{800} - 0.015 = 0.00375 \cdot C_1 \cdot x + 0.0075 $$
$$ \varphi \left( x \right) = 0.001875  C_1 \cdot x^2 + 0.0075 \cdot x + C_3 $$
$$ w \left( x \right) = -0.000625 \cdot C_1 \cdot x^3 -0.00375 \cdot x^2 - C_3 \cdot x + 0 $$

::::

:::::{exercise}
:label: temp_2_3
:nonumber: true

Bepaal de waardes van de integratieconstantes

```{h5p} https://tudelft.h5p.com/content/1292671264027013177/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

$$ C_1 = -0.375 $$
$$ C_3 = -0.015 $$

::::

:::::{exercise}
:label: temp_2_4
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292671266355957267/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Als de temperatuur verder toeneemt, dan wordt de absolute waarde van maximale verplaatsing eerst kleiner dan groter. 

::::

:::::{exercise}
:label: temp_2_5
:nonumber: true

Waar is het buigpunt?

```{h5p} https://tudelft.h5p.com/content/1292696178444240937/embed
```

:::::

## Exercise 2

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/temperatuur2

Given the following structure. 

```{figure} intro_data/struct.svg
:align: center
```

:::::{exercise}
:label: temp_1_1
:nonumber: true

Find the curvature and strain due to the temperature influence

```{h5p} https://tudelft.h5p.com/content/1292660766863817267/embed
```

:::::

:::::{exercise}
:label: temp_1_2
:nonumber: true

Create a statically determinate system which uses the following displacement constraint: $w_{\rm{C}}^{\rm{BC}} = w_{\rm{C}}^{\rm{CD}}$ with $N_{\rm{CD}}$ as the statical indeterminate force. It is shown in the figure below without equivalent forces for the temperature influence.

```{figure} intro_data/SD.svg
:align: center
```


What are the force distributions and displacements due to the distributed load as a function of $N_{\rm{CD}}$? So don't include kinematical equivalent forces due to the temperature influence.

```{h5p} https://tudelft.h5p.com/content/1292660774931288447
```

:::::

:::::{exercise}
:label: temp_1_3
:nonumber: true

What are the force distributions and displacements including temperature influences and as a function of $N_{\rm{CD}}$?

```{h5p} https://tudelft.h5p.com/content/1292660796839945267/embed
```

:::::

:::::{exercise}
:label: temp_1_4
:nonumber: true

Use the displacement constraint to solve for $N_{\rm{CD}}$

```{h5p} https://tudelft.h5p.com/content/1292660799484783077/embed
```

:::::

:::::{exercise}
:label: temp_1_5
:nonumber: true

What are the bending moments?

```{h5p} https://tudelft.h5p.com/content/1292660805509625677/embed
```

:::::

:::::{exercise}
:label: temp_1_6
:nonumber: true

What is the curvature?

```{h5p} https://tudelft.h5p.com/content/1292660806977160817/embed
```

:::::

:::::{exercise}
:label: temp_1_7
:nonumber: true

What are the displacements?

```{h5p} https://tudelft.h5p.com/content/1292660808935020687/embed
```

:::::