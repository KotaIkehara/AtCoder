import sys
sys.setrecursionlimit(500000)


h, w = map(int, input().split())
C = [list(input()) for i in range(h)]


def search(x, y):
    if(y < 0 or w <= y or x < 0 or h <= x):
        return
    if(C[x][y] == "#"):
        return
    if(C[x][y] == "g"):
        print("Yes")
        exit()
    C[x][y] = "#"
    search(x+1, y)
    search(x-1, y)
    search(x, y+1)
    search(x, y-1)


for i, c in enumerate(C):
    if("s" in c):
        search(i, c.index("s"))
        break
print("No")
