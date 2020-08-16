R, C, K = map(int, input().split())
V = [[0]*C for i in range(R)]

for i in range(K):
    r, c, v = map(int, input().split())
    V[r-1][c-1] = v
print(V)
