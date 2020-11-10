s = int(input())
l = [s]
m = 1
while(m < 1000000):
    if(s % 2 == 0):
        s = s//2
    else:
        s = 3*s + 1

    m += 1
    if s not in l:
        l.append(s)
    else:
        print(m)
        break
