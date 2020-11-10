A, B = map(int, input().split())

count = 0
for i in map(str, range(A, B+1)):
    if(i == i[::-1]):
        count += 1
print(count)
