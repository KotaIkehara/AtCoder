N, M = map(int, input().split())
S = []
C = []

for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

if(N == 1):
    flag = all((str(0)[s-1] == str(c)) for s, c in zip(S, C))
    if(flag):
        print(0)
        exit()

for i in range(10**(N-1), 10**N):
    flag = all((str(i)[s-1] == str(c)) for s, c in zip(S, C))
    if(flag):
        print(i)
        exit()
print(-1)
