import math
from functools import reduce


def lcm(x, y):
    return (x*y)//math.gcd(x, y)


N = int(input())
T = [int(input()) for i in range(N)]

print(reduce(lcm, T))
