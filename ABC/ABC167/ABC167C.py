N, M, X = map(int, input().split())

L = []
for i in range(N):
    l = list(map(int, input().split()))
    L.append(l)

res = float("inf")
for i in range(2**N):
    cost = 0
    U = [0]*M
    for j in range(N):
        if((i >> j) & 1):
            cost += L[j][0]
            for k in range(M):
                U[k] += L[j][k+1]
    if(all(U[j] >= X for j in range(M))):
        res = min(res, cost)
print(res if(res != float("inf")) else -1)
