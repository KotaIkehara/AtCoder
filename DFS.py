N, M, s, t = map(int, input().split())
seen = [False]*N

def dfs(G, v):
    seen[v] = True
    print(v)
    for u in G[v]:
        if seen[u]:
            continue
        dfs(G, u)


G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

print(G)
dfs(G, s-1)
if seen[t-1]:
    print("Yes")
else:
    print("No")