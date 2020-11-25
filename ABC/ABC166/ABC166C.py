import collections
N, M = map(int, input().split())
H = list(map(int, input().split()))

P = collections.defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    P[a].append(b)
    P[b].append(a)

res = 0
for i in range(N):
    flag = True
    for j in P[i]:
        if(H[i] <= H[j]):
            flag = False
            break
    if flag:
        res += 1
print(res)
