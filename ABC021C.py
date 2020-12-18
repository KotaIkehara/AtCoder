from collections import deque
N = int(input())
a,b = map(int, input().split())
M = int(input())

mod = 10**9+7

R = [[] for i in range(N+1)]
for i in range(M):
    x,y = map(int, input().split())
    R[x].append(y)
    R[y].append(x)

dist = [-1]*(N+1)
count = [0]*(N+1)

def bfs(v):
    Q = deque()
    dist[v] = 0
    count[a] = 1
    Q.append(v)
    while(Q):
        u = Q.popleft()
        for e in R[u]:
            if(dist[e] == -1):
                dist[e] = dist[u] + 1
                count[e]  = (count[e] + count[u])%mod
                Q.append(e)
            elif(dist[e] == dist[u] + 1):
                count[e]  = (count[e] + count[u])%mod
                
       
bfs(a)
print(count[b])