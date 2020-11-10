X = int(input())

m = 100
res = 0
while(m < X):
    m += m//100
    res += 1
print(res)
