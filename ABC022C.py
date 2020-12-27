import Queue
from collections import defaultdict
from itertools import combinations

N,M = map(int, input().split())

L = [[float('inf')]*N for _ in range(N)]
for i in range(M):
    u,v,l = map(int, input().split())
    L[u-1][v-1] = L[v-1][u-1] = l

def dijkstra(G):
    Q = Queue.Queue
    Q.put(())

    while(Q):
        

d = dijkstra(L)

res = float('inf')
for i,j in combinations(nearby, 2):
    res = min(res, L[0][i] + L[0][j] + d[i][j])

print(-1 if(res == float('inf')) else res)