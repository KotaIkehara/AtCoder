T = list(map(int, input().split()))

res = 0
for i in range(len(T)):
    res = max(res, abs(T[i] - T[i-1]))
print(res)
