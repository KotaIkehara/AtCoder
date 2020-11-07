import itertools

A = list(map(int, input().split()))

B = [sum(i) for i in itertools.combinations(A, 3)]
print(sorted(B)[-3])
