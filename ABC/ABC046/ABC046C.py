from decimal import Decimal, ROUND_CEILING
import math

N = int(input())
T,A = 1,1

for i in range(N):
    t,a = map(int, input().split())
    k = max(math.ceil(Decimal(str(T))/Decimal(str(t))), math.ceil(Decimal(str(A))/Decimal(str(a))))
    T,A = k*t, k*a

print(T+A)