import sympy as sym

EI, q, L1, L2, M = sym.symbols('EI q L1 L2 M')

EI = sym.Rational(16, 3) * 10**3
print(EI)

L1 = 4
L2 = 6

q = 25

phi_1 = M * L1 / EI / 3 + q * L1**3 / EI / 24
phi_2 = - M * L2 / EI / 3

print(phi_1, phi_2)
eq = sym.Eq(phi_1, phi_2)

sol = sym.solve(eq, M)[0]
print(sol)

w = 5 / 384 * q * L1**4 / EI + 1 / 16 * sol * L1**2 / EI
w_2 = 1/16 * sol * L2**2 / EI

print(w)
print(w_2)

EI, q, L1, L2, A_v = sym.symbols('EI q L1 L2 A_v')

L1 = 4
L2 = 6
q = sym.nsimplify(25)
EI = sym.nsimplify(2.133333333333333333*3/6*5*1000)
print(EI)
print(EI.evalf())
#q = sym.nsimplify(25)
#EI = 80000*2/3

M_B = - q * L1**2 / 2 + A_v * L1
print(M_B)

phi_B = M_B * L2 / EI / 3
print(phi_B)
print(phi_B.evalf())
4
w_A = phi_B * L1 - q * L1**4 / 8 / EI + A_v * L1**3 / 3 / EI
print(w_A)
print(w_A.evalf())

eq = sym.Eq(w_A, 0)
sol = sym.solve(eq, A_v)[0]
print(sol)

print(M_B.subs(A_v, sol))