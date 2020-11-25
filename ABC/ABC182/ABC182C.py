N = input()
k = len(N)

S = 0
for n in N:
    S += int(n)

r = S % 3
if(r == 0):
    print(0)
    exit()

L = [2, 1]
count = 0
for n in N:
    if(int(n) % 3 == r and k > 1):
        print(1)
        exit()
    if(int(n) % 3 == L[r-1]):
        count += 1

if(count >= 2 and k > 2):
    print(2)
else:
    print(-1)
