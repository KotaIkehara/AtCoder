N, M = map(int, input().split())

res = 0
if(N > 0 and M > 1):
    res += min(N, M//2)
    if(N > M//2):
        print(res)
        exit()
    else:
        M = M - N*2
        N = 0

if(N == 0 and M > 2):
    res += M//4

print(res)
