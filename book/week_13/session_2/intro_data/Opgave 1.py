from mmap import mmap
import numpy as np

b = 200
h = 200
t = 15
h1 = 50

sigma_a = h1*t*(0.5*h-0.5*h1)
sigma_b = sigma_a + b*t*0.5*h
sigma_d = sigma_b = 0.5*h*t*1/4*h

F1 = sigma_a*2/3*h1
F2 = sigma_a*b+(sigma_b-sigma_a)*0.5*b
F3 = sigma_b*h+2/3*(sigma_d-sigma_b)*h

x = (F2 * h + 2 * F1 * b) / (F3-2*F1)

print(F1,F2,F3,x)