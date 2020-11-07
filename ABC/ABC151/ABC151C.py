N, M = map(int, input().split())
AC = [0]*N
WA = [0]*N
penalty = 0
for i in range(M):
    p, s = input().split()
    p = int(p) - 1
    if(s == "AC" and WA[p] != -1):
        AC[p] = 1
        penalty += WA[p]
        WA[p] = -1
    elif(s == "WA" and WA[p] != -1):
        WA[p] += 1
print(AC.count(1), penalty)
