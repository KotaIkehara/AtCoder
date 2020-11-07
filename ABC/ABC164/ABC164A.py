S, W = map(int, input().split())
print("unsafe" if(S <= W) else "safe")
K = int(input())
A, B = map(int, input().split())

for i in range(A, B+1):
    if(i % K == 0):
        print("Yes")
        exit()
print("No")
