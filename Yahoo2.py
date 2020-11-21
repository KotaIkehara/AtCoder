N, K = map(int, input().split())

read = []

for i in range(N):
    q = input()
    if(q[0] == "b"):
        x = int(q.split()[1])
        read.append(x)
        print(x)
    else:
        x = max(read[:len(q)-K-1])
        read.remove(x)
        read.append(x)
        print(x)
