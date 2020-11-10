N, K = map(int, input().split())
A = list(map(int, input().split()))
T = [0]*(N+1)
for i in range(N):
    T[i+1] += T[i]+A[i]
res = 0
for i in range(K):
    res += T[N-K+1+i] - T[i]
print(res)
