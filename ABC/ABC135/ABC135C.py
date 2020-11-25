N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for i in range(N):
    kill1 = min(B[i], A[i])
    res += kill1
    kill2 = min(A[i+1], B[i] - kill1)
    A[i+1] -= kill2
    res += kill2

print(res)
