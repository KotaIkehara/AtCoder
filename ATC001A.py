import sys
sys.setrecursionlimit(500000)

H,W = map(int, input().split())
field = [list(input()) for _ in range(H)]

dxdy = [(0,1), (1,0), (0,-1), (-1, 0)]

seen = [[False]*W for _ in range(H)]
def dfs(h, w):
    seen[h][w] = True
    for dx,dy in dxdy:
        nh = h + dx
        nw = w + dy

        if(nh < 0 or nh>=H or nw < 0 or nw >=W):
            continue
        if(field[nh][nw] == '#'):
            continue
        if(seen[nh][nw]):
            continue

        dfs(nh, nw)

for h in range(H):
    for w in range(W):
        if(field[h][w] == 's'):
            sh = h
            sw = w
        if(field[h][w] == 'g'):
            gh = h
            gw = w

dfs(sh, sw)


if(seen[gh][gw]):
    print("Yes")
else:
    print("No")

