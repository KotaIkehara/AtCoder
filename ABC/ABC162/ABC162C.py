from math import gcd
K = int(input())

S = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            S += gcd(gcd(a, b), c)
print(S)
