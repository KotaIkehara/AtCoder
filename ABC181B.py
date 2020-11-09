N = int(input())

S = 0
for i in range(N):
    a, b = map(int, input().split())
    S += (b*(b+1)//2 - a*(a-1)//2)
print(S)
