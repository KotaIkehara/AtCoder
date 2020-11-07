import collections
N = int(input())
a, b = map(int, input().split())
K = int(input())
P = collections.Counter((list(map(int, input().split())) + [a, b]))

print("YES" if(len(P) == K+2) else "NO")
