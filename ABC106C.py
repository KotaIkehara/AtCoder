S = input()
K = int(input())

count = 0
for s in S:
    if(s == "1"):
        count += 1
    else:
        break

if(K <= count):
    print(1)
else:
    print(S[count])
