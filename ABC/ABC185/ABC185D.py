import math
N,M = map(int,input().split())
A = sorted(list(map(int, input().split())))

if(M == 0):
    print(1)
    exit()
if(N==M):
    print(0)
    exit()
    

L = []
if(A[0]>1):
    L.append(A[0]-1)
for i in range(M-1):
    diff = A[i+1]-A[i]-1
    if(diff>0):
        L.append(diff)
if(A[-1] != N):
    L.append(N-A[-1])

k = min(L)
res = 0
for l in L:
    res += math.ceil(l/k)

print(res)