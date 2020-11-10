N = int(input())
C = input()

res = sorted([C.count(i) for i in '1234'])
print(res[-1], res[0])
