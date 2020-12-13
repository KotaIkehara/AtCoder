N = int(input())
A = list(map(int, input().split()))

quad = 0
double = 0
for a in A:
    if a % 4 == 0:
        quad += 1
    elif a % 2 == 0:
        double += 1

if quad == 0 and double == 0:
    flag = False
elif quad == 0 and double > 0:
    flag = N == double
elif quad > 0 and double == 0:
    flag = N <= (2*quad+1)
else:
    flag = N <= (2*quad+1) + (double-1)
print("Yes" if flag else "No")
