L, R = map(int, input().split())
m = 2019
res = float("inf")
if(R-L > 2019):
    print(0)
    exit()
else:
    L = L % 2019
    R = R % 2019
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            res = min(res, i*j % m)
    print(res)
