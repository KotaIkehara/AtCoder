from itertools import product

N = int(input())

for i in product("abc", repeat=N):
    print(*i, sep='')
