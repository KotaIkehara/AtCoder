S = input()
L = int(S[:2])
R = int(S[2:])

# 境界条件をしっかり確認しよう
if(1 <= L <= 12):
    if(1 <= R <= 12):
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if(1 <= R <= 12):
        print("YYMM")
    else:
        print("NA")
