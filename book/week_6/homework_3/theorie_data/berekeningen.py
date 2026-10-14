import sympy as sym
Av, Ah, EI, EA, F, L = sym.symbols('Av Ah EI EA F L')
L = 6
EI = 5000
F = sym.S(30)

M_C = F * L / 2
M_B = Av * L
phi_B = - M_C * L / 2 / EI / 6 - M_B * L / 2 / EI / 3 #linksom positief
w_A = - (phi_B * L - Av * L**3 / EI / 3)

display(M_C)
display(M_C.evalf())
display(M_B)
display(M_B.evalf())
display(phi_B)
display(phi_B.evalf())
display(w_A)
display(w_A.evalf())

eq = sym.Eq(w_A, 0)
sol = sym.solve(eq, Av)
display(sol[0])

display(M_B.subs(Av, sol[0]))