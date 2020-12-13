N,M,T = list(map(int, input().split()))
N_max = N
time = 0
for i in range(M):
    a,b = list(map(int, input().split()))
    N -=  a-time
    if(N<=0):
        print("No")
        exit()
    else:
        N += b-a
        if(N>=N_max):
            N = N_max
        time = b
N -= T-time
if(N<=0):
    print("No")
else:
    print("Yes")
