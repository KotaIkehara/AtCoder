A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

print(A * S + B * T if (S + T < K) else A * S + B * T - C * (S + T))

