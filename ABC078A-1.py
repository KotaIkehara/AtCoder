X, Y = input().split()
print(["=", ">", "<"][X > Y or -(X < Y)])
