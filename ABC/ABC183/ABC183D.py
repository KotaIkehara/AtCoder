N, W = map(int, input().split())
T = 2*(10**5)
table = [0] * (T+1)

for i in range(N):
    s, t, p = map(int, input().split())
    table[s] += p
    table[t] -= p

for i in range(T):
    table[i+1] += table[i]
print("Yes" if(max(table) <= W) else "No")
