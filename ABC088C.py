C = [list(map(int, input().split())) for i in range(3)]

flag = True
for i in range(3):
    if(not C[i][0] - C[i-1][0] == C[i][1] - C[i-1][1] == C[i][2] - C[i-1][2]):
        flag = False
        break
for i in range(3):
    if(not C[0][i] - C[0][i-1] == C[1][i] - C[1][i-1] == C[2][i] - C[2][i-1]):
        flag = False
        break
print("Yes" if flag else "No")
