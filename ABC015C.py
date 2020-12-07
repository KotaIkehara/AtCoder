import itertools

N,K = map(int, input().split())
T =[]
for i in range(N):
    t = list(map(int, input().split()))
    T.append(t)

for v in itertools.product(list(range(K)), repeat=N):
    hasBug = T[0][v[0]]
    for i in range(1,N):
        hasBug ^= T[i][v[i]]
    if hasBug == 0:
        print("Found")
        exit()

print("Nothing")