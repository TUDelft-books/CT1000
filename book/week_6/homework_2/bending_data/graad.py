#plotter from https://github.com/lisette-924/ANS
from plotter import *

A = Point(0,0,'A',('top','center'))
B = Point(4,0,'B',('top','center'))
C = Point(10,0,'C',('top','center'))

s = Structure()
s.add_beam(Beam(A, B))
s.add_beam(Beam(A, C))
s.add_pointload(PointLoad(A, None, dxdy = (0, -1) , color = 'green'))
s.add_pointload(PointLoad(A, None, dxdy = (-1, 0) , color = 'green'))
s.add_pointload(PointLoad(B, None, dxdy = (0, -1) , color = 'green'))
s.add_pointload(PointLoad(C, None, dxdy = (0, -1) , color = 'green'))

plot(s,seed='2')