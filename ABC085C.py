N, Y = map(int, input().split())

for x in range(N+1):
    for y in range(N-x+1):
        z = (N - x - y)
        if(10*x+5*y+z == Y//1000):
            print(x, y, z)
            exit()
print("-1 -1 -1")
