K, X = map(int, input().split())

left = X-(K-1)
right = X+(K-1)
if(left < -10**6):
    left = -10**6
if(right > 10**6):
    right = 10**6

for i in range(left, right+1):
    print(i, "", end="")
print()
