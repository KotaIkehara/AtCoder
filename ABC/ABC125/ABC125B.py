N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

res = 0
for v, c in zip(V, C):
    if(v > c):
        res += v-c
print(res)
