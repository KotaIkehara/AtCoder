N,K = map(int, input().split())
D = list(map(int, input().split()))


def dislike(num):
    num = str(num)
    for n in num:
        if(int(n) in D):
            return True
    return False

while(dislike(N)):
    N += 1
print(N)