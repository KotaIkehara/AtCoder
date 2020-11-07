import collections
N = int(input())
A = list(map(int, input().split()))
S = 0
if(N % 2 == 0):
    for i in range(N//2):
        S += (2*i+1)*2
else:
    for i in range(N//2+1):
        S += (2*i)*2

if(S == sum(A)):
    print((2**(N//2)) % (10**9+7))
else:
    print(0)
