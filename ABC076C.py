import re

S = input().replace("?", ".")  # 正規表現において"."は任意の文字を表す
T = input()

for i in range(len(S)-len(T), -1, -1):
    if(re.match(S[i:i+len(T)], T)):
        S = S.replace(".", "a")
        S = S[0:i] + T + S[i+len(T):]
        print(S)
        break
else:
    print("UNRESTORABLE")
