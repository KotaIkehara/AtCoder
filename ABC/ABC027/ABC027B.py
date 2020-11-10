N = int(input())
A = list(map(int, input().split()))

if(sum(A) % N != 0):
    print(-1)
    exit()
else:
    num = sum(A)//N
    res = 0
    for i in range(N-1):
        if(sum(A[:i+1]) != num*(i+1) or sum(A[i+1:]) != num*(N-(i+1))):
            res += 1
print(res)
