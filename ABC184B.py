N, X = map(int, input().split())
S = input()

res = X
for s in S:
    if(s == "x" and res > 0):
        res -= 1
    elif(s == "o"):
        res += 1
print(res)
