import sympy as sym

A_v = sym.nsimplify(29.5/8)
C_v = sym.nsimplify(168.5/6)

B_v = 11 * 6 - C_v + A_v
print(B_v)
print(B_v.evalf())