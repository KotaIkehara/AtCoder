# 65536

N = int(input())
A = list(map(int, input().split()))
L = list((a, i+1) for i, a in enumerate(A))

while(N > 1):
    nextList = []
    for j in range(2**N//2):
        nextList.append(max(L[2*j], L[2*j+1]))
    L = nextList.copy()
    N -= 1

a, b = L
print(a[1] if(a[0] < b[0]) else b[1])
