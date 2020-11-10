N, M = map(int, input().split())
S = [list(map(int, input().split()))[1:] for i in range(M)]
P = list(map(int, input().split()))

res = 0
for i in range(2**N):
    for m in range(M):
        switch = 0
        for s in S[m]:
            if((i >> s-1) & 1):
                switch += 1
        if(switch % 2 != P[m]):
            break
    else:
        res += 1
print(res)
