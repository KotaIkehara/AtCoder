N = int(input())

res = 100000
for i in range(N+1):
    count = 0
    t = i
    while(t > 0):
        count += t % 6
        t = t//6
    t = N-i
    while(t > 0):
        count += t % 9
        t = t//9
    if(t > 0):
        count += t
    res = min(res, count)
print(res)
