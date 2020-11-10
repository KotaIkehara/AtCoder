N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

res = -float("inf")
for i in range(1, 2**10):
    sum = 0
    for f, p in zip(F, P):
        count = 0
        for j in range(10):
            if((i >> j) & f[j]):
                count += 1
        sum += p[count]
    res = max(res, sum)
print(res)
