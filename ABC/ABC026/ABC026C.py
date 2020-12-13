import collections
N = int(input())
B = list(int(input()) for i in range(N-1))

buka = collections.defaultdict(list)
for i, b in enumerate(B):
    buka[b-1].append(i+1)

sal = [0]*N
for i in range(N-1,-1,-1):
    if(i not in buka):
        sal[i] = 1
    else:
        L = buka[i]
        sal[i] = max(list(sal[l] for l in L)) + min(list(sal[l] for l in L)) + 1
print(sal[0])