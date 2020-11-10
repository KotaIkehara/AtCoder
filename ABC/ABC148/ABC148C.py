import math
from functools import reduce

A, B = map(int, input().split())

print(A*B//math.gcd(A, B))
