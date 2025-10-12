import sympy as sym

L1, L2, q, L3, N_CD, w_D, EI, EA = sym.symbols('L1 L2 q L3 N_CD w_D EI EA')

L1 = 4
L2 = 3
L3 = 5

q = sym.nsimplify(23.625*4)

EA = sym.nsimplify(1250)
EI = sym.nsimplify(42000)

M_B = N_CD * L2 * -1

phi_B = q * L1 **3 / 24 / EI +  M_B * L1 / (3 * EI)

print("phi_B =", phi_B)

eq1 = sym.Eq(w_D, - phi_B * L2 + N_CD * L2 **3 / (3 * EI))

N_CD_BC = sym.solve(eq1, N_CD)[0]
print("N_CD_BC =", N_CD_BC)

eq2 = sym.Eq(w_D, - N_CD * L3 / EA)

N_CD_CD = sym.solve(eq2, N_CD)[0]
print("N_CD_CD =", N_CD_CD)

eq3 = sym.Eq(N_CD_BC, N_CD_CD)
print(eq3)
w_D_sol = sym.solve(eq3, w_D)[0]
print("w_D =", w_D_sol)
print("w_D =", w_D_sol.evalf())

print("N_CD =", N_CD_BC.subs(w_D, w_D_sol))
print("M_B =", M_B.subs(N_CD, N_CD_BC.subs(w_D, w_D_sol)))