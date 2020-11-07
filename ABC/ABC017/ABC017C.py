N, M = map(int, input().split())
table = [0]*(M+1)

sum = 0
for i in range(N):
    l, r, s = map(int, input().split())
    table[l-1] += s
    table[r] -= s
    sum += s

for i in range(1, M):
    table[i] += table[i-1]

print(sum-min(table[:-1]))
