N = int(input())
P = list(map(int, input().split()))

count = 0
for i in range(N):
    if(P[i] != i+1):
        count += 1
print("YES" if(count == 2 or count == 0) else "NO")
