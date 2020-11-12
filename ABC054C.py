import itertools
import collections
N, M = map(int, input().split())

E = collections.defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

res = 0
for route in itertools.permutations(range(2, N+1), N-1):
    flag = True
    now = 1
    for r in route:
        if(r in E[now]):
            now = r
        else:
            flag = False
            break
    if flag:
        res += 1

print(res)
