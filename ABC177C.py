N = int(input())
A = list(map(int, input().split()))
m = 10**9+7
table = [0]*(N+1)

for i in range(N):
    table[i+1] += A[i] + table[i]

S = 0
for i in range(N):
    S = (S+A[i] * (table[N] - table[i+1])) % m
print(S)
