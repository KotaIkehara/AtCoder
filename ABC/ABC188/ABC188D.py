import collections
N, Cost = map(int, input().split())
L = collections.defaultdict(int)
for _ in range(N):
    a, b, c = map(int, input().split())
    if a in L:
        L[a] += c
    else:
        L[a] = c
    if b+1 in L:
        L[b+1] -= c
    else:
        L[b+1] = -c

L = sorted(L.items(), key=lambda x: x[0])

table = [b for a, b in L]

for i in range(1, len(L)):
    table[i] += table[i-1]

res = 0
for i in range(len(L)-1):
    if(table[i] < Cost):
        res += table[i]*(L[i+1][0]-L[i][0])
    else:
        res += Cost*(L[i+1][0]-L[i][0])
print(res)
