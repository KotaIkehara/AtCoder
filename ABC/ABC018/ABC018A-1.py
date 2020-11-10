X = [int(input()) for i in range(3)]
S = sorted(X)[::-1]

for x in X:
    print(S.index(x)+1)
