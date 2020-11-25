N, A, B, C = map(int, input().split())
L = [int(input()) for i in range(N)]


def dfs(cur, a, b, c):
    if(cur == N):
        # -30で最初に追加するときのコストを消す
        return abs(a-A) + abs(b-B) + abs(c-C)-30 if(min(a, b, c) > 0) else float("inf")
    ret0 = dfs(cur+1, a, b, c)
    ret1 = dfs(cur+1, a+L[cur], b, c)+10
    ret2 = dfs(cur+1, a, b+L[cur], c)+10
    ret3 = dfs(cur+1, a, b, c+L[cur])+10
    return min(ret0, ret1, ret2, ret3)


print(dfs(0, 0, 0, 0))
