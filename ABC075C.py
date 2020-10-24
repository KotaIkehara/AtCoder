N, M = map(int, input().split())
A = []
B = []

for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

res = 0
flag = True


while(flag):
    for i in range(N):
        ca = A.count(i+1)
        ba = B.count(i+1)
        if(ca + ba == 1):
            if(ca == 1):
                idx = A.index(i+1)
            else:
                idx = B.index(i+1)
            A.pop(idx)
            B.pop(idx)
            res += 1
            break
    else:
        flag = False

print(res)
