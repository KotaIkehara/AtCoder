a, b, c, d = map(int, input().split())

flag = True
while(a > 0 and c > 0):
    if flag:
        c -= b
        flag = False
    else:
        a -= d
        flag = True
print("Yes" if(c <= 0) else "No")
