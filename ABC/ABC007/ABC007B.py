A = input()

if(len(A) == 1):
    if(A == "a"):
        print(-1)
    else:
        print(chr(ord(A)-1))
else:
    print(A[:-1])
