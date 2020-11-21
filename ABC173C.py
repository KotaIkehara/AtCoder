H, W, K = map(int, input().split())
C = [input() for i in range(H)]

res = 0
for h in range(2**H):
    for w in range(2**W):
        black = 0
        for i in range(H):
            for j in range(W):
                if(((h >> i) & 1) == 0 and ((w >> j) & 1) == 0 and C[i][j] == "#"):
                    black += 1
        if(black == K):
            res += 1
print(res)
