N = int(input())
A = [input() for i in range(N)]

mul = [["s", "sh", "ch", "o", "x"], ["f", "fe"],
       ["a", "i", "u", "e", "o"]]

for a in A:
    if(a[-1] in mul[0] or a[-2:] in mul[0]):
        print(a+"es")
    elif(a[-1] in mul[1]):
        print(a[:-1] + "ves")
    elif(a[-2:] in mul[1]):
        print(a[:-2] + "ves")
    elif(a[-1] == "y" and a[-2] not in mul[2]):
        print(a[:-1] + "ies")
    else:
        print(a + "s")
