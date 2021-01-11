N, M = map(int, input().split())
A = list(map(int, input().split()))
maze = [[] for _ in range(N)]
print(maze)
for i in range(M):
    x, y = map(lambda x: int(x)-1, input().split())
    maze[x].append(y)
print(maze)
