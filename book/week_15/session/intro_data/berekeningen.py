import sympy as sym

w_B = sym.symbols('w_B')

EI, EA, F = sym.symbols('EI EA F')

EI = sym.nsimplify(192*4000)
EA = sym.nsimplify(125000)

F = sym.nsimplify(45*2)

print(f'EI = {EI}')
print(f'EA = {EA}')
print(f'F = {F}')

V_B = sym.symbols('V_B')
N_BC = sym.symbols('N_BC')

w_B_1 = sym.Eq(w_B, V_B * 4**3 / (3 * EI))
V_B = sym.solve(w_B_1, V_B)[0]
print(f'V_B = {V_B}')

H_B = sym.Eq(w_B / 5 * 3, N_BC * 5 / EA)
N_BC = sym.solve(H_B, N_BC)[0]
print(f'N_BC = {N_BC}')

sumF = sym.Eq(0, F - V_B - N_BC*3/5)
w_sol = sym.solve(sumF, w_B)[0]
print(f'w_B = {w_sol}')

A_V = EI / 4**3 * 3 * w_sol
print(f'A_V = {A_V}')