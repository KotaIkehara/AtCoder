N, W = map(int, input().split())
A = []
dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    v, w = map(int, input().split())
    A.append((v, w))

for i in range(N):
    value, weight = A[i]
    for w in range(W+1):
        if w >= weight:
            dp[i+1][w] = max(dp[i][w-weight] + value, dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
print(dp[N][W])
