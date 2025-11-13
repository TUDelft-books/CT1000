Izz = 655e6

tau_G = -3e3 * -250*10*286 / 20 / Izz
print(tau_G)

tau_C = -3e3 * -250*20*(286-500) / 40 / Izz
print(tau_C)

sigma_G = +6.73
tau_G = -tau_G
sigma_G_1 = 1/2 * (sigma_G + 0) + ((1/2 * (sigma_G + 0))**2 + tau_G**2)**0.5
sigma_G_2 = 1/2 * (sigma_G + 0) - ((1/2 * (sigma_G + 0))**2 + tau_G**2)**0.5
print(sigma_G_1, sigma_G_2)

sigma_H = +6.73
tau_G = 0
sigma_H_1 = 1/2 * (sigma_H + 0) + ((1/2 * (sigma_H + 0))**2 + tau_G**2)**0.5
sigma_H_2 = 1/2 * (sigma_H + 0) - ((1/2 * (sigma_H + 0))**2 + tau_G**2)**0.5
print(sigma_H_1, sigma_H_2)

sigma_I = -2
tau_I = +0.35
sigma_I_1 = 1/2 * (sigma_I + 0) + ((1/2 * (sigma_I + 0))**2 + tau_I**2)**0.5
sigma_I_2 = 1/2 * (sigma_I + 0) - ((1/2 * (sigma_I + 0))**2 + tau_I**2)**0.5
print(sigma_I_1, sigma_I_2)

sigma_C = -8.53
tau_C = -tau_C
sigma_C_1 = 1/2 * (sigma_C + 0) + ((1/2 * (sigma_C))**2 + tau_C**2)**0.5
sigma_C_2 = 1/2 * (sigma_C + 0) - ((1/2 * (sigma_C))**2 + tau_C**2)**0.5
print(sigma_C_1, sigma_C_2)