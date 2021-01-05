N = int(input())
A = sorted(list(map(int, input().split())))[::-1]
seki = A[:]
for i in range(len(A)-1):
    seki[i+1] = seki[i+1] + seki[i]

res = 0
for i in range(1,len(A)):
    res += (N-i)*(A[i-1]) - (seki[-1]-seki[i-1])
print(res)