W, H, x, y = map(int, input().split())

S1 = min((H-y) * W, y*W)
S2 = min((W-x) * H, x*H)

if(x*2 == W and y*2 == H):
    print(W*H/2, 1)
else:
    print(W*H/2, 0)
