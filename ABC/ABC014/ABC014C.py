n = int(input())

table = [0] * (10**6+1+1)
for i in range(n):
    a, b = map(int, input().split())
    table[a] += 1
    table[b+1] -= 1

for i in range(10**6+1):
    table[i+1] += table[i]

print(max(table))
