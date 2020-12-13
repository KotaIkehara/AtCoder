import itertools
N,M = map(int, input().split())
L = []
for i in range(M):
    a,b = map(int, input().split())
    L.append((a-1,b-1))
    L.append((b-1,a-1))

A = [0]*N
for v in itertools.combinations(list(range(N)),2):
    if(v in L):
        continue
    L1 = []
    L2 = []
    for i in range(M*2):
        if(v[0] ==  L[i][0]):
            L1.append(L[i][1])
        if(v[1] ==  L[i][0]):
            L2.append(L[i][1])
    for l in L1:
        if(l in L2):
            A[v[0]] += 1
            A[v[1]] += 1
            break
        
for a in A:
    print(a)