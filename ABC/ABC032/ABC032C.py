N, K = map(int, input().split())
S = [int(input()) for i in range(N)]

res = 0
right = 0
mul = 1
if(0 in S):
    print(N)
    exit()
for left in range(N):
    while(right < N and mul * S[right] <= K):
        mul *= S[right]
        right += 1
    res = max(res, right - left)
    if(left == right):
        right += 1
    else:
        mul /= S[left]
print(res)
