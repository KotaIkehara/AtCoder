import numpy as np
from itertools import permutations
import math

N = int(input())
L = np.array([list(map(int, input().split())) for i in range(N)])

dist = 0
for route in permutations(L):
    for i in range(N-1):
        dist += np.linalg.norm(route[i] - route[i+1])
print(dist/math.factorial(N))
