import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

L1, L2, L3, F, EI, n, w_0 = sym.symbols('L1 L2 L3 F EI n w_0')

L1 = 4
L2 = 5
L3 = 4
EI = sym.nsimplify(64000*5)
F = sym.nsimplify(15*24)

alpha, delta_T, h = sym.symbols('alpha delta_T h')

alpha = sym.nsimplify(1e-5)

phi, M_C, M_C_2, M_C_3 = sym.symbols('phi, M_C, M_C_2, M_C_3')

eq1 = sym.Eq(phi, -M_C * L2 / 4 / EI)

M_C = sym.solve(eq1, M_C)[0]
print(M_C)

eq2 = sym.Eq(phi, M_C_2 * L3 / 3 / n / EI)
M_C_2 = sym.solve(eq2, M_C_2)[0]
print(M_C_2)

M_C_3 = F * L1

eq3 = sym.Eq(M_C + M_C_2 - M_C_3, 0)
phi = sym.solve(eq3, phi)[0]
print(phi)

w_D = phi * L1 + F * L1**3 / 3 / EI
print(w_D)
print(w_D.subs(n, 0))
print(sym.limit(w_D, n, sym.oo))

plt.figure()
print(w_D)
w_D_func = sym.lambdify(n, w_D, 'numpy')
n_vals = np.linspace(0, 1000, 400)
plt.plot(n_vals, w_D_func(n_vals))
plt.ylim([float(w_D.subs(n, 0)), float(sym.limit(w_D, n, sym.oo))])