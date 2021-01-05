H,W = map(int, input().split())

res = H*W
for h in range(1,H+1):
    a = h*W
    w = W//2
    b = (H-h)*w
    c = (H-h)*(W-w)
    res = min(res, max(a,b,c) - min(a,b,c))

    bh = (H-h)//2
    b = bh*W
    c = (H-h-bh)*W
    res = min(res, max(a,b,c) - min(a,b,c))

for w in range(1,W+1):
    a = w*H
    h = H//2
    b = (W-w)*h
    c = (W-w)*(H-h)
    res = min(res, max(a,b,c) - min(a,b,c))

    bw = (W-w)//2
    b = bw*H
    c = (W-w-bw)*H
    res = min(res, max(a,b,c) - min(a,b,c))
    
print(res)