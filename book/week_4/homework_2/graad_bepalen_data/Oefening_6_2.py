#plotter from https://github.com/lisette-924/ANS
from plotter import *

A = Point(0,0)
B = Point(2,0)
C = Point(5,0)
D = Point(6,0)
E = Point(8,0)
F = Point(9,0)

s = Structure()
s.add_beam(Beam(A, F))
s.add_hinge(B)
s.add_hinge(C)
s.add_hinge(E)
s.add_support(Support(A, 'fixed', angle=-90))
s.add_support(Support(B, 'roller'))
s.add_support(Support(D, 'pinned'))
s.add_support(Support(F, 'roller'))
s.add_distributedload(DistributedLoad(B, D,5,5,alternative_label_begin = '', alternative_label_end = ''))
plot(s,seed='1')

margin = 8
margin2 = 1
A = Point(0,0)
B1 = Point(2,0)
B2 = Point(B.x + margin, 0)
C1 = Point(C.x + margin, 0)
C2 = Point(C.x + margin*2, 0)
D = Point(D.x + margin*2, 0)
E1 = Point(E.x + margin*2, 0)
E2 = Point(E.x + margin*3, 0)
F = Point(F.x + margin*3, 0)

s = Structure()
s.add_beam(Beam(A, B1))
s.add_beam(Beam(B2, C1))
s.add_beam(Beam(C2, E1))
s.add_beam(Beam(E2, F))

s.add_hinge(B1)
s.add_hinge(C2)
s.add_hinge(E1)

s.add_distributedload(DistributedLoad(B2, C1,5,5,alternative_label_begin = '', alternative_label_end = ''))
s.add_distributedload(DistributedLoad(C2, D,5,5,alternative_label_begin = '', alternative_label_end = ''))

s.add_pointload(PointLoad(A, None, dxdy = (0, -1) , color = 'green'))
s.add_pointload(PointLoad(A, None, dxdy = (-1, 0) , color = 'green'))
s.add_moment(Moment(A, None, angle = 90, color = 'green'))
s.add_pointload(PointLoad(B1, None, dxdy = (0, 1), color='blue'))
s.add_pointload(PointLoad(B1, None, dxdy = (1, 0), color='blue'))
s.add_pointload(PointLoad(B1, None, dxdy = (0, -1), color='green'))

s.add_pointload(PointLoad(B2, None, dxdy = (0, -1), color='blue'))
s.add_pointload(PointLoad(B2, None, dxdy = (-1, 0), color='blue'))

s.add_pointload(PointLoad(C1, None, dxdy = (0, -1), color='blue'))
s.add_pointload(PointLoad(C1, None, dxdy = (1, 0), color='blue'))

s.add_pointload(PointLoad(C2, None, dxdy = (0, 1), color='blue'))
s.add_pointload(PointLoad(C2, None, dxdy = (-1, 0), color='blue'))

s.add_pointload(PointLoad(D, None, dxdy = (0 , -1), color= 'green'))
s.add_pointload(PointLoad(D, None, dxdy = (-1 , 0), color= 'green'))

s.add_pointload(PointLoad(E1, None, dxdy = (0, 1), color='blue'))
s.add_pointload(PointLoad(E1, None, dxdy = (1, 0), color='blue'))

s.add_pointload(PointLoad(E2, None, dxdy = (0, -1), color='blue'))
s.add_pointload(PointLoad(E2, None, dxdy = (-1, 0), color='blue'))

s.add_pointload(PointLoad(F, None, dxdy = (0 , 1), color= 'green'))

plot(s,seed='2')
