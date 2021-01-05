N = int(input())
A = set(map(int, input().split()))

L = set()
for a in A:
    while(a%2 == 0):
        a//=2
    L.add(a)
print(len(L))