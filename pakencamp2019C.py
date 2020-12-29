import itertools

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

res = 0
for t1, t2 in itertools.combinations(range(M), 2):
    score = 0
    for i in range(N):
        score += max(A[i][t1], A[i][t2])
    res = max(res, score)

print(res)
