N = int(input())
K = int(input())
X = map(int, input().split())

res = 0
for x in X:
    if(x < K-x):
        res += 2*x
    else:
        res += 2*(K-x)
print(res)
