S = input()
T = input()
s = sorted(map(S.count, set(S)))
t = sorted(map(T.count, set(T)))
print("Yes" if(s == t) else "No")