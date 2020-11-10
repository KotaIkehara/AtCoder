n, X = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(n):
    if((X >> i) & 1):
        sum += A[i]
print(sum)
