N = int(input())
S = input()

res = 0
for i in range(10**3):
    key = str(i).zfill(3)
    if(key[0] in S):
        idx = S.index(key[0])
        L = S[idx+1:]
        if(key[1] in L):
            idx = L.index(key[1])
            L = L[idx + 1:]
            if(key[2] in L):
                res += 1
print(res)
