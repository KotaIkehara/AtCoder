H, W = map(int, input().split())
S = ["."*(W+2)] + ["." + input() + "." for i in range(H)] + ["."*(W+2)]

for i in range(W):
    for j in range(H):
        if(S[j][i] == "#"):
            if(S[j-1][i] != "#" and S[j+1][i] != "#" and S[j][i-1] != "#" and S[j][i+1] != "#"):
                print("No")
                exit()
print("Yes")
