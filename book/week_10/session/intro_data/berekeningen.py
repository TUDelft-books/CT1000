import sympy as sym

Bv = sym.symbols('Bv')

EA = sym.nsimplify(45000)

N_AD = -Bv / 4 * 5
N_BD = Bv
N_CD = -Bv / 4 * 3

L_AD = sym.nsimplify(sym.sqrt((9/2)**2 + 6**2))
print(L_AD)

deltaL_AD = N_AD * L_AD / (EA)
deltaL_BD = N_BD * 6 / (EA)
deltaL_CD = N_CD * 6 / (EA)

print('deltaL_AD =', deltaL_AD)
print('deltaL_BD =', deltaL_BD)
print('deltaL_CD =', deltaL_CD)