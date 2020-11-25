import math
import functools
N = int(input())
A = list(map(int, input().split()))

L = [0]*(N+1)
R = [0]*(N+1)
L[0] = 0
R[N] = 0

for i in range(N):
    L[i+1] = math.gcd(L[i], A[i])
    R[N-i-1] = math.gcd(R[N-i], A[N-i-1])

res = 0
for i in range(N):
    res = max(res, math.gcd(L[i], R[i+1]))

print(res)
