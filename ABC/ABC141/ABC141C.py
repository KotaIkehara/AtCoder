N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]
Point = [0]*N

for a in A:
    Point[a-1] += 1

for i in range(N):
    if(K-Q+Point[i] > 0):
        print("Yes")
    else:
        print("No")
