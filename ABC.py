N = int(input())
A = list(map(int, input().split()))

res = 0
prev = A[0]
for i in range(1, N):
    if(prev > A[i]):
        res += prev - A[i]
    else:
        prev = A[i]
print(res)
