N, M, A, B = map(int, input().split())
C = [int(input()) for i in range(M)]

for i in range(M):
    if(N <= A):
        N += B
    N -= C[i]
    if(N < 0):
        print(i+1)
        break
else:
    print("complete")
