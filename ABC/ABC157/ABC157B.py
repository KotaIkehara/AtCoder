A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
B = [int(input()) for i in range(N)]

for i in range(3):
    for j in range(3):
        for b in B:
            if(A[i][j] == b):
                A[i][j] = "#"

for a in A:
    if(a == ["#", "#", "#"]):
        print("Yes")
        exit()
for a in zip(*A):
    if(a == ("#", "#", "#")):
        print("Yes")
        exit()

if(A[0][0] == "#" and A[1][1] == "#" and A[2][2] == "#"):
    print("Yes")
    exit()
if(A[2][0] == "#" and A[1][1] == "#" and A[0][2] == "#"):
    print("Yes")
    exit()
print("No")
