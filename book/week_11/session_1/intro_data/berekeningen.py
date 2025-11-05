import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
%config InlineBackend.figure_format = 'svg'

x_CD = 1.8
x_BC = 2.6
x_AB = 2.2
F = 10
q = 10
h = 0.300
b = 0.100
tl = 0.004
tf = 0.012

Ar = h* tl * 2 + b * tf * 2
print('Oppervlakte=',Ar)

Izz = 1/12 * tl * h **3 * 2 + 1/12 * b * tf **3 * 2 + 2 * b * tf * (h/2) **2

print("Buigtraagheidsmoment=",Izz)

M_B = -F*x_AB
M_C = -F*(x_AB+x_BC)+q*x_BC*0.5*x_BC
M_D = -F*(x_AB+x_BC+x_CD)+q*x_BC*(0.5*x_BC+x_CD)
V_B = -F
V_C = -F+q*x_BC

print("M_B=",M_B," , M_C=",M_C,',M_D = ',M_D,', V_B=',V_B,', V_C=',V_C)

#hoekpunt, midden

S_A = b * tf * h / 2
S_B = b * tf * h / 2 + 2 * tl * h/2 * h/4
S_E = b * tf * h / 2 + 2 * tl * h/4 * h/8*3
print('Statisch moment A',S_A,', B=',S_B)
tau_Ab = (V_C*1e3 * S_A )/ (2*tf*Izz)
tau_Ao = (V_C*1e3 * S_A )/ (2*tl*Izz)
tau_B = (V_C*1e3 * S_B )/ (2*tl*Izz)
tau_E = (V_C*1e3 * S_E )/ (2*tl*Izz)

print('Schuifspanning buiging tau_Ab=',tau_Ab,', tau_A0 =',tau_Ao,', tau_B =',tau_B,', tau_E =',tau_E)

sigma_buiging = - M_C*1e3 * (h/4) / Izz
print('sigma_buiging=',sigma_buiging)

tau = tau_E / 1e6
sigma_x = sigma_buiging / 1e6
sigma_y = 0

sigma_min = (sigma_y+sigma_x)/2-np.sqrt(((sigma_x-sigma_y)/2)**2+tau**2)
sigma_max = (sigma_y+sigma_x)/2+np.sqrt(((sigma_x-sigma_y)/2)**2+tau**2)
alpha = np.arctan(2*tau/(sigma_x-sigma_y))/2
tau_max = np.sqrt(((sigma_y-sigma_x)/2)**2+tau**2)
print('sigma_min=',sigma_min)
print('sigma_max=', sigma_max)
print(np.rad2deg(alpha))


plt.figure()
ax = plt.gca()
ax.set_aspect('equal')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_color('none')
plt.grid()
if sigma_min<0:
    plt.xlim([1.1*sigma_min,1.4*sigma_max])
else:
    plt.xlim([0.7*sigma_min,1.1*sigma_max])
plt.ylim([-1.1*tau_max,1.1*tau_max])
plt.xlabel('xx, yy')
ax.xaxis.set_label_coords(0.95, 0.55)
ax.yaxis.set_label_coords(0,0.95)
#plt.ylabel(r'$\tau$')
plt.plot(sigma_x,-tau,marker='o')
plt.plot(sigma_y,tau,marker='o')
#plt.show()
plt.plot([sigma_x,sigma_y],[-tau,tau])
plt.plot((sigma_x+sigma_y)/2,0,marker='o')
circle1 = plt.Circle([(sigma_x+sigma_y)/2,0],np.sqrt(((sigma_x-sigma_y)/2)**2+tau**2),fill=False)
ax.add_artist(circle1)
plt.plot(sigma_max,0,marker='o')
plt.plot(sigma_min,0,marker='o')
#plt.show()
plt.plot([sigma_y,sigma_x],[-tau,-tau],color='black')
plt.plot([sigma_y,sigma_y],[-tau,tau],color='black')
plt.plot(sigma_y,-tau,marker='o',color='black')
plt.plot([sigma_y,sigma_max],[-tau,0],color='black')


# Add curved arrow from sigma_y/2, -tau to the last line shown
arrow = patches.FancyArrowPatch((sigma_x/2, -tau), (sigma_x/2*np.cos(alpha), -tau+np.sin(alpha)*sigma_x/2), connectionstyle="arc3,rad=.3", color="black", arrowstyle='simple',mutation_scale=15)
ax.add_patch(arrow)
plt.show()



s_v = np.sqrt(sigma_min**2-sigma_min*sigma_max+sigma_max**2)
print('vloeispanning =',s_v)
#plt.show()