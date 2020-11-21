X, N = map(int, input().split())
P = set(map(int, input().split()))

res = 101
d = 100
# 答えは0, 101にもなりうる
for i in range(102):
    if(i not in P and abs(X-i) < d):
        d = abs(X-i)
        res = i
print(res)
