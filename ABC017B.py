X = input()

print("YES" if(X.replace("ch", '').replace("o", '').replace(
    "k", '').replace("u", '') == '') else "NO")
