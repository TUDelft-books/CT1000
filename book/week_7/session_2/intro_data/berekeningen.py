import sympy as sym

EA, EI, F, L_BE, L_CF, L_EF = sym.symbols('EA EI F L_BE L_CF L_EF')
N_EF = sym.symbols('N_EF')
w_F = sym.symbols('w_F')

#L_BE = 6
#L_CF = 4
EI = 500000
EA = 20000
F = sym.nsimplify(45)
L_EF = sym.nsimplify(10)
L_BE = L_EF/2

Eq1 = sym.Eq(w_F, F * L_EF **3 / (EI) / 3 - N_EF * L_EF **3 / EI / 3)
N_EF_1 = sym.solve(Eq1, N_EF)[0]
display(N_EF_1)

Eq2 = sym.Eq(w_F - N_EF * L_BE / EA , N_EF * L_BE**3 / EI / 3 + L_BE **3 / EI / 3 * sym.nsimplify(45))
N_EF_2 = sym.solve(Eq2, N_EF)[0]
display(N_EF_2)

Eq3 = sym.Eq(N_EF_1, N_EF_2)
w_F_sol = sym.solve(Eq3, w_F)[0]
display(w_F_sol)
display(N_EF_1.subs(w_F, w_F_sol).evalf())