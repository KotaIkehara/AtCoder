import itertools
N, K = map(int, input().split())

if(N >= 10):
    print(0)
    exit()
l = [i for i in range(1, 2*N+1)]
d = {}
s = set(l)
res = 0
for c in itertools.combinations(s, N):
    t1 = tuple(sorted(c))
    t2 = tuple(sorted(s - set(c)))
    diff = 0
    for i in range(N):
        diff += abs(t1[i] - t2[i])
    if(diff <= K):
        res += 1
print(res)
