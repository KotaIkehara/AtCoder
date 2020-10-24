N, M = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
res = [0]*N

for i in range(M):
    res[A[i]-1] += 1
    res[B[i]-1] += 1

for i in range(N):
    print(res[i])
