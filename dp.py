N = int(input())
A = [int(input()) for _ in range(N)]

dp = [0]*(N+1)

for i in range(N):
    dp[i+1] = max(dp[i], dp[i]+A[i])
print(dp)
