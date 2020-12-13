N = int(input())
A = list(map(int, input().split()))

res = -float('inf')
prevS = 0
for i in range(N):
    m = -float('inf')
    for j in range(N):
        if(i == j):
            continue
        else:
            l = min(i,j)
            r = max(i,j)
            S = sum(A[l+1:r+1:2])
            if(S > m):
                idx = (l,r)
                m = S
    res = max(res, sum(A[idx[0]:idx[1]+1:2]))
    
print(res)
