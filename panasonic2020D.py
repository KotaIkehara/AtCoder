N = int(input())


def func(S, L):
    if(len(S) == N):
        print(S)
    else:
        for i in range(L+1):
            if i == L:
                func(S+chr(ord("a")+i), L+1)
            else:
                func(S+chr(ord("a")+i), L)


func("a", 1)
