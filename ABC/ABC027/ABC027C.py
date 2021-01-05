N = int(input())
x = 1
name = ["Takahashi", "Aoki"]

depth = -1
C = N
while(C>0):
    C = C//2
    depth += 1

alpha = (depth+1)%2
beta = depth%2
turn = 0
while(x<=N):
    if(turn%2 == 0):
        x = x*2 + alpha
    else:
        x = x*2 + beta
    turn = (turn+1)%2

print(name[turn%2])