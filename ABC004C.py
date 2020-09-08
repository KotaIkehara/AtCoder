N = int(input())
A = [i+1 for i in range(6)]

x = (N // 5) % 6
A = (A[x:] + A[:x])

for i in range(N % 5):
    tmp = A[i % 5]
    A[i % 5] = A[i % 5+1]
    A[i % 5+1] = tmp
print(*A, sep='')
