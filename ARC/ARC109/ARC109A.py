a, b, x, y = map(int, input().split())

if(a == b):
    print(x)
elif(a < b):
    print(min(x*(2*(b-a)+1), x+y*(b-a)))
elif(a > b):
    print(min(x*(2*(a-b)-1), x+y*(a-b-1)))
