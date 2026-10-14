import sympy as sym

alpha, EA, F, L1, delta_T = sym.symbols('alpha EA F L1 delta_T')

alpha = sym.nsimplify(0.0002)
EA = sym.nsimplify(15000)
delta_T = sym.nsimplify(12.1)

L1 = 5

F = 0#sym.Rational(80)

B_v = sym.symbols('B_v')

N_CD = (-F * L1 / 2 + B_v * L1) / (L1 * 2) * sym.sqrt(5)
print(N_CD)

deltaL_CD = N_CD * L1 / 2 * sym.sqrt(5) / EA + alpha * delta_T * L1 / 2 * sym.sqrt(5)

N_AD = (N_CD / sym.sqrt(5) * 2 + F ) / 2 * sym.sqrt(5)
print(N_AD)

deltaL_AD = N_AD * L1 /2 * sym.sqrt(5) / EA + alpha * delta_T * L1 / 2 * sym.sqrt(5)
print(deltaL_AD)

N_BD = - B_v

w_C_h = deltaL_AD * sym.sqrt(5) / 4 - deltaL_CD * sym.sqrt(5) / 4
w_C_v = deltaL_AD * sym.sqrt(5) /2 + deltaL_CD * sym.sqrt(5) / 2

Delta_L_BD = N_BD * L1 / 2 / EA

w_B_v = w_C_v - Delta_L_BD - alpha * delta_T * L1 / 2

print(w_B_v)

sol = sym.solve(sym.Eq(w_B_v,0), B_v)[0]

print(sol,sol.evalf())

print(deltaL_AD.subs(B_v, sol),deltaL_AD.subs(B_v, sol).evalf())
print(deltaL_CD.subs(B_v, sol),deltaL_CD.subs(B_v, sol).evalf())
print(w_C_h.subs(B_v, sol),w_C_h.subs(B_v, sol).evalf())
print(w_C_v.subs(B_v, sol),w_C_v.subs(B_v, sol).evalf())
print(N_AD.subs(B_v, sol),N_AD.subs(B_v, sol).evalf())
print(N_CD.subs(B_v, sol),N_CD.subs(B_v, sol).evalf())

