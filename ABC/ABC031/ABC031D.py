from collections import defaultdict

K, N = map(int, input().split())

L = []
for i in range(N):
    v, w = input().split()
    L.append((v, w))


for i in range(3**K):
    res = defaultdict(set)
    B = [0]*K
    power3 = 1
    for j in range(K):
        B[j] = (i//power3) % 3+1
        power3 *= 3
    for num, s in L:
        flag = True
        l = 0
        for n in num:
            l += B[int(n)-1]
        if(l != len(s)):
            flag = False
            break
    if flag:
        for num, s in L:
            prev = 0
            for i, n in enumerate(num):
                n = int(n)
                res[n].add(s[prev:prev+B[n-1]])
                prev += B[n-1]
        for r in sorted(res):
            print(*res[r])
        exit()
