N = int(input())
A = list(map(int, input().split()))

res = 0
for a in A:
    while(a % 2 == 0):
        a /= 2
        res += 1
print(res)
