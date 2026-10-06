# Guided exercise

```{figure-start} ./lesoefening1_data/constructie.svg
:align: center
:source: source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrix_2
:number:
:figclass: sticky-margin
```

- $EI = 4 \ \rm{MNm^2}$
- $EA \gg EI$

```{figure-end}
```

::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[\begin{pmatrix} 4000 & 2000 \\\ 2000 & 4000 \end{pmatrix}]
^^^
? Determine the element stiffness matrix $\mathbf{K}^{(e)}$ for one element. Note that all elements have the same length and stiffness. Use the 'Insert Matrix' function.

$\mathbf{K}^{(e)} = $ {gap}

---

::::

% solution_start

::::{admonition} Solution
:class: solution, dropdown

$$\mathbf{K}^{(e)} = \begin{bmatrix} \cfrac{4EI}{l} & \cfrac{2EI}{l} \\ \cfrac{2EI}{l} & \cfrac{4EI}{l} \end{bmatrix} = \begin{bmatrix} 4000 & 2000 \\ 2000 & 4000 \end{bmatrix}$$

::::

% solution_end

Use the displacement vector $ \mathbf{u} =  \begin{bmatrix}  \varphi_{\rm{A}} \\  \varphi_{\rm{B}} \\ \varphi_{\rm{C}} \\ \varphi_{\rm{D}} \\ \varphi_{\rm{E}} \end{bmatrix} $

::::{question} Exercise
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

---

M[\begin{pmatrix} 4000 & 2000 & 0 & 0 & 0 \\\ 2000 & 12000 & 2000 & 2000 & 0 \\\ 0 & 2000 & 8000 & 0 & 2000 \\\ 0 & 2000 & 0 & 4000 & 0 \\\ 0 & 0 & 2000 & 0 & 4000 \end{pmatrix}] Determine the global stiffness matrix $\mathbf{K}$. Use the 'Insert Matrix' function again.

---

::::

% solution_start

::::{admonition} Solution
:class: solution, dropdown

The global stiffness matrix can be assembled from the element stiffness matrices by placing each element's terms in the rows and columns corresponding to its nodes and adding them together.

$$\mathbf{K} =
\begin{bmatrix} 
4000 & 2000 & 0 & 0 & 0 \\ 
2000 & 4000+4000+4000 & 2000 & 2000 & 0 \\ 
0 & 2000 & 4000+4000 & 0 & 2000 \\ 
0 & 2000 & 0 & 4000 & 0 \\ 
0 & 0 & 2000 & 0 & 4000 
\end{bmatrix}
=
\begin{bmatrix} 
4000 & 2000 & 0 & 0 & 0 \\ 
2000 & 12000 & 2000 & 2000 & 0 \\ 
0 & 2000 & 8000 & 0 & 2000 \\ 
0 & 2000 & 0 & 4000 & 0 \\ 
0 & 0 & 2000 & 0 & 4000 
\end{bmatrix}$$

::::

% solution_end

::::{question} Exercise
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

---

M[\begin{pmatrix} M_A \\\ 0 \\\ 73 \\\ 0 \\\ 0 \end{pmatrix}] Determine the force vector $\mathbf{F}$. Use the 'Insert Matrix' function again.

---
::::

% solution_start

::::{admonition} Solution
:class: solution, dropdown

Only joint $\rm{C}$ is subjected to an external moment of $73 \rm{kNm}$ clockwise (so it is positive).

$$\mathbf{F} = \begin{bmatrix} M_{\rm{A}} \\ 0 \\ 73 \\ 0 \\ 0 \end{bmatrix}$$

::::

% solution_end


::::{question} Exercise
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[0]
M[-2]
M[11]
M[1]
M[-5.5]
^^^
? Determine the values of the degrees of freedom $\varphi_{\rm{B}}$, $\varphi_{\rm{C}}$, $\varphi_{\rm{D}}$ and $\varphi_{\rm{E}}$.

- $\varphi_{\rm{A}} = ${gap}$ \rm{mrad} $
- $\varphi_{\rm{B}} = ${gap}$ \rm{mrad} $
- $\varphi_{\rm{C}} = ${gap}$ \rm{mrad} $
- $\varphi_{\rm{D}} = ${gap}$ \rm{mrad} $
- $\varphi_{\rm{E}} = ${gap}$ \rm{mrad} $ 
---
::::

% solution_start

::::{admonition} Solution
:class: solution, dropdown

Joint $\rm{A}$ is fixed, so its rotation $\varphi_{\rm{A}}$ is equal to 0.

The complete system of equations is:

$$
\begin{aligned}
\mathbf{K} \mathbf{u} &= \mathbf{F} \\
\begin{bmatrix} 
4000 & 2000 & 0 & 0 & 0 \\ 
2000 & 12000 & 2000 & 2000 & 0 \\ 
0 & 2000 & 8000 & 0 & 2000 \\ 
0 & 2000 & 0 & 4000 & 0 \\ 
0 & 0 & 2000 & 0 & 4000 
\end{bmatrix}
\begin{bmatrix} 
0 \\ 
\varphi_{\rm{B}} \\ 
\varphi_{\rm{C}} \\ 
\varphi_{\rm{D}} \\ 
\varphi_{\rm{E}}
\end{bmatrix}
&=
\begin{bmatrix} M_{\rm{A}} \\ 0 \\ 73 \\ 0 \\ 0 \end{bmatrix}
\end{aligned}
$$

Since $\varphi_{\rm{A}}$ is equal to 0, the first row and first column can be omitted. This gives:

$$
\begin{bmatrix} 
12000 & 2000 & 2000 & 0 \\ 
2000 & 8000 & 0 & 2000 \\ 
2000 & 0 & 4000 & 0 \\ 
0 & 2000 & 0 & 4000 
\end{bmatrix}
\begin{bmatrix} 
\varphi_{\rm{B}} \\ 
\varphi_{\rm{C}} \\ 
\varphi_{\rm{D}} \\ 
\varphi_{\rm{E}}
\end{bmatrix}
&=
\begin{bmatrix} 0 \\ 73 \\ 0 \\ 0 \end{bmatrix}
$$

The system above can then be solved for $\varphi_{\rm{B}}$, $\varphi_{\rm{C}}$, $\varphi_{\rm{D}}$ and $\varphi_{\rm{E}}$.

$\mathbf{u} = \begin{bmatrix} 0 \\ -\cfrac{1}{500} \\ \cfrac{11}{1000} \\ \cfrac{1}{1000} \\ -\cfrac{11}{2000} \end{bmatrix} \, \rm{in} \, \rm{rad}$

::::

% solution_end
