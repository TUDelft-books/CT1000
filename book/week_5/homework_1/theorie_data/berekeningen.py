import sympy as sym
sym.nsimplify(2/2.5e3)

sym.nsimplify(6 * 2 * 0.5 / 2.5e3)

B_v = sym.symbols('B_v')

w_C = -sym.nsimplify(6 * 2 * 0.5 / 2.5e3) + B_v *2 / 2500
w_B = -sym.nsimplify(6 * 2 * 0.5 / 2.5e3) + B_v * 2 *2 / 2500
print(w_B)
print(w_B.evalf())

eq = sym.Eq(w_B, 0)

B_v_solution = sym.solve(eq, B_v)[0]
print(B_v_solution)

w_C_solution = w_C.subs(B_v, B_v_solution)
print(w_C_solution.evalf())