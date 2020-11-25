K, N = map(int, input().split())
A = list(map(int, input().split()))

D = [K-A[-1] + A[0]] + [abs(A[i] - A[i-1]) for i in range(1, N)]
print(K - max(D))
