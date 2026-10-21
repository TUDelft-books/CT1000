import sympy as sym

L1, L2, L3, EA, EI, w_0, q = sym.symbols('L1 L2 L3 EA EI w_0 q')

L2 = sym.Integer(7)
L3 = sym.Integer(3)
L1 = sym.Integer(3)

EI = sym.Integer(62720) # kNm^2
EA = sym.Integer(7200*2) # kN

E = 1e9 # 1 GPa 1 G N /m^2
print(EI*1000/E*1e12)
print(EA*1000/E*1e6)

q = sym.Integer(32)

M_D = sym.symbols('M_D')

phi_D_AD = - M_D * L3 / EI

print('phi_D_AD: ', phi_D_AD)

print(phi_D_AD.subs(M_D, 316.2))

N_BC = q * L2 / 2 + M_D / L2

print('N_BC: ', N_BC)

w_C = N_BC * L1 / EA

print('w_C: ', w_C)

phi_D_CD = M_D * L2 / EI / 3 + q / 24 * L2**3 / EI + N_BC * L1 / EA / L2 

print(q / 24 * L2**3 / EI)
print(N_BC * L1 / EA / L2)

print('phi_D_CD: ', phi_D_CD)

eq1 = sym.Eq(phi_D_AD, phi_D_CD)

M_D_sol = sym.solve(eq1, M_D)[0]

print('solution: ', M_D_sol.expand())

print(phi_D_AD.subs(M_D, M_D_sol).expand())

print(N_BC.subs(M_D, M_D_sol)*L1/EA)
