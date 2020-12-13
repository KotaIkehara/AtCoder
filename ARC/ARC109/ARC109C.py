import math
n, k = map(int, input().split())
s = input()


def janken(a, b):
    if(a == b):
        return a
    else:
        if(a == "R" and b == "P" or a == "P" and b == "R"):
            return "P"
        if(a == "R" and b == "S" or a == "S" and b == "R"):
            return "R"
        if(a == "P" and b == "S" or a == "S" and b == "P"):
            return "S"


def dfs(l, r):
    if(r-l == 1):
        return s[l % n]
    if(r-l == 2):
        return janken(s[l % n], s[(l+1) % n])
    m = (l+r)//2
    return janken(dfs(l, m), dfs(m, r))


print(dfs(0, 2**k))
