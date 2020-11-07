A, B, C, D = map(int, input().split())
diff = min(B, D) - max(A, C)
print(diff if(diff >= 0) else 0)
