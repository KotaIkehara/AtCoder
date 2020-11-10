n = int(input())
A = list(map(int, input().split()))


def Sequence(A, positive):
    res = 0
    x = 0
    for i in range(n):
        x += A[i]
        if(positive and x <= 0):
            res += 1-x
            x = 1
        elif(not positive and x >= 0):
            res += 1+x
            x = -1
        positive = not positive
    return res


print(min(Sequence(A, True), Sequence(A, False)))
