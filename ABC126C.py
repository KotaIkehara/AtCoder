import math
N, K = map(int, input().split())

res = 0.0
for i in range(N):
    tmp = 1/N
    now = i+1
    while(now < K):
        now *= 2
        tmp /= 2

    res += tmp
print(res)
