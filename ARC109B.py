import math
from decimal import Decimal
n = int(input())

print(n+1-int((Decimal(str(1+8*n+8))**Decimal('0.5')-1)*Decimal("0.5")))
