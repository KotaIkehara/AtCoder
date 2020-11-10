N, M = map(int, input().split())

A = []
for i in range(N):
    a, b = map(int, input().split())
    A.append([a, b])

B = []
for i in range(M):
    c, d = map(int, input().split())
    B.append([c, d])

for i in range(N):
    dist = [abs(A[i][0] - B[j][0]) + abs(A[i][1] - B[j][1])
            for j in range(M)]
    print(dist.index(min(dist))+1)
