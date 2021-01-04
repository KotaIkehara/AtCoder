N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))

L = [float('inf')]*(2**N)
for i in range(2**N):
    num = 0
    for j in range(N):
        if((i >> j) & 1):
            num += A[j]
    L[i] = num
for m in M:
    if(m in L):
        print("yes")
    else:
        print("no")
