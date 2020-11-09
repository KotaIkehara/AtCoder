S = input()
T = input()

L = ["a", "t", "c", "o", "d", "e", "r"]

for i in range(len(S)):
    if(S[i] != T[i]):
        if(S[i] != "@" and T[i] != "@"):
            print("You will lose")
            exit()
        if(S[i] == "@" and T[i] not in L):
            print("You will lose")
            exit()
        if(T[i] == "@" and S[i] not in L):
            print("You will lose")
            exit()
print("You can win")
