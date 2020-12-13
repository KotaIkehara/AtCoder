N, K = map(int, input().split())
R = sorted(list(map(int, input().split())))
res = 0
for i in range(K):
    res = (res + R[N-K+i])/2

print(res)
