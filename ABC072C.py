N = int(input())
A = list(map(int, input().split()))

L = [0]*(10**5+2)

for a in A:
    L[a] += 1
    L[a+1] += 1
    L[a+2] += 1
print(max(L))
