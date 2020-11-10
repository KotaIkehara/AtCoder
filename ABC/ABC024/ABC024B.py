N, T = map(int, input().split())
A = [int(input()) for i in range(N)]

res = T

for i in range(1, N):
    diff = A[i] - A[i-1]
    if(diff < T):
        res += diff
    else:
        res += T
print(res)
