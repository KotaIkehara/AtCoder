A, B, X = map(int, input().split())
lower = 0
upper = 10**9+1
res = 0
while(upper - lower > 1):
    mid = (upper + lower) // 2
    if(A*mid + B*len(str(mid)) > X):
        upper = mid
    else:
        lower = mid
print(lower)
