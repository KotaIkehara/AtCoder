M = int(input())
S = sorted([list(map(int, input().split()))
            for _ in range(M)], key=lambda x: (x[0], -x[1]))
N = int(input())
A = sorted([list(map(int, input().split()))
            for _ in range(N)],  key=lambda x: (x[0], -x[1]))


def check(Map, dx, dy):
    for i in range(M):
        x, y = Map[i]
        if([x+dx, y + dy] in A):
            continue
        else:
            return False
    return True


x, y = S[0]
for ax, ay in A:
    dx = ax - x
    dy = ay - y
    if check(S, dx, dy):
        print(dx, dy)
        exit()
