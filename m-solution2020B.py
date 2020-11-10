a, b, c = map(int, input().split())
K = int(input())

for i in range(K):
    if(a >= b):
        b *= 2
    elif(b >= c):
        c *= 2
print("Yes" if a < b < c else "No")
