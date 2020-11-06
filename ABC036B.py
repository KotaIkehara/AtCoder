N = int(input())
S = [input() for i in range(N)]
for s in zip(*S):
    print("".join(s[::-1]))
