import queue

H, W = map(int, input().split())
M = [list(input()) for i in range(H)]

dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for h in range(H):
    for w in range(W):
        if(M[h][w] == 'S'):
            sh = h
            sw = w
        if(M[h][w] == 'G'):
            gh = h
            gw = w

dist = [[-1]*W for _ in range(H)]
prev_x = [[-1]*W for _ in range(H)]
prev_y = [[-1]*W for _ in range(H)]


def bfs(G):
    Q = queue.Queue()
    Q.put((sh, sw))
    dist[sh][sw] = 0
    while not Q.empty():
        v = Q.get()
        h, w = v
        for dx, dy in dxdy:
            nh = h + dx
            nw = w + dy
            if(nh < 0 or nh >= H or nw < 0 or nw >= W):
                continue
            if(G[nh][nw] == '#'):
                continue
            if(dist[nh][nw] == -1):
                Q.put((nh, nw))
                dist[nh][nw] = dist[h][w] + 1
                prev_x[nh][nw] = h
                prev_y[nh][nw] = w


bfs(M)
for h in range(H):
    for w in range(W):
        if(M[h][w] != '.'):
            print('%2s ' % M[h][w], end="")
        else:
            print('%2d ' % dist[h][w], end="")
    print()
print()

h = gh
w = gw
while(h != -1 and w != -1):
    M[h][w] = 'o'

    # 以下の実装だとwの値が変わってしまうので注意
    # h = prev_x[h][w]
    # w = prev_y[h][w]

    ph = prev_x[h][w]
    pw = prev_y[h][w]
    h = ph
    w = pw

for h in range(H):
    for w in range(W):
        print('%2s ' % M[h][w], end="")
    print()
