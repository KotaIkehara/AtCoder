N, A, B = map(int, input().split())
W, E = 0, 0
for i in range(N):
    s, d = input().split()
    d = int(d)
    if(d < A):
        d = A
    elif(d > B):
        d = B

    if(s == "West"):
        W += d
    else:
        E += d

if(W > E):
    print("West", W-E)
elif(W < E):
    print("East", E-W)
else:
    print(0)
