import sympy as sym

q, L, EA, EI, Bv, Bh = sym.symbols('q L EA EI Bv Bh', real=True)
L2 = sym.symbols('L2', real=True)

L2 = sym.Integer(3)

n = sym.symbols('n', real=True)

EI = sym.Integer(1200)

EA = 2 * EI / 10

print('EA =', EA)

q = sym.Integer(162) / 10

print(q)

L = sym.Integer(6)

x = sym.symbols('x', real=True)
delta_L = sym.integrate(q * (L - x) / (EA), (x, 0, L))

print('delta_L =', delta_L)

w_C = delta_L + Bv * L / EA

M_C = Bh * L2 + Bv * L2 / 3 * 4

print('M_C =', M_C)

u_C = Bh * L**3 / EI / 3 + M_C * L**2 / EI / 2

theta_C = Bh * L**2 / EI / 2 + M_C * L / EI

print('theta_C =', theta_C)
print('u_C =', u_C)
print('w_C =', w_C)

w_B = w_C + theta_C * L2 / 3 * 4
u_B = u_C + theta_C * L2

print('w_B =', w_B)
print('u_B =', u_B)

sol = sym.solve([w_B, u_B], (Bv, Bh))
print(sol)

print('w_C =', w_C.subs({Bv: sol[Bv], Bh: sol[Bh]}))
print('u_C =', u_C.subs({Bv: sol[Bv], Bh: sol[Bh]}))
print('M_C =', M_C.subs({Bv: sol[Bv], Bh: sol[Bh]}))
print('theta_C =', theta_C.subs({Bv: sol[Bv], Bh: sol[Bh]}))