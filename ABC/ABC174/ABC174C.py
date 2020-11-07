K = int(input())

# これがないとTLE食らう
if K % 2 == 0 or K % 5 == 0:
    print(-1)
    exit()

# ai = (ai*10 + 7) % Kをr=にするとくそ遅くなる
res = -1
count = 0
ai = 0
while(True):
    ai = (ai*10 + 7) % K
    count += 1
    if(ai == 0):
        res = count
        break

print(res)
