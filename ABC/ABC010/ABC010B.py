n = int(input())
A = list(map(int, input().split()))

res = 0
for a in A:
    tmp = 0
    flag = True
    while(flag):
        if(a % 2 == 0 or a % 3 == 2):
            a -= 1
            tmp += 1
        else:
            res += tmp
            flag = False
print(res)
