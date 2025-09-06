# Working out

## Preqrequisite test 1

Given is the truss structure as shown below:

```{figure} ./answer_data/structure1.svg
:align: center
```

### 1a Determine the normal force in bar $\rm{CD}$ and $\rm{AC}$

```{figure} ./answer_data/FBD_1.svg
:align: center
```

$$
\begin{aligned}
    \mathop {{{\left. {\sum T } \right|}_A}}\limits^↺ &= 0 \\
    360 \cdot 10 - \frac{4}{5} N_{\rm{CD}} \cdot 7.5 &= 0 \\
    N_{\rm{CD}} &= +600 \ \rm{kN}
\end{aligned}
$$

```{figure} ./answer_data/FBD_2.svg
:align: center
```

$$
\begin{aligned}
    \mathop {{{\sum {\left. T \right|} }_B}}\limits^↺ &= 0 \\
    360 \cdot 20 - 180 \cdot 10 - {A_{\rm{v}}} \cdot 10 &= 0 \\
    {A_{\rm{v}}} &= + 540 \ {\rm{ kN}}
\end{aligned}
$$

```{figure} ./answer_data/FBD_3.svg
:align: center
```

$$\mathop {{{\sum {\left. T \right|} }_B}}\limits^↺ = 0$$
$$360 \cdot 20 - 540 \cdot 10 - {3 \over 5}{N_{{\rm{AC}}}} \cdot 10 = 0$$
$${N_{{\rm{AC}}}} = + 300 \ {\rm{ kN}}$$

### 1b Determine the displacement of node $\rm{C}$. You can estimate the value from your graph.

```{figure} ./answer_data/FBD_4.svg
:align: center
```

$$
\begin{aligned}
    \mathop {\sum {{{\left. T \right|}_A}} }\limits^↘ &= 0 \\
    -540 + {N_{{\rm{AC}}}} + {N_{{\rm{BC}}}} &= 0 \\
    -540 + 300 + {N_{{\rm{BC}}}} &= 0 \\
    {N_{{\rm{BC}}}} &= + 240 \ {\rm{ kN}}
\end{aligned}
$$

$$
A = \pi \left( {{{\left( {\cfrac{{\left( {\cfrac{{150}}{{\sqrt \pi }}} \right)}}{2} + \cfrac{{50}}{{\sqrt \pi }}} \right)}^2} - {{\left( {\cfrac{{\left( {\cfrac{{150}}{{\sqrt \pi }}} \right)}}{2}} \right)}^2}} \right) = 10000 \ {\rm{ m}}{{\rm{m}}^2}\\
\Delta {L_{{\rm{AC}}}} = \cfrac{{300 \cdot {{10}^3} \cdot 6.25}}{{25 \cdot {{10}^9} \cdot 10000 \cdot {{10}^{ - 6}}}} = + 7.5 \cdot {10^{ - 3}} \ {\rm{ m}}\\
\Delta {L_{{\rm{BC}}}} = \cfrac{{600 \cdot {{10}^3} \cdot 6.25}}{{25 \cdot {{10}^9} \cdot 10000 \cdot {{10}^{ - 6}}}} = + 15 \cdot {10^{ - 3}} \ {\rm{ m}}
$$


Williot graph gives:

```{figure} ./answer_data/williot.svg
:align: center
```

## Prerequisite test 2

Given is the structure as shown below:

```{figure} ./FMM_data/2.1.svg
:align: center
```

### 2a Determine the support reaction at $\rm{D}$.

```{figure} ./answer_data/AS.svg
:align: center
```

$$
\begin{aligned}
\mathop {\sum {{{\left. T \right|}_{{S_1}}}} }\limits^↺ &= 0 \\
{A_{\rm{v}}} &= 0 \ {\rm{ kN}}
\end{aligned}
$$

```{figure} ./answer_data/AS2.svg
:align: center
```

$$
\begin{aligned}
\mathop {\sum {{{\left. T \right|}_{{S_2}}}} }\limits^↺ &= 0 \\
50 \cdot 8 \cdot 4 + 100 \cdot 8 - {B_{\rm{v}}} \cdot 4 &= 0 \\
{B_{\rm{v}}} &=  \ {\rm{ kN}}
\end{aligned}
$$

```{figure} ./answer_data/VLS_geheel.svg
:align: center
```

$$
\begin{aligned}
\mathop {\sum {{{\left. T \right|}_c}} }\limits^↺ &= 0 \\
50 \cdot 8 \cdot 8 + 100 \cdot 12 - 600 \cdot 8 - 50 \cdot 4 \cdot 2 + {D_{\rm{v}}} \cdot 8 &= 0 \\
{D_{\rm{v}}} &= 100 \ {\rm{ kN}}
\end{aligned}
$$

### 2b Determine the bending moment in $\rm{C}$ using virtual work.

```{figure} ./answer_data/mechanica.svg
:align: center
```

$$
\begin{aligned}
\delta A = 0\\
+ 100 \cdot \delta u - {M_{\rm{D}}} \cdot \cfrac{{\delta u}}{4} = 0\\
{M_{\rm{D}}} = 400 \ {\rm{kNm}}
\end{aligned}
$$

