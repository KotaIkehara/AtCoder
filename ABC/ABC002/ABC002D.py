import itertools

N, M = map(int, input().split())
L = []
for _ in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    L.append((x, y))

res = 1
for i in range(2**N):
    giin = []
    count = 0
    for j in range(N):
        if((i >> j) & 1):
            giin.append(j)
            count += 1

    isHabatsu = True
    for pair in itertools.combinations(giin, 2):
        if(pair in L):
            continue
        else:
            isHabatsu = False
            break
    if(isHabatsu):
        res = max(res, count)
print(res)
