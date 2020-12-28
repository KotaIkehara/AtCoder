N = int(input())
A = int(input())
L = [int(input()) for _ in range(N)]

dp = [[False]*(A+1) for _ in range(N+1)]

dp[0][0] = True
for i in range(N):
    for j in range(A+1):
        dp[i+1][j] = dp[i][j] or dp[i+1][j]
        if(j >= L[i]):
            dp[i+1][j] = dp[i][j-L[i]] or dp[i+1][j]

print(dp[N][A])
