while True:
    N = int(input())
    if(N == 0):
        break
    W = list(map(int, input().split()))
    dp = [[0]*(N+1) for _ in range(N+1)]

    for w in range(2, N+1):
        for l in range(N-w+1):
            r = l + w
            if dp[l+1][r-1] == r-l-2:
                if abs(W[l] - W[r-1]) <= 1:
                    dp[l][r] = max(dp[l][r], r-l)

            for mid in range(l+1, r):
                dp[l][r] = max(dp[l][mid] + dp[mid][r], dp[l][r])
    print(dp[0][N])
