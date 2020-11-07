N = int(input())
A = list(set([int(input()) for i in range(N)]))
print(sorted(A)[-2])
