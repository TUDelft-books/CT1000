import sympy as sym

EI, EA, L1, L2, delta_T, h = sym.symbols('EI EA L1 L2 delta_T h')

L1 = sym.nsimplify(3)
L2 = sym.nsimplify(3)
h = sym.nsimplify(0.25)

EI = sym.nsimplify(7875)
EA = sym.nsimplify(2000)

delta_T = sym.nsimplify(66.5)
print(delta_T.evalf())

alpha = sym.nsimplify(1e-5)

L3 = L2 / 3 * 4
L4 = L2 / 3 * 5

M_A, N_BD = sym.symbols('M_A N_BD')

A_v_2 = (- M_A + N_BD / 5 * 4 * L2) / (L1 + L2)

B_v = (M_A + N_BD / 5 * 4 * L1) / (L1 + L2)

A_v = N_BD / 5 * 4 - B_v

M_T = EI * alpha * delta_T / h

print(M_T, M_T.evalf())

w_D_1 = M_A * (L1 + L2)**2 / (EI * 16) - M_T * (L1 + L2)**2 / (EI * 16) * 2 + N_BD / 5 * 4 * (L1 + L2)**3 / (EI * 48)

print('w_D_1:', w_D_1, 'approx',w_D_1.evalf())

w_D_2 = N_BD * L4 / EA * sym.nsimplify(-5 / 4)

print(w_D_2)

phi_A = M_A * (L1 + L2) / (EI * 3) - M_T * (L1 + L2) / (EI * 6) - M_T * (L1 + L2) / (EI * 3) + N_BD / 5 * 4 * (L1 + L2)**2 / (EI * 16)

print('phi_A:', phi_A, 'approx',phi_A.evalf())

eq1 = sym.Eq(w_D_1, w_D_2)
eq2 = sym.Eq(phi_A, 0)

print('eq1',eq1)
print('eq2',eq2)
sol = sym.solve([eq1, eq2], (M_A, N_BD))
print(sol)
for s in sol:
    print(sol[s].evalf())

print(w_D_1.subs(sol))
print(w_D_2.subs(sol).evalf())

print(A_v.subs(sol))
print(A_v.subs(sol).evalf())

print(A_v_2.subs(sol))
print(A_v_2.subs(sol).evalf())