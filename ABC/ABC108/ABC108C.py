import itertools
N, K = map(int, input().split())
num = [0] * K
res = 0
for i in range(1, N+1):
    num[i % K] += 1
for a in range(K):
    b = (-a) % K
    c = (-a) % K
    res += num[a] * num[b] * num[c]

print(res)
