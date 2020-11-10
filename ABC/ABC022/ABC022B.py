N = int(input())
A = [int(input()) for i in range(N)]
visit = set()

count = 0
for a in A:
    if(a in visit):
        count += 1
    else:
        visit.add(a)
print(count)
