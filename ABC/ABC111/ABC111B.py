N = int(input())
n = N//100
if(N > n*100 + n*10 + n):
    print((n+1)*100 + (n+1)*10 + (n+1))
else:
    print(n*100 + n*10 + n)
