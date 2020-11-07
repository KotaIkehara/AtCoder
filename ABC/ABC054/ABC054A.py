A, B = map(lambda x: ((int(x)+13) % 15), input().split())

if(A > B):
    print("Alice")
elif(A < B):
    print("Bob")
else:
    print("Draw")
