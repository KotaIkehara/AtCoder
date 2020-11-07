import collections

N = int(input())
A = list(map(int, input().split()))
C = collections.Counter(A)
x = []

for c in C:
    if(C[c] > 1):
        x.append(c)
    if(C[c] > 3):
        x.append(c)
x.sort()
print(x[-1]*x[-2] if(len(x) >= 2) else 0)
