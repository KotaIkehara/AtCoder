N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]
num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# 最大桁数を求める
dp = [-float("inf")]*(N+1)
dp[0] = 0
for i in range(1, N+1):
    for a in A:
        if(i-num[a] >= 0):  # これを忘れていて3_hand_5についてREになった(原因は恐らく配列の範囲外へのアクセス)
            dp[i] = max(dp[i], dp[i-num[a]]+1)

res = 0
for i in range(dp[N]-1, -1, -1):
    for a in A:
        if(N-num[a] >= 0 and dp[N-num[a]] == dp[N]-1):
            res += a * 10**i
            N -= num[a]
            break
print(res)
