N = int(input())
A = list(map(int, input().split()))

L = [0]*9
for a in A:
    if a >= 3200:
        L[8] += 1
    else:
        L[a//400] += 1

m = sum([l > 0 for l in L[:-1]])
# L[8]だけの時はm = 1
if(m == 0 and L[-1] > 0):
    print(1, L[-1])
else:
    print(m, m+L[-1])
