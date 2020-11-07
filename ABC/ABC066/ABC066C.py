n = int(input())
A = list(map(int, input().split()))

print(*A[::-2], *A[n % 2::2])
