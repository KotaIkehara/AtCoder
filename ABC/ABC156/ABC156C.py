N = int(input())
X = list(map(int, input().split()))

res = float("inf")
for p in range(101):
    S = 0
    for x in X:
        S += (x-p)**2
    res = min(res, S)
print(res)
