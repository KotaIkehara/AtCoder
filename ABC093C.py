L = sorted(list(map(int, input().split())))

a, b, c = L
res = 0
if(sum(L) % 2 != (3*c) % 2):
    c += 1

while(c-a >= 2):
    a += 2
    res += 1
while(c-b >= 2):
    b += 2
    res += 1
while(c-a >= 1 or c-b >= 1):
    a += 1
    b += 1
    res += 1
print(res)
