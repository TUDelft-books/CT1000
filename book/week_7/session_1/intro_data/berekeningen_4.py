import sympy as sym

M_D_AD, M_D_CD, M_D_DB, phi = sym.symbols('M_D_AD M_D_CD M_D_DB phi')

EI, T = sym.symbols('EI T')


EI = 120000
T = 29


eq1 = sym.Eq(phi, M_D_AD * 5 / 4/ EI)
M_D_AD_sol = sym.solve(eq1, M_D_AD)[0]
print("M_D_AD =", M_D_AD_sol)

eq2 = sym.Eq(phi, -M_D_CD * 5 / 3 / EI)
M_D_CD_sol = sym.solve(eq2, M_D_CD)[0]
print("M_D_CD =", M_D_CD_sol)

eq3 = sym.Eq(phi, -M_D_DB * 2 / 3 / EI - T * sym.S(2) / 6 / EI)
M_D_DB_sol = sym.solve(eq3, M_D_DB)[0]
print("M_D_DB =", M_D_DB_sol)

eq4 = sym.Eq(M_D_AD_sol - M_D_CD_sol - M_D_DB_sol + T, 0)
phi_sol = sym.solve(eq4, phi)[0]
print("phi =", phi_sol)
print("phi =", phi_sol.evalf())

print("M_D_AD =", M_D_AD_sol.subs(phi, phi_sol).evalf())
print("M_D_CD =", M_D_CD_sol.subs(phi, phi_sol).evalf())
print("M_D_DB =", M_D_DB_sol.subs(phi, phi_sol).evalf())