S = input()
T = int(input())

d = abs(S.count("U")-S.count("D")) + abs(S.count("R")-S.count("L"))
q = S.count("?")

if(T == 1):
    print(d+q)
else:
    if(d > q):
        print(d-q)
    else:
        print((q-d) % 2)
