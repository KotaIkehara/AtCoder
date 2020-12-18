import math
a, b, c, d, e, f = map(int, input().split())

water = set()
for i in range(math.ceil(f/(100*a))+1):
    for j in range(math.ceil(f/(100*b))+1):
        W = 100*a*i + 100*b*j
        if(0 < W <= f):
            water.add(W)
        else:
            break
suger = set()
for i in range(math.ceil(f/c)+1):
    for j in range(math.ceil(f/d)+1):
        S = c*i + d*j
        if(0 <= S <= f):
            suger.add(S)
        else:
            break

max_noudo = 0
res = [100*a, 0]
for w in water:
    for s in suger:
        if(s+w > f):
            continue
        else:
            noudo = (100*s)/(w+s)
        if(noudo <= (100*e)/(100+e) and noudo > max_noudo):
            max_noudo = noudo
            res = [w+s, s]
print(*res)