### 2c Draw the bending moment diagram including values.

```{figure} ./answer_data/AB.svg
:align: center
```

$$
\begin{aligned}
\mathop {\sum {{{\left. T \right|}_B}} }\limits^↺ &= 0 \\
100\cdot 4 + 50 \cdot 4 \cdot 2 + {M_{\rm{B}}} &= 0 \\
{M_{\rm{B}}} &= - 800 \ {\rm{ kNm}}
\end{aligned}
$$

For $\rm{S}_1\rm{B}$, $\rm{BS}_2$, $\rm{BS}_2$ and $\rm{CE}$:
$M_{\rm{halfway} \ \rm{below} \ \rm{chord}}={1 \over 8} \cdot 50 \cdot {4^2} = 100 \ {\rm{ kNm}}$

Constructing the M-line gives:

```{figure} ./answer_data/M-lijn.svg
:align: center
```

### 2d Draw the shear stress distribution just left of $\rm{C}$ including values.

$$
{V_{\rm{C}}} = {\left. {\cfrac{{dM\left( x \right)}}{{dx}}} \right|_{x = 14}} = \cfrac{{400}}{4} = 100 \ {\rm{ kN}} $$

$$A = 2 \cdot 5 \cdot 400 + 4 \cdot 200 = 4800 \ {\rm{ mm}}^2$$

```{figure} ./answer_data/cross-section.svg
:align: center
```

$${S_{\bar z}} = 5 \cdot 400 \cdot 200 \cdot 2 + 200 \cdot 4 \cdot 400 = 1120000{ \ \rm{ m}}{{\rm{m}}^3}$$

$${{\bar z}_{{\rm{NC}}}} = \cfrac{{1120000}}{{4800}} \approx 233.33{ \ \rm{ mm}}$$

$${I_{zz}} = \left( {\cfrac{1}{{12}} \cdot 5 \cdot {{400}^3} + 400 \cdot 5 \cdot {{\left( {\cfrac{{400}}{2} - 233.33} \right)}^2}} \right) \cdot 2 + \cfrac{1}{{12}} \cdot 200 \cdot {4^3} + 4 \cdot 200 \cdot {\left( {400 - 233.33} \right)^2} \approx 8.00 \cdot {10^7}{ \ \rm{ m}}{{\rm{m}}^4}$$

$$S_z^{\rm{G}} = 233.33 \cdot 5 \cdot \cfrac{{ - 233.33}}{2} \approx - 136111{ \ \rm{ m}}{{\rm{m}}^3}$$

$${\tau _{\rm{G}}} = - \cfrac{{100 \cdot {{10}^3} \cdot - 136111}}{{5 \cdot 8.00 \cdot {{10}^7}}} \approx 34 \ {\rm{ MPa}}$$

$$S_z^{\rm{H}} = 400 \cdot 5 \cdot \left( {\left( {400 - 233.33} \right) - \cfrac{{400}}{2}} \right) \approx - 66666{\ \rm{ m}}{{\rm{m}}^3}$$

$$\tau _{\rm{G}}^{{\rm{web}}} = - \cfrac{{100 \cdot {{10}^3} \cdot - 66666}}{{5 \cdot 8.00 \cdot {{10}^7}}} \approx 17{\ \rm{ MPa}}$$

$$\tau _{\rm{H}}^{{\rm{flange}}} = - \cfrac{{100 \cdot {{10}^3} \cdot - 66666}}{{4 \cdot 8.00 \cdot {{10}^7}}} \approx 21{\ \rm{ MPa}}$$

```{figure} ./answer_data/shear_stress.svg
:align: center
```

### 2e Determine the displacement at $\rm{S}_2$. You can use the additional forget-me-not.

```{figure} ./answer_data/CD.svg
:align: center
```

$${\theta _{\rm{C}}} = \cfrac{1}{3}\cfrac{{400 \cdot {{10}^3} \cdot 8}}{{360 \cdot {{10}^9} \cdot 8.00 \cdot {{10}^{ - 5}}}} + \cfrac{3}{{128}} \cdot \cfrac{{50 \cdot {{10}^3} \cdot {8^3}}}{{360 \cdot {{10}^9} \cdot 8.00 \cdot {{10}^{ - 5}}}} \approx 0.0578 \ {\rm{ rad}}$$

```{figure} ./answer_data/S2D.svg
:align: center
```

$${w_{{{\rm{S}}_2}}} = 0.0578 \cdot 4 + \cfrac{1}{3}\cfrac{{400 \cdot {{10}^3} \cdot {8^3}}}{{360 \cdot {{10}^9} \cdot 8.00 \cdot {{10}^{ - 5}}}} = 0.306 \ {\rm{ m}}$$
$$V_{\rm{S}_2} = V_{\rm{C}} = 100 \ \rm{ kN}$$

### 2f Sketch the displaced structure without values. Make the following explicitly clear: direction of curvature, straight or curved sections, kinks, and points or parts which are not displaced.

```{figure} ./answer_data/displaced.svg
:align: center
```
