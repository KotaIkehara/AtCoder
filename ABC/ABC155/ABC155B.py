N = int(input())
A = map(int, input().split())

print("DENIED" if all(a & 1 or a % 3 == 0 or a % 5 for a in A) else "APPROVED")

