import sympy as sym

b, h, t = sym.symbols('b h t')

b = sym.nsimplify(500)
h = sym.nsimplify(600)
t = sym.nsimplify(12)

A = b * t + 2 * (h/4*5 * t)
print(f'A = {A}')

NC_z = sym.simplify(h/4*5*t*2*h/2 / (h/4*5*t*2 + b*t))
print(f'NC_z = {NC_z}')

I_zz = sym.nsimplify(1/12 * b * t**3 + b * t * NC_z**2 + 2 * (1/12 * t*5/4 * h**3 + h/4*5 * t * (h/2 - NC_z)**2))
print(f'I_zz = {I_zz}')

F, a, L = sym.symbols('F a L')

F = sym.nsimplify(420.032 * 150)
print(f'F = {F} = {F.evalf()} N')

a = sym.nsimplify(600)

L = sym.nsimplify(10000)

tau_V = sym.simplify(F * b*t*NC_z / I_zz / 2 / t)
print(f'tau_V = {tau_V} = {tau_V.evalf()} MPa')

tau_M = F * a / 2 / t / (b * h / 2)
print(f'tau_M = {tau_M} = {tau_M.evalf()} MPa')

sigma_M = F * L * NC_z / I_zz
print(f'sigma_M = {sigma_M} = {sigma_M.evalf()} MPa')

nu = sym.nsimplify(0.3)
E = sym.nsimplify(210000)

sigma_yy = sigma_M

sigma_xy = tau_M + tau_V

sigma_xx = 0

eps_xx = (1/E) * (sigma_xx - nu * sigma_yy)
eps_yy = (1/E) * (sigma_yy - nu * sigma_xx)
eps_xy = (1 + nu) / E * sigma_xy

print(f'eps_xx = {eps_xx} = {eps_xx.evalf()} ')
print(f'eps_yy = {eps_yy} = {eps_yy.evalf()} ')
print(f'eps_xy = {eps_xy} = {eps_xy.evalf()} ')

eps_1 = (eps_xx + eps_yy) / 2 + sym.sqrt( ((eps_xx - eps_yy)/2)**2 + eps_xy**2 )
eps_2 = (eps_xx + eps_yy) / 2 - sym.sqrt( ((eps_xx - eps_yy)/2)**2 + eps_xy**2 )

print(f'eps_1 = {eps_1} = {eps_1.evalf()} ')
print(f'eps_2 = {eps_2} = {eps_2.evalf()} ')

alpha = sym.atan2(2*eps_xy, eps_xx - eps_yy) / 2

print(f'alpha = {alpha} = {(alpha * 180 / sym.pi).evalf()} graden')

eps_xx_rot = (eps_xx + eps_yy) / 2 + (eps_xx - eps_yy) / 2 * sym.cos(2*alpha) + eps_xy * sym.sin(2*alpha)
print(f'eps_xx_rot = {eps_xx_rot} = {eps_xx_rot.evalf()} ')