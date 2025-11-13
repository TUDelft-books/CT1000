import numpy as np
A = 100*10+500*10+100*10*2+500*10+250*10*2+np.pi*100*10
print(A)

z_c = (100*10*50+500*10*100+2*100*10*150+500*10*200+2*250*10*300+np.pi*100*10*(400 - 2 / np.pi * 100))/A
print(z_c)
Izz = (1/12)*10*100**3 + 10*100*(z_c-50)**2 + (1/12)*500*10**3 + 500*10*(z_c-100)**2 + 2*(1/12)*10*100**3 + 2*10*100*(z_c-150)**2 + (1/12)*500*10**3 + 500*10*(z_c-200)**2 + 2*(1/12)*10/4*5*200**3 + 2*10*250*(z_c-300)**2 + (np.pi/2-4/np.pi)*100**3*10+np.pi*100*10*(400-z_c - 2/np.pi * 100)**2
Iyy = (1/12)*100*10**3 + 1/12 * 10 * 500 **3 + 1/12 * 100 * 10 **3 * 2 + 100 * 10 * 250**2 * 2 + 1/12*10*500**3 + 1/12*10/3*5*150**3*2 + 10*250 * 2 * 175**2 + 1/2 * np.pi * 100 **3 * 10
print(Izz, Iyy)

import sympy as sym

a, b = sym.symbols('a b')

eq1 = sym.Eq(-z_c + 200, a * -250 + b)
eq2 = sym.Eq(400-z_c, -100* a + b)

sol = sym.solve((eq1, eq2), (a, b))
display(sol)
a_2 = sol[a]
b_2 = sol[b]

x = sym.symbols('x')
y_2 = sym.solve(sym.Eq(a_2*x+b_2,0), x)[0]
print(y_2)

import sympy as sym

a, b = sym.symbols('a b')

eq1 = sym.Eq(-z_c, a * 0 + b)
eq2 = sym.Eq(-z_c+100, 250 * a + b)

sol = sym.solve((eq1, eq2), (a, b))
display(sol)
a_4 = sol[a]
b_4 = sol[b]

x = sym.symbols('x')
y_4 = sym.solve(sym.Eq(a_4*x+b_4,0), x)[0]
print(y_4)



e_y_1 = -Iyy / (A * -250)
print(e_y_1, 0)
e_y_2 = -Iyy / (A * y_2)
e_z_2 = -Izz / (A * b_2)
print(e_y_2, e_z_2)
e_z_3 = -Izz / (A * (400 - z_c))
print(0,e_z_3)
print(-e_y_2, e_z_2)
e_y_4 = -Iyy / (A * y_4)
e_z_4 = -Izz / (A * b_4)
print(e_y_4, e_z_4)
e_z_5 = -Izz / (A * -z_c)
print(0, e_z_5)
print(-e_y_4, e_z_4)