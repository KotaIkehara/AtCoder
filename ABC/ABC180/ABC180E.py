import itertools

N = int(input())
C = list(list(map(int, input().split())) for i in range(N))

res = float("inf")
for c in list(itertools.permutations(C)):
    dist = 0
    for i in range(0, N):
        dist += abs(c[i][0]-c[i-1][0]) + abs(c[i][1]-c[i-1]
                                             [1]) + max(0, c[i][2] - c[i-1][2])
    res = min(res, dist)
print(res)
