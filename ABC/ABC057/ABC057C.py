N = int(input())

i = int(N**0.5)
while(N % i != 0):
    i -= 1
print(len(str(N//i)))
