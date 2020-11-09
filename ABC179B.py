N = int(input())

doublet = 0
for i in range(N):
    a, b = map(int, input().split())
    if(a == b):
        doublet += 1
    else:
        doublet = 0
    if(doublet == 3):
        print("Yes")
        break
else:
    print("No")
