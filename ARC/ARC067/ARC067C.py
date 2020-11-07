import math

N = math.factorial(int(input()))

res = 2
i = 2

while i*i <= N:
    cnt = 1
    while(N % i == 0):
        cnt += 1
        N //= i
    res *= cnt
    i += 1
if(N == 1):
    res //= 2
print(res % (10**9+7))
