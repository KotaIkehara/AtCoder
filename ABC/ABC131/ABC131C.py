import math

a, b, c, d = map(int, input().split())

all = b-a+1
divC = b//c - (a-1)//c
divD = b//d - (a-1)//d
lcm = c*d//math.gcd(c, d)
divCD = b // lcm - (a-1)//lcm

print(all-(divC + divD - divCD))
