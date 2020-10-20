import sys
import queue
sys.setrecursionlimit(500000)


R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

L = [list(input()) for i in range(R)]
dydx = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(y, x, d):
    Q = queue.Queue()
    Q.put([y, x, d])
    while(not Q.empty()):
        v = Q.get()
        y, x, d = v[0], v[1], v[2]
        if(y == gy and gx == x):  # Arrived at the goal
            print(d)
            exit()
        if(L[y-1][x-1] == "#"):  # Visited
            continue
        if(y == 1 or y == R or x == 1 or x == C):
            continue
        for dy, dx in dydx:
            if(L[y+dy-1][x+dx-1] != "#" and 1 <= y <= R and 1 <= x <= C):
                Q.put([y+dy, x+dx, d+1])
        L[y-1][x-1] = "#"


bfs(sy, sx, 0)
