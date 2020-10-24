N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [b-a for a, b, in zip(A, B)]
G = [[] for i in range(N)]

for i in range(M):
    c, d = map(int, input().split())
    G[c - 1].append(d - 1)
    G[d - 1].append(c - 1)

visited = [-1]*N
if(sum(C) != 0):
    print("No")
    exit()
for i in range(N):
    tmp = C[i]
    if(visited[i] == -1):
        stack = [i]
        visited[i] = i
        while(stack):
            next = stack.pop()
            for j in (G[next]):
                if(visited[j] == -1):
                    stack.append(j)
                    visited[j] = i
                    tmp += C[j]
        if tmp != 0:
            print("No")
            exit()
print("Yes")
