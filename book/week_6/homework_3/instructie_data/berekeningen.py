import sympy as sym

Bv = sym.symbols('Bv')

F = sym.symbols('F')

EI = sym.symbols('EI')
EA = sym.symbols('EA')

L1, L2, L3, L4 = sym.symbols('L1 L2 L3 L4')

L1 = 4
L2 = 4

EA = 4000
EI = 64000

F = sym.S(84)

q = F / 8
print('q =', q)

L5 = sym.symbols('L5')

L5 = 8

N_BD = - Bv
N_CG = F / 2
V_D = F / 2 + Bv
print('V_D =', V_D)
M_D = F / 2 * L2
print('M_D =', M_D)

w_D = V_D * L1 **3 / 3 / EI + M_D * L1**2 / 2 / EI
print('w_D =', w_D )
print('w_D =', w_D.evalf() )

phi_D = V_D * L1 **2 / 2 / EI + M_D * L1 / EI

print('phi_D =', phi_D)
print('phi_D =', phi_D.evalf() )

w_E = w_D + phi_D * L2 + F/2 * L2 **3 / 3 / EI

print('w_E =', w_E)
print('w_E =', w_E.evalf() )

deltaL_CG = F/2 * L5 / EA

print('deltaL_CG =', deltaL_CG)
deltaL_BD = N_BD * L5 / EA

print('deltaL_BD =', deltaL_BD)

w_B = w_D - deltaL_BD

print('w_B =', w_B)
print('w_B =', w_B.evalf() )

sol = sym.solve(sym.Eq(w_B, 0), Bv)[0]

print('Bv =', sol)

print('Check w_E =', w_E.subs(Bv, sol))
print('Check w_E =', w_E.subs(Bv, sol).evalf())
print('Check w_B =', w_B.subs(Bv, sol))
print('Check deltaL_CG =', deltaL_CG.subs(Bv, sol))
print('Check deltaL_BD =', deltaL_BD.subs(Bv, sol))
print('Check N_BD =', N_BD.subs(Bv, sol))
print('Check V_D =', V_D.subs(Bv, sol))
print('Check M_D =', M_D.subs(Bv, sol))
print('Check w_D =', w_D.subs(Bv, sol))
print('check w_D =', w_D.subs(Bv, sol).evalf())
print('Check phi_D =', phi_D.subs(Bv, sol))
print('check phi_D =', phi_D.subs(Bv, sol).evalf())

w_G = deltaL_CG

print('w_G =', w_G)
print('w_G =', w_G.evalf())
w_F = (w_G + w_E.subs(Bv, sol) ) / 2 + F * (L1*2)**3 / 48 / EI

print('w_F =', w_F)
print('w_F =', w_F.evalf() )

M_F = q * 8 **2 / 8

print('M_F =', M_F)

M_A = F / 2 * L2 * 2 + Bv * L1
print('M_A =', M_A.subs(Bv, sol))

V_A = F / 2 + Bv
print('V_A =', V_A.subs(Bv, sol))

print((276 - 168)/4)