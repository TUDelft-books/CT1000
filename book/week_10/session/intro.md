```{index} Static indeterminate structures; Exam assignment
```

(exam1)=
# Exam Friday November 8th

Today you'll make the first exam assignment covering Statically indeterminate structures including its prerequisites. For more information about the exam see [the assessment information in course information](exam-general)

## Exam assignment
Your own submission and its grading can be found here: [<img height="12px" src="../../figures/ANS.svg" alt="ANS"> exam assignment Statically indeterminate structures 1](https://ans.app/universities/1/courses/437261/assignments/1147226/go_to). The exam assignment was provided as follows:

Given is the structure as shown in the figure below.

```{figure} intro_data/structure.svg
:align: center
```

Calculate the displacement of $\rm{D}$ and the normal forces in all the members using a force-, displacement- or hybrid- ('hoekveranderingsvergelijkingen' with moveable nodes) method.

````{admonition} Solution assignment 1
:class: tip, dropdown

Convert the structure into a statically determinate structure with a displacement or force condition.

For example when using the force method:

```{figure} intro_data/statically_determinate.svg
:align: center
```

This gives:
- ${N_{{\rm{AD}}}} = - \cfrac{4}{5}{B_{\rm{v}}}$
- ${N_{{\rm{BD}}}} = + {B_{\rm{v}}}$
- ${N_{{\rm{CD}}}} = - \cfrac{3}{4}{B_{\rm{v}}}$

This gives elongations:

- $\Delta {L_{{\rm{BD}}}} = \cfrac{{{B_{\rm{v}}}}}{{7500}}$
- $\Delta {L_{{\rm{AD}}}} = - \cfrac{{{B_{\rm{v}}}}}{{4800}}$
- $\Delta {L_{{\rm{CD}}}} = - \cfrac{{{B_{\rm{v}}}}}{{10000}}$

Resulting in a williot like this (keeping the unknown value of $B_\rm{v}$ constant for all elongations):

```{figure} intro_data/williot.svg
:align: center
```

This gives a vertical displacement of $\rm{B}$ of $\cfrac{{3{B_{\rm{v}}}}}{{6400}}$.

With the requirements of $30 \rm{ mm}$ this leads to $B_\rm{v} = 64 \ \rm{ kN}$, resulting in:

- $N_\rm{BD} = +64 \ \rm{ kN}$
- $N_\rm{AD} = -80 \ \rm{ kN}$
- $N_\rm{CD} = -48 \ \rm{ kN}$
- $u_{\rm{D,h}} = 6.4 \ \rm { mm} \left( \to \right)$
- $u_{\rm{D,v}} = 21.4667 \ \rm{ mm} \left( \downarrow \right)$

````