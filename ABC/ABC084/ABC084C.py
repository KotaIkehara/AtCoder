N = int(input())

L = [0]*N
for i in range(N-1):
    c, s, f = map(int, input().split())
    for j in range(i+1):
        if(L[j] >= s):
            L[j] += (f - L[j] % f) % f+c
        else:
            L[j] += s - L[j] + c

for l in L:
    print(l)
