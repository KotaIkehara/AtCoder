N, K = map(int, input().split())
D = []
A = []
for i in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    D.append(d)
    A.append(a)

have = set()
for a in A:
    for i in a:
        have.add(i)
print(N-len(have))
