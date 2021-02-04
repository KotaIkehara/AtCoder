N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
for a, b in zip(A, B):
    sum += a * b
print("Yes" if(sum == 0) else "No")
