import sympy as sym

b1, b2, h1, h2, h3 = sym.symbols('b1 b2 h1 h2 h3', positive=True)

b1 = sym.nsimplify(300)
h1 = sym.nsimplify(100)
b2 = sym.nsimplify(150)
h2 = sym.nsimplify(50)
h3 = sym.nsimplify(250)

A = b1*h1 + b2 * h3 + (b1 + b2) * h2 / 2

print("A=", A, "\approx", A.evalf())

Sz = b1*h1*h1/2 + (b1 + b2) * h2 / 2 * (h1 + h2/3 * (b1 + 2*b2)/(b1 + b2)) + b2 * h3 * (h1 + h2 + h3/2)

z_bar = Sz / A

print("z_bar=", z_bar.simplify(), "\approx", z_bar.evalf())

Izz = b1*h1**3/12 + b1*h1*(z_bar - h1/2)**2 + \
      b2*h3**3/12 + b2*h3*(z_bar - (h1 + h2 + h3/2))**2 + \
      (b2**2 + 4 * b1 * b2 + b1**2)/(b1 + b2)/36 * h2**3 + (b1 + b2) * h2 / 2 * (z_bar - (h1 + h2/3 * (b1 + 2*b2)/(b1 + b2)))**2

print("I_zz=", Izz.simplify(), "\approx", Izz.evalf())

z_snede = sym.nsimplify(250)
Sz = ((h1 + h2 + h3 + z_snede)/2 - z_bar) * (h1 + h2 + h3 - z_snede) * b2

print(Sz)
print(Sz.evalf())

V = sym.nsimplify(600000)

tau = V * Sz / (Izz * b2)
print("tau=", tau.simplify(), "\approx", tau.evalf())

Bv = V / 1000

L = sym.symbols('L', positive=True)
L = sym.nsimplify(8)
q = sym.symbols('q', positive=True)

eq = sym.Eq(Bv * L - q * (L*5/8)**2 / 2, 0)
sol = sym.solve(eq, q)
print("q=", sym.simplify(sol[0]), "\approx", sol[0].evalf())

M = Bv * L * 1000 / 8 * 3 * 1000

print("M=", M, "\approx", M.evalf())

sigma = M * (z_snede - z_bar) / Izz
print("sigma=", sigma.simplify(), "\approx", sigma.evalf())

alpha = sym.atan(tau / ((sigma - 0)/2))/2

print("alpha=", alpha.simplify(), "\approx", (alpha*180/sym.pi).evalf())

sigma_1 = sigma/2 + sigma*sym.cos(2*alpha)/2 + tau*sym.sin(2*alpha)
sigma_2 = sigma/2 - sigma*sym.cos(2*alpha)/2 - tau*sym.sin(2*alpha)
print("sigma_1=", sigma_1.simplify(), "\approx", sigma_1.evalf())
print("sigma_2=", sigma_2.simplify(), "\approx", sigma_2.evalf())

sigma_1_2 = sigma/2 + sym.sqrt((sigma/2)**2 + tau**2)
print("sigma_1_2=", sigma_1_2.simplify(), "\approx", sigma_1_2.evalf())