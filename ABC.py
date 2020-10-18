S = input()

res = 0
for i in range(2**(len(S)-1)):
    sum = ""
    for j in range(len(S)):
        if((i >> j) & 1):
            sum += S[j] + "+"
        else:
            sum += S[j]
    res += eval(sum)
print(res)
