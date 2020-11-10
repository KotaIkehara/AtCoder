X, K, D = map(int, input().split())

if(X > 0):
    if(X-K*D >= 0):
        print(X-K*D)
    else:
        l = X//D
        X = X-D*(l+1)
        K = K-l-1
        if(K % 2 == 0):
            print(abs(X))
        else:
            print(abs(X+D))
elif(X < 0):
    if((X+K*D) <= 0):
        print(abs(X+K*D))
    else:
        l = -X//D
        X = X + D*(l+1)
        K = K-l-1
        if(K % 2 == 0):
            print(abs(X))
        else:
            print(abs(X-D))
else:
    if(K % 2 == 0):
        print(0)
    else:
        print(abs(D))
