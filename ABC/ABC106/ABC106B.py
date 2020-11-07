import math
N = int(input())

res = 0
for i in range(1, math.ceil(N/2)+1):
    n = i*2-1
    div = 0
    for j in range(1, n+1):
        if(n % j == 0):
            div += 1
    if(div == 8):
        res += 1
print(res)
