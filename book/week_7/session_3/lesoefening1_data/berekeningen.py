from pygame import K_2
import sympy as sym

L, EI, T = sym.symbols('L EI T')

L = 4
T = 73
EI = sym.nsimplify(4000)

K_el = EI / L * sym.Matrix([[4, 2], [2, 4]])
print(K_el)

K = EI / L * sym.Matrix([[12, 2, 2, 0],
                         [ 2, 8, 0, 2],
                         [ 2, 0, 4, 0],
                         [ 0, 2, 0, 4]])

K_2 = EI / L * sym.Matrix([[4, 2, 0, 0, 0],
                         [ 2, 12, 2, 2, 0],
                         [ 0, 2, 8, 0, 2],
                         [ 0, 2, 0, 4, 0],
                         [ 0, 0, 2, 0, 4]])

print(K_2)

F = sym.Matrix([0, T, 0, 0])


# Create augmented matrix and solve the system
augmented_matrix = K.row_join(sym.Matrix(F))
sol = sym.solve_linear_system_LU(augmented_matrix, sym.symbols('phi1 phi2 phi3 phi4'))
print(sol)
for key, value in sol.items():
    print(f"{key} = {value.evalf()}")