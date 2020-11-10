H, W = map(int, input().split())
A = [[s for s in input()] for i in range(H)]
B = [a for a in A if("#" in a)]
C = zip(*[b for b in zip(*B) if("#" in b)])
for c in C:
    print("".join(c))
