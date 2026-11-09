import sympy as sym

h, t , F, M , L= sym.symbols('h t F M L', real=True, positive=True)

F = sym.Integer(80)

h = sym.Integer(5)/10

t = sym.Integer(15)/1000

L = sym.Integer(4)

M = F * 3/4 * L
print(M)

V = F * 3/4
print(V)

A = h * t * sym.sqrt(2) * 2
print(A*10000)

Izz = t*sym.sqrt(2)*h**3/12 * 2

print(Izz*100000000)

sigma = -M * 1000 * h / 4 / Izz
tau = V * 1000 * t * sym.sqrt(2) * h/8 * ( h/4) / t / Izz

print('sigma:', sigma, sigma.evalf())
print('tau:', tau)

sigma_1 = sigma/2 + sym.sqrt( sigma**2 + tau**2 * 4 ) / 2
print(sigma_1, sigma_1.evalf())
sigma_2 = sigma/2 - sym.sqrt( sigma**2 + tau**2 * 4 ) / 2
print(sigma_2, sigma_2.evalf())
sigma_3 = 0

sigma_0 = (sigma_1 + sigma_2 + sigma_3) / 3

print('sigma_0:', sigma_0, sigma_0.evalf())

s = sym.Matrix([[sigma_1 - sigma_0], [sigma_2 - sigma_0], [sigma_3 - sigma_0]])
print(s,s.evalf())

s_max = sym.sqrt( ((sigma_1 - sigma_2)**2 + (sigma_2 - sigma_3)**2 + (sigma_3 - sigma_1)**2 ) / 3)
print(s_max)

theta = sym.atan(2*tau/(sigma_1 - sigma_2))/2
print('theta:', theta, theta.evalf())
print('theta:', theta*180/sym.pi, (theta*180/sym.pi).evalf())