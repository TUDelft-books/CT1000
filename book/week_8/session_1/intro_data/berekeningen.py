import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

L1, L2, L3, F, EI, n, w_0 = sym.symbols('L1 L2 L3 F EI n w_0')

L1 = 4
L2 = 5
L3 = 4
EI = sym.nsimplify(64000*5)
print('EI=',EI,' approx ',EI.evalf())
F = sym.nsimplify(15*24*31/100)
alpha = sym.nsimplify(1e-5)

w_0 = sym.nsimplify(31 / 1000)
print('F=',F,' approx ',F.evalf())
print('w_0=',w_0,' approx ',w_0.evalf())

alpha, delta_T, h = sym.symbols('alpha delta_T h')

alpha = sym.nsimplify(1e-5)

phi, M_C, M_C_2, M_C_3 = sym.symbols('phi, M_C, M_C_2, M_C_3')

eq1 = sym.Eq(phi, M_C * L2 / 4 / EI)

M_C = sym.solve(eq1, M_C)[0]
print(M_C)

eq2 = sym.Eq(phi, M_C_2 * L3 / 3 / n / EI)
M_C_2 = sym.solve(eq2, M_C_2)[0]
print(M_C_2)

M_C_3 = F * L1

eq3 = sym.Eq(M_C + M_C_2 - M_C_3, 0)
phi = sym.solve(eq3, phi)[0]
print('phi=',phi)

w_D = phi * L1 + F * L1**3 / 3 / EI
print('w_D=',w_D,' approx ',w_D.evalf())
print('w_D(n=0)=',w_D.subs(n, 0),' = approx ',w_D.subs(n, 0).evalf())
print('w_D(n=oo)=',sym.limit(w_D, n, sym.oo),' = approx ',sym.limit(w_D, n, sym.oo).evalf())

plt.figure()
print(w_D)
w_D_func = sym.lambdify(n, w_D, 'numpy')
n_vals = np.linspace(0, 100, 400)
plt.plot(0, float(w_D.subs(n, 0)), 'ro')  # point at n=0
plt.plot(n_vals, w_D_func(n_vals))
#add horizontal lines for w_D at n=0 and n=oo
plt.axhline(y=float(sym.limit(w_D, n, sym.oo)), color='g', linestyle='--', label='w_D(n=oo)')
plt.xlim([0, 100])
#plt.ylim([float(w_D.subs(n, 0)), float(sym.limit(w_D, n, sym.oo))])
plt.show()

Av, Ah = sym.symbols('Av Ah')

M_C_4 = F * L1 - Ah * L3
V_C = F - Av

print('M_C_4=',M_C_4)
print('V_C=',V_C)

w_C = M_C_4 * L2**2 / 2 / EI + V_C * L2**3 / 3 / EI + w_0
phi_C = M_C_4 * L2 / EI + V_C * L2**2 / 2 / EI

print('w_C=',w_C,'approx ',w_C.evalf())
print('phi_C=',phi_C,'approx ',phi_C.evalf())

w_A_v = w_C
w_A_h = phi_C * L3 - Ah * L3**3 / 3 / EI

print('w_A_v=',w_A_v)
print('w_A_h=',w_A_h)

eq4 = sym.Eq(w_A_v, 0)
eq5 = sym.Eq(w_A_h, 0)

sol = sym.solve([eq4, eq5], (Av, Ah))
print('Av=',sol[Av],'approx ',sol[Av].evalf())
print('Ah=',sol[Ah],'approx ',sol[Ah].evalf())

h, delta_T = sym.symbols('h delta_T')

h = sym.nsimplify(0.2)
delta_T = sym.nsimplify(32)

kappa_T = alpha * delta_T / h
print('kappa_T=',kappa_T)
M_T = EI * kappa_T

print('M_T=',M_T,'approx ',M_T.evalf())

w_C = w_C - w_0 + M_T * L2**2 / 2 / EI
print('w_C with thermal=',w_C)
phi_C = phi_C + M_T * L2 / EI
print('phi_C with thermal=',phi_C)

w_A_v = w_C
w_A_h = phi_C * L3 - alpha * sym.nsimplify(16) * L2 - Ah * L3**3 / 3

print('w_A_v with thermal=',w_A_v)
print('w_A_h with thermal=',w_A_h)

eq6 = sym.Eq(w_A_v, 0)
eq7 = sym.Eq(w_A_h, 0)
sol_T = sym.solve([eq6, eq7], (Av, Ah))
print('With thermal effects:')
print('Av=',sol_T[Av],'=',sym.simplify(sol_T[Av]).expand(),'approx ',sol_T[Av].evalf())
print('Ah=',sol_T[Ah],'=',sym.simplify(sol_T[Ah]).expand(),'approx ',sol_T[Ah].evalf())