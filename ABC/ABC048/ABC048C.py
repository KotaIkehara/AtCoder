N, x = map(int, input().split())
A = list(map(int, input().split()))

res = 0
if(A[0] > x):
    res += A[0] - x
    A[0] -= res
for i in range(1, N):
    diff = A[i-1] + A[i] - x
    if(diff > 0):
        res += diff
        A[i] -= diff
print(res)
