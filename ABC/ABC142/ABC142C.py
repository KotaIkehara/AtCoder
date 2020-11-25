N = int(input())
A = list(map(int, input().split()))

res = [0]*N
for i, a in enumerate(A):
    res[a-1] = i+1
print(*res)
