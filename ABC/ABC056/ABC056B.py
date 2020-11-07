W, a, b = map(int, input().split())

print(max(abs(b-a)-W, 0))
