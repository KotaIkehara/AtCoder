from collections import defaultdict
from collections import deque

n = int(input())

L = defaultdict(list)

for i in range(n):
    U = list(map(int, input().split()))
    L[U[0]] = U[2:]

visited = [False]*n
visited[0] = True

Q = deque()
Q.append(1)

D = [-1]*n
D[0] = 0

while(len(Q) > 0):
    pos = Q.popleft()
    for v in L[pos]:
        if(visited[v-1]):
            continue
        visited[v-1] = True
        D[v-1] = D[pos-1] + 1
        Q.append(v)

for i in range(n):
    print(i+1, D[i])
