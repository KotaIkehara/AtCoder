import itertools
N = int(input())

res = 0
for a in range(1, N):
    res += (N-1)//a

print(res)
