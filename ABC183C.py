import itertools
N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]
res = 0

for root in itertools.permutations(range(2, N+1), N-1):
    time = T[0][root[0]-1]
    for i in range(N-2):
        time += T[root[i]-1][root[i+1]-1]
    time += T[root[-1]-1][0]
    if time == K:
        res += 1

print(res)
