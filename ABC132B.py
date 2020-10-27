n = int(input())
P = list(map(int, input().split()))

res = 0
for i in range(1, n-1):
    if(P[i-1] < P[i] < P[i+1] or P[i-1] > P[i] > P[i+1]):
        res += 1
print(res)
