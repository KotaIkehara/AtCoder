N, A, B = map(int, input().split())

res = 0
for i in range(1, N+1):
    if(A <= sum(map(int, str(i))) <= B):
        res += i

print(res)
