N = int(input())
C = input()

count = 0
for i in range((C.count("R"))):
    if(C[i] == 'W'):
        count += 1
print(count)
