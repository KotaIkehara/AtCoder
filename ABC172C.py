N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [0]*(N+1)
b = [0]*(M+1)

for i in range(N):
    a[i+1] = A[i] + a[i]
for i in range(M):
    b[i+1] = B[i] + b[i]

res = 0
j = M
for i in range(N+1):
    if(a[i] > K):
        break
    while(a[i] + b[j] > K):
        j -= 1
    res = max(res, i+j)
print(res)

# in
# 2 2 4
# 3 1
# 2 3
# の時に答えが違う

# time = 0
# res = 0
# a = 0
# b = 0
# for i in range(N+M):
#     if(time >= K):
#         break
#     if(a < N and b < M):
#         if(A[a] > B[b]):
#             time += B[b]
#             b += 1
#         else:
#             time += A[a]
#             a += 1
#     elif(a >= N and b < M):
#         time += B[b]
#         b += 1
#     elif(a < N and b >= M):
#         time += A[a]
#         a += 1
#     res += 1

# print(res if(time == K) else res - 1)
