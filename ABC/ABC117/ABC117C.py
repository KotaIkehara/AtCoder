N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

S = []
for i in range(1, M):
    S.append(X[i] - X[i-1])
S = sorted(S)[::-1]
print(sum(S[N-1:]))
