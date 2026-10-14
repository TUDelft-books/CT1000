import sympy as sym

B_v, N_C = sym.symbols("B_v N_C")

EA = sym.nsimplify(125000)
EI = sym.nsimplify(768000)

V_B_AB = 90 + N_C / 5 * 3
N_AB = - B_v - N_C / 5 * 4

w_B = - N_AB * 4 / EA
print('w_B =', w_B*1000, 'approx', (w_B*1000).evalf())

w_B_2 = V_B_AB * 4 **3 / 3 / EI
print('w_B_2 =', w_B_2*1000, 'approx', (w_B_2*1000).evalf())

delta_L = N_C * 5 / EA
print('delta_L =', delta_L*1000, 'approx', (delta_L*1000).evalf())

w_C = w_B_2 / 5 * 3 + delta_L + w_B / 5 * 4
print('w_C =', w_C*1000, 'approx', (w_C*1000).evalf())

eq1 = sym.Eq(w_B, 0)
eq2 = sym.Eq(w_C, 0)

sol = sym.solve([eq1, eq2], (B_v, N_C))
print(sol)