N, x = map(int, input().split())
while(N != 0 or x != 0):
    res = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if(i+j+k == x):
                    res += 1
    print(res)
    N, x = map(int, input().split())
