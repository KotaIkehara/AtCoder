N, K = map(int, input().split())
A = list(map(int, input().split()))

# 2**K <= 32768
# print((2**15) * 15)
res = float('inf')
for i in range(2**N+1):
    # solve
    cost = 0
    count = 1
    m = A[0]
    for j in range(1, N):
        if (i >> j) & 1:
            if(A[j] <= m):
                cost += m - A[j] + 1
                m = m + 1
            else:
                m = A[j]
            count += 1
        else:
            m = max(m, A[j])  # 見えないときでも，mの更新を忘れずに！
    # check
    if count >= K:
        res = min(res, cost)
print(res)
