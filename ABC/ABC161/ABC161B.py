N, M = map(int, input().split())
A = list(map(int, input().split()))

border = sum(A)/(4*M)
count = 0
for a in A:
    if(a >= border):
        count += 1
print("Yes" if count >= M else "No")
