S = input()[0:12]
key = "WBWBWWBWBWBW"*2
res = ["Do", "", "Re", "", "Mi", "Fa", "", "So", "", "La", "", "Si"]

print(res[(key.find(S))])
