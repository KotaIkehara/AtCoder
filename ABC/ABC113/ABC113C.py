import collections
N, M = map(int, input().split())
L = collections.defaultdict(list)
res = [None]*M

for i in range(M):
    p, y = map(int, input().split())
    L[p].append((y, i))

for p, l in L.items():
    if not l:
        continue
    l.sort()
    for j, (y, i) in enumerate(l):
        res[i] = '{:06d}{:06d}'.format(p, j+1)

print(*res, sep="\n")
