N = int(input())
L = []
for i in range(N):
    x, y, h = map(int, input().split())
    L.append((x, y, h))
    if h > 0:
        std = x, y, h


# H = h + | X-Cx | + | Y-Cy |
for i in range(101):
    for j in range(101):
        x, y, h = std
        H = h + abs(x-i) + abs(y-j)
        flag = True
        for x, y, h in L:
            if(max(H-abs(x - i) - abs(y - j), 0) != h):
                flag = False
                break
        if(flag):
            print(i, j, H)
            exit()
