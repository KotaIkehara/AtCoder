N, M = map(int, input().split())
A = [input() for i in range(N)]
B = [input() for i in range(M)]

for i in range(N-M+1):
    for j in range(N-M+1):
        if([row[j:j+M] for row in A[i:i+M]] == B):
            print("Yes")
            exit()
print("No")
