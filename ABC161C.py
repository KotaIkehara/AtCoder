N, K = map(int, input().split())

print(min(N-K*(N//K), -N+K*(N//K+1)))
