N = int(input())

L = [1, 2, 4, 8]
res = [0]*4

for i in range(3, -1, -1):
    L[i] = N//(2**i)
    N = N-(2**i) * L[i]

print(sum(L))
for i in range(4):
    if(L[i] > 0):
        for j in range(L[i]):
            print(2**i)
