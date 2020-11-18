import itertools
N = int(input())
L = []
for i in range(N):
    a, b = map(int, input().split())
    L.append((a, b))

for p, q, r in itertools.combinations(L, 3):
    if(p[0] == q[0]):
        if(p[0] == r[0]):
            print("Yes")
            exit()
    elif(p[1] == q[1]):
        if(p[1] == r[1]):
            print("Yes")
            exit()
    else:
        if(r[1]-p[1] == ((q[1]-p[1])/(q[0]-p[0])) * (r[0]-p[0])):
            print("Yes")
            exit()
print("No")
