K = int(input())

res = -1
count = 1
sum = 7
prev = []
r = sum % K
while(r not in prev):
    prev.append(r)
    sum = sum * 10 + 7
    r = sum % K
    if(r == 0):
        res = count+1
        break
    count += 1

print(res)
