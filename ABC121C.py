N, M = map(int, input().split())
L = sorted([list(map(int, input().split())) for i in range(N)])

res = 0
for i in range(N):
    if(M > 0):
        num = min(M, L[i][1])
        res += L[i][0] * num
        M -= num
    else:
        break
print(res)
