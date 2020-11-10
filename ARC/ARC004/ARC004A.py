N = int(input())
P = [list(map(int, input().split())) for i in range(N)]

res = 0
for i in range(N):
    for j in range(i+1, N):
        d = (P[i][0] - P[j][0])**2 + (P[i][1] - P[j][1])**2
        res = max(res, d)
print(res ** 0.5)
