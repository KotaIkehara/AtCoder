X, Y = map(int, input().split())

res = 0
while(X <= Y):
    X *= 2
    res += 1
print(res)
