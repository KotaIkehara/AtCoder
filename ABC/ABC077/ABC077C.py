import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

res = 0
for b in B:
    res += bisect.bisect_left(A, b)*(N-bisect.bisect_right(C, b))

print(res)
