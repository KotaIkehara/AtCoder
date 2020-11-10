N = input()

sum = 0
for n in N:
    sum += int(n)
print("Yes" if(sum % 9 == 0) else "No")
