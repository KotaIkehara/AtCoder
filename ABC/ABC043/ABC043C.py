from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

x = int(input())
A = list(map(int, input().split()))

ave = Decimal(str(sum(A)/x)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

res = 0
for a in A:
    res += (a-ave)**2

print(res)
