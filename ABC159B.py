S = input()
N = len(S)

cond1 = S[:N//2] == S[N//2+1:][::-1]
cond2 = S[:(N-1)//2] == S[:(N-1)//2][::-1]
cond3 = S[(N+3)//2-1:] == S[(N+3)//2-1:][::-1]
print("Yes" if(cond1 and cond2 and cond3) else "No")
