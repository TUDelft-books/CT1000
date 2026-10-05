import sympy as sym

EI = sym.symbols('EI')
EA = sym.symbols('EA')

EI = sym.nsimplify(20e3)
EA = sym.nsimplify(10e3)
q = sym.symbols('q')
q = 8 #sym.S(5)
q_sol = 8 #5
N_CD = sym.symbols('N_CD')

deltaT_AC_eps = 50
deltaT_AC_kap = 8
deltaT_CD = 50
h = sym.nsimplify(0.4)
alpha = sym.nsimplify(1e-5)

kappa_AC = sym.nsimplify(1e-5) * deltaT_AC_kap / h
print(kappa_AC, kappa_AC.evalf())

eps_AC = sym.nsimplify(1e-5) * deltaT_AC_eps

print(eps_AC, eps_AC.evalf())