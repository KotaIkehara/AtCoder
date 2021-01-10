import numpy as np
import copy
R, C = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(R)])

res = 0
for i in range(2**R):
    L = A.copy()
    for j in range(R):
        if (i >> j) & 1:
            L[j] = L[j] ^ 1
    heads = L.sum(axis=0)
    count = 0
    for h in heads:
        count += max(h, R-h)
    res = max(res, count)
print(res)


### ---WA for set 3 and TLE for set4,5--- ###
# res = 0
# for i in range(2**R):
#     L = A[:] # これはLに変更を加えると，Aにも影響が出る．A.copy() or cppy.deepcopy(A)を用いる
#     for j in range(R):
#         if((i >> j) & 1):
#             for k in range(C):
#                 L[j][k] = 1 - L[j][k]
#     count = 0
#     for k in range(C):
#         heads = 0
#         for j in range(R):
#             if L[j][k]:
#                 heads += 1
#         count += max(heads, R-heads)
#     res = max(res, count)
# print(res)
