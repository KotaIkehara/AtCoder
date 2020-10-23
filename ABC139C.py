N = int(input())
H = list(map(int, input().split()))
dp = [0]*N
count = 0
for i in range(1, N):
    if(H[i-1] >= H[i]):
        count += 1
    else:
        count = 0
    dp[i] = count
print(max(dp))
