N = int(input())
T = list(map(int, input().split()))
M = int(input())

S = sum(T)
for i in range(M):
    p, x = map(int, input().split())
    print(S-T[p-1] + x)
