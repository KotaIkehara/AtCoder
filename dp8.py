S = input()
T = input()

ls = len(S)
lt = len(T)

dp = [[0]*(lt+1) for _ in range(ls+1)]

for i in range(ls):
    for j in range(lt):
        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        if(S[i] == T[j]):
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j], dp[i][j+1])
print(dp[ls][lt])
