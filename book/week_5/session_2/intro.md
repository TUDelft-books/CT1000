```{index} Force method; demonstration bending
```

(lesson5.2)=
# Lesson Wednesday Oktober 1st

During today's lesson it's demonstrated how you to use the force method for statically indeterminate problems which involve bending.

## Demonstration
Given a structure as shown below:

```{figure} ./intro_data/structure.svg
:align: center

Structure
```

1. Determine the degree of statical determinacy.
2. Transform the structure in a statical determinant system by releasing a support, splitting the structure at a two-force member or adding hinges: add unknown statically indeterminate forces and displacement constraints for each of the support you released and hinges you added. Be aware that you don't transform the structure in a (partial) mechanism!

# Solve displacements
The third step of the force method is as follows: Solve for the displacement in terms of the unknown indeterminate forces as you would normally do for a statically determinate structure. Therefore, we first solve for the force distribution, which then allows us to determine the displacements.


$$
\begin{align}
\sum \left. T \right|_{\rm{E}}^{\rm{EG}} &= 0 \\
84 \cdot 4 - N_{\rm{CG}} \cdot 8 &= 0 \\
N_{\rm{CG}} &= 42 \ \rm{kN}
\end{align}
$$

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{BD}} &= 0 \\
B_{\rm{v}} + N_{\rm{BD}}&= 0 \\
N_{\rm{BD}} &= -B_{\rm{v}}
\end{align}
$$

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{DG}} &= 0 \\
V_{\rm{D}}^{\rm{AD}}-B_{\rm{v}} - 84 + 42 &= 0 \\
V_{\rm{D}}^{\rm{AD}} &= B_{\rm{v}} + 42
\end{align}
$$

$$
\begin{align}
\sum \left. T \right|_{\rm{D}}^{\rm{DG}} &= 0 \\
M_{\rm{D}} + 84 \cdot 8 - 42 \cdot 12 &= 0 \\
M_{\rm{D}} &= -168 \ \rm{kNm}
\end{align}
$$

$$
\begin{align}
w_{\rm{D}} &= \cfrac{168 \cdot 4^2}{2 \cdot 64000} + \cfrac{\left( B_{\rm{v}} + 42 \right) \cdot 4^3}{3 \cdot 64000} \\
w_{\rm{D}} &= \cfrac{1}{3000} \cdot B_{\rm{v}} + 0.035 \\
w_{\rm{D}} & \approx 0.000333 \cdot B_{\rm{v}} + 0.035
\end{align}
$$

$$
\begin{align}
w_{\rm{B}} &= w_{\rm{D}} + \Delta L_{\rm{BD}} \\
w_{\rm{B}} &= w_{\rm{D}} + \cfrac{-B_{\rm{v}} \cdot 8}{4000} \\
w_{\rm{B}} &= \cfrac{7}{3000} \cdot B_{\rm{v}} + 0.035 \\
w_{\rm{B}} & \approx 0.00233\cdot B_{\rm{v}} + 0.035 \\
\end{align}
$$

$$
\begin{align}
w_{\rm{B}} &= 0 \\
\cfrac{7}{3000} \cdot B_{\rm{v}} + 0.035 &= 0 \\
B_{\rm{v}} &= -15 \ \rm{kN}
\end{align}
$$

$$
\begin{align}
\varphi_{\rm{D}} &= \cfrac{168 \cdot 4}{64000} + \cfrac{\left( -15 + 42 \right) \cdot 4^2}{2 \cdot 64000} \\
\varphi_{\rm{D}} &= \cfrac{1}{3000} \cdot B_{\rm{v}} + 0.035 \\
\varphi_{\rm{D}} & \approx 0.000125 \cdot B_{\rm{v}} + 0.01575
\end{align}
$$

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{EG}} &= 0 \\
V_{\rm{E}}- 84 + 42 &= 0 \\
V_{\rm{E}} &= 42 \ \rm{kN}
\end{align}
$$

$$
\begin{align}
w_{\rm{E}} &= w_{\rm{D}} + \varphi_{\rm{D}} \cdot 4 + \cfrac{ 42 \cdot 4^3}{3 \cdot 64000} \\
w_{\rm{E}} &= 0.0995 \ \rm{m} \\
\end{align}
$$

4. Use your displacement constraints to solve for the statically indeterminate forces
