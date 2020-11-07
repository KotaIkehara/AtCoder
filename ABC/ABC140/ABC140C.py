N = int(input())
B = list(map(int, input().split()))

res = 0
for i in range(N-2):
    res += min(B[i], B[i+1])
print(B[0] + res+B[N-2])
