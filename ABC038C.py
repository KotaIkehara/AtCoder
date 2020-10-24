N = int(input())
A = list(map(int, input().split()))

right = 1
res = 0

for left in range(N):
    while(right < N and (A[right-1] < A[right] or right == left)):
        right += 1
    res += right - left
    if(left == right):
        right += 1


print(res)
