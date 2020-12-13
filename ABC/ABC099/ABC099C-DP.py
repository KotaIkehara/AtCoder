N = int(input())

dp = [N]*(N+1)
dp[0] = 0

for i in range(1, N+1):
    pow6 = 1
    while(pow6 <= N):
        dp[i] = min(dp[i], dp[i-pow6]+1)
        pow6 *= 6

    pow9 = 1
    while(pow9 <= N):
        dp[i] = min(dp[i], dp[i-pow9]+1)
        pow9 *= 9

print(dp[N])
