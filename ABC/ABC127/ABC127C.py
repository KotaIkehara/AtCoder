N, M = map(int, input().split())

table = [0]*(N+1)

for i in range(M):
    l, r = map(int, input().split())
    table[l-1] += 1
    table[r] -= 1

for i in range(1, N+1):
    table[i] += table[i-1]

print(sum(t == M for t in table))
