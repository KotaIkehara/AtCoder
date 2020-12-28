N, A = map(int, input().split())
L = [int(input()) for _ in range(N)]

dp = [[0]*(A+1) for _ in range(N+1)]

dp[0][0] = 1

for i in range(N):
    for j in range(A+1):
        dp[i+1][j] += dp[i][j]
        if(j >= L[i]):
            dp[i+1][j] += dp[i][j-L[i]]
print(dp[N][A])
