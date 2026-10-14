import sympy as sym

P1=sym.nsimplify(3/2) #random(1,2,0.5)

P2=1 #random(1,2,0.5)

P3=9 * 34*5/10 #sym.symbols('P3') #random(18,450,9)

print(P3)

P4=35 #sym.symbols('P4') #10

ans_a = (2*P3*P2)/9
ans_b = (5*P3*P2)/9
ans_c = (2*P3*P2)/(15*P1)
ans_d = (P3*P2*P2*(3*P2+5*P1))/P4/9

print(ans_a, ans_b, ans_c, ans_d)