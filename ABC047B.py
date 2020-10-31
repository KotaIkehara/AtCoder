W, H, N = map(int, input().split())
b, c = 0, 0

for i in range(N):
    x, y, a = map(int, input().split())
    if(a == 1):
        b = max(b, x)
    elif(a == 2):
        W = min(W, x)
    elif(a == 3):
        c = max(c, y)
    else:
        H = min(H, y)

print(max(0, W-b) * max(0, H-c))
