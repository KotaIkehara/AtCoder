a = int(input())
b = int(input())
n = int(input())

res = max(a, b)
while(res % a != 0 or res % b != 0 or res < n):
    res += 1

print(res)
