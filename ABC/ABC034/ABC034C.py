import math
W, H = map(int, input().split())
m = 10**9+7
print(math.factorial(W+H-2)*pow(math.factorial(H-1)
                                * math.factorial(W-1) % m, m-2, m) % m)
