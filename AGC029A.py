S = input()

res = 0
b = 0
for i in range(len(S)):
    if(S[i] == "B"):
        b += 1
    else:
        res += b
print(res)
