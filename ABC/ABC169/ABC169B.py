N = int(input())
A = list(map(int, input().split()))

if(0 in A):
    print(0)
else:
    res = 1
    for a in A:
        res *= a
        if(res > 10**(18)):  # これがないとTLEした
            print(-1)
            exit()
    print(res)
