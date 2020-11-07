N = int(input())
T = [[-1]*N for i in range(N)]

for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        T[i][x-1] = y

res = 0
for i in range(2**N):
    honest = [0] * N
    for j in range(N):
        if((i >> j) & 1):
            honest[j] = 1
        flag = True
    for j in range(N):
        if(honest[j]):
            for k in range(N):
                if(T[j][k] == -1):
                    continue
                if(T[j][k] != honest[k]):
                    flag = False
    if flag:
        res = max(res, honest.count(1))
print(res)
