N = int(input())
A = list(map(int, input().split()))

res = []
for i in range(2, max(A)+1):
    k = 0
    for a in A:
        if(a % i == 0):
            k += 1
    res.append(k)
print(res.index(max(res))+2)
