H,W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

m = 100
for a in A:
    for n in a:
        m = min(m,n)

res = 0
for a in A:
    for n in a:
        res += n-m
print(res)