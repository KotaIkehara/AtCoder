N, D , K = map(int, input().split())

def f(s,t,list):
    now = s
    if(s<t):
        for i, (l,r) in enumerate(list):
            if(l<=now<=r):
                now = r
            if(now >=t):
                return i+1
    else:
        for i, (l,r) in enumerate(list):
            if(l<=now<=r):
                now = l
            if(now <= t):
                return i+1


M = []
for i in range(D):
    l,r = map(int, input().split())
    M.append((l, r))

for i in range(K):
    s,t = map(int, input().split())
    print(f(s,t,M))
