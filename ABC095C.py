a, b, c, x, y = map(int, input().split())

res = a*x+b*y
for i in range(1, max(x, y)+1):
    if(x > 0):
        x -= 1
    if(y > 0):
        y -= 1
    res = min(res, a*x+b*y + c*i*2)
print(res)
