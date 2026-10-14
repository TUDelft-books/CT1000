#plotter from https://github.com/lisette-924/ANS
from plotter import *

A = Point(0,0,'A',('top','left'))
B = Point(4,0,'B',('top','right'))
C = Point(10,0,'C',('top','center'))

s = Structure()
s.add_beam(Beam(A, B))
s.add_beam(Beam(A, C))
s.add_support(Support(B, 'roller'))
s.add_support(Support(A, 'pinned'))
s.add_support(Support(C, 'roller'))
s.add_distributedload(DistributedLoad(A, B, 25))
s.add_length(Length(A, B), Length(B, C))
plot(s,seed='1')