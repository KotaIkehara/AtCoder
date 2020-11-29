xa, ya, xb, yb, T, V = map(int, input().split())
n = int(input())
M = []

max_diff = T*V

for i in range(n):
    x, y = map(int, input().split())
    diff = ((x-xa)**2 + (y-ya)**2)**.5 + ((x-xb)**2 + (y-yb)**2)**.5
    if diff <= max_diff:
        print("YES")
        exit()
print("NO")
