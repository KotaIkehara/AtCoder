D, N = map(int, input().split())

# N=100の時に注意
print(100**D * N if(N < 100) else 100**D*(N+1))
