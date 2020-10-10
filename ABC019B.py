from itertools import groupby

s = input()

res = ''
for k, g in groupby(s):
    res += k + str(len(list(g)))
print(res)
