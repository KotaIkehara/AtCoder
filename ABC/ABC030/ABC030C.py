import bisect
N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

time = 0
res = 0

while(time <= A[-1]):
    time = A[bisect.bisect_left(A, time)] + X
    if(time <= B[-1]):
        time = B[bisect.bisect_left(B, time)] + Y
        res += 1
    else:
        break
print(res)
