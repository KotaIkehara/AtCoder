N, K = map(int, input().split())
X = list(map(int, input().split()))

res = float("inf")
for i in range(N-K+1):
    distL = abs(X[i]) + abs(X[i]-X[i+K-1])
    distR = abs(X[i+K-1]) + abs(X[i+K-1]-X[i])
    res = min(res, distL, distR)
print(res)
