import math

A, B, H, M = map(int, input().split())

hx = A*math.cos(2*math.pi * H/12 + math.pi/6 * M/60)
hy = A*math.sin(2*math.pi * H/12 + math.pi/6 * M/60)

mx = B*math.cos(math.pi * (M/30))
my = B*math.sin(math.pi * (M/30))

print(((hx-mx)**2 + (hy-my)**2)**.5)
