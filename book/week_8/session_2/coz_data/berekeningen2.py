import numpy
import sympy as sym
P1=4 #sym.Symbol('P1')#random(4,8,2)

P2=6 #sym.Symbol('P2')#random(3,9,2)

P3=sym.nsimplify(2.5) #sym.Symbol('P3')#random(1,3,.5)

P4=9 #sym.Symbol('P4') #random(5,10,1)

P5=sym.nsimplify(48) #sym.Symbol('P5') #random(20,40,5)
print(P5)

ans_6145211 = abs(1/1000*(-500*P1**2*P2*P3*P5+3*20000*P1*P4+3*20000*P2*P4)/P1/P2/(P1+P2))
print(ans_6145211)
ans_208021 = sym.nsimplify(1000)*(-(-P4/P1/1000+sym.nsimplify(1/60000)*(-P3*P5+30000*(-1/1000*P4/P1-1/1000*P4/P2+P5*P3*P1/120000)/(P1+P2))*P1)*P3+P5*P3**3/60000)  

print(ans_208021)