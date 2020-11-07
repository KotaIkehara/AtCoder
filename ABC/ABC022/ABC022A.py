N, S, T = map(int, input().split())
A = [int(input()) for i in range(N)]

W = count = 0
for a in A:
    W += a
    if S <= W <= T:
        count += 1
print(count)
