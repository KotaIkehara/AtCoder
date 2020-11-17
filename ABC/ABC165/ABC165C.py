import itertools

N, M, Q = map(int, input().split())
L = []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    L.append((a, b, c, d))

res = 0
for A in itertools.combinations_with_replacement(range(1, M+1), N):
    point = 0
    for a, b, c, d in L:
        if(A[b-1] - A[a-1] == c):
            point += d
    res = max(res, point)

print(res)
