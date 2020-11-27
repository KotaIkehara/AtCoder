N = int(input())

prev = (0, 0, 0)
flag = True
for i in range(N):
    t, x, y = map(int, input().split())
    pt, px, py = prev

    diff = abs(x-px) + abs(y-py)
    if(t-pt < diff or ((t-pt) % 2 != diff % 2)):
        flag = False
        break
    prev = (t, x, y)

print("Yes" if flag else "No")
