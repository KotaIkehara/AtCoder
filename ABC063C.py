N = int(input())
S = sorted([int(input()) for i in range(N)])

res = sum(S)
if(res % 10 == 0):
    for s in S:
        if s % 10 != 0:
            print(res-s)
            exit()
    print(0)
else:
    print(res)
