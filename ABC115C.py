N, K = map(int, input().split())
H = sorted([int(input()) for i in range(N)])

res = float("inf")
for i in range(N-K+1):
    res = min(res, H[i+K-1]-H[i])

print(res)
