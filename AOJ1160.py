import sys
sys.setrecursionlimit(500000)


dxdy = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

def dfs(seen, h,w):
    seen[h][w] = True
    
    for dx,dy in dxdy:
        nh = h + dx
        nw = w + dy

        if nh<0 or nh>=H or nw<0 or nw>=W:
            continue
        if(C[nh][nw] == 0):
            continue
        if seen[nh][nw]:
            continue

        dfs(seen, nh, nw)


while(True):
    W,H = map(int, input().split())
    if(W == 0 and H == 0):
        exit()
    # 1:陸, 0:海
    C = [list(map(int, input().split())) for _ in range(H)]
    seen = [[False]*W for _ in range(H)]

    res = 0
    for h in range(H):
        for w in range(W):
            if seen[h][w]:
                continue
            else:
                if(C[h][w] == 0):
                    continue
                else:
                    dfs(seen, h,w)
                    res += 1

    print(res)