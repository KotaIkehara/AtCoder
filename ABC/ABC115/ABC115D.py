N, X = map(int, input().split())
A = [1]
P = [1]
# レベルiに含まれるPの数
for i in range(N):
    A.append(2*A[i] + 3)
    P.append(2*P[i] + 1)


def f(n, x):
    if(n == 0):
        return 0 if(x <= 0) else 1
    elif(x <= 1+A[n-1]):
        return f(n-1, x-1)
    else:
        return P[n-1] + 1 + f(n-1, x-2-A[n-1])


print(f(N, X))
