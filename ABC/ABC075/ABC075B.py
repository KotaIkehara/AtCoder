H, W = map(int, input().split())
outline = ["."*(W+2)]
S = outline + ["." + input() + "." for i in range(H)] + outline

for j in range(1, H+1):
    for i in range(1, W+1):
        count = 0
        if(S[j][i] == "#"):
            print("#", sep="", end="")
            continue
        if(S[j+1][i-1] == "#"):
            count += 1
        if(S[j+1][i] == "#"):
            count += 1
        if(S[j+1][i+1] == "#"):
            count += 1
        if(S[j][i+1] == "#"):
            count += 1
        if(S[j-1][i+1] == "#"):
            count += 1
        if(S[j-1][i] == "#"):
            count += 1
        if(S[j-1][i-1] == "#"):
            count += 1
        if(S[j][i-1] == "#"):
            count += 1
        print(count, sep="", end="")
    print()
