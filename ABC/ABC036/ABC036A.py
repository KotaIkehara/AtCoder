N, K = map(int, input().split())
T = [int(input()) for i in range(N)]

res = -1
for i in range(2, N):
    if(sum(T[i-2:i+1]) < K):
        res = i+1
        break
print(res)
