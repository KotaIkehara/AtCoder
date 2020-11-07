N = int(input())
A = list(map(int, input().split()))

table = [0]*(N+1)
for i in range(N):
    table[i+1] += table[i] + A[i]

print(min(abs(table[N]-2*table[i]) for i in range(1, N)))
