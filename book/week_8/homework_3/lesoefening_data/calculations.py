import sympy as sym
sym.init_printing()

T, L1, L2, alpha, Delta_T, h = sym.symbols('T L1 L2 alpha Delta_T h')

Delta_T = sym.S(30)
h = sym.nsimplify(0.2)
alpha = sym.nsimplify(0.0001)
L1 = sym.S(8)
T = sym.S(6)

EI = sym.symbols('EI')

EI = sym.nsimplify(800/3)

x = sym.symbols('x')

C_1, C_2, C_3, C_4 = sym.symbols('C_1 C_2 C_3 C_4')

q = 0

C_2 = T
C_4 = sym.S(0)

V = -sym.integrate(q, x) + C_1

print('V = ', V)

M = sym.integrate(V, x) + C_2

print('M = ', M)

kappa_T = - alpha * Delta_T / h

print(kappa_T.evalf(), (T/EI).evalf())

kappa = M / EI + kappa_T

print('kappa = ', kappa.evalf())

phi = sym.integrate(kappa, x) + C_3

w = -sym.integrate(phi, x) + C_4

print('w =',w.evalf())

sym.pprint(w)

eq1 = sym.Eq(w.subs(x,0),0)
eq2 = sym.Eq(w.subs(x,L1),0)
eq3 = sym.Eq(phi.subs(x,L1),0)
eq4 = sym.Eq(M.subs(x,0),T)


sol = sym.solve([eq1, eq2, eq3, eq4], (C_1, C_3))
print(sol[C_1].evalf(), sol[C_3].evalf())

print('V = ',V.subs(sol))
print('w = ',w.subs(sol).evalf())

M_0 = sym.solve(sym.Eq(M.subs(sol),0), x)[0]
print('M = ', M.subs(sol).evalf())
print('M_0 = ', M_0)
kappa_0 =sym.solve(sym.Eq(kappa.subs(sol),0), x)[0]
print('kappa_0 = ', kappa_0)
print('kappa_0 = ', kappa_0.evalf())

sym.plot(-M.subs(sol), (x, 0, L1), title='Verplaatsing van de balk', ylabel='Verplaatsing (m)', xlabel='Lengte (m)', show=True)