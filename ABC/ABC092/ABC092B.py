N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]

# D = 7, A = 2 -> 1, 3, 5, 7
# A = 5 -> 1, 6
# A = 10 -> 1
s = 0
for a in A:
    s += (D-1)//a+1
print(s+X)
