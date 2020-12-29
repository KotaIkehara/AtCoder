import itertools

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

res = float('inf')
for u, v in itertools.product(range(N), repeat=2):
    en = L[u][0]
    ex = L[v][1]
    dist = 0
    for a, b in L:
        dist += abs(en - a) + abs(b-a) + abs(ex-b)
    res = min(res, dist)

print(res)
