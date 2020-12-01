s = input()
K = int(input())

L = set()

for l in range(1, K+1):
    for i in range(len(s) - l + 1):
        L.add(s[i:i+l])
print(sorted(L)[K-1])
