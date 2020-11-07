from math import factorial
N, M = map(int, input().split())
m = 10**9+7
if(N-M == 0):
    print(2*factorial(N)*factorial(M) % m)
elif(abs(N-M) == 1):
    print(factorial(N) * factorial(M) % m)
else:
    print(0)
