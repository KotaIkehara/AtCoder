N, K = map(int, input().split())

L = [0]*(10**5+1)
for i in range(N):
    a, b = map(int, input().split())
    L[a] += b

count = 0
for i, l in enumerate(L):
    if(l != 0):
        count += l
        if(K <= count):
            print(i)
            break
