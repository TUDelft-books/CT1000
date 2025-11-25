import sympy as sym
import numpy as np

b = 200
h = 200
t = 15
h1 = 50

sigma_a = h1*t*(0.5*h-0.5*h1)
sigma_b = sigma_a + b*t*0.5*h
sigma_c = sigma_b + 0.25*h*t*3/8*h
sigma_d = sigma_b + 0.5 * h *t * 0.25 * h

F1 = sigma_a*2/3*h1
F2 = sigma_a*b+(sigma_b-sigma_a)*0.5*b
F3 = sigma_b*h+2/3*(sigma_d-sigma_b)*h

x = (F2 * h + 2 * F1 * b) / (F3-2*F1)

print(F1,F2,F3,x)

V = 2000
Izz =(1/12 * 15 * 200**3 
    + 2 * (1/12 * 200 * 15**3 + 15 * 200 * 100**2) 
    + 2 * (1/12 * 15 * 50**3 + 50 * 15 * 75**2)) 

print(Izz)


tau_1 = sigma_a * V / Izz / t
tau_2 = sigma_b * V / Izz / t
tau_3 = sigma_c * V / Izz / t
tau_4 = sigma_d * V / Izz / t
print(tau_1, tau_2, tau_3, tau_4)

x = sym.symbols('x')

sigma_a_2 = (x)*t*(h1 + x/2)
print(sigma_a, sigma_a_2.subs(x,h1))

F1_2 = sym.integrate(sigma_a_2, (x, 0, h1))
print(F1_2)

F2 = sigma_a*b+(sigma_b-sigma_a)*0.5*b
F3 = sigma_b*h+2/3*(sigma_d-sigma_b)*h

x2 = (F2 * h + 2 * F1_2 * b) / (F3-2*F1_2)

print(x2)