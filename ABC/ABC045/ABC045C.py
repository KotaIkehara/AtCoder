S = input()

res = 0
for i in range(2**(len(S)-1)):  # |S|<=10なので，高々(2^10)*9通り
    sum = ""
    for j in range(len(S)):
        print("i: ", i, ", j: ", j, "i >> j: ", i >>
              j, "(i >> j) & 1: ", (i >> j) & 1)
        if((i >> j) & 1):  # iをjビット右にシフトする
            sum += S[j] + "+"
        else:
            sum += S[j]
    res += eval(sum)
print(res)
