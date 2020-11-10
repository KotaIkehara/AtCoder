N = int(input())
H = list(map(int, input().split()))

res = 1
m = H[0]
for i in range(1, N):
    if(H[i] - m >= 0):
        res += 1
    m = max(m, H[i])
print(res)
