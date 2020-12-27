import queue
N, M = map(int, input().split())

G = [[] for _ in range(N)]

dist = [-1]*N


def bfs(G):
    Q = queue.Queue()
    dist[0] = 0
    Q.put(0)
    while(not Q.empty()):
        v = Q.get()
        for u in G[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] + 1
            Q.put(u)


for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

bfs(G)
print(dist)
