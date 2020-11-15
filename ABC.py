H, W = map(int, input().split())
S = ["#"*(W+2)] + ["#" + input() + "#" for i in range(H)] + ["#"*(W+2)]
res = 0


def func(x, y):
    global res
    if(S[x][y] == "#"):
        return
    if(x == H and y == W):
        res += 1
    i = 1
    while(i < W+2-x):
        if(S[x+i][y] == "#"):
            break
        else:
            func(x+i, y)
        i += 1
    i = 1
    while(i < H+2-y):
        if(S[x][y+i] == "#"):
            break
        else:
            func(x, y+i)
        i += 1
    i = 1
    while(i < W+2-x and i < H+2-y):
        if(S[x+i][y+i] == "#"):
            break
        else:
            func(x+i, y+i)
        i += 1


func(1, 1)
mod = 10**9 + 7
print(res % mod)
