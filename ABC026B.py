import math
N = int(input())
R = sorted([int(input())**2 for i in range(N)])[::-1]

print((sum(R[::2])-sum(R[1::2]))*math.pi)
