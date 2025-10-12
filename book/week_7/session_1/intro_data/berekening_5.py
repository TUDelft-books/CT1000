import sympy as sym

import numpy as np

EI = sym.nsimplify(120000)

K_AD = EI/ 5 * sym.Matrix([[4, 2], [2, 4]])
K_CD = EI/ 5 * sym.Matrix([[4, 2], [2, 4]])
K_DB = EI / 2 * sym.Matrix([[4, 2], [2, 4]])

print("K_AD =", K_AD)
print("K_CD =", K_CD)
print("K_DB =", K_DB)

K_tot = sym.Matrix([[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])

for i, row in enumerate([0,3]):
    for j, col in enumerate([0,3]):
        K_tot[row,col] += K_AD[i,j]
print("K_tot after DB =", K_tot)

for i, row in enumerate([2,3]):
    for j, col in enumerate([2,3]):
        K_tot[row,col] += K_DB[i,j]
print("K_tot after CD =", K_tot)

for i, row in enumerate([3,1]):
    for j, col in enumerate([3,1]):
        K_tot[row,col] += K_CD[i,j]

print("K_tot after AD =", K_tot)

M_A = sym.symbols('M_A')

F = sym.Matrix([M_A, -29, 0, 29])

print("F =", F)

K_red = K_tot[1:4, 1:4]
F_red = F[1:4, 0]

# inverse K_red
u = K_red.inv() * F_red
print("u =", u)
for i, row in enumerate([1,2,3]):
    print(f"u_{row} =", u[i].evalf())