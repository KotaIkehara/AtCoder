N = int(input())
A = list(map(int, input().split()))

dp = [0]*(N+1)
res = 0
for i in range(1, N+1):
    dp[i] += dp[i-1] + A[i-1]
dp2 = [0]*(N+1)
for i in range(1, N+1):
    dp2[i] += dp2[i-1] + dp[i-1]
res = max(dp[1:]) + max(dp2[1:])
print(res if(res > 0) else 0)
