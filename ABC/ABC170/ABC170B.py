X, Y = map(int, input().split())

# b = X - a
# a*2+(X-a)*4 = Y

for i in range(X+1):
    if(i*2 + (X-i)*4 == Y):
        print("Yes")
        exit()
print("No")
