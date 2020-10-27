N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = [0]*(N+1)
T = [0]*(N+1)

for i in range(1, N+1):
    S[i] = S[i-1] + A[i-1]
    T[i] = T[i-1] + B[i-1]
res = 0
for i in range(1, N+1):
    res = max(res, S[i] + (T[N] - T[i-1]))
print(res)
