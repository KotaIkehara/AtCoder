N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

res = B[A[0]-1]
for i in range(1, N):
    res += B[A[i]-1]
    if(A[i-1] == A[i]-1):
        res += C[A[i]-2]
print(res)
