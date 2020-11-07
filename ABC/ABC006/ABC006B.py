n = int(input())

m = 10**4+7
a, b, c = 0, 0, 1
for i in range(n-1):
    a, b, c = b, c, (a+b+c) % m
print(a)
