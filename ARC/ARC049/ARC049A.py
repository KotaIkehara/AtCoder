S = list(input())
A, B, C, D = map(int, input().split())
S.insert(D, "\"")
S.insert(C, "\"")
S.insert(B, "\"")
S.insert(A, "\"")

print(*S, sep="")
