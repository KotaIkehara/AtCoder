N = int(input())
A = list(map(int, input().split()))
res = [(height, num) for num, height in enumerate(A, start=1)]
for a in sorted(res, reverse=True):
    print(a[1])
