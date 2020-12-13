D, G = map(int, input().split())
L = []

res = 0
for i in range(D):
    p, c = map(int, input().split())
    L.append((100*(i+1), p, c))
    res += p

for i in range(2**D):
    solved = 0
    sum = 0
    for j in range(D):
        score, p, c = L[j]
        if((i >> j) & 1):
            solved += p
            sum += score * p + c

    for j in range(D-1, -1, -1):
        if(sum >= G):
            break
        if((i >> j) & 1):
            continue
        score, p, c = L[j]
        for k in range(p):
            solved += 1
            sum += score
            if(sum >= G):
                break
    if(sum >= G):
        res = min(res, solved)

print(res)
