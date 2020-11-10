import math

N = int(input())
if(N <= 5):
    print(-1)
    exit()
A = math.log(N-5, 3)
B = math.log(N-3, 5)

for a in range(1, int(A)+2):
    for b in range(1, int(B)+2):
        if(3**a + 5**b == N):
            print(a, b)
            exit()
print(-1)
