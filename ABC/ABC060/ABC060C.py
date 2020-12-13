N, T = map(int, input().split())
L = list(map(int, input().split()))

res = T
for i in range(1, N):
    diff = L[i]-L[i-1]
    if diff <= T:
        res += diff
    else:
        res += T
print(res)
