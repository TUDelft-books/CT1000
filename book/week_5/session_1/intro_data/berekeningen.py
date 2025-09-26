EA = sym.nsimplify(200e9*25e-6)

import sympy as sym

N_BC = sym.Symbol('N_BC')
N_BE = sym.Symbol('N_BE')

eq1 = sym.nsimplify(sym.Eq(N_BC * 3.6 / (3.6**2 + 1.5**2)**0.5 * 1.5 - 4000 * (1.5+1.5) + N_BE * 3.6 / (3.6**2 + (1.5 + 1.5 + 1.8)**2)**0.5 * (1.5+1.5+1.8), 0))

N_BC_sol = sym.solve(eq1, N_BC)[0]
display(N_BC_sol)

w_C = N_BC_sol * sym.nsimplify((3.6**2 + 1.5**2)**0.5 / EA / 3.6 * (3.6**2 + 1.5**2)**0.5)
display(w_C)

w_E_1 = w_C / sym.nsimplify((3 / 2)) * sym.nsimplify((4+8/10))
display(w_E_1)

w_E_2 = N_BE * sym.nsimplify((3.6**2 + (1.5 + 1.5 + 1.8)**2)**0.5 / EA / 3.6 * (3.6**2 + (1.5 + 1.5 + 1.8)**2)**0.5)

display(w_E_2)

eq2 = sym.Eq(w_E_1, w_E_2)
N_BE_sol = sym.solve(eq2, N_BE)[0]
display(N_BE_sol.evalf())
display(N_BE_sol)
display(N_BC_sol.subs(N_BE, N_BE_sol).evalf())
display(N_BC_sol.subs(N_BE, N_BE_sol))

display(w_E_2.subs(N_BE, N_BE_sol).evalf())

display((sym.atan(w_E_2.subs(N_BE, N_BE_sol) / sym.nsimplify((4+8/10)))*180/sym.pi).evalf())