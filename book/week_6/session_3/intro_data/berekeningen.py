import sympy as sym

q = sym.symbols('q')

q = 11
EI = sym.symbols('EI')
M_D, M_B_BD, M_B_AB, M_B_BC = sym.symbols('M_D M_B_BD M_B_AB M_B_BC')

eq1 = sym.Eq(M_D * 6 / 3 / EI, - M_D * 8 / 3 / EI - M_B_BD * 8 / 6 / EI)
eq2 = sym.Eq(M_B_AB * 10 / 3 / EI, M_B_BD * 8 / 3 / EI + M_D * 8 / 6 / EI)
eq3 = sym.Eq(M_B_AB * 10 / 3 / EI, M_B_BC * 6 / 3 / EI + q * 6 ** 3 / EI / 24)
eq4 = sym.Eq(M_B_BD + M_B_AB + M_B_BC,0)
display(eq1, eq2, eq3)

sol = sym.solve([eq1, eq2, eq3, eq4], (M_D, M_B_BD, M_B_AB, M_B_BC))
display(sol)

print(1/8 * 11 * 6**2)
print(-59/2/2+1/8*11*6**2)
print(-59/2/2+1/8*11*6**2*2)