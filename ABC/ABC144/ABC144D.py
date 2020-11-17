import math
a, b, x = map(int, input().split())

l = 0
r = 90

for i in range(10000):
    m = (l + r) / 2
    if(b*math.tan(math.radians(90-m)) <= a):
        V = ((b*math.tan(math.radians(90-m)))*b*a) / 2
    else:
        V = a*a*b - (a*a*(a*math.tan(math.radians(m))))/2

    if(x <= V):
        l = m
    else:
        r = m
print(l)
