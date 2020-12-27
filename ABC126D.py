import sys
sys.setrecursionlimit(500000)


N = int(input())

color = [-1]*N


def dfs(G, v, p, c):
    color[v] = c
    for u, w in G[v]:
        if(u == p):
            continue
        if(w % 2 == 1):
            dfs(G, u, v, 1-c)
        else:
            dfs(G, u, v, c)


G = [[] for _ in range(N)]
for i in range(N-1):
    u, v, w = map(int, input().split())
    G[u-1].append([v-1, w])
    G[v-1].append([u-1, w])

dfs(G, 0, -1, 1)

for c in color:
    print(c)