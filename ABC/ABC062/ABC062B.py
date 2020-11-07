H, W = map(int, input().split())
outline = ["#"*(W+2)]
A = outline + ["#" + input() + "#" for i in range(H)] + outline

for a in A:
    print(a)
